
# Installation Python version should be >= 3.10
#pip install git+https://github.com/batprem/price-loaders.git

from price_loaders.tradingview import load_asset_price
import pandas as pd
import datetime

def asset_history(chart='OANDA:EURUSD',timeframe='15',candle_no=199,):
    TZ = datetime.timezone(datetime.timedelta(seconds=12600)) #IRAN +03:30 = 12600 seconds
    df = load_asset_price(symbol=chart,look_back_bars=candle_no,time_frame=timeframe,timezone=TZ)
    return df



if __name__ == "__main__":
    pass

