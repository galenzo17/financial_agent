import alpaca_trade_api as tradeapi
import yfinance as yf
import time

# 1. Configure Alpaca API keys
API_KEY = 'YOUR_ALPACA_API_KEY'
SECRET_KEY = 'YOUR_ALPACA_SECRET_KEY'
BASE_URL = 'https://paper-api.alpaca.markets'  # Using the paper trading environment

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# 2. Define a function to get the top 3 stocks to invest in
def get_top_stocks():
    # List of some popular symbols (you can expand this list)
    symbols = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'META', 'TSLA', 'JNJ', 'V', 'WMT', 'NVDA']

    volumes = {}
    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period='1d')
        if not data.empty:
            volumes[symbol] = data['Volume'].iloc[-1]
        else:
            volumes[symbol] = 0  # Assign volume 0 if no data is available

    # Sort by volume and get the top 3
    selected_stocks = sorted(volumes, key=volumes.get, reverse=True)[:3]
    return selected_stocks

# 3. Get the stocks and calculate how much to invest in each
total_capital = 50.0  # Total capital available in USD
stocks = get_top_stocks()
capital_per_stock = total_capital / len(stocks)

print(f"Selected stocks: {stocks}")
print(f"Capital per stock: {capital_per_stock} USD")

# 4. Place buy orders
for symbol in stocks:
    # Get the current price of the stock
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='1d')
    if not data.empty:
        current_price = data['Close'].iloc[-1]
        # Calculate the number of shares to buy
        quantity = int(capital_per_stock / current_price)
        if quantity > 0:
            try:
                order = api.submit_order(
                    symbol=symbol,
                    qty=quantity,
                    side='buy',
                    type='market',
                    time_in_force='gtc'
                )
                print(f"Placed buy order for {quantity} shares of {symbol} at {current_price:.2f} USD per share.")
            except Exception as e:
                print(f"Error placing order for {symbol}: {e}")
        else:
            print(f"Not enough capital to buy shares of {symbol} at {current_price:.2f} USD.")
    else:
        print(f"Could not retrieve data for {symbol}.")

# 5. Monitor the stock prices
try:
    while True:
        print("\nMonitoring prices...")
        for symbol in stocks:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period='1d')
            if not data.empty:
                current_price = data['Close'].iloc[-1]
                print(f"The current price of {symbol} is {current_price:.2f} USD.")
            else:
                print(f"Could not retrieve data for {symbol}.")
        time.sleep(60)  # Wait 60 seconds before the next check
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")