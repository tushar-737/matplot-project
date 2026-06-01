import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("05-stock_data.csv")

# Convert Date Column
df["Date"] = pd.to_datetime(df["Date"])

# Sort by Date
df = df.sort_values("Date")

# Calculate Moving Averages
df["MA_7"] = df["Close"].rolling(window=7).mean()
df["MA_30"] = df["Close"].rolling(window=30).mean()

# Calculate Daily Returns
df["Daily_Return"] = df["Close"].pct_change() * 100

# Basic Statistics
print("\n===== STOCK ANALYSIS =====")
print("Highest Closing Price:", df["Close"].max())
print("Lowest Closing Price:", df["Close"].min())
print("Average Closing Price:", round(df["Close"].mean(), 2))
print("Average Trading Volume:", round(df["Volume"].mean(), 2))

# Dashboard
fig, axes = plt.subplots(3, 2, figsize=(15, 12))

# 1. Closing Price Trend
axes[0, 0].plot(df["Date"], df["Close"])
axes[0, 0].set_title("Closing Price Trend")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Close Price")

# 2. Trading Volume
axes[0, 1].bar(df["Date"], df["Volume"])
axes[0, 1].set_title("Trading Volume")
axes[0, 1].set_xlabel("Date")
axes[0, 1].set_ylabel("Volume")

# 3. High vs Low Price
axes[1, 0].plot(df["Date"], df["High"], label="High")
axes[1, 0].plot(df["Date"], df["Low"], label="Low")
axes[1, 0].set_title("High vs Low Price")
axes[1, 0].legend()

# 4. Closing Price Distribution
axes[1, 1].hist(df["Close"], bins=15)
axes[1, 1].set_title("Closing Price Distribution")
axes[1, 1].set_xlabel("Price")

# 5. Moving Averages
axes[2, 0].plot(df["Date"], df["Close"], label="Close")
axes[2, 0].plot(df["Date"], df["MA_7"], label="7-Day MA")
axes[2, 0].plot(df["Date"], df["MA_30"], label="30-Day MA")
axes[2, 0].set_title("Moving Average Analysis")
axes[2, 0].legend()

# 6. Daily Returns
axes[2, 1].plot(df["Date"], df["Daily_Return"])
axes[2, 1].set_title("Daily Returns (%)")
axes[2, 1].set_xlabel("Date")
axes[2, 1].set_ylabel("Return %")

plt.tight_layout()
plt.show()