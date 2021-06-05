import RPi.GPIO as GPIO
import time
import datetime
from picamera import PiCamera
from time import sleep
camera=PiCamera()

GPIO.setmode(GPIO.BOARD)
pulse_start=0
pulse_end=0
distance=0
pulse_duration=0
trig = 16
echo = 18
i=1
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.output(trig, False)
print ("Calibrating......")
time.sleep(1)

try:
    while True:
        GPIO.output(trig,True)
        time.sleep(0.000001)
        GPIO.output(trig, False)
        while GPIO.input(echo)==0:
            pulse_start =time.time()
        while GPIO.input(echo)==1:
            pulse_end=time.time()
        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration*17150
        distance=round(distance+1.15,2)
        print (distance)
         
        if distance<22:
            camera.start_preview()
               
            sleep(2)
            camera.capture('/home/pi/Desktop/captured/image%s.jpg' % i)
            i=i+1
            camera.stop_preview()
            print("captured object")
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()