import RPi.GPIO as GPIO
relay_ch = 26
##This is the pin attached to the relay

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_ch, GPIO.OUT)
GPIO.setup(relay_ch, GPIO.LOW)
