import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Obtain Time Series Data
bitcoin_api_url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2022-01-01&end=2022-12-31"
response = requests.get(bitcoin_api_url)
data = response.json()

dates = list(data['bpi'].keys())
prices = list(data['bpi'].values())

df = pd.DataFrame({'Date': dates, 'USD': prices})
df['Date'] = pd.to_datetime(df['Date'])

# Plot the time series data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['USD'], label='Bitcoin Price (USD)')
plt.title('Bitcoin Price Time Series')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Data Transformations
df['Returns'] = df['USD'].pct_change()
df['Log_Price'] = np.log(df['USD'])

# Plot the transformed data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Returns'], label='Daily Returns')
plt.title('Bitcoin Daily Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend()
plt.show()
