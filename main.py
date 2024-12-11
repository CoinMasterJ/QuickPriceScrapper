import yfinance as yf
import pandas as pd

def fetch_ohlcv_data(ticker, interval="1h", period="1d"):
    """
    Fetch OHLCV data for a specified asset ticker.

    Args:
        ticker (str): Ticker symbol (e.g., "ETH-USD", "BTC-USD").
        interval (str): Data interval (e.g., "1h" for hourly, "5m" for 5-minute).
        period (str): Period for the data (e.g., "1d" for 1 day, "7d" for 7 days).

    Returns:
        pd.DataFrame: OHLCV data for the specified asset.
    """
    print(f"Fetching data for {ticker} with interval '{interval}' and period '{period}'...")
    
    # Fetch data from Yahoo Finance
    data = yf.download(ticker, interval=interval, period=period)
    
    # Check if data is empty
    if data.empty:
        raise ValueError(f"No data found for {ticker}. Check interval and period.")
    
    # Reset index for better formatting
    data.reset_index(inplace=True)
    
    # Filter for relevant columns
    ohlcv_data = data[["Datetime", "Open", "High", "Low", "Close", "Volume"]]
    
    # Ensure numeric columns are cast as float
    for col in ["Open", "High", "Low", "Close", "Volume"]:
        ohlcv_data[col] = ohlcv_data[col].astype(float)
    
    return ohlcv_data

def save_to_csv(data, ticker):
    """
    Save OHLCV data to a CSV file.

    Args:
        data (pd.DataFrame): The OHLCV data to save.
        ticker (str): Ticker symbol for the asset.

    Returns:
        str: Path to the saved file.
    """
    # Construct file name with ticker for uniqueness
    file_path = f"{ticker}_ohlcv.csv"
    data.to_csv(file_path, index=False)
    print(f"Data for {ticker} saved to {file_path}.")
    return file_path

def main():
    """
    Main function to fetch and save OHLCV data for a single asset.
    """
    try:
        # Specify the asset ticker here (e.g., "ETH-USD" for Ethereum)
        ticker = "BTC-USD"  # Change this to the desired asset ticker

        # Fetch OHLCV data
        ohlcv_data = fetch_ohlcv_data(ticker=ticker, interval="1h", period="1mo")
        
        # Display the first few rows of data
        print("OHLCV Data:")
        print(ohlcv_data.head())

        # Save the data to a CSV file
        save_to_csv(ohlcv_data, ticker)

    except Exception as e:
        print(f"Error: {e}")

# Execute the script
if __name__ == "__main__":
    main()
