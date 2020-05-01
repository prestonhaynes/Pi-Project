#!/usr/bin/python3

# Ryan Kupka, Preston Haynes, Aidan Irish, Wenning Jiang, Muhammad Hassan Rao, Sanskriti Timseena

import sys
import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

temperature = ((temperature * (9/5)) + 32)

print('Temp: {0:0.1f} F  Humidity: {1:0.1f} %'.format(temperature, humidity))
