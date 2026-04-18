import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")

df

df["revenue"]=df["Quantity"]*df["UnitPrice"]
customer_revenue=df.groupby("CustomerID")["revenue"].mean()
print(customer_revenue)





