import os
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from tqdm import tqdm

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
FUNDAMENTALS_FILE = os.path.join(DATA_DIR, "fundamentals.csv")
HISTORICAL_FILE = os.path.join(DATA_DIR, "historical.csv")

os.makedirs(DATA_DIR, exist_ok=True)

NIFTY50_TICKERS = [
    "RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS","HINDUNILVR.NS","SBIN.NS","BHARTIARTL.NS","KOTAKBANK.NS",
    "ITC.NS","LT.NS","AXISBANK.NS","BAJFINANCE.NS","HCLTECH.NS","MARUTI.NS","ASIANPAINT.NS","SUNPHARMA.NS",
    "ULTRACEMCO.NS","WIPRO.NS","NTPC.NS","TITAN.NS","ONGC.NS","JSWSTEEL.NS","POWERGRID.NS","ADANIENT.NS",
    "ADANIPORTS.NS","COALINDIA.NS","M&M.NS","BAJAJFINSV.NS","TECHM.NS","NESTLEIND.NS","HDFCLIFE.NS","GRASIM.NS",
    "TATAMOTORS.NS","TATASTEEL.NS","HINDALCO.NS","BRITANNIA.NS","CIPLA.NS","DIVISLAB.NS","DRREDDY.NS","HEROMOTOCO.NS",
    "SBILIFE.NS","EICHERMOT.NS","BAJAJ-AUTO.NS","INDUSINDBK.NS","UPL.NS","APOLLOHOSP.NS","SHREECEM.NS","BPCL.NS","HDFCAMC.NS"
]

END_DATE = datetime.today()
START_DATE = END_DATE - timedelta(days=5*365)

def fetch_fundamentals(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "Symbol": ticker,
        "Company": info.get("longName", ticker),
        "Sector": info.get("sector", "NA"),
        "MarketCap": info.get("marketCap", None),
        "TrailingPE": info.get("trailingPE", None),
        "ForwardPE": info.get("forwardPE", None),
        "PB": info.get("priceToBook", None),
        "EPS": info.get("trailingEps", None),
        "DividendYield": info.get("dividendYield", None),
        "52WeekHigh": info.get("fiftyTwoWeekHigh", None),
        "52WeekLow": info.get("fiftyTwoWeekLow", None),
        "CurrentPrice": info.get("currentPrice", None)
    }

def fetch_historical(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(start=START_DATE, end=END_DATE)
    hist.reset_index(inplace=True)
    hist["Symbol"] = ticker
    return hist[["Date", "Symbol", "Open", "High", "Low", "Close", "Volume"]]

def main():
    fundamentals_data, historical_data = [], []

    print("📊 Fetching fundamentals...")
    for ticker in tqdm(NIFTY50_TICKERS):
        try:
            fundamentals_data.append(fetch_fundamentals(ticker))
        except Exception as e:
            print(f"⚠️ Fundamentals error {ticker}: {e}")

    pd.DataFrame(fundamentals_data).to_csv(FUNDAMENTALS_FILE, index=False)
    print(f"✅ Fundamentals saved: {FUNDAMENTALS_FILE}")

    print("📈 Fetching historical (last 5 years)...")
    for ticker in tqdm(NIFTY50_TICKERS):
        try:
            historical_data.append(fetch_historical(ticker))
        except Exception as e:
            print(f"⚠️ Historical error {ticker}: {e}")

    pd.concat(historical_data, ignore_index=True).to_csv(HISTORICAL_FILE, index=False)
    print(f"✅ Historical saved: {HISTORICAL_FILE}")

if __name__ == "__main__":
    main()
