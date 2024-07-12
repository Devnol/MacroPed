from adafruit_hid.keycode import Keycode
#from enum import Enum

#class mode(Enum):
##button modes
PRESS = 1 # just like on a keyboard, send on press, release on release
LOCK = 2 # send on press, release on press again
DUAL = 3 #send once on press, send once on release (optionally different keys), this is useful for things like vim where you might want to send a command on press and then escape on release
MACRO = 4 #send a sequence of keys in series, this is useful for things like opening a terminal and running a command

##define keymaps below:
#keymaps are a list of dictionaries, each dictionary represents a button
#each dictionary has a "mode" key and a "press" key
#the "mode" key is a mode enum (see above)
#the "press" key is a list of keycodes to send when the button is pressed, depending on the mode
#the "release" key is a list of keycodes to send when the button is released, only used in DUAL mode
#the "delay" key is an array of floats representing the delay in seconds between each key in the macro, only used in MACRO mode

map1 = (
	{
		"mode":PRESS,
		"press": [Keycode.COMMAND, Keycode.CONTROL, Keycode.SHIFT, Keycode.FOUR]
	},
	{
		"mode": MACRO,
		"press": [[Keycode.ESCAPE], [Keycode.SHIFT, Keycode.SEMICOLON], [Keycode.W], [Keycode.ENTER]],
		"delay": [0.1, 2, 0.1]
	},
	{
		"mode": PRESS,
		"press": [Keycode.SHIFT]
	},
	{
		"mode": PRESS,
		"press": [Keycode.L]
	},
	{
		"mode": DUAL,
		"press": [Keycode.I],
		"release": [Keycode.ESCAPE]
	},
	{
		"mode": PRESS,
		"press": [Keycode.UP_ARROW]
	},
	{
		"mode": PRESS,
		"press": [Keycode.DOWN_ARROW]
	}
)

none = ()

# Assign a keymap to each of the 6 buttons (7th button is reserved for storage mount)
keymapslist = [none, none, none, none, map1, none]