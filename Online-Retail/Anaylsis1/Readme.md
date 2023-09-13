<h2> Objective Question: Based on the data, which customers have similar preferences in their purchases? Why? </h2>

##### Table of Content :

Title | Content
------|---------
Clustering Result Summary|[**Jump**](#-clustering-result-summary- "Clustering Result Summary")
Analysis Process Description|[**Jump**](#-Analysis-Process-Description- "Analysis Process Description")
Results Elaboration|[**Jump**](#-Results-Elaboration- "Results Elaboration")

### **=== Clustering Result Summary ===**

 Clusters number : **7** [0, 1, 2, 3, 4, 5, 6]

**1. Recency :** 

- Customers in `Cluster 1` has a higher loyalty.
- `Cluster 1` has a higher frequency on purchasing.

**2. Frequency :**

- Purchasing Frequency : `Cluster 1` > `Cluster 2` > `Cluster 3` .

**3. Monetary :**

- Customers in `Cluster 1` have a higher distribution on sales revenue to the store.
- Customers in `Cluster 1` and `Cluster 3` have close average expense on each transaction.

**4. Location :**

- No Significant difference on clusters.

**5. Other Clusters :**

- `Cluster 0` and `Cluster 6` mostly contain outliers.
- I consider `Cluster 0` and `Cluster 6` are noise customers in the dataset.

`KMeans Core Features Plot`

![](https://github.com/ChenTaHung/Online-Retail-Data-Analysis/blob/main/Online-Retail/pics/Kmeans%20Core%20Feature%20Plot.png)


`KMeans Location Plot`

![](https://github.com/ChenTaHung/Online-Retail-Data-Analysis/blob/main/Online-Retail/pics/Cluster_Result_with_Location_Percentage.png)

[Back to ToC](#table-of-content- "Jump to the top")

<h2> Analysis Process Description </h2>

### **=== Process Details ===**

- Using external data[`"Contries-continent.csv"`](https://github.com/dbouquin/IS_608/blob/master/NanosatDB_munging/Countries-Continents.csv) to minimize the granularity of the `Country` column and extract the continent variable as the feature for customer location.

- [`Online Retail Data Set`](https://archive.ics.uci.edu/ml/datasets/Online+Retail) provides a description of the `stockCode` field below, but it should be written as a capital C.

> InvoiceNo: Invoice number. Nominal, a 6-digit integral number uniquely assigned to each transaction. If this code starts with letter 'c', it indicates a cancellation.

- Remove the transactions meaning a refund. 

- Clean the `UnitPrice` and `Quantity` where have showed the data in non-sense to prevent from causing negative impact when calculating `TotalPrice`. 

- In the data description, it is mentioned that the 5-digit numbers in StockCode represent unique product codes, but the "Postage" item does not have a 5-digit StockCode.

- Next, we will create feature data for each `CustomerID`:
    - **Recency** related: 
     1. Average number of days between two consecutive transactions
     2. Number of days since the last purchase relative to the last date in the dataset
    - **Frequenct** related:
     1. Total number of transactions (InvoiceNo)
     2. Number of occurrences per year
     3. Number of occurrences per quarter
     4. Number of occurrences per month
     5. Number of occurrences per day
    - **Monetary** related:
     1. Total spending
     2. Average spending per transaction
    - **Location** related:
     1. Continent(one-hot encoding and drop the `unspecified`)
    
- Applying K-means clustering:

    - Initially, after scaling the data, it was observed that the performance was still not satisfactory, as there was no optimal number of clusters found using silhouette scores.
    - Considering the possibility of outliers affecting the results, a "clamp transformation" was applied to limit the data within a certain range defined by the median ± n times the standard deviation.
    - Later, it was noted that the data included Dummy variables for Continent, so a "Min-Max Scaling" was applied to normalize each feature to a range between 0 and 1.
    - Observing the silhouette coefficients, it was found that a cluster size of 7 yielded a relatively better solution.

> Notes : The results of K-means clustering varied even when the same random_state was set after reallocating resources in GoogleColab. Therefore, only the results obtained using the MinMaxScale method were retained. The details of the other steps have been recorded as supplementary notes at the bottom of the notebook file. Thank you.

`Clustering Performance`

![](https://github.com/ChenTaHung/Online-Retail-Data-Analysis/blob/main/Question2/pics/MinMaxScale_Kmeans_Validation.png)

[Back to ToC](#table-of-content- "Jump to the top")

<h2> Results Elaboration </h2>

### **=== Analysis Results Details ===**    

I adopted the concept of RFM analysis and selected four core variables: `"time since last transaction"`, `"total transaction count"`, `"total transaction amount"`, and `"average transaction amount"` to represent the concepts of R (Recency), F (Frequency), and M (Monetary).

As there were still some outliers that significantly affected the visualization and interpretation of boxplots, I decided to only visualize the data within a range of median ± n times the standard deviation.

**Results Elaboration :**

Cluster Conclusion: 7 clusters were created.

`Percentage in each cluster`

![](https://github.com/ChenTaHung/Online-Retail-Data-Analysis/blob/main/Online-Retail/pics/MinMaxScale_Kmeans_Validation.png)

1. We can observe from the boxplots that in Cluster 1, customers have fewer days since their last transaction compared to other clusters. Corresponding to the Total Transaction Count, we can understand that Cluster 1 consists of customers with relatively higher loyalty.

2. We notice that the average transaction amount in Cluster 1 is similar to Cluster 3. However, when combining the frequency of transactions, i.e., considering the Total Transaction Amount, we find that Cluster 1 represents a group of customers who contribute significantly to store revenue over the long term.

3. Given the opportunity, it might be beneficial to grant VIP status to customers in Cluster 1 since they are core customers. Offering timely discounts and rewards to this group can enhance customer retention. Additionally, these customers can be used to attract others, and if new customers exhibit similar consumption behavior to Cluster 1, they can also be converted into VIP members.

4. Cluster 3 consists of a larger number of customers, and their average spending is also good. By increasing the frequency of purchases through marketing or incentives, store revenue can be significantly boosted.

5. As data with tails has been excluded before drawing the box plots, Cluster 0 and Cluster 6 have a higher concentration of such data, making these two clusters represent relatively niche customer segments.

6. If there is additional data and time available, analyzing the product content might be valuable. You can examine the preferred product categories for each cluster and tailor promotions and advertisements accordingly.

7. Currently, there doesn't appear to be significant regional differences in consumer behavior. However, by continuing to analyze product content, you may discover regional preferences for specific types or categories of products in each continent.



![](https://github.com/ChenTaHung/Online-Retail-Data-Analysis/blob/main/Online-Retail/pics/MinMaxScale_SamplePercentage.png)

[Back to ToC](#table-of-content- "Jump to the top")

<h1> Thanks for reading!</h1>
