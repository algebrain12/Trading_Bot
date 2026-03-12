import pandas as pd
import matplotlib.pyplot as plt
import time
import yfinance as yf

def get_nifty50_data():
    nifty50 = yf.download("^NSEI", period="10d", interval="1h")
    nifty50.to_csv("nifty50_data.csv")
    return nifty50 

print(get_nifty50_data())
