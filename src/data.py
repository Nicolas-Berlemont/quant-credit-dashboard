import yfinance as yf


def get_prices(tickers, start="2015-01-01"):
    df = yf.download(tickers, start=start, auto_adjust=True, progress=False)["Close"]
    return df.dropna()


if __name__ == "__main__":
    p = get_prices(["LQD", "HYG", "IEF"])
    print(p.tail())
    print("shape:", p.shape)
    assert not p.isna().any().any(), "NaN dans les prix"
    print("OK data")