import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a DataFrame
df = pd.read_csv('government_budget_large.csv')

# Display the first few rows of the dataset
print("Budget Data:")
print(df.head())

# Basic statistics of the dataset
print("\nSummary statistics:")
print(df.describe())

# Separate revenue and expenses
revenue = df[df['Type'] == 'Revenue']
expenses = df[df['Type'] == 'Expense']

# Group by year and sum the amount for each type
annual_revenue = revenue.groupby('Year')['Amount'].sum()
annual_expenses = expenses.groupby('Year')['Amount'].sum()

# Calculate annual surplus or deficit
annual_balance = annual_revenue - annual_expenses

print("\nAnnual Revenue:")
print(annual_revenue)

print("\nAnnual Expenses:")
print(annual_expenses)

print("\nAnnual Surplus/Deficit:")
print(annual_balance)

# Plot 1: Line plot for Revenue, Expenses, and Surplus/Deficit over time
plt.figure(figsize=(10, 6))
plt.plot(annual_revenue, label='Revenue', marker='o')
plt.plot(annual_expenses, label='Expenses', marker='o')
plt.plot(annual_balance, label='Surplus/Deficit', marker='o')
plt.title('Government Budget Analysis')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: Bar plot of Total Revenue and Expenses by Year
plt.figure(figsize=(10, 6))
width = 0.4  # Width of bars
years = annual_revenue.index

plt.bar(years - width/2, annual_revenue, width, label='Revenue')
plt.bar(years + width/2, annual_expenses, width, label='Expenses')
plt.title('Total Revenue and Expenses by Year')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
plt.show()

# Plot 3: Pie Chart for Expense Categories
expense_by_category = expenses.groupby('Category')['Amount'].sum()

plt.figure(figsize=(8, 8))
plt.pie(expense_by_category, labels=expense_by_category.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribution of Expenses by Category')
plt.show()

# Plot 4: Line plot for Revenue and Expenses by Category over time
plt.figure(figsize=(12, 8))

# Plot revenue categories over time
for category in revenue['Category'].unique():
    category_data = revenue[revenue['Category'] == category].groupby('Year')['Amount'].sum()
    plt.plot(category_data, label=f'{category} (Revenue)', linestyle='--', marker='o')

# Plot expense categories over time
for category in expenses['Category'].unique():
    category_data = expenses[expenses['Category'] == category].groupby('Year')['Amount'].sum()
    plt.plot(category_data, label=f'{category} (Expense)', marker='o')

plt.title('Revenue and Expenses by Category Over Time')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.legend()
plt.grid(True)
plt.show()
