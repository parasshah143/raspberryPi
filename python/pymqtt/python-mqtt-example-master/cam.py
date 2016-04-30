import os
import time
import picamera

with picamera.PiCamera() as camera:
    #time.sleep(1)
    camera.capture('/home/pi/pymqtt/python-mqtt-example-master/image.jpg')
    print("Image captured")
    os.rename("/home/pi/pymqtt/python-mqtt-example-master/image.jpg", time.strftime("%Y%m%d%H%M%S.jpg"))
