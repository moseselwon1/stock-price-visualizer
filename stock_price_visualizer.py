import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- Config ---
ticker = "AAPL"  # Or change to TSLA, MSFT, etc.
start_date = "2023-01-01"
end_date = "2024-12-31"

# --- Download Data ---
data = yf.download(ticker, start=start_date, end=end_date)

# --- Calculate Moving Averages ---
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

# --- Plot Price and Moving Averages ---
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['MA20'], label='20-Day MA', color='orange')
plt.plot(data['MA50'], label='50-Day MA', color='green')
plt.title(f"{ticker} Price Chart with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

