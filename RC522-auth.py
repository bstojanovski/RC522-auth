#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import csv
 
continue_reading = True 
 
# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
 
# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)
 
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
 
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
 
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
        
        # Declare variables
        name = ""
        uid_authorized = "false"
    
        #Open CSV file and compare the readed card UID with entries from the CSV file
        with open('authorized.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    if str(uid) == str(row[0]):
                        if row[2] == "true":
                            name = row[1]
                            uid_authorized = "true"
                line_count += 1
        
        # Configure LED Output Pin
        LED = 18
        GPIO.setup(LED, GPIO.OUT)
        GPIO.output(LED, GPIO.LOW)
        
        # Check to see if the card is authorized
        if uid_authorized == "true":
            print "Hello", name
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(LED, GPIO.LOW)
            
        else:
            print("ERROR: Access Denied")
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.HIGH) 
            time.sleep(0.1)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.HIGH) 
            time.sleep(0.1)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.1)
