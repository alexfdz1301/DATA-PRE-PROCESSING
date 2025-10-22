import pandas as pd

# Read dataset
df = pd.read_csv('DATA-PRE-PROCESSING\data\sample_data.csv')

# Ordinal mapping for Size
size_order = {'Small': 1, 'Medium': 2, 'Large': 3}
df['Size_Encoded'] = df['Size'].map(size_order)

print("Original Data:")
print(df[['Size']])
print("\nAfter Ordinal Encoding:")
print(df[['Size', 'Size_Encoded']])
