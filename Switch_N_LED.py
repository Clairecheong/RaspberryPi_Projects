#import the python libraries needed
import RPi.GPIO as GPIO #import library RPi.GPIO & calling it GPIO
import time             #import time library to call time.sleep (delay)

#set the GPIO mode to Broadcom pin
GPIO.setmode(GPIO.BCM) #Broadcom(BCM) use to configure Raspberry Pi pins using the Broadcom channel num.

GPIO.setwarnings(False)#Suppresse any warnings generated by RPi.GPIO library

#set the pins and if its an output or input
LED = 21                #assign GPIO pin number 21 as LED 
SW = 26                 #assign GPIO pin number 26 as SW
GPIO.setup(LED,GPIO.OUT)#set the LED GPIO pin as an output
GPIO.setup(SW,GPIO.IN)  #set the SW GPIO pin as an output


#--------- coding situation: when switch is on LED turn on, when switch is off LED turns off ---------

while True:
    SW_state= GPIO.input(26) #resigning pin 26 as SW_state

    if SW_state == True:     #when switch is switched {checking: on switch}
        print ("LED on")     #print "LED on" in the terminal
        GPIO.output(LED,True)#Turn on the LED
        time.sleep(2)        #wait 2 seconds
    else: 
        print ("LED off")      #print LED on in the terminal    
        GPIO.output(LED,False) #Turn off the LED
        time.sleep(2)          #wait 2 seconds

#Clean up GPIO and release resources
GPIO.cleanup#Clean up