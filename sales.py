import pandas as pd

# Data load
products = pd.DataFrame({'Name': ['Shirts', 'Shorts', 'Trousers'], 'Price': [50, 35, 60]})

# Calculate income
products['Amount'] = [1000, 1500, 4200]
products['Income'] = products['Price'] * products['Amount']

# Export data
products.to_csv("sales.csv", sep=";", index=False)