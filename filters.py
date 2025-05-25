import pandas as pd

df = pd.read_csv('candy-data.csv')

def filter_candies(chocolate=None, fruity=None, price_max=None):
    filtered = df.copy()
    if chocolate is not None:
        filtered = filtered[filtered['chocolate'] == chocolate]
    if fruity is not None:
        filtered = filtered[filtered['fruity'] == fruity]
    if price_max is not None:
        filtered = filtered[filtered['pricepercent'] <= price_max]
    return filtered.sort_values(by='winpercent', ascending=False)

# Example usage
filtered = filter_candies(chocolate=1, fruity=0, price_max=0.5)
print(filtered[['winpercent', 'pricepercent', 'chocolate', 'fruity']].head())