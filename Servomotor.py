# Import the python libraries needed
import RPi.GPIO as GPIO # Import library RPi.GPIO & calling it GPIO
import time             # Import time library to call time.sleep (delay)

# Set the GPIO mode to Broadcom pin
GPIO.setmode(GPIO.BCM)  # Broadcom(BCM) use to configure Raspberry Pi pins using the Broadcom channel nu
GPIO.setwarnings(False) # Suppresse any warnings generated by RPi.GPIO library

# Set the GPIO pin you connected the servo signal wire to
servo_pin = 17                  # Assign GPIO pin number 17 as servo motor 
GPIO.setup(servo_pin, GPIO.OUT) # Set the servo_pin GPIO pin as an output

# Create a PWM object
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms period)

# Start the PWM with 0% duty cycle (servo at one extreme position)
pwm.start(2.5)


while True:
    # Move the servo to the other extreme position
    pwm.ChangeDutyCycle(12.5)
    # Wait 1 Second
    time.sleep(1)
    # Move the servo back to the initial position
    pwm.ChangeDutyCycle(2.5)
    # Wait 1 Second
    time.sleep(1)

# Clean up
pwm.stop()
# Clean up GPIO and release resources
GPIO.cleanup() 
