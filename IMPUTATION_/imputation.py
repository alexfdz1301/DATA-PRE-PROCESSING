import pandas as pd

# Read dataset
df = pd.read_csv('DATA-PRE-PROCESSING\data\sample_data.csv')

print("Original Data:")
print(df)

# Mean imputation for numeric columns
df['Price'].fillna(df['Price'].mean(), inplace=True)
df['Quantity'].fillna(df['Quantity'].mean(), inplace=True)

# Mode imputation for categorical column
df['Color'].fillna(df['Color'].mode()[0], inplace=True)

print("\nAfter Imputation:")
print(df)
