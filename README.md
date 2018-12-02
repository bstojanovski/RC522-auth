# RC522-auth
Authentication of UID from cards with CSV provided file with data. The idea behind using the CSV type of data is that the file is reusable and compatible with other services and platforms.

## CSV file
The **authorized.csv** file format is UID;Name;Authorization which is basically the **UID** of the card, **Name** of the user and the **Authorization** status (true/false).

## LED light status
The LED light connected on **GPIO 18** is used to determine the status whether the card is authorized or not. 
#### Long or 3 seconds light
Means that the card is authorized (true)
#### Blinking light
Means that the card is unauthorized (false)

## Requirements
This code requires you to have SPI-Py installed from [this repository](https://github.com/lthiery/SPI-Py)

## MFRC522
This project is based on the [MFRC522](https://github.com/mxgxw/MFRC522-python)

## Pins
You can use [this](https://i.stack.imgur.com/pXzYv.png) image for reference on how to connect RFID-RC522 with your Raspberry Pi.
