#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

def setup(leds):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    for led in leds:
        GPIO.setup(led, GPIO.OUT)

def turn_all_off(leds):
    for led in leds:
        GPIO.output(led, False)

def turn_all_on(leds):
    for led in leds:
        GPIO.output(led, True)

def rolling_lights(leds):
    print("Running Rolling Lights")
    try:
        while True:
            for led in leds:
                GPIO.output(led, True)
                sleep(.5)
                GPIO.output(led, False)
                sleep(.5)

    except KeyboardInterrupt:
        print("\nProgram exiting, turning off leds.")
        turn_all_off(leds)

def flash_x_times(leds, amount_to_flash):
    for _ in range(amount_to_flash):
        turn_all_on(leds)
        sleep(.1)
        turn_all_off(leds)
        sleep(.1)

def display_bin_num(bin, leds):
    
    bin_list = list(bin)
    for i in range(8):
        if bin_list[i] == '1':
            GPIO.output(leds[i], True)
    
    sleep(.5)
    turn_all_off(leds)

def blinking_binaries(leds):
    print("Running Blinking Binaries")

    for num in range(256):
        bin_rep = format(num, '08b')
        print("Displaying: {0}, {1}".format(num, bin_rep))
        display_bin_num(bin_rep, leds)

def main(leds):
    print("Program Running.")

    try:
        flash_x_times(leds, 5)
        blinking_binaries(leds)
        flash_x_times(leds, 5)


    except KeyboardInterrupt:
        print("\nProgram exiting, turning off leds.")
        turn_all_off(leds)

if __name__=="__main__":
    # leds = [7, 11, 15, 29, 31, 33, 37, 13]
    leds = [13, 37, 33, 31, 29, 15, 11, 7]
    setup(leds)
    main(leds)