# RC522-auth
Authentication of UID from cards with CSV provided file with data. The CSV file format is UID;Name;Authorization which is basically the **UID** of the card, **Name** of the user and the **Authorization** status (true/false).

## LED light status
The LED light connected on **GPIO 18** is used to determine the status whether the user (card) is authorized or not. **Long or 3 seconds light** means authorized (true) while **blinking light** means unauthorized (false).

This project is based on the [MFRC522](https://github.com/mxgxw/MFRC522-python)

## Requirements
This code requires you to have SPI-Py installed from [this repository](https://github.com/lthiery/SPI-Py)

## Pins
You can use [this](https://i.stack.imgur.com/pXzYv.png) image for reference on how to connect RFID-RC522 with your Raspberry Pi.
