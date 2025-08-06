import yfinance as yf
def portfolio():
    stocks = {
        "APOLLO": 1805, "BEL": 1000, "BHEL": 5000, "BBOX": 700, "BAJAJHFL": 2000,
        "CRISIL": 50, "ETERNAL": 1200, "HERITGFOOD": 130, "INDIAMART": 100,
        "INDIGOPNTS": 32, "IREDA": 1500, "IRFC": 1420, "JIOFIN": 1000,
        "POLICYBZR": 163, "TATAMOTORS": 140, "UJJIVANSFB": 2285,
        "VIJAYA": 110, "YESBANK": 2265
    }

    tickers = [key + ".NS" for key in stocks]

    # Download stock data
    data = yf.download(
        tickers=" ".join(tickers),
        period="1d",
        interval="1m",
        group_by='ticker',
        auto_adjust=True,
        threads=True,
        progress=False
    )

    # Portfolio summary
    portfolio_value = 0

    print("\n┌──────────────┬──────────┬────────────┬────────────┐")
    print("│ Ticker       │ Price ₹  │ Quantity   │ Value ₹    │")
    print("├──────────────┼──────────┼────────────┼────────────┤")

    for ticker in tickers:
        try:
            latest_price = data[ticker]["Close"].dropna().iloc[-1]
            quantity = stocks[ticker[:-3]]
            value = latest_price * quantity
            portfolio_value += value

            print(f"│ {ticker:<12} │ {latest_price:>8.2f} │ {quantity:>10} │ {value:>10.2f} │")

        except Exception as e:
            print(f"│ {ticker:<12} │   ERROR   │            │            │")

    print("└──────────────┴──────────┴────────────┴────────────┘")
    print(f"\n💼 Total Portfolio Value: ₹{portfolio_value:,.2f}")


if __name__ == "__main__":
    portfolio()
