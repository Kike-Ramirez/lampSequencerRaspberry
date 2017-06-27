# TODO:
# 	- Refresh properties only when receivedBool == True

import RPi.GPIO as GPIO
from time import sleep
import math
from scipy import signal




PIN_NUM_1 = 4
PIN_NUM_2 = 17
PIN_NUM_3 = 18
PIN_NUM_4 = 10
PIN_NUM_5 = 25
PIN_NUM_6 = 7
PIN_NUM_7 = 5
PIN_NUM_8 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUM_1, GPIO.OUT)
GPIO.setup(PIN_NUM_2, GPIO.OUT)
GPIO.setup(PIN_NUM_3, GPIO.OUT)
GPIO.setup(PIN_NUM_4, GPIO.OUT)
GPIO.setup(PIN_NUM_5, GPIO.OUT)
GPIO.setup(PIN_NUM_6, GPIO.OUT)
GPIO.setup(PIN_NUM_7, GPIO.OUT)
GPIO.setup(PIN_NUM_8, GPIO.OUT)


def translate(val, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(val - leftMin) / float(leftSpan)

    return rightMin + (valueScaled * rightSpan)



if __name__ == '__main__':


	GPIO.output(PIN_NUM_1, GPIO.HIGH)
	GPIO.output(PIN_NUM_2, GPIO.HIGH)
	GPIO.output(PIN_NUM_3, GPIO.HIGH)
	GPIO.output(PIN_NUM_4, GPIO.HIGH)
	GPIO.output(PIN_NUM_5, GPIO.HIGH)
	GPIO.output(PIN_NUM_6, GPIO.HIGH)
	GPIO.output(PIN_NUM_7, GPIO.HIGH)
	GPIO.output(PIN_NUM_8, GPIO.HIGH)

	receivedBool = True
	receivedStr = "tri-10-CCW"
	wave = ""
	speed = 0.
	rotation = ""
	value = 0.
	seqPos = 0
	prevPos = -1

	

	while True:
		try:
			# if ...:
			# 	receivedBool = True


			wave = receivedStr.split("-")[0]
			speed = float(receivedStr.split("-")[1])
			rotation = receivedStr.split("-")[2]

			if wave == 'sin':
				if receivedBool:
					value = -1
				sleep(1/(speed + 0.01))
				seqPos = math.floor(translate(math.sin(value), -1, 1, 0, 8))
			elif wave == 'tri':
				if receivedBool:
					value = 0
				sleep(1/(speed + 0.01))
				seqPos = math.floor(translate((abs(signal.sawtooth(value)*2)-1), 0-1, 1, 0, 8))
			elif wave == 'ramp':
				if receivedBool:
					value = 0
				sleep(0.5/(speed + 0.01))
				seqPos = math.floor(translate(signal.sawtooth(value), -1, 1, 0, 8))

			if rotation == 'CCW':
				seqPos = 7 - seqPos


			if prevPos != seqPos and speed != 0:
				if seqPos == 0:
					GPIO.output(PIN_NUM_1, GPIO.LOW)
					GPIO.output(PIN_NUM_2, GPIO.HIGH)
					GPIO.output(PIN_NUM_3, GPIO.HIGH)
					GPIO.output(PIN_NUM_4, GPIO.HIGH)
					GPIO.output(PIN_NUM_5, GPIO.HIGH)
					GPIO.output(PIN_NUM_6, GPIO.HIGH)
					GPIO.output(PIN_NUM_7, GPIO.HIGH)
					GPIO.output(PIN_NUM_8, GPIO.HIGH)
					print('Relay 1')
				if seqPos == 1:
					GPIO.output(PIN_NUM_2, GPIO.LOW)
					GPIO.output(PIN_NUM_1, GPIO.HIGH)
					GPIO.output(PIN_NUM_3, GPIO.HIGH)
					GPIO.output(PIN_NUM_4, GPIO.HIGH)
					GPIO.output(PIN_NUM_5, GPIO.HIGH)
					GPIO.output(PIN_NUM_6, GPIO.HIGH)
					GPIO.output(PIN_NUM_7, GPIO.HIGH)
					GPIO.output(PIN_NUM_8, GPIO.HIGH)
					print('Relay 2')
				if seqPos == 2:
					GPIO.output(PIN_NUM_3, GPIO.LOW)
					GPIO.output(PIN_NUM_1, GPIO.HIGH)
					GPIO.output(PIN_NUM_2, GPIO.HIGH)
					GPIO.output(PIN_NUM_4, GPIO.HIGH)
					GPIO.output(PIN_NUM_5, GPIO.HIGH)
					GPIO.output(PIN_NUM_6, GPIO.HIGH)
					GPIO.output(PIN_NUM_7, GPIO.HIGH)
					GPIO.output(PIN_NUM_8, GPIO.HIGH)
					print('Relay 3')
				if seqPos == 3:
					GPIO.output(PIN_NUM_4, GPIO.LOW)
					GPIO.output(PIN_NUM_1, GPIO.HIGH)
					GPIO.output(PIN_NUM_2, GPIO.HIGH)
					GPIO.output(PIN_NUM_3, GPIO.HIGH)
					GPIO.output(PIN_NUM_5, GPIO.HIGH)
					GPIO.output(PIN_NUM_6, GPIO.HIGH)
					GPIO.output(PIN_NUM_7, GPIO.HIGH)
					GPIO.output(PIN_NUM_8, GPIO.HIGH)
					print('Relay 4')
				if seqPos == 4:
					GPIO.output(PIN_NUM_5, GPIO.LOW)
					GPIO.output(PIN_NUM_1, GPIO.HIGH)
					GPIO.output(PIN_NUM_2, GPIO.HIGH)
					GPIO.output(PIN_NUM_3, GPIO.HIGH)
					GPIO.output(PIN_NUM_4, GPIO.HIGH)
					GPIO.output(PIN_NUM_6, GPIO.HIGH)
					GPIO.output(PIN_NUM_7, GPIO.HIGH)
					GPIO.output(PIN_NUM_8, GPIO.HIGH)
					print('Relay 5')
				if seqPos == 5:
					GPIO.output(PIN_NUM_6, GPIO.LOW)
					GPIO.output(PIN_NUM_1, GPIO.HIGH)
					GPIO.output(PIN_NUM_2, GPIO.HIGH)
					GPIO.output(PIN_NUM_3, GPIO.HIGH)
					GPIO.output(PIN_NUM_4, GPIO.HIGH)
					GPIO.output(PIN_NUM_5, GPIO.HIGH)
					GPIO.output(PIN_NUM_7, GPIO.HIGH)
					GPIO.output(PIN_NUM_8, GPIO.HIGH)
					print('Relay 6')
				if seqPos == 6:
					GPIO.output(PIN_NUM_7, GPIO.LOW)
					GPIO.output(PIN_NUM_1, GPIO.HIGH)
					GPIO.output(PIN_NUM_2, GPIO.HIGH)
					GPIO.output(PIN_NUM_3, GPIO.HIGH)
					GPIO.output(PIN_NUM_4, GPIO.HIGH)
					GPIO.output(PIN_NUM_5, GPIO.HIGH)
					GPIO.output(PIN_NUM_6, GPIO.HIGH)
					GPIO.output(PIN_NUM_8, GPIO.HIGH)
					print('Relay 7')
				if seqPos == 7:
					GPIO.output(PIN_NUM_8, GPIO.LOW)
					GPIO.output(PIN_NUM_1, GPIO.HIGH)
					GPIO.output(PIN_NUM_2, GPIO.HIGH)
					GPIO.output(PIN_NUM_3, GPIO.HIGH)
					GPIO.output(PIN_NUM_4, GPIO.HIGH)
					GPIO.output(PIN_NUM_5, GPIO.HIGH)
					GPIO.output(PIN_NUM_6, GPIO.HIGH)
					GPIO.output(PIN_NUM_7, GPIO.HIGH)
					print('Relay 8')
			prevPos = seqPos


			value += speed / 100
			receivedBool = False		# Indent when if condition added



		except KeyboardInterrupt, SystemExit:
			GPIO.cleanup()
			raise SystemExit


