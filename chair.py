#!/usr/bin/python
import serial
import pygvoicelib

ser = serial.Serial('/dev/ttyACM0', 9600)
client = pygvoicelib.GoogleVoice('rudydude53@gmail.com','rkswxivkhjjidmfv','DQAAAP4AAAA1MFOT2vIVytOXaD0QvodOCMcjc2GFtfS7CJsneNTvJF0ByETkNDSaqdy2_7dc7u5hLSvahDU7KNjyFCOAK7_K8LuUS-QbANR4mghR-oZJWzbyd0Whigv38IwPz5Veb9_ryMDfEG3EuJC2r5C0pB_1it_EHDKiKnm2mcSkk7NWLjV6Q3r0nn19Uzh7hsR0srXNQZ3kJIasazqiVmp-jWbpVJx1zyqfJ-TkZvGFFuuvbpeCsHj8qNxlypIn_gTw5_IadkNEIXRhunLEEDPurHtRd5o8G7PKZws8IZP3N03HXUvAeNbQ7NIN4d8nK3EstxUYLljr4ShbZyvG6BvH9O6j','uVtFA9MrINl47hYMMo6KKfYn648=')

reading = ""

number = raw_input('Please enter the number you wish\n\tto send notifications to: ')
max_sitting_time = raw_input('Please enter the amount of time you wish\n\tto elapse before notification is sent: ')
max_sitting_timeI = int(max_sitting_time)

message1 = "You have been sitting for " + max_sitting_time + " seonds."
message2 = "You have been sitting for " + max_sitting_time + " more seconds."

counterA = 0
counterB = 0

print("\n\nRunning...")
print("To exit press 'CTL-C'")

while 1 :
    reading = ser.readline()
    readingI = int(reading)


    if (readingI > 400):
        counterA = counterA + 1
        counterB = counterB + 1
    else:
        counterA = 0
        counterB = 0

    if ((counterA > max_sitting_timeI) & (counterB > (max_sitting_timeI + 1))):
        client.sms(number, message2)
        counterA = 0
    elif (counterA > max_sitting_timeI):
        client.sms(number, message1)
        counterA = 0