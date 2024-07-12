
from Asset_Data import asset_history
from scipy.signal import savgol_filter
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


# Calculating ATR indecator 
def wwma(values, n):
    """
     J. Welles Wilder's EMA 
    """
    return values.ewm(alpha=1/n, adjust=False).mean()

def add_atr(df, n=7):
    data = df.copy()
    high = data['high']
    low = data['low']
    close = data['close']
    data['tr0'] = abs(high - low)
    data['tr1'] = abs(high - close.shift())
    data['tr2'] = abs(low - close.shift())
    tr = data[['tr0', 'tr1', 'tr2']].max(axis=1)
    atr = wwma(tr, n)
    df['atr']=atr
    return df

def smooth_data(df):
    df["close_smooth"] = savgol_filter(df.close, 2, 1)
    return df

def find_peaks_inx(df):
    df = add_atr(df)
    df = smooth_data(df)
    atr = df.atr.iloc[-1] # all the first atrs are NaN
    peaks_idx,_ = find_peaks(df.close_smooth, distance = 7,width = 3, prominence=atr)
    peaks_items = df.filter(items=peaks_idx, axis=0)
    return peaks_items

def find_troughs_inx(df):
    df = add_atr(df)
    df = smooth_data(df)
    atr = df.atr.iloc[-1] # all the first atrs are NaN
    troughs_idx,_ = find_peaks(-1*df.close_smooth, distance = 15,width = 3, prominence=atr)
    troughs_items = df.filter(items=troughs_idx, axis=0)
    return troughs_items


if __name__ == "__main__":
    df = asset_history()
        
    print(find_peaks_inx(df))
    df = smooth_data(df=df)

    plt.plot(df[['close','close_smooth']])
    plt.scatter(find_peaks_inx(df).index,find_peaks_inx(df)['close'],c='r')
    plt.scatter(find_troughs_inx(df).index,find_troughs_inx(df)['close'],c='g')
    plt.show()
    #print(df)