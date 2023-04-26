import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas dataframe
df = pd.read_csv('house.csv')

# Print some basic statistics about the dataset
print(df.describe())

# Create a scatter plot of square footage vs. price
plt.scatter(df['Square Footage'], df['Price'])
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.title('Housing Prices')
plt.show()

# Calculate the correlation between square footage and price
correlation = df['Square Footage'].corr(df['Price'])
print('Correlation between square footage and price:', correlation)

# Create a histogram of the price distribution
plt.hist(df['Price'], bins=20)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Housing Prices')
plt.show()
