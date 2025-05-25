import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('candy-data.csv')

# Top 10 most popular candies
top_candies = df.sort_values(by='winpercent', ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(data=top_candies, x='winpercent', y=top_candies.index)
plt.title('Top 10 Most Popular Candies')
plt.savefig('candies.webp')
plt.show()
# Sugar vs. Win%
sns.scatterplot(data=df, x='sugarpercent', y='winpercent', hue='chocolate')
plt.title('Sugar Content vs Popularity')
plt.savefig('sugar_vs_popularity.png')
plt.show()

# Heatmap
plt.figure(figsize=(10, 8))
correlation_matrix=df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('correlation_heatmap.png')
plt.show()