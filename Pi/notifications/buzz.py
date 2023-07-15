import sys
import RPi.GPIO as GPIO
import time

triggerPIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN,GPIO.OUT)


buzzer = GPIO.PWM(triggerPIN, 100) # Set frequency to 1 Khz
buzzer.start(10) # Set dutycycle to 10

time.sleep(5)
GPIO.cleanup()
