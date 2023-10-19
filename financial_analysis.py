#LIBRARIES
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
from plotly import express as px
import nbformat

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

#SIMPLE VISUAL
px.line(
    data_frame=stock_df.set_index('Date')
)

# Professionalize the plot
fig = px.line(
    data_frame=stock_df.set_index('Date'),
    color_discrete_map={
        "Close": "#2C3E50",
        "mavg_short": "#E31A1C",
        "mavg_long": "#18BC9C"
    },
    title=f"{symbol} Stock Chart"
)

fig = fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='rgba(0,0,0,0)',
    legend_title_text=''
)

fig = fig.update_yaxes(
    title="Share Price",
    tickprefix="$",
    gridcolor='#2c3e50'
)

fig = fig.update_xaxes(
    title='',
    gridcolor='#2c3e50'
)

fig










