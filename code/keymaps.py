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
#the "delay" key is an array of floats representing the delay in seconds after each key in the macro, only used in MACRO mode (e.g. to wait for UI))

#Keymap for Visual Studio Code with Vim extension
VScodeVim = (
	{ # open command palette
		"mode": PRESS,
		"press": [Keycode.COMMAND, Keycode.SHIFT, Keycode.P]
	},
	{ # save file
		"mode": MACRO,
		"press": [[Keycode.ESCAPE], [Keycode.SHIFT, Keycode.SEMICOLON], [Keycode.W], [Keycode.ENTER]],
		"delay": [0.1, 0.1, 0.1, 0]
	},
	{ # hold for visual mode
		"mode": DUAL,
		"press": [Keycode.V],
		"release": [Keycode.ESCAPE]
	},
	{ # jump to definition
		"mode": PRESS,
		"press": [Keycode.F12]
	},
	{ # hold for insert mode
		"mode": DUAL,
		"press": [Keycode.I],
		"release": [Keycode.ESCAPE]
	},
	{ # Open integrated terminal
		"mode": PRESS,
		"press": [Keycode.CONTROL, Keycode.GRAVE_ACCENT]
	},
	{ # Show IntelliSense
		"mode": PRESS,
		"press": [Keycode.CONTROL, Keycode.SPACE]
	}
)

Fusion360 = (
	{ # open parametric menu
		"mode": MACRO,
		"press": [[Keycode.S], [Keycode.P], [Keycode.A], [Keycode.R], [Keycode.A], [Keycode.M], [Keycode.ENTER]],
		"delay": [0.2, 0.1, 0.1, 0.1, 0.1, 0.2, 0]
	},
	{ # orbit with mouse
		"mode": PRESS,
		"press": [Keycode.SHIFT]
	},
	{ # zoom with mouse
		"mode": PRESS,
		"press": [Keycode.COMMAND]
	},
	{ # sketch constraint: midpoint 
		"mode": MACRO,
		"press": [[Keycode.S], [Keycode.M], [Keycode.I], [Keycode.D], [Keycode.ENTER]],
		"delay": [0.2, 0.1, 0.1, 0.2, 0]
	},
	{ # sketch constraint: coincident
		"mode": MACRO,
		"press": [[Keycode.S], [Keycode.C], [Keycode.O], [Keycode.I], [Keycode.N], [Keycode.ENTER]],
		"delay": [0.2, 0.1, 0.1, 0.1, 0.2, 0]
	},
	{ # sketch constraint: collinear
		"mode": MACRO,
		"press": [[Keycode.S], [Keycode.C], [Keycode.O], [Keycode.L], [Keycode.ENTER]],
		"delay": [0.2, 0.1, 0.1, 0.2, 0]
	},
	{ # create sketch
		"mode": MACRO,
		"press": [[Keycode.S], [Keycode.S], [Keycode.K], [Keycode.E], [Keycode.T], [Keycode.ENTER]],
		"delay": [0.2, 0.1, 0.1, 0.1, 0.2, 0]
	}
)

test = (
	{
		"mode": PRESS,
		"press": [Keycode.A]
	},
	{
		"mode": PRESS,
		"press": [Keycode.B]
	},
	{
		"mode": PRESS,
		"press": [Keycode.C]
	},
	{
		"mode": PRESS,
		"press": [Keycode.D]
	},
	{
		"mode": PRESS,
		"press": [Keycode.E]
	},
	{
		"mode": PRESS,
		"press": [Keycode.F]
	},
	{
		"mode": PRESS,
		"press": [Keycode.G]
	}
)

none = ([]*7)

# Assign a keymap to each of the 6 buttons (7th button is reserved for storage mount)
keymapslist = [test, VScodeVim, Fusion360, none, none, none]