import pandas as pd

df = pd.read_csv('candy-data.csv')

print("Data types:\n", df.dtypes)
print("\nStatistical Summary:\n", df.describe())

# Binary feature counts
binary_features = df.columns[0:9]  # chocolate to pluribus
for feature in binary_features:
    print(feature,"\ncounts\n", df[feature].value_counts())
correlation_matrix=df.corr(numeric_only=True)
# Correlation matrix
print("\nCorrelation matrix:\n", correlation_matrix)