#!/usr/bin/env python3
# Write an 8x8 Red/Green LED matrix
# https://www.adafruit.com/product/902

import smbus
import time

bus = smbus.SMBus(1)
matrix = 0x70

delay = 1  # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)  # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)  # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xE7, 0)  # Full brightness (page 15)

# The first byte is GREEN, the second is RED.
smile = [
    0x00,
    0x3C,
    0x00,
    0x42,
    0x28,
    0x89,
    0x04,
    0x85,
    0x04,
    0x85,
    0x28,
    0x89,
    0x00,
    0x42,
    0x00,
    0x3C,
]
frown = [
    0x3C,
    0x00,
    0x42,
    0x00,
    0x85,
    0x20,
    0x89,
    0x00,
    0x89,
    0x00,
    0x85,
    0x20,
    0x42,
    0x00,
    0x3C,
    0x00,
]
neutral = [
    0x3C,
    0x3C,
    0x42,
    0x42,
    0xA9,
    0xA9,
    0x89,
    0x89,
    0x89,
    0x89,
    0xA9,
    0xA9,
    0x42,
    0x42,
    0x3C,
    0x3C,
]

bus.write_i2c_block_data(matrix, 0, frown)
for fade in range(0xEF, 0xE0, -1):
    bus.write_byte_data(matrix, fade, 0)
    time.sleep(delay / 10)

bus.write_i2c_block_data(matrix, 0, neutral)
for fade in range(0xE0, 0xEF, 1):
    bus.write_byte_data(matrix, fade, 0)
    time.sleep(delay / 10)

bus.write_i2c_block_data(matrix, 0, smile)
