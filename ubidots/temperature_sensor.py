from ubidots import ApiClient
import random
import time
import Adafruit_BBIO.ADC as ADC
sensor_pin = 'P9_39'
ADC.setup()
#Create an "API" object

api = ApiClient("88a38af294d0281ee1153b650ad13ce8314833f4")

#Create a "Variable" object

test_variable = api.get_variable("56b047d67625425379ae8359")

#Here is where you usually put the code to capture the data, either through your GPIO pins or as a calculation. We'll simply put a random value here:

while True:
	test_value = ADC.read(sensor_pin)
	#Write the value to your variable in Ubidots
	volt = test_value * 1800
	digital = ((volt*4096)/1800/23)
	test_variable.save_value({'value':digital})
	print('Temperature is %d' %digital)
	time.sleep(1)
