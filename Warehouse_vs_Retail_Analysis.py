import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\Ann S Vettoor\OneDrive\Desktop\Mtech\Data Mining\Assignment_1\Warehouse_and_Retail_Sales.csv")
print(df.head())
print(df.info())
# ==========================================
# 3. Data Preparation
# ==========================================

# Create Date column from YEAR and MONTH
df['Date'] = pd.to_datetime(df['YEAR'].astype(str) + '-' + df['MONTH'].astype(str) + '-01')

# Extract time components
df['Year'] = df['Date'].dt.year
df['Quarter'] = df['Date'].dt.to_period('Q')
df['Month'] = df['Date'].dt.to_period('M')

df['Date']

# ==========================================
# TASK 1: Total Retail Sales Over Time
# ==========================================

# Monthly Retail Sales
monthly_retail = df.groupby('Month')['RETAIL SALES'].sum()

plt.figure()
monthly_retail.plot()
plt.title("Monthly Retail Sales Trend")
plt.xlabel("Month")
plt.ylabel("Retail Sales")
plt.show()

# Quarterly Retail Sales
quarterly_retail = df.groupby('Quarter')['RETAIL SALES'].sum()

plt.figure()
quarterly_retail.plot()
plt.title("Quarterly Retail Sales Trend")
plt.xlabel("Quarter")
plt.ylabel("Retail Sales")
plt.show()


# Yearly Retail Sales
yearly_retail = df.groupby('Year')['RETAIL SALES'].sum()

plt.figure()
yearly_retail.plot(kind='bar')
plt.title("Yearly Retail Sales")
plt.xlabel("Year")
plt.ylabel("Retail Sales")
plt.show()
monthly_pattern = df.groupby('MONTH')['RETAIL SALES'].sum()

plt.figure()
monthly_pattern.plot(kind='bar')
plt.title("Retail Sales by Month")
plt.xlabel("Month")
plt.ylabel("Total Retail Sales")
plt.show()
monthly_pattern = df.groupby('Quarter')['RETAIL SALES'].sum()

plt.figure()
monthly_pattern.plot(kind='bar')
plt.title("Retail Sales by Quarter")
plt.xlabel("Quarter")
plt.ylabel("Total Retail Sales")
plt.show()
monthly_pattern = df.groupby('YEAR')['RETAIL SALES'].sum()

plt.figure()
monthly_pattern.plot(kind='bar')
plt.title("Retail Sales by Year")
plt.xlabel("Year")
plt.ylabel("Total Retail Sales")
plt.show()

# ==========================================
# TASK 2: Warehouse Sales Over Time
# ==========================================

monthly_warehouse = df.groupby('Month')['WAREHOUSE SALES'].sum()

plt.figure()
monthly_warehouse.plot()
plt.title("Monthly Warehouse Sales")
plt.xlabel("Month")
plt.ylabel("Warehouse Sales")
plt.show()

comparison = df.groupby('Month')[['RETAIL SALES','WAREHOUSE SALES']].sum()

