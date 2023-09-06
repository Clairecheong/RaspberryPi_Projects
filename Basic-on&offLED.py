#import the python libraries needed
import RPi.GPIO as GPIO #import library RPi.GPIO & calling it GPIO
import time

#set the GPIO mode to Broadcom pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set the pins and if its an output or input
LED =21                 #assign GPIO pin number 21 as LED 
GPIO.setup(LED,GPIO.OUT)#set the LED GPIO pin as an output

#--------- coding to on and off the led ---------

print ("LED on")          #print LED on in the terminal
GPIO.output(LED,GPIO.HIGH)#Turn on the LED

time.sleep(5)             #Wait 5 seconds

print ("LED off")        #print LED on in the terminal    
GPIO.output(LED,GPIO.LOW)#Turn off the LED