import pandas as pd

# Load data
data = pd.read_csv('candy-data.csv')

# Basic checks
print("Shape:", data.shape)
print("Columns:", data.columns)
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Optional: Rename columns for readability (optional)
data.columns = [col.lower().strip() for col in data.columns]

# Save cleaned data
data.to_csv('candy-data.csv', index=False)