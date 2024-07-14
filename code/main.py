import board
import microcontroller
from digitalio import DigitalInOut, Direction, Pull
from time import sleep
import usb_hid
from adafruit_hid.keyboard import Keyboard 
from adafruit_hid.keycode import Keycode

from keymaps import *

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

kbd = Keyboard(usb_hid.devices)

keymap = none
Run = False

# menu loop for changing keymaps
def menu():
	global keymap
	global Run
	while not Run:
		#blink  the led to indicate menu mode
		led.value = not led.value
		for button in range(len(buttons)): #btn 7 is reserved for storage mount
			if not buttons[button].value:
				if button == 6:
					microcontroller.reset() # hard reset the board
				keymap = keymapslist[button]
				print("keymap changed to " + str(keymapslist[button]))
				Run = True
				break

		sleep(0.5)
	led.value = False
	main() # return to main loop

# main operation loop
def main():
	global Run 
	button_state = [False] * len(buttons) #populate a list to store the state of each button
	while Run:
		for button in range(len(buttons)):
			mode = keymap[button]["mode"] # get mode
			if not buttons[button].value: # when button pressed
				#basically a switch statement
				if mode == PRESS: #basic send button press
					kbd.press(*keymap[button]["press"])
				elif mode == LOCK: # holds down key on first press, releases on second press
					sleep(0.2) # extra debounce for hold mode
					if button_state[button] == False:
						kbd.press(*keymap[button]["press"])
						button_state[button] = True
						break
					else:
						kbd.release(*keymap[button]["press"])
						button_state[button] = False
						break
				elif mode == DUAL and button_state[button] == False: #
					kbd.send(*keymap[button]["press"])
				elif mode == MACRO and button_state[button] == False:
					for key in keymap[button]["press"]:
						kbd.send(*key)
						sleep(keymap[button]["delay"][keymap[button]["press"].index(key)]) #delay between each key, stored in the delay array
				button_state[button] = True
			if button_state[button] and buttons[button].value: #only runs if state is true and button is released
				if mode == PRESS:
					kbd.release(*keymap[button]["press"])
				elif mode == DUAL:
					kbd.send(*keymap[button]["release"])
				if mode != LOCK: button_state[button] = False
		# If both buttons 1 and 7 are pressed for longer than 5 seconds, reset the board
		if not buttons[0].value and not buttons[6].value:
			rstcount = 0
			while rstcount < 5:
				sleep (1)
				rstcount += 1
				if buttons[0].value or buttons[6].value:
					sleep(1)
					break
			if rstcount == 5:
				Run = False # exit the loop
		sleep(0.01) # debounce
	led.value = True # indicate entering menu mode
	sleep(2) # wait before returning to menu so user can lift their feet
	menu() # return to menu

#setup 7 buttons from GP 9-15
button_pins = [board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15]
buttons = []
for pin in button_pins:
	button = DigitalInOut(pin)
	button.direction = Direction.INPUT
	button.pull = Pull.UP
	buttons.append(button)

print("buttons initialized")

menu()

print("keymap initialized")

main() # never forget to call the main loop		
