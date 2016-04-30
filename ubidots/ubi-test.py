from ubidots import ApiClient
import random
import time

#Create an "API" object

api = ApiClient("88a38af294d0281ee1153b650ad13ce8314833f4")

#Create a "Variable" object

test_variable = api.get_variable("56b047d67625425379ae8359")

#Here is where you usually put the code to capture the data, either through your GPIO pins or as a calculation. We'll simply put a random value here:

while True:
	test_value = random.randint(1,100)
	#Write the value to your variable in Ubidots
	test_variable.save_value({'value':test_value})
	print('Random value is %d' %test_value)
	time.sleep(1)
