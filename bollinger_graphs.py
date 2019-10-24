# Draw Bollinger Bands on your currency of choice!

# Imports
import requests
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
from seaborn import set_style

print('Draw Bollinger Bands on your currency of choice!')

# This is where the user defines the start_date, end_date, coin, and time period

start_date = input('Start date (yyyy-mm-dd): ')

end_date = input('End date (yyyy-mm-dd):   ')

coin1 = input('First coin (use abbreviations, i.e. USD) : ').upper()

coin2 = input('Second coin (use abbreviations, i.e. USD) : ').upper()

ma_bb = int(input('Size of time period in days for Moving Average and Bollinger Bands (Enter an integer!): '))

# API

x = requests.get(f'https://api.exchangeratesapi.io/history?start_at={start_date}&end_at={end_date}&symbols={coin2}&base={coin1}')

# Error management

if x.status_code != 200:
	print(f"Error: {x.json()['error']}")
else:
	# Pulling out and organizing the data from the API

	ordered_data = OrderedDict(sorted(x.json()['rates'].items()))

	# Putting the data into a dataframe with the index being the dates and columns being the currencies

	df = pd.DataFrame(data=ordered_data).transpose()

	# Setting the index to a datetime series

	df.index = pd.to_datetime(df.index)

	# Renaming Columns
	df.columns = ['Closing Price']

	# Moving Average
	df[f'{ma_bb} Day Mean'] = df['Closing Price'].rolling(window=ma_bb).mean()

	# Upper Band
	df['Upper Band'] = df[f'{ma_bb} Day Mean'] + 2*(df['Closing Price'].rolling(ma_bb).std())

	# Lower Band
	df['Lower Band'] = df[f'{ma_bb} Day Mean'] - 2*(df['Closing Price'].rolling(ma_bb).std())

	# Plotting
	set_style('darkgrid')
	df[['Closing Price',f'{ma_bb} Day Mean','Upper Band','Lower Band']].plot(figsize=(16,6))
	plt.title(coin1+' / '+coin2+' Bollinger Bands')
	plt.legend(bbox_to_anchor=(1, 0.65), loc=2)
	plt.show()