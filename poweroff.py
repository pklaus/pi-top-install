# poweroff.py
#
# shuts power of pi-top hub controller off
# do not run except at the end of a shutdown !!!!

from datetime import datetime
import os
from spidev import SpiDev
import time
import sys

# Set states globally
current_brightness = 0
new_brightness = 0
screen_off = 0
shutdown = 0

# Parity bits
brightness_parity = 0
state_parity = 0

# Timeout limits
counter_max = 5

# Time to pause between command sends
cycle_sleep_time = 0.25

def setupSPI():
        spi = SpiDev()
        spi.open(0,1) # Bus 0, Chip Select 1
        spi.max_speed_hz = 9600
        spi.mode = 0b00
        spi.bits_per_word = 8
        spi.cshigh = True
        spi.lsbfirst = False
        return spi

# Calculates the parity of an integer, returning 0 if there are an even number of set bits, and 1 if there are an odd number
def parityOf(int_type):
        parity = 0
        for bit in bin(int_type)[2:]:
                parity ^= int(bit)
        return parity

def parseStateToBits():
        global current_brightness
        global new_brightness
        global brightness_change
        global screen_off
        global shutdown
        global brightness_parity
        global state_parity
        global newBrightness

        new_brightness= current_brightness

        # Set bits to send according to state variables 
        shutdown = 1
        screen_off = 0

        # print "Brightness parity: " + str(parityOf(current_brightness))
        brightness_parity = str(parityOf(new_brightness))
        # print "State parity: " + str(parityOf((2 * int(screen_off)) + shutdown))
        state_parity = str(parityOf((2 * int(screen_off)) + shutdown))

        # Determine new bits to send
        bitsToSend = (128 * int(brightness_parity)) + (8 * new_brightness) + (4 * int(state_parity)) + (2 * int(screen_off)) + shutdown
        # e.g. bits = "10101010" - # Brightness parity = 1, brightness = 5, state parity = 0, screen_off = 1, shutdown = 0

        return bitsToSend

def transceiveSPI(spi, bitsToSend):

        # print "Communicating with hub"
        bitsToSend_hex_str = '0x' + str(hex(bitsToSend))[2:].zfill(2)
        bitsToSend_bin_str = '{0:b}'.format(int(bitsToSend_hex_str[2:],16)).zfill(8)
        print "Sending:   " + bitsToSend_hex_str + " : " + bitsToSend_bin_str
        # Initiate receiving communication from hub
        spi.cshigh = False
        # Transfer data with hub
        resp = spi.xfer2([bitsToSend], spi.max_speed_hz)
        spi.cshigh = True
        
        resp_hex = hex(resp[0])
        
        resp_hex_str = '0x' + str(resp_hex)[2:].zfill(2)
        resp_bin_str = '{0:b}'.format(int(resp_hex_str[2:],16)).zfill(8)
        print "Receiving: " + resp_hex_str + " : " + resp_bin_str
        
        # return (resp_hex, resp_bin_str)
        return resp_bin_str

def getInitData(spi):
        global current_brightness
        global screen_off
        global shutdown

        valid = False

        # This will cycle through forever until the Pi is communicating with the hub

        last_brightness = 0
        current_brightness = 1
        while last_brightness <> current_brightness:
                last_brightness = current_brightness
                while valid != True:
                        # Send 0xFF to get data from hub
                        resp_bin_str = transceiveSPI(spi, 255)

                        # Check if response is valid
                        valid = isValid(resp_bin_str)
                
                        time.sleep(cycle_sleep_time)

                current_brightness = int(resp_bin_str[1:5], 2)
        print "Current brightness is  " + str(current_brightness)
        
        bitsToSend = parseStateToBits()
        return (bitsToSend)

def isValid(resp):
        # Check parity bit
        parity_bit = resp[0]
        correct_parity_val = str(parityOf(int(resp[1:8], 2)))

        if parity_bit != correct_parity_val:
                print "Invalid parity bit"
                return False

        # Check that screen_off bit has valid value (i.e. 1 if lid is 0 or matches state sent by Pi)
        lid_bit = resp[5]
        screen_off_bit = resp[6]

        if lid_bit == "0" and screen_off_bit == "0":
                print "Invalid combination of bit 5 and 6"
                return False
        
        return True


# MAIN CODE STARTS HERE
def main():
        global current_brightness
        global new_brightness
        global brightness_change
        global newBrightness
        
        # Set up SpiDev
        spi = setupSPI()

        # Get current values from hub
        # THIS WILL CYCLE THROUGH UNTIL VALID DATA IS RECEIVED
        bitsToSend = getInitData(spi)

        # Transmit bits and capture response twice
        print "Setting brightness to", new_brightness
        resp_bin_str = transceiveSPI(spi, bitsToSend)
        time.sleep(cycle_sleep_time)
        resp_bin_str = transceiveSPI(spi, bitsToSend)


# Call main function
if __name__ == '__main__': 
    main()
