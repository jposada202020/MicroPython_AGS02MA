# SPDX-FileCopyrightText: Copyright (c) 2022 ladyada for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_ags02ma import AGS02MA

i2c = I2C(1, sda=Pin(2), scl=Pin(3), freq=20000)  # Correct I2C pins for RP2040
ags = AGS02MA(i2c)


while True:
    try:
        res = ags.gas_resistance / 1000
        print(f"Gas resistance: {res:.1f} Kohms")
        tvoc = ags.TVOC
        print(f"TVOC: {tvoc} ppb")
    except RuntimeError:
        print("Retrying....")
    time.sleep(1)
