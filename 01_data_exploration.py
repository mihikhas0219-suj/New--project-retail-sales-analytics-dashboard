import pandas as pd
df=pd.read_csv("dataset/retail_sales_dataset.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print("Duplicated rows:",df.duplicated().sum())
print(df[["Age","Quantity","Price per Unit","Total Amount"]].describe())
# convert date col to datetime
df["Date"]=pd.to_datetime(df["Date"])
print(df.dtypes)
# Create month name
df["Month Name"]=df["Date"].dt.strftime("%B")
# create month num
df["Month Number"]=df["Date"].dt.month
print(df[["Date","Month Name","Month Number"]].head())
df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
print(df.head())
total_sales=df["Total Amount"].sum()
print("Total Sales:",total_sales)
total_quantity=df["Quantity"].sum()
print("Total Quantity Sold:",total_quantity)
total_transaction=df["Transaction ID"].count()
print("Total Transactions:",total_transaction)
average_transaction=df["Total Amount"].mean()
print("Average Transaction Amount:",average_transaction)
sales_by_category=df.groupby("Product Category")["Total Amount"].sum()
print(sales_by_category)
quantity_by_category=df.groupby("Product Category")["Quantity"].sum()
print(quantity_by_category)
monthly_sales=df.groupby("Month")["Total Amount"].sum()
print(monthly_sales)
print(monthly_sales.to_string())
# percentage of total sales comes from Beauty,Clothing,and Electronics
category_sales=df.groupby("Product Category")["Total Amount"].sum()
category_percentage=(category_sales/total_sales)*100
print(category_percentage)
# sales by gender
sales_by_gender=df.groupby("Gender")["Total Amount"].sum()
print(sales_by_gender) 
# monthly sales
monthly_sales=df.groupby("Month")["Total Amount"].sum()
print("Monthly Sales:")
print(monthly_sales)
# top-selling category/product
top_category=sales_by_category.idxmax()
top_category_sales=sales_by_category.max()
print("Top Category:",top_category)
print("Top Category:",top_category_sales)
# avg sales by category
average_sales_category=df.groupby("Product Category")["Total Amount"].mean()
print("Average sales by category:")
print(average_sales_category)
df.to_csv("dataset/retail_sales_cleaned.csv",index=False)
print("Cleaned dataset saved successfully,")