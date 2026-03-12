import pandas as pd
import matplotlib.pyplot as plt
import time
import yfinance as yf

def get_nifty50_data():
    nifty50 = yf.download("^NSEI", period="100d", interval="1h")
    return nifty50 

