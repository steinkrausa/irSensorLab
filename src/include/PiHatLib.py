#!/usr/bin/python

# Library for SB Components PiMotor Shield V2
# Developed by: Alec Steinkraus
# Change log:
# v0.1      Created for easy access to IR sensor inputs

#Import GPIO library
import RPi.GPIO as GPIO  

# import time
# from time import sleep

#Set GPIO pin numbering
GPIO.setmode(GPIO.BOARD)                       

GPIO.setwarnings(False)

# GPIO pins that IR sensors are connected to
IR1_INPUT_PIN = 7
IR2_INPUT_PIN = 12

DARK = 1        # When there is not enough reflected IR light, GPIO reads as 1
LIGHT = 0       # When there is enough reflected IR light, GPIO reads as 0

INVALID = -1

# Configure IR sensor Pins to be inputs
GPIO.setup(IR1_INPUT_PIN, GPIO.IN)
GPIO.setup(IR2_INPUT_PIN, GPIO.IN)

def get_ir_state(inputPin):
    if inputPin not in [IR1_INPUT_PIN, IR2_INPUT_PIN]:
        print("get_ir_state was called with an invalid input pin number: " + str(inputPin))
        print("valid pin numbers include: " + str(IR1_INPUT_PIN) + ", " + str(IR2_INPUT_PIN) + ".")
        return -1
    else:
        pinValue = GPIO.input(inputPin)
        return pinValue
        
