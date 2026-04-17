import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")

df
df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"],dayfirst=True)
df["Month"]=df["InvoiceDate"].dt.month
print(df[["InvoiceDate","Month"]])
df["Revenue"]=df["Quantity"]*df["UnitPrice"]
Month_revenue=df.groupby("Month")["Revenue"].sum().reset_index()
print(Month_revenue)

fig, ax=plt.subplots()
sns.barplot(
    data=Month_revenue,
    x="Month",
    y="Revenue",
    ax=ax
)
ax.set_title("Revenue by Month")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
plt.show()







