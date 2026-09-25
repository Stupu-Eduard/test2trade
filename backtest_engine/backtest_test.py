# import the necessary packages
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# set the start and end dates for our market data request
end_date = datetime(year=2025, month=3, day=1)
start_date = datetime(year=2023, month=1, day=1)

# set the name of the ticker we want to download market data for
ticker = "NVDA"

# download market data for a single ticker
df_single = yf.download(
    tickers=ticker,
    start=start_date,
    end=end_date,
    interval="1d",
    group_by="ticker",
    auto_adjust=True,
    progress=False
)
df_single
