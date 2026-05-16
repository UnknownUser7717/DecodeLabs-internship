import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_excel("Data/cleaned_dataset.xlsx")

sns.set_theme(style="darkgrid")

# ── Plot 1 — TotalPrice Distribution ──────────────────────────────────────────
plt.figure(figsize=(10, 5))
sns.histplot(df['TotalPrice'], bins=30, kde=True, color='steelblue')
plt.title('Distribution of Total Price')
plt.xlabel('Total Price ($)')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.show()

# ── Plot 2 — TotalPrice Boxplot (Outliers) ────────────────────────────────────
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['TotalPrice'], color='steelblue')
plt.title('TotalPrice Boxplot')
plt.xlabel('Total Price ($)')
plt.tight_layout()
plt.show()

# ── Plot 3 — Orders by Product ────────────────────────────────────────────────
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Product', order=df['Product'].value_counts().index, color='steelblue')
plt.title('Orders by Product')
plt.xlabel('Product')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.show()

# ── Plot 4 — Orders by OrderStatus ───────────────────────────────────────────
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='OrderStatus', order=df['OrderStatus'].value_counts().index, color='steelblue')
plt.title('Orders by Status')
plt.xlabel('Order Status')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.show()

# ── Plot 5 — Orders by ReferralSource ────────────────────────────────────────
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='ReferralSource', order=df['ReferralSource'].value_counts().index, color='steelblue')
plt.title('Orders by Referral Source')
plt.xlabel('Referral Source')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.show()

# ── Plot 6 — UnitPrice by Product (Boxplot) ───────────────────────────────────
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='Product', y='UnitPrice', color='steelblue')
plt.title('UnitPrice Distribution by Product')
plt.xlabel('Product')
plt.ylabel('Unit Price ($)')
plt.tight_layout()
plt.show()

# ── Plot 7 — Total Sales Over Time ────────────────────────────────────────────
monthly_sales = df.groupby(['Year', 'Month'])['TotalPrice'].sum().reset_index()
monthly_sales['Date'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(day=1))

plt.figure(figsize=(12, 5))
plt.plot(monthly_sales['Date'], monthly_sales['TotalPrice'], color='steelblue', marker='o')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.show()

# ── Plot 8 — Orders by Month ──────────────────────────────────────────────────
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Month', color='steelblue')
plt.title('Number of Orders by Month')
plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.show()
