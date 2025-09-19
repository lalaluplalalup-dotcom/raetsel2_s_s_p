zufall = 0

def on_gesture_shake():
    global zufall
    zufall += randint(1, 3)
    if zufall == 1:
        basic.show_icon(IconNames.SCISSORS)
    if zufall == 2:
        basic.show_icon(IconNames.CHESSBOARD)
    if zufall == 3:
        basic.show_icon(IconNames.SQUARE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
