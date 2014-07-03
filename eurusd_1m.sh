#!/bin/bash

##/This code requires an authorization key, which will be provided by Oanda
##/after API access is granted.  https://api-fxpractice.oanda.com can be used
##/as well if you do not have access to a live API account. 

curl --header "Authorization: Bearer xxxx(insert key here)xxxxx" "https://api-fxtrade.oanda.com/v1/candles?instrument=EUR_USD&granularity=M1&count=1000&candleFormat=midpoint" > eurusd_1m.json 
