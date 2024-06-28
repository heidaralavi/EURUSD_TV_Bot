
def body(open:float,close:float) -> float:
    return abs(open-close)

def shadows(open:float,close:float,low:float,high:float) -> dict:
    shadow = {}
    if open > close:
        up_shadow = high - open
        down_shadow = close - low
    else:
        up_shadow = high - close
        down_shadow = open - low
    shadow['up']= up_shadow
    shadow['down']= down_shadow
    return shadow

def IsUpTrend(open:float,close:float) -> bool:
    if close > open:
        return True
    else:
        return False

def IsDownTrend(open:float,close:float) -> bool:
    if open > close:
        return True
    else:
        return False

def IsUpPinBar(open:float,close:float,low:float,high:float) -> bool:
    condition_1:bool = IsUpTrend(open=open,close=close)
    condition_2:bool = shadows(open=open,close=close,low=low,high=high)['down'] > (3 * body(open=open,close=close))
    condition_3:bool = shadows(open=open,close=close,low=low,high=high)['up'] < (0.5 * body(open=open,close=close))
    if condition_1 and condition_2 and condition_3:
        return True
    else:
        return False

def IsDownPinBar(open:float,close:float,low:float,high:float) -> bool:
    condition_1:bool = IsDownTrend(open=open,close=close)
    condition_2:bool = shadows(open=open,close=close,low=low,high=high)['up'] > (3 * body(open=open,close=close))
    condition_3:bool = shadows(open=open,close=close,low=low,high=high)['down'] < (0.5 * body(open=open,close=close))
    if condition_1 and condition_2 and condition_3:
        return True
    else:
        return False

def Is3SMABullish(sma_7:float,sma_14:float,sma_21:float) -> bool:
    if sma_7 > sma_14 and sma_14 > sma_21:
        return True
    else:
        return False
    
def Is3SMABearish(sma_7:float,sma_14:float,sma_21:float) -> bool:
    if sma_7 < sma_14 and sma_14 < sma_21:
        return True
    else:
        return False

def IsPriceOverSma7(low:float,sma_7:float) ->bool:
    if low > sma_7:
        return True
    else:
        return False
def IsPriceUnderSma7(high:float,sma_7:float) ->bool:
    if high < sma_7:
        return True
    else:
        return False

def ThreeSMA(chart_data) -> list:
    
    chart_data['SMA_7'] = chart_data.close.rolling(7).mean()
    chart_data['SMA_14'] = chart_data.close.rolling(14).mean()
    chart_data['SMA_21'] = chart_data.close.rolling(21).mean()
    last_data = chart_data.tail(2).to_dict('list')
    times = str(last_data['time'][0])
    results = ['No_Signal',times]
    open,close,low,high= float(last_data['open'][0]),float(last_data['close'][0]),float(last_data['low'][0]),float(last_data['high'][0])
    sma_7,sma_14,sma_21= float(last_data['SMA_7'][0]),float(last_data['SMA_14'][0]),float(last_data['SMA_21'][0])
    
    # print(time)
    # print('open =',open,'high =',high,'low =',low,'close =',close)
    # print('sma7 =',sma_7,'sma14 =',sma_14,'sma21 =',sma_21)
    # print('UP_PIN_BAR: ',IsUpPinBar(open=open,close=close,low=low,high=high))
    # print('DOWN_PIN_BAR: ',IsDownPinBar(open=open,close=close,low=low,high=high))
    # print('3SMA_Bullish: ',Is3SMABullish(sma_7=sma_7,sma_14=sma_14,sma_21=sma_21))
    # print('3SMA_Bearish: ',Is3SMABearish(sma_7=sma_7,sma_14=sma_14,sma_21=sma_21))


    # Analysis Return
    if IsPriceOverSma7(low=low,sma_7=sma_7) and Is3SMABullish(sma_7=sma_7,sma_14=sma_14,sma_21=sma_21) and IsUpTrend(open=open,close=close):
        results = ['Week BUY',times]
    if IsUpPinBar(open=open,close=close,low=low,high=high) and Is3SMABullish(sma_7=sma_7,sma_14=sma_14,sma_21=sma_21):
        results = ['Stonge BUY',times]
    if IsPriceUnderSma7(high=high,sma_7=sma_7) and Is3SMABearish(sma_7=sma_7,sma_14=sma_14,sma_21=sma_21) and IsDownTrend(open=open,close=close):
        results = ['Week SELL',times]
    if IsDownPinBar(open=open,close=close,low=low,high=high) and Is3SMABearish(sma_7=sma_7,sma_14=sma_14,sma_21=sma_21):
        results = ['Stronge SELL',times]
    return results
    





if __name__ == "__main__":
    pass