# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Configure the count of pixels:
PIXEL_COUNT = 60

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

for j in range(10):
    pixels.clear()
    pixels.show()
    color = (255-25*j, 25*j, 0)
    pixels.set_pixel(0, Adafruit_WS2801.RGB_to_color(color[0], color[1], color[2]))
    pixels.show()
    time.sleep(5)
