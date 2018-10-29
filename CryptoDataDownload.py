# -*- coding: utf-8 -*-

from __future__ import print_function
import pandas as pd

def read_hrly_csv(file):
    '''
    Reads and parses 'Hourly' csv file
    from CryptoDataDownload.com
    
    param file: 'filename.csv' which should be in the folder 'data/'
    return: parsed df of sorted DatetimeIndex and OHLC and V(Volume To)
    '''
    file = 'data/' + file
    df = pd.read_csv(file, header=1, index_col=0,
                     usecols=[0, 2, 3, 4, 5, 7])
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d %I-%p')
    df = df.sort_index()
    df = df.rename(columns={'Open':'O', 'High':'H', 'Low':'L', 'Close':'C', 'Volume To':'V'})
    df.index.name = 'T'  # Time
    return df


if __name__ == '__main__':
    df = read_hrly_csv('Binance_BTCUSDT_1h.csv')
    print(df.tail())
