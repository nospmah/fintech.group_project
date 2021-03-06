# **Bitcoin - Past, Present, is the Future**

## Team Members
---
* Abdullahi Said
* Ryan Howard
* Max Larsen
* Brian Hampson
<p>

## **Foreward**
---
#### We started this project out with certain indicators in mind that are unique to bitcoin (on-chain analysis). We decided to run correlations on price vs some of these indicators, of which most returned insignificant correlation values (under .5). Instead of chasing after indicators that resulted in high correlation values, we chose to display them regardless. Our hypothesis based on what we knew about these indicators turned out to be false. 
<p>

## **Research Questions**
---

**Should you buy bitcoin, historically?**
<p>

* We wanted to know what would a $x.xx investment be worth today had we invested it in a series of different asset classes over x period of time. 

**Should you buy bitcoin, historically**

* We wanted to look into whether or not buying bitcoin right now is a good idea given the current market conditions. 
<p>

## **Description and Outline**
---
For our project we will use various models and research methods to decide if Bitcoin is a good investment at this time and over what period.
<p>

**Historical Analysis**

We compared Bitcoin to the following benchmark assets:
* SPY (S&P 500)
* GLD (Gold)
* ETH (Ethereum)
* LTC (Litecoin)
* XRP (Ripple)

### Standard Deviation

There were to particularly deep insights with respect to standard deviation; Bitcoin deviates more than GLD and SPY by a fair margin but much less than the other crypto assets we compared.

### Cumulative Returns

Bitcoin was definitely the winner in 2020 with respect to cumulative returns

### Monte Carlo Simulation

There is a 95% chance that an initial investment of $10,000 in the portfolio over the next 5 years will end within in the range of $11324.42 and $3050996.83

<br><br/>

**Technical Analysis** 

Then we decided to look at current markets and network data to understand what's happening in real time with the BTC markets. We used the following market indicators, as well as a new generations of "on-chain" indicators to analyze movement on the bitcoin network. 

* On-Chain indicator 1 - Exchange Netflow (Ryan)
    * Used as an indicator of overall market sentiment towards to long term viability and belief in the asset as a store of value. More money entering exchanges signals a selling, more money leaving the exchanges indicates holding patterns. 
    
* On-Chain indicator 2 - Puell Multiple Vs Price (Max)
    
    * This metric looks as the supply side of Bitcoin's economy and highlights the beginning and ending of market cycles. It takes into account bitcoin miners, their revenue, as well as their need to cover fixed cost; so in theory the revenue they generate, should influence price over time. More specifically, the puell multiple is calculated by dividing the daily issuance of value of bitcoin by the 365-day moving average of daily issuance value.
    * How is the Puell Multiple used?
As we have discussed earlier, this asset is prone to fairly extremem swings and a result there are periods of time where the value of bitcoins being mined and entering the market is too high or too low compared to historical norms. But by visualizing the puell multiple along with the price of Bitcoin, Bitcoin investors can better understand these high and low periods and capitalize their investments by selling when Puell multiple reaches the 'sell zone'(around 4 or higher) and buying when the Puell Multiple reaches the "buy zone"(0.3 to 0.5). Historically, each time the Puell Multiple has dropped into the "buy zone", Bitcoin investors who bought here obained an average return of 5,000%.
    
* On-Chain indicator 3 - All Exchanges Reserve
    *  This indicator measures how many bitcoins are held on exchanges, otherwise known as exchange reserves. The reserves of exchanges increase when investors exchange their Bitcoin for cash. Typically, deposits or inflows are considered selling pressure, because traders have to send BTC to exchanges in order to sell. This suggests that more users prefer to store their bitcoin in private wallets, which may lead to a lower selling pressure. This results in a holding mentality where there are more buyers than sellers in the market causing the price of bitcoin increase. Recently bitcoin reserves have reached the lowest level since 2018. This can be one factor as to why the price of bitcoin has increased quickly over the last couple of months. While this theory does make sense intuitively, quantitatively we have not seen a strong correlation between the price of bitcoin and the amount of reserve bitcoin held on exchanges. This does not necessarily mean that the two are unrelated. It could just be a limitation of our analysis. Using a Multivariate regression model that takes into account other factors might prove more useful at predicting price movements.
    
* Market Indicator 1- 21 Week MA
    *  As the name implies, the 21 week moving average takes the mean of the weekly closing prices for bitcoin over the last 21 weeks. Historical it has proven very accurate for predicting buying and selling points. The 21 week moving average serves as a resistance line to spot bull runs. Typically when the price of bitcoin surpasses the 21 week moving average, it signals a bull run. Over time the 21 week moving average will also increase and the convergence of the two signals the end of the bull run which indicates a selling point. Currently the price of bitcoin is well above it’s 21 week moving average, which indicates the price will fall to meet the 21 week moving average.

* Market indicator 2 - MVRV Z-Score (Ryan)
    * Taking the overall market cap and dividing it by realized value, or the value that a specific asset was bought/sol for and calculating it's value. A high or low score can indicate and overbought/oversold sentiment. 
* Market indicator 3 -  Standard Deviation (Brian/Max)
<p>

## Final outcome: 
---
We found that over a 1 year period, investing $10,000 into BTC 1 year ago, would have led to a 450% gain. The models from the monte carlo simulation showed, with potential data errors, a significant amount of upside for similar or less risk as gold. 

Looking at current indicators we found mixed signals from the indicators. Some showed a strong buy/hold pattern, while others suggested the markets were too hot and it may not be the right time to buy. 

We concluded that right now, an investment of $10,000 would result in a range of $11324.43 to $3050996.83 with approximately 95% confidence.


[**Dashboard with our results**](https://github.com/nospmah/fintech.group_project/blob/main/reports/analysis.ipynb?short_path=9ddbebd)

## Datasources
---
* [CryptoQuant](cryptoquant.com)
* [Alpaca SDK](alpaca.com)
* [Open API](openapi.io)


