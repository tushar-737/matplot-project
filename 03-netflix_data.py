import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("03-netflix.csv")

# ------------------------
# 1. Movies vs TV Shows
# ------------------------

content_count = df["Type"].value_counts()

plt.figure(figsize=(6,5))
content_count.plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# ------------------------
# 2. Content by Country
# ------------------------

country_count = df["Country"].value_counts()

plt.figure(figsize=(8,5))
country_count.plot(kind="bar")
plt.title("Content by Country")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()

# ------------------------
# 3. Release Year Trend
# ------------------------

year_count = df["Release_Year"].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(year_count.index, year_count.values, marker='o')
plt.title("Netflix Content by Release Year")
plt.xlabel("Year")
plt.ylabel("Titles Released")
plt.grid(True)
plt.show()

# ------------------------
# 4. Ratings Distribution
# ------------------------

rating_count = df["Rating"].value_counts()

plt.figure(figsize=(8,5))
rating_count.plot(kind="pie", autopct='%1.1f%%')
plt.title("Ratings Distribution")
plt.ylabel("")
plt.show()

# ------------------------
# 5. Top Countries
# ------------------------

top_countries = df["Country"].value_counts().head(5)

plt.figure(figsize=(8,5))
top_countries.plot(kind="barh")
plt.title("Top Countries on Netflix")
plt.xlabel("Titles")
plt.show()

# ------------------------
# Dashboard
# ------------------------

fig, axes = plt.subplots(2,2, figsize=(14,10))

content_count.plot(kind="bar", ax=axes[0,0])
axes[0,0].set_title("Movies vs TV Shows")

country_count.plot(kind="bar", ax=axes[0,1])
axes[0,1].set_title("Content by Country")

axes[1,0].plot(year_count.index, year_count.values)
axes[1,0].set_title("Release Year Trend")

rating_count.plot(kind="pie", ax=axes[1,1], autopct='%1.1f%%')
axes[1,1].set_title("Ratings Distribution")

plt.tight_layout()
plt.show()

# ------------------------
# Insights
# ------------------------

print("Movies vs TV Shows:")
print(content_count)

print("\nTop Countries:")
print(country_count.head())

print("\nRatings:")
print(rating_count)