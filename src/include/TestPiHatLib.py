#!/usr/bin/python

# Script for testing PiHatLib.py functionality
# Developed by: Alec Steinkraus
# Change log:
# v0.1      Test functionality for PiHatLib.py v0.1

from PiHatLib import *
import time

try:
    while True:
#-----------Check IR1 Value------------# 
        print("Reading IR1")
        ir1Value = get_ir_state(IR1_INPUT_PIN)
        if(ir1Value == DARK):
            print("IR1 is Dark")
        elif(ir1Value == LIGHT):
            print("IR1 is LIGHT")
        elif(ir1Value == INVALID):
            print("INVALID pin")
        time.sleep(2)
#--------------------------------------#

#-----------Check IR2 Value------------# 
        print("Reading IR2")
        ir2Value = get_ir_state(IR2_INPUT_PIN)
        if(ir2Value == DARK):
            print("IR2 is Dark")
        elif(ir2Value == LIGHT):
            print("IR2 is LIGHT")
        elif(ir2Value == INVALID):
            print("INVALID pin")
        time.sleep(2)
#--------------------------------------#

#-------Check Invalid pin Value--------# 
        print("Reading Invalid pin")
        irValue = get_ir_state(1)
        if(irValue == DARK):
            print("IR is Dark")
        elif(irValue == LIGHT):
            print("IR is LIGHT")
        elif(irValue == INVALID):
            print("INVALID pin")
        time.sleep(2)
#--------------------------------------#
        
except KeyboardInterrupt:
    GPIO.cleanup()
