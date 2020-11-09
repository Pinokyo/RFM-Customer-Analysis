## Customer Segmentation with RFM Analysis (RFM Analizi ile Müşteri Segmentasyonu)
### What is RFM?
RFM stands for Recency, Frequency, and Monetary value, each corresponding to some key customer trait. These RFM metrics are important indicators of a customer’s behavior because frequency and monetary value affects a customer’s lifetime value, and recency affects retention, a measure of engagement.

- Recency - Time since the customer's last purchase. In other words, it is the "time elapsed since the last contact of the customer".
Formula = Today's date - Last purchase date. <br>
While the analyzes are carried out in general terms, the part we define as "Today's history" is accepted as the day of analysis.
- Frequency - The total number of purchases of the customer.
- Monetary - The total expenditure made by the customer.

### Data Set Information:
https://archive.ics.uci.edu/ml/datasets/Online+Retail+II <br>
This Online Retail II data set contains all the transactions occurring for a UK-based and registered, non-store online retail between 01/12/2009 and 09/12/2011.The company mainly sells unique all-occasion gift-ware. Many customers of the company are wholesalers. 

### Attribute Information:
- InvoiceNo: Invoice number. Nominal. A 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter 'c', it indicates a cancellation.
- StockCode: Product (item) code. Nominal. A 5-digit integral number uniquely assigned to each distinct product.
- Description: Product (item) name. Nominal.
- Quantity: The quantities of each product (item) per transaction. Numeric.
- InvoiceDate: Invice date and time. Numeric. The day and time when a transaction was generated.
- UnitPrice: Unit price. Numeric. Product price per unit in sterling (Â£).
- CustomerID: Customer number. Nominal. A 5-digit integral number uniquely assigned to each customer.
- Country: Country name. Nominal. The name of the country where a customer resides. <br> 

This project includes the segmentation of customers in the Online Retail II dataset under two main headings, Data Pre-processing and RFM Analysis. For more detailed information: https://www.kaggle.com/thepinokyo/customer-segmentation-with-rfm-analysis

***
### RFM Nedir?
RFM, müşteri değerini analiz etmek için kullanılan bir yöntemdir. Veritabanı pazarlama ve doğrudan pazarlamada yaygın olarak kullanılmaktadır ve perakende ve profesyonel hizmetler endüstrilerinde özel ilgi görmüştür. RFM üç boyutu temsil eder:

- Recency (Yenilik) — Müşterinin son satın almasından bugüne kadar geçen süredir. Diğer bir ifade ile “Müşterinin son temasından bugüne kadar geçen süre” dir.
Formül = Bugünün tarihi — Son satın alma tarihi. <br>
Genel anlamda analizler yapılıyorken “Bugünün tarihi” olarak tanımladığımız kısım analizin yapıldığı gün olarak kabul edilmektedir. Çıkan değerin küçük olması istenir.
- Frequency (Sıklık) — Müşterinin toplam satın alma sayısıdır.
- Monetary (Parasal Değer) — Müşterinin yaptığı toplam harcamadır.

### Dataset Bilgisi:
https://archive.ics.uci.edu/ml/datasets/Online+Retail+II <br>
Online Retail II isimli veri seti İngiltere merkezli online bir satış mağazasının 01/12/2009 - 09/12/2011 tarihleri arasındaki satışlarını içermektedir. Bu şirket hediyelik eşya satışı yapmaktadır. Promosyon ürünleri gibi düşünebilir ve müşterilerinin çoğu da toptancıdır.

### Değişkenler
- InvoiceNo: Fatura numarası. Her işleme yani faturaya ait eşsiz numara. Eğer bu kod C ile başlıyorsa işlemin iptal edildiğini ifade eder.
- StockCode: Ürün kodu. Her bir ürün için eşsiz numara.
- Description: Ürün ismi.
- Quantity: Ürün adedi. Faturalardaki ürünlerden kaçar tane satıldığını ifade etmektedir.
- InvoiceDate: Fatura tarihi ve zamanı.
- UnitPrice: Ürün fiyatı.(Sterlin cinsinden)
- CustomerID: Eşsiz müşteri numarası.
- Country: Ülke ismi. Müşterinin yaşadığı ülke. <br>

Bu proje Data Pre-processing ve RFM Analysis adında iki temel başlık altında Online Retail II dataset'indeki müşterilerin segmentasyonunu içermektedir. Daha detaylı bilgi için: https://www.kaggle.com/thepinokyo/customer-segmentation-with-rfm-analysis
