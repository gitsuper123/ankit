from machine import Pin
from time import sleep
led = Pin(2,Pin.OUT)
while 1:
  led.value(0)
  sleep(0.5)
  led.value(1)
  sleep(0.5)
