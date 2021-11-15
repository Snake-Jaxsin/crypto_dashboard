s

import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objects as go
from PIL import Image

# Title/Header
st.write("""
# Cryptocurrency DashBoard Application 
Visually show data of crypto (BTC, DOGE, & ETH) from **'2020-06-04' to '2021-06-04'**
""")

image = Image.open("/Users/jessehernandez/ChooseToCode/PycharmProjects/Crypto_DashBoard/images/cryptoPic.jpeg")
# Displays Image from the Image.open method.
st.image(image, use_column_width=True)

st.sidebar.header("User Input")

# Getting information from the dash board of the 3 different parameters.
def get_input():
    start_date = st.sidebar.text_input("Start Date", '2020-06-04')
    end_date = st.sidebar.text_input("End Date", '2021-06-04')
    crypto_symbol = st.sidebar.text_input("Crypto Symbol", "BTC")
    return start_date, end_date, crypto_symbol

def get_crypto_name(symbol):
    if symbol == "BTC":
        return "Bitcoin"
    elif symbol == "ETH":
        return 'Ethereum'
    elif symbol == 'DOGE':
        return 'Dogecoins'
    else:
        return "None"

# Function to get the proper data and proper time frame.
def get_data(symbol, start, end):
    symbol == symbol.upper()
    if symbol == "BTC":
        df = pd.read_csv("/Users/jessehernandez/ChooseToCode/PycharmProjects/Crypto_DashBoard/data/BTC-USD.csv")
    elif symbol == "ETH":
        df = pd.read_csv("/Users/jessehernandez/ChooseToCode/PycharmProjects/Crypto_DashBoard/data/ETH-USD.csv")
    elif symbol == "DOGE":
        df = pd.read_csv("/Users/jessehernandez/ChooseToCode/PycharmProjects/Crypto_DashBoard/data/DOGE-USD.csv")
    else:
        df = pd.DataFrame(columns =['Date', 'Close', 'Open', 'Volume', 'Adj Close'])

    # Converting startDate/endDate to datetime.
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    # return data from df from the start date to end date.
    return df.loc[start:end]

start, end, symbol = get_input()
df = get_data(symbol, start, end)
crypto_name = get_crypto_name(symbol)

# Candle Interactive Crypto Stock Figure.
fig = go.Figure(
    data = [go.Candlestick(
         x = df.index,
         open = df['Open'],
         high = df['High'],
         low = df['Low'],
         close = df['Close'],
        increasing_line_color = 'green',
        decreasing_line_color = 'red'
    )
  ]
)

# Show some data and header for display.
st.header(crypto_name+" Data")
st.write(df)

st.header(crypto_name+" Data Statistics")
st.write(df.describe())

st.header(crypto_name+" Close Price")
st.line_chart(df['Close'])

st.header(crypto_name+" Volume")
st.bar_chart(df['Volume'])

st.header(crypto_name+" Candle Stick")
st.plotly_chart(fig)