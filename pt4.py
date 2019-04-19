import spidev
from numpy import interp
from time import sleep

spi=spidev.SpiDev()
spi.open(0,0)

def analogInput(channel):
    spi.max_speed_hz=1350000
    adc=spi.xfer2([1,(8+channel)<<4,0])
    data=((adc[1]&3)<<8)+adc[2]
    return data

while True:
    output=analogInput(0)
    print(output)
    sleep(0.1)
