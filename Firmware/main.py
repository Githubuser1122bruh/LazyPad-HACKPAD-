import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap, Wait

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1]  # Adjust if your wiring is different

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        # Key 1: Launch Slack
        KC.Macro(
            Press(KC.LCMD), Tap(KC.SPACE), Release(KC.LCMD),  # Cmd+Space for Spotlight
            Wait(300),
            Tap(KC.S), Tap(KC.L), Tap(KC.A), Tap(KC.C), Tap(KC.K),
            Wait(200),
            Tap(KC.ENTER)
        ),

        # Key 2: Launch Discord
        KC.Macro(
            Press(KC.LCMD), Tap(KC.SPACE), Release(KC.LCMD),
            Wait(300),
            Tap(KC.D), Tap(KC.I), Tap(KC.S), Tap(KC.C), Tap(KC.O), Tap(KC.R), Tap(KC.D),
            Wait(200),
            Tap(KC.ENTER)
        ),

        # Key 3: Launch Google Chrome
        KC.Macro(
            Press(KC.LCMD), Tap(KC.SPACE), Release(KC.LCMD),
            Wait(300),
            Tap(KC.C), Tap(KC.H), Tap(KC.R), Tap(KC.O), Tap(KC.M), Tap(KC.E),
            Wait(200),
            Tap(KC.ENTER)
        ),

        # Key 4: Launch VS Code
        KC.Macro(
            Press(KC.LCMD), Tap(KC.SPACE), Release(KC.LCMD),
            Wait(300),
            Tap(KC.V), Tap(KC.S), Tap(KC.C), Tap(KC.O), Tap(KC.D), Tap(KC.E),
            Wait(200),
            Tap(KC.ENTER)
        ),
    ]
]

if __name__ == '__main__':
    keyboard.go()
