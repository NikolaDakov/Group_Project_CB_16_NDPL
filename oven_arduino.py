import time
import sys
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

def setup():
    global board
    board = CustomTelemetrix()
    board.set_pin_mode_digital_input_pullup(8)
    board.set_pin_mode_digital_output(4)

def button():
    time.sleep(0.01)

    data = board.digital_read(8)
    if data:
        level = data[0]
        if (level == 0):
            board.analog_write(4, 0)
            timer()


def timer():
    currentTime = 5*2
    while currentTime >= 0:
        board.displayShow(currentTime)
        currentTime -=1
        time.sleep(1)
    
    print("Timer finished!")
    board.displayShow("OPE")
    board.digital_write(4, 1)


def loop():
    button()

setup()
while True:
    try:
        loop()
    except KeyboardInterrupt:
        print('shutdown')
        board.shutdown()
        sys.exit(0)
