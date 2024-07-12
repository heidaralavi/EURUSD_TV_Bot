from Asset_Data import asset_history
from Strategy import ThreeSMA
from smstochannel import sms
import datetime as dt
import time

df = asset_history()
print(df)




'''
while True:
    if dt.datetime.now(dt.UTC).second == 5 and dt.datetime.now(dt.UTC).minute in range(0,60,15):
        df = asset_history()
        results = ThreeSMA(df)
        #print(results[0])
               
        if results[0] == "Week BUY":
            msg ="{} - EURUSD : Week BUY Signal (15m TimeFrame)".format(results[1])
            sms(msg=msg)
        if results[0] == "Stonge BUY":
            msg ="{} - EURUSD : Stonge BUY Signal (15m TimeFrame)".format(results[1])
            sms(msg=msg)
        if results[0] == "Week SELL":
            msg ="{} - EURUSD : Week SELL Signal (15m TimeFrame)".format(results[1])
            sms(msg=msg)
        if results[0] == "Stronge SELL":
            msg ="{} - EURUSD : Stronge SELL Signal (15m TimeFrame)".format(results[1])
            sms(msg=msg)
       
        
    time.sleep(1)
'''