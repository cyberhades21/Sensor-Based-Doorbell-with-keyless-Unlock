from pushbullet import Pushbullet
def push():
    pb = Pushbullet("o.tRVSrkyXbeyuBg3kyhwb7vvYt1EQTEN9")
    dev = pb.get_device('OnePlus AC2001')
    push = dev.push_note("Alert!!", "someone is Knockin the Door")

def buzz():
    import sys
    import RPi.GPIO as GPIO
    import time

    triggerPIN = 32
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(triggerPIN,GPIO.OUT)

    buzzer = GPIO.PWM(triggerPIN, 1000) # Set frequency to 1 Khz
    buzzer.start(10) # Set dutycycle to 10

    time.sleep(1)
