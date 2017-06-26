import RPi.GPIO as GPIO
from time import sleep
import threading
from threading import Thread


PIN_NUM_A1 = 12
PIN_NUM_B1 = 12
# PIN_NUM_C1 = 19
# PIN_NUM_D1 = 29
# PIN_NUM_E1 = 37
# PIN_NUM_F1 = 12
# PIN_NUM_G1 = 22
# PIN_NUM_H1 = 26
# PIN_NUM_I1 = 32
# PIN_NUM_J1 = 32


# pote 4, 17

PIN_NUM_A2 = 19
PIN_NUM_B2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUM_A1, GPIO.OUT)
GPIO.setup(PIN_NUM_B1, GPIO.OUT)

KEY_UP = 'a'
KEY_DOWN = 'z'

typedNum = 0.
typedChar = ""
direction = ""

pHeight = 0

def moveFixedTime(run_event):
    global KEY_UP, KEY_DOWN, typedNum, typedChar, direction
    while run_event.is_set():
        sleep(0.1)
        typedString = raw_input()
        typedChar = typedString.lower()
        if typedChar == KEY_UP:
            direction = KEY_UP
            print(25 * "*")
            print(25 * "-")
            print("Direction setted to: UP")
            print(25 * "-")
            print(25 * "*")
        elif typedChar == KEY_DOWN:
            print(25 * "*")
            direction = KEY_DOWN
            print(25 * "-")
            print("Direction setted to: DOWN")
            print(25 * "-")
            print(25 * "*")
        else:
            if direction != "":
                try:
                    typedNum = float(typedString) / 1000
                except Exception:
                    pass
            else: 
                print("### Err: Type number of milliseconds or change direction UP/DOWN (" + KEY_UP + "/" + KEY_DOWN + ")")

if __name__ == '__main__':
    print("First set direction:")
    run_event = threading.Event()
    run_event.set()
    t_moveDuringN = Thread(target=moveFixedTime, args=(run_event,))
    t_moveDuringN.daemon = True
    t_moveDuringN.start()
    try:
        while 1:
            sleep(0.01)
            # height =  r.get("height")
            # if pHeight != height: 
            #     print height
            #     pHeight = height

            if direction == KEY_UP:
                if typedNum != 0:
                    print(25 * "*")
                    print("------- MOVING UP -------")
                    print("GPIO " + str(PIN_NUM_A1) + ": " + "LOW")
                    print("GPIO " + str(PIN_NUM_A2) + ": " + "LOW")
                    print("GPIO " + str(PIN_NUM_B1) + ": " + "HIGH")
                    print("GPIO " + str(PIN_NUM_B2) + ": " + "HIGH")
                    print(25 * "-")
                    GPIO.output(PIN_NUM_A1, GPIO.LOW)
                    # GPIO.output(PIN_NUM_A2, GPIO.LOW)
                    GPIO.output(PIN_NUM_B1, GPIO.HIGH)
                    # GPIO.output(PIN_NUM_B2, GPIO.HIGH)
                    sleep(typedNum)
                    GPIO.output(PIN_NUM_A1, GPIO.HIGH)
                    # GPIO.output(PIN_NUM_A2, GPIO.HIGH)
                    GPIO.output(PIN_NUM_B1, GPIO.HIGH)
                    # GPIO.output(PIN_NUM_B2, GPIO.LOW)
                    print("GPIO " + str(PIN_NUM_A1) + " was low " + str(typedNum) + " s.")
                    print("GPIO " + str(PIN_NUM_A2) + " was low " + str(typedNum) + " s.")
                    print("GPIO " + str(PIN_NUM_B1) + " was hight " + str(typedNum) + " s.")
                    print("GPIO " + str(PIN_NUM_B2) + " was hight " + str(typedNum) + " s.")
                    print(25 * "-")
                    print("GPIO " + str(PIN_NUM_A1) + ": " + "HIGH")
                    print("GPIO " + str(PIN_NUM_A2) + ": " + "HIGH")
                    print("GPIO " + str(PIN_NUM_B1) + ": " + "LOW")
                    print("GPIO " + str(PIN_NUM_B2) + ": " + "LOW")
                    print("GPIO " + str(PIN_NUM_A1) + ": " + "HIGH")
                    print("--- FINISHED MOVEMENT ---")
                    print(25 * "*")
                    typedNum = 0
            elif direction == KEY_DOWN:
                if typedNum != 0:
                    print(25 * "*")
                    print("------ MOVING DOWN ------")
                    print("GPIO " + str(PIN_NUM_A1) + ": " + "HIGH")
                    print("GPIO " + str(PIN_NUM_A2) + ": " + "HIGH")
                    print("GPIO " + str(PIN_NUM_B1) + ": " + "LOW")
                    print("GPIO " + str(PIN_NUM_B2) + ": " + "LOW")
                    print(25 * "-")
                    GPIO.output(PIN_NUM_A1, GPIO.HIGH)
                    GPIO.output(PIN_NUM_B1, GPIO.LOW)
                    sleep(typedNum)
                    GPIO.output(PIN_NUM_A1, GPIO.HIGH)
                    GPIO.output(PIN_NUM_B1, GPIO.HIGH)
                    print("GPIO " + str(PIN_NUM_A1) + " was hight " + str(typedNum) + " s.")
                    print("GPIO " + str(PIN_NUM_A2) + " was hight " + str(typedNum) + " s.")
                    print("GPIO " + str(PIN_NUM_B1) + " was low " + str(typedNum) + " s.")
                    print("GPIO " + str(PIN_NUM_B2) + " was low " + str(typedNum) + " s.")
                    print(25 * "-")
                    print("GPIO " + str(PIN_NUM_A1) + ": " + "LOW")
                    print("GPIO " + str(PIN_NUM_A2) + ": " + "LOW")
                    print("GPIO " + str(PIN_NUM_B1) + ": " + "HIGH")
                    print("GPIO " + str(PIN_NUM_B2) + ": " + "HIGH")
                    print("--- FINISHED MOVEMENT ---")
                    print(25 * "*")
                    typedNum = 0
    except KeyboardInterrupt, SystemExit:
        GPIO.cleanup()
        run_event.clear()
        t_moveDuringN.join(0)
print("Stopped!")