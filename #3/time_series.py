# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import requests

# Set the API endpoint for Bitcoin prices (replace with your actual endpoint)
bitcoin_api_url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2022-01-01&end=2022-12-31"

# Fetch data from the API
response = requests.get(bitcoin_api_url)
data = response.json()

# Extract dates and prices
dates = list(data['bpi'].keys())
prices = list(data['bpi'].values())

# Convert the data to a DataFrame
df = pd.DataFrame({'Date': dates, 'USD': prices})

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plot the time series data
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['USD'], label='Bitcoin Price (USD)')
plt.title('Bitcoin Price Time Series')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()
