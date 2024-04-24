import board
import busio
import digitalio as dio
from circuitpython_nrf24l01.rf24 import RF24

# SPI Pin Configuration
mosi = board.MOSI
miso = board.MISO
sck = board.SCK

# SPI Bus
spi = busio.SPI(sck, MOSI=mosi, MISO=miso)

# NRF24L01+ Pin Configuration
ce = dio.DigitalInOut(board.D17)
csn = dio.DigitalInOut(board.D8)

print(spi._pins)

# NRF24L01+ Initialization
nrf = RF24(spi, csn, ce)