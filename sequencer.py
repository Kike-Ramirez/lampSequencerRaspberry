import time
import math
from scipy import signal

receivedStr = "sin-7.4566530197519745-CCW"
wave = ""
step = 0.
speed = 0.
value = 0.
rotation = ""


if __name__ == '__main__':
	wave = receivedStr.split("-")[0]
	speed = float(receivedStr.split("-")[1])
	rotation = receivedStr.split("-")[2]

	while True:
		try:
			time.sleep(1/speed)
			# seqPos = math.floor((signal.sawtooth(speed) + 1) * 4)
			# seqPos = math.floor((abs(signal.sawtooth(speed))) * 8)
			

			if wave == 'sin':
				seqPos = math.floor((math.sin(value) + 1) * 4)
			elif wave == 'tri':
				seqPos = math.floor((abs(signal.sawtooth(value))) * 8)
			elif wave == 'ramp':
				seqPos = math.floor((signal.sawtooth(value) + 1) * 4)

			value += speed / 100
			print(seqPos)
		except KeyboardInterrupt, SystemExit:
			raise SystemExit


