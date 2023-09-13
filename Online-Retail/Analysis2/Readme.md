<h1> Objective Question: Determine the future purchases of the following three customers and provide explanations for these predictions. </h1>

1. [**17841**](#recommendation-for-customerid-17841 "17841")

2. [**12433**](#recommendation-for-customerid-12433 "12433")

3. [**15344**](#recommendation-for-customerid-15344 "15344")
 
If you want to : 
[**Jump to Analysis Process Description**](#Analysis Process Description "Analysis Process Description")

### **=== Analysis Summary ===**

- Core Method : `Cosine Similarity`
- Why cosine similarity? : Cosine similarity provides an intuitive measure of the similarity between any two vectors. When applied to recommendations, it helps us easily grasp the relationship between the recommended item and the target item.
- I select the customer with the "highest cosine similarity" to the "recommended customer (target)" compared to the "recommended customer (reference)" and, based on the purchase list of the reference customer, if the purchase quantity of the reference customer is greater than that of the target customer, then those items are recommended to the target customer.
    - The purchasse quantities of four products [A,B,C,D] of target customer is [1,1,1,0], and the purchase quantities of refgerence customer are [1,1,2,1], then teh recommendation result will be [C,D]

#### **Recommendation for CustomerID: 17841**

`#` |Recommend Items
--|---------------
1 |SKULL AND CROSSBONES GARLAND
2 |4 PEAR BOTANICAL DINNER CANDLES
3 |GAOLERS KEYS DECORATIVE GARDEN
4 |SWALLOW SQUARE TISSUE BOX
5 |SET 3 PAPER VINTAGE CHICK PAPER EGG
6 |GLASS APOTHECARY BOTTLE PERFUME
7 |CLASSIC GLASS SWEET JAR
8 |VINTAGE 2 METER FOLDING RULER
9 |DOG LICENCE WALL ART
10|BICYCLE SAFTEY WALL ART
11|SMALL LICORICE DES PINK BOWL
12|ANTIQUE SILVER TEA GLASS ETCHED

#### **Recommendation for CustomerID: 12433**

`#` |Recommend Items
--|---------------
1 |CREAM HEART CARD HOLDER
2 |REGENCY CAKESTAND 3 TIER
3 |GREEN REGENCY TEACUP AND SAUCER
4 |PINK REGENCY TEACUP AND SAUCER
5 |ROSES REGENCY TEACUP AND SAUCER
6 |PHOTO FRAME CORNICE
7 |TRIPLE PHOTO FRAME CORNICE
8 |FAMILY PHOTO FRAME CORNICE
9 |12 MESSAGE CARDS WITH ENVELOPES
10|RECYCLED ACAPULCO MAT GREEN
11|RECYCLED ACAPULCO MAT BLUE
12|RECYCLED ACAPULCO MAT PINK
13|KNICKERBOCKERGLORY MAGNET ASSORTED

#### **Recommendation for CustomerID: 15344**

`#` |Recommend Items
--|---------------
1 |RED TOADSTOOL LED NIGHT LIGHT
2 |RED HANGING HEART T-LIGHT HOLDER
3 |LOVEBIRD HANGING DECORATION WHITE
4 |HANGING METAL HEART LANTERN
5 |HEART OF WICKER SMALL
6 |WOODEN STAR CHRISTMAS SCANDINAVIAN
7 |CARD HOLDER GINGHAM HEART
8 |WICKER WREATH SMALL
9 |RABBIT NIGHT LIGHT
10|CARD HOLDER LOVE BIRD SMALL
11|WHITE HANGING HEART T-LIGHT HOLDER

## Analysis Process Description ##

### **=== Process Details ===**

- Create a vector for each customer representing the quantity of all products. There are a total of 4338 customer IDs and 3665 products.
- Calculate the cosine similarity between the purchase vector of each customer ID and all customers, resulting in a 4338x4338 matrix.
- Identify the customer IDs with the highest similarity to the target customers [17841, 12433, 15344] which are the reference customers.
- Subtract the purchase product quantity vector of the reference customers from the target customer's purchase product quantity vector, selecting items with quantities > 0 (`StockCode`).
- Convert the extracted `StockCode` into corresponding product names and use them as the recommended product list.


<h1>Thanks for reading!</h1>
