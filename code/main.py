import board
from digitalio import DigitalInOut, Direction, Pull
from time import sleep
import usb_hid
from adafruit_hid.keyboard import Keyboard 
from adafruit_hid.keycode import Keycode

from keymaps import *

kbd = Keyboard(usb_hid.devices)

keymap = default

def init_keymap():
	global keymap
	for button in range(len(buttons) - 1): #btn 7 is reserved for storage mount
		if not buttons[button].value:
			keymap = keymapslist[button]
			print("keymap changed to " + str(keymapslist[button]))
			break

#setup 7 buttons from GP 9-15
button_pins = [board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15]
buttons = []
for pin in button_pins:
	button = DigitalInOut(pin)
	button.direction = Direction.INPUT
	button.pull = Pull.UP
	buttons.append(button)

print("buttons initialized")

init_keymap()

print("keymap initialized")

sleep(4) #wait before setting state to false
button_state = [False] * len(buttons) #populate a list to store the state of each button
# main operation loop
while True:
	for button in range(len(buttons)):
		mode = keymap[button]["mode"] # get mode
		if not buttons[button].value: # when button pressed
			if mode == NORMAL: #basically a switch statement
				kbd.press(*keymap[button]["press"])
			elif mode == HOLD: # holds down key on first press, releases on second press
				sleep(0.2) # extra debounce for hold mode
				if button_state[button] == False:
					kbd.press(*keymap[button]["press"])
					button_state[button] = True
					break
				else:
					kbd.release(*keymap[button]["press"])
					button_state[button] = False
					break
			elif mode == VIM and button_state[button] == False: #only sends vim key once to prevent iiiiiiii
				kbd.send(*keymap[button]["press"])
			elif mode == MACRO and button_state[button] == False:
				for key in keymap[button]["press"]:
					kbd.send(*key)
			button_state[button] = True
		if button_state[button] and buttons[button].value: #only runs if state is true and button is released
			if mode == NORMAL:
				kbd.release(*keymap[button]["press"])
			elif mode == VIM:
				kbd.send(*keymap[button]["release"])
			if mode != HOLD: button_state[button] = False
	sleep(0.01) # debounce