import pandas as pd
import numpy as np

# Read dataset
df = pd.read_csv('../data/sample_data.csv')

# Get unique colors
unique_colors = df['Color'].dropna().unique()

# Create one-hot encoded columns manually
for color in unique_colors:
    df[color] = np.where(df['Color'] == color, 1, 0)

print("Original Data:")
print(df[['Color']])
print("\nAfter One-Hot Encoding:")
print(df[['Color'] + list(unique_colors)])
