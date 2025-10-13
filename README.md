Here is a README file for your data fetching script and Power BI dashboard project:

***

# NIFTY 50 Stock Data Fetcher & Dashboard

This project fetches fundamental and historical stock data for NIFTY 50 companies using Yahoo Finance API (yfinance) and stores it as CSV files. The collected data is then used in a Power BI dashboard to visualize and analyze stock performance and key metrics.

## Features

- Fetches fundamental data: company info, sector, market cap, PE ratios, EPS, dividend yield, price stats, and current price
- Downloads 5 years of historical daily stock price and volume data
- Saves data to CSV files for easy integration with BI tools like Power BI
- Ready for building financial dashboards and performing stock market analysis

## Requirements

- Python 3.x
- pandas
- yfinance
- tqdm

## Installation

Install required Python packages:

```bash
pip install pandas yfinance tqdm
```

## Usage

1. Run the data fetching script:

```bash
python fetch_nifty50_data.py
```

2. The script will save two CSV files in the `data` directory (created if not existing):

- `fundamentals.csv` — fundamental data for each company
- `historical.csv` — 5 years of historical daily prices

3. Import these CSV files into your Power BI dashboard.

4. Use Power BI tools to create visualizations and insights based on the stock data.

## How It Works

- The script defines the NIFTY 50 tickers and a 5-year date range.
- Utilizes yfinance to pull info and historical price data for each ticker.
- Handles errors to continue fetching even if some tickers have issues.
- Saves the aggregated dataframes into CSV files for dashboard integration.

## Power BI Dashboard

- The provided CSV files are the data sources for your Power BI dashboard.
- Visualize trends, compare companies, and track financial metrics.
- Customize visuals such as line charts, bar charts, and KPIs based on this data.

## License

This project is open-source under the MIT License.

***

This README clearly introduces your data fetching script and its connection to the Power BI dashboard. Let me know if you want the README to include more Power BI dashboard specifics or visuals!Here is a README file for your NIFTY 50 data fetching script and Power BI dashboard project:

***

# NIFTY 50 Data Fetcher and Power BI Dashboard

This project consists of a Python script that fetches fundamental and historical stock data for NIFTY 50 companies using Yahoo Finance (`yfinance`). The fetched data is saved as CSV files and subsequently used to create a Power BI dashboard for analysis and visualization.

## Features

- Fetches key fundamental metrics including market cap, P/E ratios, EPS, dividend yield, and price stats.
- Downloads last 5 years’ daily historical stock price and volume data.
- Saves fundamentals and historical data separately as CSV files.
- Designed for seamless integration with Power BI dashboards.
  
## Requirements

- Python 3.x
- pandas
- yfinance
- tqdm
  
Install dependencies via:

```bash
pip install pandas yfinance tqdm
```

## Usage

1. Run the script to download data:

```bash
python fetch_nifty50_data.py
```

2. Data files `fundamentals.csv` and `historical.csv` will be saved in the `data` folder created alongside the script.

3. Load these CSV files into Power BI to create dashboards and perform financial analysis based on NIFTY 50 stocks.

## How the Script Works

- Defines NIFTY 50 stock tickers.
- Uses Yahoo Finance API to fetch company fundamentals and historical price data for the last five years.
- Saves results to CSV files for easy access and integration.
- Employs error handling to continue fetching data if any ticker retrieval fails.

## Power BI Dashboard

The data collected with this script serves as input to a Power BI dashboard, enabling:

- Visualization of stock price trends over time.
- Comparison of key financial ratios across companies.
- Summary and analysis of market capitalization, dividend yield, and other metrics.

## License

Open source under the MIT License.

***

This README clearly explains your script, dependencies, usage, and the connection to your Power BI dashboard project. Let me know if you want to add more details about the dashboard setup or visuals!
