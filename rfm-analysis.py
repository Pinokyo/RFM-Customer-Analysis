'''For Recency, Calculate the number of days between present date and date of last purchase each customer.
For Frequency, Calculate the number of orders for each customer.
For Monetary, Calculate sum of purchase price for each customer.'''

rfm= uk.groupby('customer_id').agg({'invoice_date': lambda date: (PRESENT - date.max()).days,
                                        'invoice': lambda num: len(num),
                                        'price': lambda price: price.sum()})
# Let's change the name of columns
rfm.columns=['monetary','frequency','recency']
rfm['recency'] = rfm['recency'].astype(int)
rfm.head()

## Computing Quantile of RFM values
rfm['monetary_score'] = pd.qcut(rfm['monetary'], 5, ['5','4','3','2','1'])
rfm['frequency_score'] = pd.qcut(rfm['frequency'], 5, ['5','4','3','2','1'])
rfm['recency_score'] = pd.qcut(rfm['recency'], 5, ['1','2','3','4','5'])

## RFM Result Interpretation
#Combine all three quartiles(monetary_score, frequency_score, recency_score) in a single column, this rank will help you to segment the customers well group.

rfm['RFM_score'] = rfm.recency_score.astype(str)+ rfm.frequency_score.astype(str) + rfm.monetary_score.astype(str)
rfm.head()

# Filter out Top/Best cusotmers
rfm.sort_values('RFM_score', ascending=False)

##The best and worst customers are shown.
rfm[rfm["RFM_score"] == "553"].head()
rfm[rfm["RFM_score"] == "132"].head()

'''We classify customers according to their RFM scores. The score range for these classes is stated below. 
The reason why only Recency and Frequency are added here are only these two parameters in the table. But Monetary can also be added.'''

seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At Risk',
    r'[1-2]5': 'Can\'t Loose',
    r'3[1-2]': 'About to Sleep',
    r'33': 'Need Attention',
    r'[3-4][4-5]': 'Loyal Customers',
    r'41': 'Promising',
    r'51': 'New Customers',
    r'[4-5][2-3]': 'Potential Loyalists',
    r'5[4-5]': 'Champions'
}

## We include the seg_map defined above in the dataframe table.
rfm['Segment'] = rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str)
rfm['Segment'] = rfm['Segment'].replace(seg_map, regex=True)
rfm.head()

## We find the average and how many of the 3 parameters obtained by making groupby according to the segments.
rfm[["Segment", "recency","frequency","monetary"]].groupby("Segment").agg(["mean","count"])

## Let's take the "Need Attention" group.
rfm[rfm["Segment"] == "Need Attention"].head()

'''We have accessed the customer_id (index) values of customers that "need attention". 
Thus, promotions and mails specific to these customers can be sent through these IDs.
The reason we take these customers is because we have to follow different paths about this group.
'''
rfm[rfm["Segment"] == "Need Attention"].index

## By creating a new dataframe, we add the ID information of the customers belonging to the Need Attention group.
need_attention_df = pd.DataFrame()
need_attention_df["need_attention_id"] = rfm[rfm["Segment"] == "Need Attention"].index
need_attention_df.head()

## We made these IDs ready to use by converting them to csv format. If you want, you can also get other customer groups you want to deal with in the same way.
need_attention_df.to_csv("new_customers.csv")

## Finally, Let's look at the overall customer scale with Count Plot.
## For more detailed explanation and visuality, you should definitely go to the kaggle link.
# https://www.kaggle.com/thepinokyo/customer-segmentation-with-rfm-analysis

plt.figure(figsize=(24,5))
ax = sns.countplot(x="Segment", data=rfm,
                   facecolor=(0, 0, 0, 0),
                   linewidth=5,
                   edgecolor=sns.color_palette("dark", 10))
