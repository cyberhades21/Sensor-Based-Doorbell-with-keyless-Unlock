from pushbullet import Pushbullet
def push():
    pb = Pushbullet("Your API here")
    dev = pb.get_device('Your Device Here')
    push = dev.push_note("Alert!!", "someone is Knockin the Door")
def buzz():
    import sys
    import RPi.GPIO as GPIO
    import time

    triggerPIN = 32
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(triggerPIN,GPIO.OUT)

    buzzer = GPIO.PWM(triggerPIN, 1000) 
    buzzer.start(10) 

    time.sleep(1)
