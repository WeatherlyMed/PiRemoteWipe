import RPi.GPIO as GPIO
import time
charge_ch = 25 ##Controls battery flow

relay_ch = 26 ##Controls Capicitor Dump

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(relay_ch, GPIO.OUT)
GPIO.setup(charge_ch, GPIO.OUT)
GPIO.output(charge_ch_ch, GPIO.HIGH)
GPIO.output(relay_ch, GPIO.LOW)
time.sleep(60) ##Charge Cap for 1 minute
GPIO.output(relay_ch, GPIO.HIGH)

GPIO.cleanup()