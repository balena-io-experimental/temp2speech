#!/usr/bin/python
import time, os, subprocess
import RPi.GPIO as GPIO
# https://github.com/timofurrer/w1thermsensor
from w1thermsensor import W1ThermSensor

# Get the desired unit to measure by
unit = os.getenv('UNIT', 'celsius')

# set up GPIO on pin 17 for button press
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# initialise sensor
sensor = W1ThermSensor()
temperature = None

def read_temp():
	# uses tim furrer's w1thermsensor to read temperatures from the sensor depending resin envar.
	if unit == 'kelvin':
		temperature = sensor.get_temperature(W1ThermSensor.KELVIN)
	elif unit == 'fahrenheit':
		temperature = sensor.get_temperature(W1ThermSensor.DEGREES_F)
	elif unit == 'celsius':
		temperature = sensor.get_temperature()
	return temperature

def speak_temp(temperature): 
	# uses googles text to speech to get audiofile and passes it to mplayer
	temp_string = "The temperature is " + str(temperature) + "degrees " + unit
	subprocess.call(["chmod", "u+x", "/app/speech.sh"])
	subprocess.call(["/app/speech.sh", temp_string])

while True:
    input_state = GPIO.input(17)
    if input_state == False:
        print('Button Pressed')
        temperature = read_temp()
        speak_temp(temperature)
        time.sleep(0.2)