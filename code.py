# EatYourSheep
# 02-09-2023, updated 02-13-2023.
# code.py

import time
from adafruit_circuitplayground import cp

# Color variables.
RED = (50, 0, 0)
GREEN = (0, 50, 0)
LED_OFF = (0, 0, 0)


# Blinks LED for one second.
# ledclr specifies color.
def led_sec(ledclr):
    cp.pixels.fill(ledclr)
    time.sleep(1)
    cp.pixels.fill(LED_OFF)

# Handles button presses.
# True is the "A" button, False for "B".
# Plays a sound file and then calls led_sec.
def button_press(button):
    if button:
        print("A button pressed.")
        cp.play_file("oof.wav")
        led_sec(RED)
    else:
        print("B button pressed.")
        cp.play_file("mc.wav")
        led_sec(GREEN)


# Main program. Plays Roblox and Minecraft
# OOF sounds, then shines a color.
while True:
    if cp.button_a:
        button_press(True)
    if cp.button_b:
        button_press(False)
