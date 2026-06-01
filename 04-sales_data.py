import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("04-sales_data.csv")

# Create Revenue Column
df["Revenue"] = df["Quantity"] * df["Price"]

print(df.head())
print(df.describe())
df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = df.groupby(df["Date"].dt.month)["Revenue"].sum()

plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)

plt.show()
product_sales = df.groupby("Product")["Revenue"].sum()

plt.figure(figsize=(10,5))
product_sales.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.show()
category_sales = df.groupby("Category")["Revenue"].sum()

plt.figure(figsize=(6,6))
plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%"
)

plt.title("Category-wise Revenue")
plt.show()
top_orders = df.nlargest(10, "Revenue")

plt.figure(figsize=(10,5))
plt.bar(top_orders["Order_ID"].astype(str),
        top_orders["Revenue"])

plt.title("Top 10 Orders")
plt.xlabel("Order ID")
plt.ylabel("Revenue")

plt.show()
plt.figure(figsize=(8,5))

plt.hist(df["Quantity"], bins=10)

plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")

plt.show()
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Product Revenue
product_sales.plot(kind="bar", ax=axes[0,0])
axes[0,0].set_title("Product Revenue")

# Monthly Sales
axes[0,1].plot(monthly_sales.index,
               monthly_sales.values,
               marker='o')
axes[0,1].set_title("Monthly Sales")

# Category Revenue
axes[1,0].pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%"
)
axes[1,0].set_title("Category Revenue")

# Quantity Distribution
axes[1,1].hist(df["Quantity"], bins=10)
axes[1,1].set_title("Quantity Distribution")

plt.tight_layout()
plt.show()