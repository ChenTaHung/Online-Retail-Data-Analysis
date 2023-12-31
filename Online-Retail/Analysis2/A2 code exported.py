# -*- coding: utf-8 -*-
"""
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RXLr0mJWYdwVkKyC5uOkuoZarOvWxKtN

# **Analysis Summary**

**Core Method:**  

- Cosine Similarity

**Why Cosine Similarity?:** 

- Cosine similarity provides an intuitive measure of the similarity between any two vectors. When applied to recommendations, it also offers an intuitive understanding of the relationship between the recommended item and the target item.
Products Recommend for CustomerID : 17841
"""

pd.DataFrame({"RecommendItem":[StockCD_Description_Map.get(x) for x in Cust_17841_Rec_List]})

"""Products Recommend for CustomerID : 12433"""

pd.DataFrame({"RecommendItem":[StockCD_Description_Map.get(x) for x in Cust_12433_Rec_List]})

"""Products Recommend for CustomerID : 15344"""

pd.DataFrame({"RecommendItem":[StockCD_Description_Map.get(x) for x in Cust_15344_Rec_List]})

"""# **Objective**

(2) Please recommend the following customers and the list of products they may purchase next. Why
1. 17841
2. 12433
3. 15344

# **Import modules and data**
"""

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse

Valid_Transaction_Data = pd.read_csv("/content/Valid_Transaction_Data.csv")
Valid_Transaction_Data["InvoiceNo"] = Valid_Transaction_Data["InvoiceNo"].astype(str)
Valid_Transaction_Data["CustomerID"] = Valid_Transaction_Data["CustomerID"].astype(str)

Valid_Transaction_Data.shape

Valid_Transaction_Data["InvoiceNo_Int"].nunique() == Valid_Transaction_Data["InvoiceNo"].nunique()

"""# **Generate product purchase amount vector for each Customer**

I remove the Data with missing CustomerID since the clustering result doesn't contain those samples.
"""

Valid_Transaction_Data_NoMiss = Valid_Transaction_Data[Valid_Transaction_Data["CustomerID"] != "Missing"]

StockCode_Vector_Data = Valid_Transaction_Data_NoMiss.pivot_table(index = ["CustomerID", "InvoiceNo_Int"], columns = "StockCode", values = "Quantity", aggfunc="sum", fill_value = 0).reset_index()
print("Data dim : ", StockCode_Vector_Data.shape)
print("Unique Customer Count : ", StockCode_Vector_Data["CustomerID"].nunique())

StockCode_Vector_Data.head()

"""Create the vector of total amount on purchasing each product for every customer."""

# Mean_ProductCnt_Vector_Df = StockCode_Vector_Data.drop("InvoiceNo_Int", axis = 1).groupby("CustomerID").mean()
Sum_ProductCnt_Vector_Df = StockCode_Vector_Data.drop("InvoiceNo_Int", axis = 1).groupby("CustomerID").sum()

Sum_ProductCnt_Vector_Df.head()

"""# **Generate Dictionary for StockCode and Description**"""

temp = Valid_Transaction_Data_NoMiss.drop_duplicates("StockCode")[["StockCode", "Description"]]
StockCD_Description_Map = dict(zip(temp["StockCode"], temp["Description"]))

"""# **Define function for Recommendation**

- Using `Cosine Similarity`.
"""

def Recommend(target_Customer_ID, Mean_data_OR_Sum_data):
  if type(target_Customer_ID) is not str : 
    target_Customer_ID = str(target_Customer_ID)
  df = Mean_data_OR_Sum_data.copy()
  df_values = df.values
  # Calculate cosine similarity
  cos_sin_mat = cosine_similarity(sparse.csr_matrix(df_values))
  cos_sin_DF = pd.DataFrame(cos_sin_mat, columns = df.index, index=df.index)
  target_cust = cos_sin_DF[target_Customer_ID]
  # Prevent from selecting itselves
  Aim_target_cust = target_cust[target_cust < 1]
  Highest_Cos_CustID_Cos = Aim_target_cust[Aim_target_cust == Aim_target_cust.max()]
  print(f"CustomerID : [{Highest_Cos_CustID_Cos.index[0]}] Has the highest cosine similarity :[{float(Highest_Cos_CustID_Cos.values):.4f}]")
  Highest_Cos_CustID = Highest_Cos_CustID_Cos.index[0]
  compare_df = pd.DataFrame({Highest_Cos_CustID : df.loc[Highest_Cos_CustID,:], target_Customer_ID :df.loc[target_Customer_ID,:]}, index = df.columns)
  compare_df["RecommendMark"] = compare_df[str(Highest_Cos_CustID)] - compare_df[target_Customer_ID]
  Recommend_Stock_Code = compare_df[compare_df["RecommendMark"] > 0].index
  print("Recommend List :", list(Recommend_Stock_Code))
  return list(Recommend_Stock_Code)

"""# **CustomerID : 17841**"""

Cust_17841_Rec_List = Recommend(17841, Sum_ProductCnt_Vector_Df)

"""product Recommend for CustomerID : 17841"""

pd.DataFrame({"RecommendItem":[StockCD_Description_Map.get(x) for x in Cust_17841_Rec_List]})

"""# **CustomerID : 12433**"""

Cust_12433_Rec_List = Recommend(12433, Sum_ProductCnt_Vector_Df)

"""product Recommend for CustomerID : 12433"""

pd.DataFrame({"RecommendItem":[StockCD_Description_Map.get(x) for x in Cust_12433_Rec_List]})

"""# **CustomerID : 15344**"""

Cust_15344_Rec_List = Recommend(15344, Sum_ProductCnt_Vector_Df)

"""product Recommend for CustomerID : 15344"""

pd.DataFrame({"RecommendItem":[StockCD_Description_Map.get(x) for x in Cust_15344_Rec_List]})

