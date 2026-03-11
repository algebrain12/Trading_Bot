import finnhub
import pandas as pd
import matplotlib.pyplot as plt
import time

finnhub_client = finnhub.Client(api_key="d6oq9fpr01qi5kh3uh4gd6oq9fpr01qi5kh3uh50")

quote = finnhub_client.quote('AAPL')
print("Real-time Quote for AAPL:")
print(quote)

now = int(time.time())
one_month_ago = now - 30*24*60*60

now = int(time.time())
seven_days_ago = now - 7*24*60*60

# Step 3: Get hourly candles (resolution = 60 minutes)
candles = finnhub_client.stock_candles('AAPL', '60', seven_days_ago, now)
