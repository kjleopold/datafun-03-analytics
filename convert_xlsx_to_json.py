import pandas as pd

# Load Excel File
df = pd.read_excel("Super_Bowl_Data.xlsx")

# Conver to JSON and save
df.to_json("Super_Bowl_Data.xlsx", orient="records", indent=4)
print("Excel File successfully converted to JSON!")

