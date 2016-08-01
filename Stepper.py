# Stepper Command Library

import RPi.GPIO as GPIO
import time
from math import floor

def main():
	# Pin Definitions:
	stepPin = 21
	dirPin = 16

	# Pin setup
	GPIO.setmode(GPIO.BCM)

	myStepper = Stepper(stepPin, dirPin)

	
	myStepper.goToBottle(2)
	time.sleep(4)
	myStepper.goToBottle(4)
	time.sleep(4)
	myStepper.goToBottle(7)
	time.sleep(4)
	myStepper.goToBottle(1)
	time.sleep(4)
	myStepper.goToBottle(6)
	time.sleep(4)
	myStepper.goToBottle(3)
	time.sleep(4)
	myStepper.goToBottle(5)
	time.sleep(4)
	myStepper.goToPosition(0)
	
	

	

	GPIO.cleanup()
	print "Clean"

class Stepper():
	
	def __init__(self, stepPin, dirPin):
		"""
		This function initializes all properties of the stepper motor
		"""
		self.minSpeed = 5. 	# RPM
		self.accel = 2. 		# RPM / step
		
		
		self.stepPin = stepPin	# The GPIO pin for the stepper driver
		self.dirPin = dirPin	# The GPIO pin designating direction
		GPIO.setup(stepPin, GPIO.OUT)	# Setup the pins for use
		GPIO.setup(dirPin, GPIO.OUT)
		
		
		self.setDirection(GPIO.HIGH) 	                             
		self.setMaxSpeed(250)
		self.setSpeed(60)
		
		self.inchesPerRotation = 1.26
		self.stepsPerRotation = 200
		self.position = 0
	
		self.pos_dic = {}
		self.pos_dic[1] = 2
		self.pos_dic[2] = 7
		self.pos_dic[3] = 11.5
		self.pos_dic[4] = 16.25
		self.pos_dic[5] = 21
		self.pos_dic[6] = 26
		self.pos_dic[7] = 29.2
	
	def oneStep(self):
		"""
		"""
		GPIO.output(self.stepPin, GPIO.HIGH)
		time.sleep(self.pause_time)
		GPIO.output(self.stepPin, GPIO.LOW)
		time.sleep(self.pause_time)
	
	def setDirection(self, direc):
		"""
		"""
		GPIO.output(self.dirPin, direc)	
		self.direction = direc
		
	def setSpeed(self, rpm):
		self.speed = min(rpm, self.MaxSpeed)
		self.pause_time = 60./400./rpm
	
	def setMaxSpeed(self, maxRPM):
		self.MaxSpeed = maxRPM
		
	def movenSteps(self, nSteps):
		print "Moving %d steps" % nSteps
		self.setSpeed(self.minSpeed)
		
		ndecelSteps = (self.MaxSpeed - self.minSpeed) / self.accel
		
		for step_count in range(nSteps):
			self.oneStep()
			if step_count < (nSteps - ndecelSteps):
				self.setSpeed( min(self.speed + self.accel, self.MaxSpeed))		
			else:
				self.setSpeed( max(self.speed - self.accel, self.minSpeed))
		
			
	def moveInches(self, inches):
		if inches > 0:
			self.setDirection(GPIO.HIGH)
		else:
			self.setDirection(GPIO.LOW)
			
		self.movenSteps(abs(int(floor(inches/(self.inchesPerRotation/self.stepsPerRotation)))))
		self.position += inches

	
	def goToPosition(self, inches):
		if inches < 0:
			print "You fool"
			exit()	
		
		if inches > 30.5:
			print "You fool"
			exit()
		
		self.moveInches(inches-self.position)
	
	def goToBottle(self, bottle_num):
		
		self.goToPosition(self.pos_dic[bottle_num])
		
if __name__ == "__main__":
	main()
