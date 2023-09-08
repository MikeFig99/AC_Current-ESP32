from machine import Pin
from machine import ADC
from machine import sleep
from machine import deepsleep
from math import sqrt

pin = Pin(34)
button = Pin(0)
adc=ADC(pin)
adc.atten(ADC.ATTN_11DB)

while True:
    if button.value() == 1:
        val1=adc.read()
        val2=3.3*val1/4095
        print('Raw value: ',val1,' and voltage: ',val2)
        deepsleep(10000)
    else:
        break
