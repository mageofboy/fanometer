# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import time
import struct

#Connect the Arduino data stream into Python via serial connection
ser = serial.Serial('COM5', 9600,timeout=.1)

def byte2int(x):
    #byte2int: Convert Arduino byte into integer
    #INPUT: A byte
    #OUTPUT: An integer
    x_str=x.decode('utf-8') #byte-to-string
    if(len(x_str)>0): #use-case to avoid setting empty strings as integers
        x_int=int(x_str.strip('\r\n'))
    else:
        x_int=0
    return(x_int)

data=[]
def analyze():
    noiselevel = sum(data)/60
    s = findloudest(noiselevel)
    d = []
    for i in s:
        if len(i) > 5:
            d.append(i)
    cheers = len(d)
    length = 0
    for i in d:
        length += len(i)
    return [cheers, length, noiselevel]

def findloudest(avg):
    above = []
    cheering = False
    for i in data:
        if (i > avg) and (not cheering):
            cheering = True
            cheer = []
            cheer.append(i)
        elif (i > avg) and cheering:
            cheer.append(i)
        elif (i < avg) and cheering:
            cheering = False
            above.append(cheer)
    return above
while True:
    audraw=ser.readline() #Read raw audio level data
    aud=byte2int(audraw) #Convert to integer
    if aud>0: #If the value is legitimate, add to data
        data.append(aud)
    if len(data)==60: #Moving average was set to 60 ticks, this can be changed
        mov_avg=sum(data)/60 #Compute the average
        ma_str=str(round(mov_avg)) #Sanitize the moving average
        ser.write(ma_str.encode()) #Send moving average to Arduino
        data=data[1:] #Pop the oldest element off the stack

ser.close() #Close the serial connection
