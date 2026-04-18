import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")

df

df["morethanten"]= df["Quantity"] > 10
country_morethanten= df.groupby("Country")["morethanten"]
proportion=country_morethanten.mean().sort_values(ascending=False)
print(proportion)





