#import the python libraries needed
import RPi.GPIO as GPIO #import library RPi.GPIO & calling it GPIO
import time 

#set the GPIO mode to Broadcom pin
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#set the pins and if its an output or input
LDR=22                 #assign GPIO pin number 22 as LDR
LED= 17                #assign GPIO pin number 17 as LED
GPIO.setup(22, GPIO.IN)#set the 22/ LDR GPIO pin as an input
GPIO.setup(17,GPIO.OUT)#set the 17/ LED GPIO pin as an output


while True:
    if LDR == GPIO.HIGH:           #When LDR detects light
        GPIO.output(17, False)     #turn LED off
        print("light detected")    #Print "light detected" in the terminal
        time.sleep(2)              #wait for 2seconds
    else:                          #When LDR does not detect light
        print ("no light detected")#print "no light detected"in the terminal
        GPIO.output(17,True)       #turn LED on
        time.sleep(5)              #wait for 5seconds

GPIO.cleanup #Clean up