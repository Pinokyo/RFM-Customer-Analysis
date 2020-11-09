import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_10_11 = pd.read_excel("/kaggle/input/uci-online-retail-ii-data-set/online_retail_II.xlsx", sheet_name = "Year 2010-2011")
# df_10_11.head()

df_10_11.info()
df_10_11.isnull().sum()
df_10_11.dropna(inplace = True)
df_10_11.shape

## Let's arrange the column names for clarity and easy writing.
df_10_11.columns = map(str.lower, df_10_11.columns)
df_10_11 = df_10_11.rename(columns={"stockcode":"stock_code","invoicedate": "invoice_date", "customer id":"customer_id"})
df_10_11.head()

## We obtain information about the data set by examining statistical values, quartiles.
df_10_11.describe([0.01,0.05,0.10,0.25,0.50,0.75,0.90,0.95, 0.99]).T

## If you remember Quantity represented the number of products It expressed how many products in the invoices were sold. 
## The fact that its minimum value is -80995 indicates that some of its values are very extreme.
df_10_11.sort_values(by='quantity', ascending=True)

## This could be because cancellation items transactions are captured in negative amount. For now,let's filter the negative numbers to avoid them.
df_10_11 = df_10_11[(df_10_11['quantity']>0)]
df_10_11.describe()

df_10_11.country.unique()

country_data=df_10_11[['country','customer_id']].drop_duplicates()
country_data.country.value_counts()[:10].plot(kind='bar')

## In the given dataset, we can observe that most of the customers are from "United Kingdom". So let's filter the data for the UK customer.
uk=df_10_11[df_10_11.country=='United Kingdom']
uk = uk[(uk['quantity']>0)]
uk.describe()

## How many of the products do we have?
uk["description"].value_counts().head()

## What is the most ordered item?
uk.groupby("description").agg({"quantity":"sum"}).sort_values("quantity", ascending = False).head()

## How many invoices have been issued in total?
uk["invoice"].nunique()

## How much money is earned on average per invoice?
#uk.loc[:,'quantity'] *= -1
uk['total_price'] = uk['quantity'] * uk['price']
uk.head()

What are the most expensive products?
uk.sort_values("price", ascending = False).head()

## Let's observe the outliers for quantity, price, total_price.
for feature in ["quantity","price","total_price"]:

    Q1 = uk[feature].quantile(0.01)
    Q3 = uk[feature].quantile(0.99)
    IQR = Q3-Q1
    upper = Q3 + 1.5*IQR
    lower = Q1 - 1.5*IQR

    if uk[(uk[feature] > upper) | (uk[feature] < lower)].any(axis=None):
        print(feature,"→ YES")
        print(uk[(uk[feature] > upper) | (uk[feature] < lower)].shape[0])
    else:
        print(feature, "→ NO")
        
'''Here, we should filter the necessary columns for RFM analysis. We only need five columns customer_id, invoice_date, invoice, quantity, and price. 
customer_id will uniquely define your customers, invoice_date help you calculate recency of purchase, 
invoice helps you to count the number of time transaction performed(frequency). 
quantity purchased in each transaction and price of each unit purchased by the customer will help you to calculate the total purchased amount.
'''

from datetime import datetime

uk=uk[['customer_id','invoice_date','invoice','quantity','price']]

uk['invoice_date'].min(),uk['invoice_date'].max()
#(Timestamp('2010-12-01 08:26:00'), Timestamp('2011-12-09 12:49:00'))

PRESENT = datetime(2011,12,10)
uk['invoice_date'] = pd.to_datetime(uk['invoice_date'])

uk.head()

## Let's go to the rfm-analysis part.
