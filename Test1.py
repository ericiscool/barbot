import RPi.GPIO as GPIO
import time


# Pin Definitions:
stepPin = 21
dirPin = 16

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(stepPin, GPIO.OUT)
GPIO.setup(dirPin, GPIO.OUT)

GPIO.output(dirPin, GPIO.HIGH)

for i in range(200):
	GPIO.output(stepPin, GPIO.HIGH)
	time.sleep(0.0005)
	GPIO.output(stepPin, GPIO.LOW)
	time.sleep(0.0005)

GPIO.cleanup()


