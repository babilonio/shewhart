import pandas as pd
import requests as req

download_url = "https://query1.finance.yahoo.com/v7/finance/download/%5EGSPC?period1=-1325635200&period2=1598745600&interval=1mo&events=history"
r = req.get(download_url, allow_redirects=True)
open('historical_data.csv', 'wb').write(r.content)


historical_data = pd.read_csv("historical_data.csv")