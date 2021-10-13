"""
Based on code by Alex Newton
https://how2electronics.com/interfacing-dht11-temperature-humidity-sensor-with-raspberry-pi-pico/
© Copyright 2021, All Rights Reserved  | How To Electronics

Modified by Ivanska
"""

from machine import Pin, I2C
import utime as time
from dht import DHT11

SIX_H = 60*60*6 - 5
EIGHTEEN_H = 60*60*18 - 5
DAY = 0

LED = Pin(25, Pin.OUT)

def do_read(time):
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t = sensor.temperature
    h = sensor.humidity
    f = open("temps.csv", "a")
    f.write("{},{},{},{}\n".format(DAY,
                                   time,
                                   sensor.temperature,
                                   int(sensor.humidity)))
    f.close()


time.sleep(5)

while True:
    DAY += 1
    LED.value(True)
    do_read("0")
    time.sleep(5)
    LED.value(False)
    time.sleep(SIX_H)

    LED.value(True)
    do_read("1")
    time.sleep(5)
    LED.value(False)
    time.sleep(EIGHTEEN_H)