plt.figure()
comparison.plot()
plt.title("Warehouse vs Retail Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# ==========================================
# TASK 3: Item-Level Sales Trends
# ==========================================

item_type_sales = df.groupby('ITEM TYPE')['RETAIL SALES'].sum().sort_values(ascending=False)

plt.figure()
item_type_sales.plot(kind='bar')
plt.title("Retail Sales by Item Type")
plt.xlabel("Item Type")
plt.ylabel("Total Retail Sales")
plt.show()
item_type_sales = df.groupby('ITEM TYPE')['WAREHOUSE SALES'].sum().sort_values(ascending=False)

plt.figure()
item_type_sales.plot(kind='bar')
plt.title("Warehouse Sales by Item Type")
plt.xlabel("Item Type")
plt.ylabel("Total Retail Sales")
plt.show()


# ==========================================
# TASK 4: Sales Breakdown by Category
# ==========================================

category_sales = df.groupby('ITEM TYPE')['RETAIL SALES'].sum()

plt.figure()
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Contribution by Category")
plt.ylabel("")
plt.show()



# ==========================================
# TASK 5: Sales Breakdown by Supplier (Department Proxy)
# ==========================================

supplier_sales = df.groupby('SUPPLIER')['RETAIL SALES'].sum().sort_values(ascending=False).head(10)

plt.figure()
supplier_sales.plot(kind='bar')
plt.title("Top Department by Retail Sales")
plt.xlabel("Supplier")
plt.ylabel("Retail Sales")
plt.xticks(rotation=45)
plt.show()


# ==========================================
# TASK 6: Top N Selling Items
# ==========================================

# Top 10 Items by Retail Sales Value
top_items_sales = df.groupby('ITEM DESCRIPTION')['RETAIL SALES'].sum().sort_values(ascending=False).head(10)

plt.figure()
top_items_sales.plot(kind='bar')
plt.title("Top 10 Items by Retail Sales")
plt.xlabel("Item")
plt.ylabel("Retail Sales")
plt.xticks(rotation=60)
plt.show()


# Top 10 Items by Warehouse Movement
top_items_units = df.groupby('ITEM DESCRIPTION')['WAREHOUSE SALES'].sum().sort_values(ascending=False).head(10)

plt.figure()
top_items_units.plot(kind='bar')
plt.title("Top 10 Items by Warehouse Sales")
plt.xlabel("Item")
plt.ylabel("Warehouse Sales")
plt.xticks(rotation=60)
plt.show()


# ==========================================
# TASK 7: Sales Distribution Analysis
# ==========================================

plt.figure()

plt.hist(df['RETAIL SALES'], bins=30)

plt.title("Distribution of Retail Sales Across Products")
plt.xlabel("Retail Sales")
plt.ylabel("Frequency")

plt.show()
plt.figure()

plt.hist(df['WAREHOUSE SALES'], bins=30)

plt.title("Distribution of Warehouse Sales Across Products")
plt.xlabel("Retail Sales")
plt.ylabel("Frequency")

plt.show()

# ==========================================
# TASK 8: Warehouse vs Retail Comparison
# ==========================================

monthly_sales = df.groupby('Month')[['RETAIL SALES','WAREHOUSE SALES']].sum()

# Create side-by-side plots
plt.figure(figsize=(12,5))

# Warehouse Sales Chart
plt.subplot(1,2,1)
plt.plot(monthly_sales.index.astype(str), monthly_sales['WAREHOUSE SALES'])
plt.title("Warehouse Shipments Over Time")
plt.xlabel("Month")
plt.ylabel("Warehouse Sales")
plt.xticks(rotation=45)

# Retail Sales Chart
plt.subplot(1,2,2)
plt.plot(monthly_sales.index.astype(str), monthly_sales['RETAIL SALES'])
plt.title("Retail Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Retail Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

# Warehouse heatmap data
warehouse_heatmap = df.pivot_table(
    values='WAREHOUSE SALES',
    index='YEAR',
    columns='MONTH',
    aggfunc='sum'
)

plt.figure(figsize=(10,5))

sns.heatmap(
    warehouse_heatmap,
    annot=True,
    fmt=".0f",
    cmap="YlOrRd"
)

plt.title("Warehouse Outflows Heatmap (Year vs Month)")
plt.xlabel("Month")
plt.ylabel("Year")

plt.show()
# Retail heatmap data
retail_heatmap = df.pivot_table(
    values='RETAIL SALES',
    index='YEAR',
    columns='MONTH',
    aggfunc='sum'
)

plt.figure(figsize=(10,5))

sns.heatmap(
    retail_heatmap,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu"
)

plt.title("Retail Inflows Heatmap (Year vs Month)")
plt.xlabel("Month")
plt.ylabel("Year")

plt.show()

# ==========================================
# TASK 10: Annual Growth Rate Analysis
# ==========================================
df['Year'] = df['Year'].astype(int)

annual_category = df.groupby(['YEAR','ITEM TYPE'])['RETAIL SALES'].sum().unstack()

growth_rate = annual_category.pct_change() * 100


plt.figure(figsize=(8,5))

growth_rate.plot(marker='o')
plt.title("Year-over-Year Growth Rate by Category")
plt.xlabel("Year")
plt.ylabel("Growth Rate (%)")

plt.grid(True)

plt.show()
