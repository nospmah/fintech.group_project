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

**Historical Analysis** -

We used a Monte Carlo Simulation on the following to compare: 
* SPY (S&P 500)
* GLD (Gold)
* ETH (Ethereum)
* LTC (Litecoin)
* XRP (Ripple)

(Brian to say something here)
<br><br/>

**Technical Analysis** -

Then we decided to look at current markets and network data to understand what's happening in real time with the BTC markets. We used the following market indicators, as well as a new generations of "on-chain" indicators to analyze movement on the bitcoin network. 

* On-Chain indicator 1 - Exchange Netflow (Ryan)
* On-Chain indicator 2 - Puell Multiple Vs Price (Max)
* On-Chain indicator 3 - All Exchanges Reserve vs Price (Abdul)
* Market Indicator 1- 21 Week MA (Abdul)
* Market indicator 2 - MVRV Z-Score (Ryan)
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


