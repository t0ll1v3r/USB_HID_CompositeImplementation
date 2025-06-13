import hid
import sys
import tkinter as tk
from functools import partial
import atexit

VID, PID = 0x03EB, 0x2133
LED_IFACE_INDEX = 2
POLL_MS = 100

def find_led_path():
	devs = list(hid.enumerate(VID, PID))
	if len(devs) <= LED_IFACE_INDEX:
		raise RuntimeError(f"couldnt find nothin at index {LED_IFACE_INDEX}")
	return devs[LED_IFACE_INDEX]['path']


class LED_Panel(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Front-Panel LEDs")
		self.resizable(False, False)

		self.path = find_led_path()
		self.dev = hid.device()
		self.dev.open_path(self.path)
		self.dev.set_nonblocking(True)
		atexit.register(self.dev.close)

		self.states = [False]*8
		self.buttons = []
		for i in range(8):
			btn = tk.Button(self,
							text=f"LED {i+1}",
							width=8,
							relief="raised",
							command=partial(self._clicked, i))
			btn.grid(row=i//4, column=i%4, padx=5, pady=5)
			self.buttons.append(btn)
		self.after(POLL_MS, self._poll_device)

	# HID helpers #
	def _clicked(self, idx: int):
		self.states[idx] = not self.states[idx]
		self._apply_states_to_gui()
		self._send_mask(self._states_to_mask())

	def _send_mask(self, mask: int):
		try:
			self.dev.write(bytes([0x00, mask & 0xFF]))
		except OSError as e:
			messagebox.showerror("USB HID error", str(e))

	def _poll_device(self):
		try:
			data = self.dev.read(2)
		except OSError:
			data = []

		if data:
			if len(data) == 2:
				mask = data[1]
			else:
				mask = data[0]
			self._apply_mask(mask)
		self.after(POLL_MS, self._poll_device)

	def _apply_mask(self, mask: int):
		changed = False
		for i in range(8):
			bit = bool(mask & (1 << i))
			if bit != self.states[i]:
				self.states[i] = bit
				changed = True
		if changed:
			self._apply_states_to_gui()

	def _apply_states_to_gui(self):
		for i, on in enumerate(self.states):
			self.buttons[i].config(relief="sunken" if on else "raised")

	def _states_to_mask(self) -> int:
		mask = 0
		for i, on in enumerate(self.states):
			if on:
				mask |= (i << i)
		return mask


if __name__ == "__main__":
	app = LED_Panel()
	app.mainloop()