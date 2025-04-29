#!/usr/bin/env python3
import datetime
import yfinance as yf
import pandas as pd

# ——————————————
# 表示設定：小数点以下2桁、カンマ区切り
pd.set_option('display.float_format', '{:,.2f}'.format)
# ——————————————

def fetch_markets():
    symbols = {
        'USD/JPY': 'JPY=X',
        'S&P 500': '^GSPC',
        'Dow Jones': '^DJI',
        'NASDAQ': '^IXIC',
        'Nikkei 225': '^N225'
    }
    tickers = yf.Tickers(" ".join(symbols.values()))
    result = {}
    for name, ticker in symbols.items():
        info = tickers.tickers[ticker].history(period='1d')
        if not info.empty:
            latest = info.iloc[-1]
            result[name] = {
                '日時': latest.name.to_pydatetime().strftime('%Y-%m-%d %H:%M'),
                '始値': latest['Open'],
                '終値': latest['Close'],
                '高値': latest['High'],
                '安値': latest['Low'],
                '出来高': latest['Volume']
            }
    return pd.DataFrame(result).T

if __name__ == "__main__":
    df = fetch_markets()
    print(df)
