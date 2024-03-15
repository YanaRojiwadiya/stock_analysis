import yfinance as yf

class Yfinance:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)

    def get_stock_info(self):
        return self.ticker.info

    def fetch_stock_data(self, period, interval):
        return self.ticker.history(period=period, interval=interval)

    def get_stock_earning_date(self):
        earning_dates = self.ticker.calendar['Earnings Date']
        return [date.strftime("%d %B %Y") for date in earning_dates]

    def get_stock_news(self):
        return self.ticker.news

# if __name__ == "__main__":
#     yf = Yfinance('AAPL')

#     stock_info = yf.get_stock_info()
#     print("Stock Info:", stock_info)

#     stock_data = yf.fetch_stock_data('1d', '1m')
#     print("Stock Data:", stock_data)

#     earning_date = yf.get_stock_earning_date()
#     print("Earning Date:", earning_date)

#     stock_news = yf.get_stock_news()
#     print("Stock News:", stock_news)
