import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
#from kmk.extensions.LED import LED

#led_ext = LED(led_pin=[board.GP3])
#keyboard.extensions.append(led_ext)

keyboard = KMKKeyboard()
#keyin
keyboard.row_pins = (board.GP14, board.GP13, board.GP9, board.GP8, board.GP6, board.GP5)
#keyout
keyboard.col_pins = (board.GP12, board.GP11, board.GP15, board.GP7, board.GP10, board.GP4)
keyboard.diode_orientation = DiodeOrientation.ROW2COL
CTRLSHIFTH=KC.LCTL(KC.LSFT(KC.H))
keyboard.keymap = [
    [KC.ENTER,KC.NO,KC.N1,KC.N2,KC.NO,KC.N3,KC.NO,KC.NO,KC.N4,KC.N5,KC.NO,KC.N6,KC.NO,KC.NO,KC.N7,KC.N8,KC.F5,KC.N9,KC.BACKSPACE,KC.NO,KC.KP_ASTERISK,KC.N0,KC.NO,KC.HASH,KC.NO,KC.NO,KC.NO,CTRLSHIFTH,KC.NO,KC.NO,KC.NO,KC.F11,KC.F10]
]


if __name__ == '__main__':
    keyboard.go()


