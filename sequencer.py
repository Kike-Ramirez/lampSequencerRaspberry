# TODO:
# 	- Reset 'value' on receivedBool == True


import time
import math
from scipy import signal


receivedBool = True
receivedStr = "sin-7.4566530197519745-CW"
wave = ""
speed = 0.
rotation = ""
value = 0.
prevPos = -1





def translate(val, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(val - leftMin) / float(leftSpan)

    return rightMin + (valueScaled * rightSpan)



if __name__ == '__main__':

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
				time.sleep(1/speed)
				seqPos = math.floor(translate(math.sin(value), -1, 1, 0, 8))
			elif wave == 'tri':
				if receivedBool:
					value = 0
				time.sleep(1/speed)
				seqPos = math.floor(translate(abs(signal.sawtooth(value)), 1, 0, 0, 8))
			elif wave == 'ramp':
				if receivedBool:
					value = 0
				time.sleep(0.5/speed)
				seqPos = math.floor(translate(signal.sawtooth(value), -1, 1, 0, 8))

			if rotation == 'CCW':
				seqPos = 7 - seqPos


			if prevPos != seqPos:
				if seqPos == 0: 
					print('Relay 1')
				if seqPos == 1:
					print('Relay 2')
				if seqPos == 2:
					print('Relay 3')
				if seqPos == 3:
					print('Relay 4')
				if seqPos == 4:
					print('Relay 5')
				if seqPos == 5:
					print('Relay 6')
				if seqPos == 6:
					print('Relay 7')
				if seqPos == 7:
					print('Relay 8')
			prevPos = seqPos


			value += speed / 100
			receivedBool = False		# Indent when if condition added
			# print(seqPos)



		except KeyboardInterrupt, SystemExit:
			raise SystemExit


