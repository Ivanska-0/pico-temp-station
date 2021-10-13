"""
Based on code by Alex Newton
https://how2electronics.com/interfacing-dht11-temperature-humidity-sensor-with-raspberry-pi-pico/
© Copyright 2021, All Rights Reserved  | How To Electronics

Modified by Ivanska
"""

from machine import Pin, I2C
import utime as time
from dht import DHT11

while True:
    time.sleep(1)
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    f = open("temps.txt", "a")
    f.write("Temperature: {}, Humidity: {}\n".format(sensor.temperature, sensor.humidity))
    f.close()
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
    
    time.sleep(5)
