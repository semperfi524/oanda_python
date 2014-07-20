#!/usr/bin/python

#Matplotlib libraries left out for demonstration purposes
import json
import httplib
import urllib
import subprocess

# This command will need to be turned on to pull live data.

# subprocess.call(["sh", "eurusd_1m.sh", ">", "eurusd_1m.json"])

with open("eurusd_1m.json", "r") as eurusd_data:
        eurusd = json.load(eurusd_data)

# lists to store data from candle file
openprice = []
close     = []
high      = []
low       = []
volume    = []

# candles is an array provided by json lib
candles   = eurusd['candles']

# iterate the candle array and save values of interest
for candle in candles:
        openprice.append(candle['openMid'])
        close.append(candle['closeMid'])
        high.append(candle['highMid'])
        low.append(candle['lowMid'])
        volume.append(candle['volume'])

#// This will enumerate data for calculation in python.  
#// Matplotlib examples coming soon.

print "Last 10 Volume Amounts:" , volume[-1], volume[-2], volume[-3], volume[-4], volume[-5], volume[-6], volume[-7], volume[-8], volume[-9] 
