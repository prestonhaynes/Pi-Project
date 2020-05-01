#!/usr/bin/python

# Ryan Kupka, Preston Haynes, Aidan Irish, Wenning Jiang, Muhammad Hassan Rao, Sanskriti Timseena

import sys
import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

print('Temp: {0:0.1f} C'.format(temperature))
