import time
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

##DECLARATION
TRIG = 3
ECHO = 2

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)
GPIO.setup(ECHO,GPIO.IN)

##THis method sets up the distance for ultrasonic sesnor
def distance():
    GPIO.output(TRIG, True)
    
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(ECHO)==0:
        StartTime = time.time()
    
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    distance =  TimeElapsed * 17150
    distance = round(distance,2)
    
    return distance

while True:
    
    time.sleep(1)
    dist = distance()
    
    print("distance (cm): ")
    print(str(dist) + "cm")
    
    if (dist > 100):
        print("No Obejects Detections")
    elif (dist < 100 and dist > 50):
        print("Object Detected: Further Away")
    elif (dist < 50 and dist > 25):
        print("Object Detected: Approaches")
    elif (dist < 25):
        print("Object Detected")
    
    
    
    
    
