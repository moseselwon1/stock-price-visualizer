import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- Config ---
ticker = "TSLA"
start_date = "2022-01-01"
end_date = "2024-12-31"

# --- Download Data ---
data = yf.download(ticker, start=start_date, end=end_date)

# --- Calculate Moving Averages ---
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA100'] = data['Close'].rolling(window=100).mean()

# --- Plot ---
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['MA20'], label='20-Day MA', color='orange')
plt.plot(data['MA50'], label='50-Day MA', color='green')
plt.plot(data['MA100'], label='100-Day MA', color='red')  # New
plt.title(f"{ticker} Price Chart with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

