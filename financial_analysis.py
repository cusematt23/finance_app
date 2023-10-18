#LIBRARIES
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
from plotly import express as px

#USER INPUTS
symbol='MSFT'
period="5y"
window_mavg_short=30
window_mavg_long=90

#GET STOCK DATA
stock=yf.Ticker(symbol)

#Powerful attributes
stock_info=stock.info
stock_info

stock_incomestmt=stock.incomestmt
stock_incomestmt

stock_history = stock.history(period=period)
stock_history

#explotary data analysis
stock_info.keys()
stock_info['industry']
stock_info['fullTimeEmployees']
stock_info['website']

#Financial Ratios
stock_info['profitMargins']

#Stock history
stock_history.reset_index().info()

#Stock Data transformation
stock_df=stock_history[['Close']].reset_index()

stock_df['mavg_short']=stock_df['Close'].rolling(window=window_mavg_short).mean()
stock_df['mavg_long']=stock_df['Close'].rolling(window=window_mavg_long).mean()

stock_df






