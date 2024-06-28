from Asset_Data import asset_history
from Strategy import ThreeSMA
from smstochannel import sms
import datetime as dt
import time


while True:
    if dt.datetime.now(dt.UTC).second == 5 and dt.datetime.now(dt.UTC).minute in range(0,60,5):
        df = asset_history()
        results = ThreeSMA(df)
        #print(results[0])
               
        if results[0] == "BUY":
            msg ="{} - EURUSD : BUY Signal".format(results[1])
            sms(msg=msg)
        elif results == "SELL":
            msg ="{} - EURUSD : SELL Signal".format(results[1])
            sms(msg=msg)
        else:
            msg ="{} - EURUSD : No Signal".format(results[1])
            sms(msg=msg)
        
    time.sleep(1)
