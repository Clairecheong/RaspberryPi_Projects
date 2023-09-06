#import the python libraries needed
import RPi.GPIO as GPIO #import library RPi.GPIO & calling it GPIO
import time

#set the GPIO mode to Broadcom pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set the pins and if its an output or input
BUTTON_PIN = 16                                          #assign GPIO pin number 16 as BUTTON_PIN
LED =26                                                  #assign GPIO pin number 26 as LED 
GPIO.setup(LED,GPIO.OUT)                                 #set the LED GPIO pin as an output
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)#set the PushButton GPIO pin as an input


#---------Coding situation: When pushbutton is pressed LED turn on. N When pushbutton is not pressed LED turn off ---------
while True:
    button_state = GPIO.input(16) #resigning pin 16 as button_state instead of BUTTON_PIN
    
    if button_state == False:     #when pushbutton is pressed
        print ("LED on")          #print "LED on" in the terminal
        GPIO.output(LED,GPIO.HIGH)#Turn on LED
    else:                        #when pushbutton is not pressed
        GPIO.output(LED,GPIO.LOW)#Turn off LED

GPIO.cleanup()#Clean up