import time
import struct
import board
from digitalio import DigitalInOut
import spidev
# if running this on a ATSAMD21 M0 based board
# from circuitpython_nrf24l01.rf24_lite import RF24
from circuitpython_nrf24l01.rf24 import RF24

SPI_BUS = spidev.SpiDev()  # for a faster interface on linux
CSN_PIN = 0  # use CE0 on default bus (even faster than using any pin)
#CE_PIN = DigitalInOut(board.D22)  # using pin gpio22 (BCM numbering)
CE_PIN = DigitalInOut(board.D17)

nrf = RF24(SPI_BUS, CSN_PIN, CE_PIN)

nrf.open_tx_pipe(b"test")
buffer = struct.pack("<f", 0.0)
nrf.listen = False
start_timer = time.monotonic_ns()  # start timer
result = nrf.send(buffer)
end_timer = time.monotonic_ns()  # end timer
if not result:
    print("send() failed or timed out")
else:
    print(
        "Transmission successful! Time to Transmit:",
        "{} us. Sent: {}".format((end_timer - start_timer) / 1000, [0.0]),
    )