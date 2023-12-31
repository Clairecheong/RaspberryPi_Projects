#import the python libraries needed
import RPi.GPIO as GPIO #import library RPi.GPIO & calling it GPIO
import time             #import time library to call time.sleep (delay)     

GPIO.setwarnings(False)#Suppresse any warnings generated by RPi.GPIO library
#set the GPIO mode to Broadcom pin
GPIO.setmode(GPIO.BCM) #Broadcom(BCM) use to configure Raspberry Pi pins using the Broadcom channel num.

#set the pins and if its an output or input
LED = 16                 #assign GPIO pin number 16 as LED
PIR = 26                 #assign GPIO pin number 26 as PIR
GPIO.setup(PIR,GPIO.IN)  #set the PIR(motion sensor) GPIO pin as an input
GPIO.setup(LED, GPIO.OUT)#set the LED GPIO pin as an output

#---------Coding situation: When motion is detected, LED turn on. & When motion is not detected,LED turn off ---------
while True:
    PIR_state = GPIO.input(16)   #resigning pin 16 as PIR_state instead PIR

    if PIR_state == False:       #When PIR detects movements 
        GPIO.output(LED, True)   #LED turn on 
        print ("Motion Detected")#print in "Motion Detected" in the terminal
        time.sleep (5)           #wait for 5 seconds
    else:                        #When PIR detectes no movements
        print("no Detection")    #print in "no Detection" in the terminal
        GPIO.output(LED, False)  #LED turn off
        time.sleep(5)            #wait for 5 seconds

#Clean up GPIO and release resources
GPIO.cleanup() #clean up   