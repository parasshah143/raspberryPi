import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setwarnings(False)
##Define a function named Blink()
def Blink(numTimes,speed):
	for i in range(0,numTimes):## Run loop numTimes
		print "Paras_LED " + str(i+1)## Print current loop
		GPIO.output(7,True)## Switch on pin 7
		time.sleep(speed)## Wait
		GPIO.output(7,False)## Switch off pin 7
		time.sleep(speed)## Wait
	print "Paras LED Program is completed" ## When loop is complete, print "Done"
	GPIO.cleanup()
## Prompt user for input
Paras_LED = raw_input("Enter the total number of times to blink: ")
speed = raw_input("Enter the length of each blink in seconds: ")

## Start Blink() function. Convert user input from strings to numeric data types and pass to Blink() as parameters
Blink(int(Paras_LED),float(speed))
        