import storage
import board, digitalio

# On the Macropad, pressing a key grounds it. You need to set a pull-up.
# If not pressed, the key will be at +V (due to the pull-up).
button = digitalio.DigitalInOut(board.GP15)
button.pull = digitalio.Pull.UP

# Disable usb mass storage only if button is not pressed.
if button.value:
   storage.disable_usb_drive()