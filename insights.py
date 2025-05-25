import pandas as pd

df = pd.read_csv('candy-data.csv')

# Chocolate vs Non-Chocolate
choc_avg = df[df['chocolate'] == 1]['winpercent'].mean()
non_choc_avg = df[df['chocolate'] == 0]['winpercent'].mean()
print(f"Avg win % - Chocolate: {choc_avg:.2f}, Non-Chocolate: {non_choc_avg:.2f}")

# Do price or sugar correlate with popularity?
print("Correlation of price and sugar with popularity:")
print(df[['pricepercent', 'sugarpercent', 'winpercent']].corr())

# Best candy with caramel?
print("Best caramel candy:")
print(df[df['caramel'] == 1].sort_values(by='winpercent', ascending=False).head(1))