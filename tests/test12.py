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

nrf.open_rx_pipe(0, b"test")
buffer = struct.pack("<f", 0.0)
nrf.listen = True
start = time.monotonic()
print("before while")
while (time.monotonic() - start) < 120:
    print("before if")
    if nrf.available():
        # grab information about the received payload
        print("before payload_size")
        payload_size, pipe_number = (nrf.any(), nrf.pipe)
        # fetch 1 payload from RX FIFO
        print("before buffer")
        buffer = nrf.read()  # also clears nrf.irq_dr status flag
        # expecting a little endian float, thus the format string "<f"
        # buffer[:4] truncates padded 0s if dynamic payloads are disabled
        print("before payload")
        payload = struct.unpack("<f", buffer[:4])[0]
        # print details about the received packet
        print(
            "Received {} bytes on pipe {}: {}".format(
                payload_size, pipe_number, payload[0]
            )
        )
        start = time.monotonic()

# recommended behavior is to keep in TX mode while idle
nrf.listen = False  # put the nRF24L01 is in TX mode