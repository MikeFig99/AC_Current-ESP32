from machine import Pin
from machine import ADC
from machine import deepsleep
from time import ticks_ms

pin = Pin(34)
button = Pin(0)

adc=ADC(pin)
adc.atten(ADC.ATTN_11DB)

s = 0.066			#Sensibility

def getAverage():
    average = 0
    n = 0
    t = ticks_ms()

    while (ticks_ms() - t) <= 200:
        n += 1
        average += 3.3*adc.read()/4095
    
    return (average/n,n)
    
while True:
    if button.value() == 1:
        (average,n) = getAverage()
        print("Average:",average)
        print("Samples:",n)
               
        deepsleep(1000)

    else:
        break

