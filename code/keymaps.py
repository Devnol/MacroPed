from adafruit_hid.keycode import Keycode
#from enum import Enum

#class mode(Enum):
##button modes
NORMAL = 1 # just like on a keyboard, send on press, release on release
HOLD = 2 # send on press, release on press again
VIM = 3 #send once on press, send once on release (optionally different keys)
MACRO = 4 #send a sequence of keys in series

##define keymaps below:
#keymaps are a list of dictionaries, each dictionary represents a button
#each dictionary has a "mode" key and a "press" key
#the "mode" key is a mode enum (see above)
#the "press" key is a list of keycodes to send when the button is pressed, depending on the mode
#the "release" key is a list of keycodes to send when the button is released, only used in VIM mode

default = (
    	{
		"mode": NORMAL,
		"press": [Keycode.A]
	},
	{
		"mode": NORMAL,
		"press": [Keycode.B]
	},
	{
		"mode": NORMAL,
		"press": [Keycode.C]
	},
	{
		"mode": NORMAL,
		"press": [Keycode.D]
	},
	{
		"mode": NORMAL,
		"press": [Keycode.E]
	},
	{
		"mode": NORMAL,
		"press": [Keycode.F]
	},
	{
		"mode": NORMAL,
		"press": [Keycode.G]
	}
)

map1 = (
	{
		"mode":NORMAL,
		"press": [Keycode.COMMAND, Keycode.CONTROL, Keycode.SHIFT, Keycode.FOUR]
	},
	{
		"mode": MACRO,
		"press": [[Keycode.ESCAPE], [Keycode.SHIFT, Keycode.SEMICOLON], [Keycode.W], [Keycode.ENTER]]
	},
	{
		"mode": NORMAL,
		"press": [Keycode.SHIFT]
	},
	{
		"mode": NORMAL,
		"press": [Keycode.L]
	},
	{
		"mode": VIM,
		"press": [Keycode.I],
		"release": [Keycode.ESCAPE]
	},
	{
		"mode": VIM,
		"press": [Keycode.V],
		"release": [Keycode.Y]
	},
	{
		"mode": NORMAL,
		"press": [Keycode.SHIFT, Keycode.FOUR]
	}
)

none = ()

keymapslist = [none, map1, map1, default, map1, default]