# importing required libraries for financial plot fetch and graphing
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt


#grabbing crypto of choice: I'm going to go with Bitcoin, Ether, and Dogecoin
cryptocs = ['BTC-USD','ETH-USD', 'DOGE-USD']

#Grabbing data from a year ago
datafetch = yf.download(cryptocs, start = '2021-06-25', end = '2022-06-25')
datafetch.head()

#checking for any null statuses
datafetch.isnull().any()

#We check for closing
adj_close=datafetch['Adj Close']
adj_close.head()

# ploting the adjusted closing price
fig, axs =plt.subplots(2,2,figsize=(16,8),gridspec_kw ={'hspace': 0.2, 'wspace': 0.1})
axs[1,1].remove()
axs[0,0].plot(adj_close['BTC-USD'])
axs[0,0].set_title('BTC')
axs[0,1].plot(adj_close['ETH-USD'])
axs[0,1].set_title('ETH')
axs[1,0].plot(adj_close['DOGE-USD'])
axs[1,0].set_title('DOGE')
plt.show()

# Returns i.e. percentage change in the adjusted close price and drop the first row with NA's
returns = adj_close.pct_change().dropna(axis=0)
#view the first 5 rows of the data frame
returns.head()

#ploting the returns
fig, axs = plt.subplots(2,2,figsize=(16,8),gridspec_kw ={'hspace': 0.2, 'wspace': 0.1})
axs[1,1].remove()

axs[0,0].plot(returns['BTC-USD'])
axs[0,0].set_title('BTC')
axs[0,0].set_ylim([-0.5,0.5])
axs[0,1].plot(returns['ETH-USD'])
axs[0,1].set_title('ETH')
axs[0,1].set_ylim([-0.5,0.5])
axs[1,0].plot(returns['DOGE-USD'])
axs[1,0].set_title('DOGE')
axs[1,0].set_ylim([-0.5,0.5])
plt.show()

#volatility, standard deviation of the returns
returns.std()


#ploting the histogram
fig, axs = plt.subplots(2,2,figsize=(16,8),gridspec_kw ={'hspace': 0.2, 'wspace': 0.1})
axs[1,1].remove()
axs[0,0].hist(returns['BTC-USD'], bins=50, range=(-0.2, 0.2))
axs[0,0].set_title('BTC')
axs[0,1].hist(returns['ETH-USD'], bins=50, range=(-0.2, 0.2))
axs[0,1].set_title('ETH')
axs[1,0].hist(returns['DOGE-USD'], bins=50, range=(-0.2, 0.2))
axs[1,0].set_title('DOGE')
plt.show()

# Cumulative return series
cum_returns = ((1 + returns).cumprod() - 1) *100
cum_returns.head()

cum_returns.plot(figsize=(20,6))
plt.title('Cumulative Returns')

#compute the correlations
returns.corr()

#plot the correlations
sns.heatmap(returns.corr(), annot=True, cmap='coolwarm')
plt.show()

# compute a short-term 20-day moving average
MA20 = adj_close.rolling(20).mean()
# compute a Long-term 50-day moving average
MA50 = adj_close.rolling(100).mean()
# compute a Long-term 100-day moving average
MA100 = adj_close.rolling(100).mean()
# ploting the moving average
fig, axs = plt.subplots(2,2,figsize=(20,8),gridspec_kw ={'hspace': 0.2, 'wspace': 0.1})
axs[1,1].remove()
axs[0,0].plot(adj_close['BTC-USD'], label= 'closing')
axs[0,0].plot(MA50['BTC-USD'], label= 'MA50')
axs[0,0].set_title('BTC')
axs[0,0].legend()
axs[0,1].plot(adj_close['ETH-USD'], label= 'closing')
axs[0,1].plot(MA50['ETH-USD'], label= 'MA50')
axs[0,1].set_title('ETH')
axs[0,1].legend()
axs[1,0].plot(adj_close['DOGE-USD'], label= 'closing')
axs[1,0].plot(MA50['DOGE-USD'], label= 'MA50')
axs[1,0].set_title('DOGE')
axs[1,0].legend()
plt.show()

# ploting the moving average
fig, axs = plt.subplots(2,2,figsize=(16,8),gridspec_kw ={'hspace': 0.2, 'wspace': 0.1})
axs[1,1].remove()

axs[0,0].plot(adj_close['BTC-USD'], label= 'price')
axs[0,0].plot(MA20['BTC-USD'], label= 'MA20')
axs[0,0].plot(MA100['BTC-USD'], label= 'MA100')
axs[0,0].set_title('BTC')
axs[0,0].legend()
axs[0,1].plot(adj_close['ETH-USD'], label= 'price')
axs[0,1].plot(MA20['ETH-USD'], label= 'MA20')
axs[0,1].plot(MA100['ETH-USD'], label= 'MA100')
axs[0,1].set_title('ETH')
axs[0,1].legend()
axs[1,0].plot(adj_close['DOGE-USD'], label= 'price')
axs[1,0].plot(MA20['DOGE-USD'], label= 'MA20')
axs[1,0].plot(MA100['DOGE-USD'], label= 'MA100')
axs[1,0].set_title('DOGE')
axs[1,0].legend()
plt.show()

