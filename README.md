## AUTOMATIC OBJECT USING ULTASONIC SENSOR WITH RASPBERRY PI:

In this project I’m using ultrasonic sensor, raspberry pi and camera module to detect and capture image of an object when placed in a Targeted area.
	
## Description:

This project is divided into two parts. First we need to find if an object is placed in the targeted area, So to detect the object we are using ultrasonic sensor which is used to detect distance of object. Ultrasonic sensor consists of two main components i.e. Transmitter(trig) and Receiver(echo). First ultrasonic frequency Trigger pulse is given in trig pin and the echo pulse is receiver in echo pin. We know that 
	
Distance = speed * time
	
To find distance, time difference between trigged pulse and echo pulse and is multiplied with speed of ultrasonic pulse (17150 cm\s).
	
Lets assume that the maximum distance of targeted are is 20 cm. If an object is placed in targeted area, the distance is reduced below 20cm. then camera function can be called to capture the image of object. The captured image is stored in specified folder
