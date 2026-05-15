import pandas as pd

df = pd.read_excel("Dataset_for_Data_Analytics.xlsx")

# Step 1: Handle missing values
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')

# Step 2: Convert to category dtype
cat_cols = ['OrderStatus', 'Product', 'PaymentMethod', 'ReferralSource', 'CouponCode']
for col in cat_cols:
    df[col] = df[col].astype('category')

# Step 3: Fix float precision
df['UnitPrice'] = df['UnitPrice'].round(2)
df['TotalPrice'] = df['TotalPrice'].round(2)

# Step 4: Strip whitespace from string columns
str_cols = ['OrderID', 'CustomerID', 'Product', 'ShippingAddress',
            'PaymentMethod', 'OrderStatus', 'TrackingNumber',
            'ReferralSource', 'CouponCode']
for col in str_cols:
    df[col] = df[col].str.strip()

# Step 5: extract Year and Month from Date
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Move Year and Month next to Date column
df.insert(2, 'Year', df.pop('Year'))
df.insert(3, 'Month', df.pop('Month'))

# Step 6: Clean ShippingAddress (remove "Main St")
df['ShippingAddress'] = df['ShippingAddress'].str.replace(' Main St', '', regex=False)

print("Done! Shape:", df.shape)
print(df.head())