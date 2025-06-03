#ifndef _MAIN_H_
#define _MAIN_H_


/* ------------------------------------------------------------------------
 * --------------------------  Keyboard Functions -------------------------
 * ----------------------------------------------------------------------*/
//	\brief called by HID interface
//	callback running when USB Host enables keyboard interface
bool main_kbd_enable(void);	// returns TRUE if keyboard startup is ok

//	\brief called by HID interface
//	callback running when USB Host disables keyboard interface
void main_kbd_disable(void);

//	\brief called when a start of frame is received on USB line
void main_sof_action(void);

//	\brief enters the application in low power mode
//	callback called when USB host sets USB line in suspend state
void main_suspend_action(void);

//	\brief called by UDD when the USB line exit of suspend state
void main_resume_action(void);

//	\brief called by UDC when USB Host requests to enable remote wakeup
void main_remotewakeup_enable(void);

//	\brief called by UDC when USB Host requests to disable remote wakeup
void main_remotewakeup_disable(void);


/* ------------------------------------------------------------------------
 * --------------------------  Joystick Functions -------------------------
 * ----------------------------------------------------------------------*/
bool main_generic_enable(void);

/*! \brief Called by HID interface
 * Callback running when USB Host disable generic interface
 */
void main_generic_disable(void);

// /*! \brief Called when a start of frame is received on USB line
//  */
// void main_sof_action(void);

// /*! \brief Enters the application in low power mode
//  * Callback called when USB host sets USB line in suspend state
//  */
// void main_suspend_action(void);

// /*! \brief Called by UDD when the USB line exit of suspend state
//  */
// void main_resume_action(void);

// /*! \brief Called by UDC when USB Host request to enable remote wakeup
//  */
// void main_remotewakeup_enable(void);

// /*! \brief Called by UDC when USB Host request to disable remote wakeup
//  */
// void main_remotewakeup_disable(void);


#endif // _MAIN_H_