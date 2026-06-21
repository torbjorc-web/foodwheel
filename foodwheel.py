import codecademylib3
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Cuisine Offerings
# -----------------------------

# Load restaurants data
restaurants = pd.read_csv('restaurants.csv')

# Inspect the dataframe
print(restaurants.head())

# Number of unique cuisines
print(restaurants.cuisine.nunique())

# Count restaurants by cuisine
cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()
print(cuisine_counts)

# Pie chart of cuisine offerings
plt.figure(figsize=(8, 8))
plt.pie(cuisine_counts['name'], labels=cuisine_counts['cuisine'], autopct='%0.1f%%')
plt.title('FoodWheel Cuisine Offerings')
plt.axis('equal')
plt.show()
plt.clf()


# -----------------------------
# 2. Order Price Over Time
# -----------------------------

# Load orders data
orders = pd.read_csv('orders.csv')

# Inspect the dataframe
print(orders.head())

# Create month column from date
orders['month'] = orders.date.str.split('-').str[1]
print(orders.head())

# Average order amount by month
avg_order = orders.groupby('month').price.mean().reset_index()
print(avg_order)

# Standard deviation by month
std_order = orders.groupby('month').price.std().reset_index()
print(std_order)

# Bar plot with error bars
month_names = ['April', 'May', 'June', 'July', 'August', 'September']
x_pos = range(len(avg_order))

plt.figure(figsize=(10, 6))
plt.bar(x_pos, avg_order['price'], yerr=std_order['price'], capsize=5)
plt.xticks(x_pos, month_names)
plt.ylabel('Average Order Amount')
plt.title('Average FoodWheel Order Size by Month')
plt.show()
plt.clf()


# -----------------------------
# 3. Customer Orders
# -----------------------------

# Total spent by each customer
customer_amount = orders.groupby('customer_id').price.sum().reset_index()
print(customer_amount)

# Histogram of customer spending
plt.figure(figsize=(10, 6))
plt.hist(customer_amount['price'], range=(0, 200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Customer Spending Over the Past Six Months')
plt.show()
plt.clf()


# -----------------------------
# 4. Extra Challenge
# -----------------------------

# Count restaurants by neighborhood
neighborhood_counts = restaurants.groupby('neighborhood').name.count().reset_index()
print(neighborhood_counts)

# Fixed neighborhood bar chart
x_pos = range(len(neighborhood_counts))

plt.figure(figsize=(12, 6))
plt.bar(x_pos, neighborhood_counts['name'])
plt.xticks(x_pos, neighborhood_counts['neighborhood'], rotation=45)
plt.ylabel('Number of Restaurants')
plt.title('Restaurant Count by Neighborhood')
plt.tight_layout()
plt.show()
