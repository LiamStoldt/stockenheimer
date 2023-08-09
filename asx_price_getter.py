"""Module for getting stock prices"""

import yfinance as yf


def get_stock_daily_change(ticker: str) -> float | None:
    """Get the daily percentage change of a stock

    Get the percentage change, if the stock couldn't be found we will 
    return a None instead.
    """

    # get data
    try:
        ticker = yf.Ticker(ticker)
        open = ticker.info['open']
        current = ticker.info['ask']
    except:
        return None
    
    return current - open    

