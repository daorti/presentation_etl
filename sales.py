import pandas as pd

# Data load
products = pd.DataFrame({'Name': ['Shirts', 'Shorts', 'Trousers'], 'Price': [50, 35, 60]})

# Calculate income
products['Amount'] = [100, 150, 420]
products['Income'] = products['Price'] * products['Amount']

# Export data
products.to_csv("sales.csv", sep=";", index=False)