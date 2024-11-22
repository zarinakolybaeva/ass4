import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('supermarket_sales.csv')


print(df.info())
print(df.describe())


df['Total'] = (df['Unit price'] * df['Quantity']) + df['Tax 5%']
print(df[['Invoice ID', 'Total']].head())


city_sales = df.groupby('City')['Total'].sum()
print(city_sales)


popular_product = df['Product line'].value_counts()
print(popular_product)

avg_price = data.groupby('Product line')['Unit price'].mean()
print(avg_price)


gender_revenue = df.groupby('Gender')['Total'].sum()
print(gender_revenue)

gender_sales = data.groupby('Gender')['Invoice ID'].count()
print(gender_sales)


city_sales.plot(kind='bar')
plt.title('Sales per City')
plt.xlabel('City')
plt.ylabel('Number of Sales')
plt.show()



sns.histplot(data['Unit price'], kde=True)
plt.title('Distribution of Unit Prices')
plt.show()


gender_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales Distribution by Gender')
plt.ylabel('')
plt.show()

correlation_matrix = data[['Unit price', 'Quantity', 'Tax 5%']].corr()
print(correlation_matrix)

top_products = data['Product line'].value_counts().head(5)
print(top_products)


popular_product = df['Product line'].str.lower().value_counts()
print(popular_product)

product_counts = df[['Product line', 'Category']].apply(pd.Series.value_counts)
print(product_counts)
