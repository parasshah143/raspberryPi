import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import datetime
import os
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setwarnings(False)
touch_pin = 17 # input of  touch sensor
GPIO.setup(touch_pin, GPIO.IN) #GPIO 17  and 11
led_output = 4 # output of led_output GPIO 4  pin 7
GPIO.setup(led_output, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
date = datetime.datetime.now()
timestamp = date.strftime("%Y/%m/%d %H:%M")
def dotime():
	import datetime
        now=datetime.datetime.now()
        global timestring
        timestring = now.strftime("%m-%d-%Y %H:%M:%S") 
f = open("foo.txt", "a+")
while True:
	print(GPIO.input(touch_pin))
	if GPIO.input(touch_pin) == 1:
		GPIO.output(led_output, True)
		print("Touch")
		f.write('\n touch ')
		f.write(timestamp)
	else:
		GPIO.output(led_output, False)
		print("No Touch")
		f.write('\n No touch ')
		f.write(timestamp)
	time.sleep(0.5)
