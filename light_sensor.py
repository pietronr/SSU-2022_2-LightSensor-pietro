#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

__author__ = 'Adapted from Adafruit'
__license__ = "GPL"

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # Set pin 16 to be an output pin and set initial value to low (off)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # Idem for pin 18

#define the pin that goes to the circuit
pin_to_circuit = 29

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        light_level = rc_time(pin_to_circuit)
        #print(rc_time(pin_to_circuit))
        ledpin = 0
        if light_level < 20:
            print ('Day')
            ledpin = 16
            GPIO.output(ledpin,GPIO.LOW)
        else:
            print ('Night')
            ledpin = 18
            GPIO.output(ledpin,GPIO.HIGH)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
