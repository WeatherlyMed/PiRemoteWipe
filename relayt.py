#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
relay_pin = 17
GPIO.setup(relay_pin, GPIO.OUT)

def trigger_relay():
    GPIO.output(relay_pin, GPIO.HIGH)
    time.sleep(60)
    GPIO.output(relay_pin, GPIO.LOW)

try:
    while True:
        trigger_relay()
        print("killed")
        time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
