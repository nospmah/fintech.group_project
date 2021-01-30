import requests
import pandas as pd
import numpy as np
# from dotenv import load_dotenv
import alpaca_trade_api as tradeapi 
import json
from datetime import date

def get_stock_OHLCV(api_key, secret_key, ticker, date_start, date_end, period) :
    '''
    Historical OHLCV for stocks using Alpaca API.

            Parameters:
                    api_key (string): Alpaca api key
                    secret_key (string): Alpaca secret key
                    ticker (string): Ticker - ex) 'SPY'
                    date_start (string): example) '2015-01-01'
                    date_end (string): example) '2015-01-01'
                    period (string): example) '1D'

            Returns:
                    DateFrame with columns: ['date','open','high','low','close','volume']
    '''

    # Init Alpaca SDK
    api = tradeapi.REST(
        api_key,
        secret_key,
        api_version="v2")

    # Init start/end dates
    start_date = pd.Timestamp(date_start, tz="America/New_York").isoformat()
    end_date = pd.Timestamp(date_end, tz="America/New_York").isoformat()

    # Make API call
    raw_df = api.get_barset(
        [ticker],
        period,
        start=start_date,
        end=end_date).df

    # Init new DataFrame
    df = pd.DataFrame()
    df['open'] = raw_df[ticker]['open']
    df['high'] = raw_df[ticker]['high']
    df['low'] = raw_df[ticker]['low']
    df['close'] = raw_df[ticker]['close']
    df['volume'] = raw_df[ticker]['volume']

    # Parse date
    df['date'] = raw_df.index.date

    # Reset index
    df.reset_index(inplace=True)

    # Reorder columns
    df = df[['date','open','high','low','close','volume']]

    # Save to file
    #df.to_csv(f'../data/OHLCV/{ticker}_ohlcv_{date_start}-{date_end}_v2.csv', header=None, index=None, sep=',', mode='a')

    return df


def get_crypto_OHLCV(api_key, ticker, date_start, date_end, period) :
    '''
    Historical OHLCV for crypto using OpenAPI.io.

            Parameters:
                    api_key (string): OpenAPI.io api key
                    ticker (string): Ticker - ex) 'BTC'
                    date_start (string): example) '2015-01-01'
                    date_end (string): example) '2015-01-01'
                    period (string): example) '1DAY'

            Returns:
                    DateFrame with columns: ['date','open','high','low','close','volume']
    '''
    # CoinAPI.io REST url for historical OHLCV
    url = f'https://rest.coinapi.io/v1/ohlcv/{ticker}/USD/history?apikey={api_key}&period_id={period}&time_start={date_start}&time_end={date_end}&limit=100000'
    # url = f'https://rest.coinapi.io/v1/ohlcv/{ticker}/USD/history?apikey={api_key}&period_id={period}&time_start={date_start}&time_end={date_end}&limit=100'
    
    # List of dictionary objects
    results = requests.get(url).json()

    # Init dataframe from raw results
    df = pd.DataFrame(
        results, 
        columns=['time_period_end','price_open','price_high','price_low','price_close','volume_traded'])

    # Parse date from string
    df['time_period_end'] = pd.to_datetime(df['time_period_end']).dt.date

    # Rename columns
    df.rename(
        columns = {'time_period_end':'date',
            'price_open':'open',
            'price_high':'high',
            'price_low':'low',
            'price_close':'close',
            'volume_traded':'volume'}, 
        inplace = True)

    # Save to file
    #df.to_csv(f'../data/OHLCV/{ticker}_ohlcv_{date_start}-{date_end}_v2.csv', header=None, index=None, sep=',', mode='a')

    return df


def get_pct_chg_for_OHLCV(ohlcv_data) :
    '''
    Helper method to convert OHLCV data to pct_chg.

            Parameters:
                    ohlcv_data (DataFrame): OHLCV data (from methods above)

            Returns:
                    DateFrame with column: ['close']
    '''
    returns_df = ohlcv_data[['close']]
    returns_df['close'] = returns_df['close'].astype('float64')
    returns_df.index = ohlcv_data['date']
    returns_df = returns_df.pct_change()
    return returns_df
