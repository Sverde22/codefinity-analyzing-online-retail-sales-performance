import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load subset for performance
df = pd.read_csv("online_retail.csv")

# Your code starts here
total_item=df.groupby("Description")["Quantity"].sum().reset_index()
total_item=total_item.sort_values(by="Quantity", ascending=False)
topten=total_item[:10 ]
print(topten)

fig, ax=plt.subplots()
sns.barplot(
    data=topten,
    y="Description",
    x="Quantity",
    ax=ax
)
ax.set_title("Top ten items")
ax.set_xlabel("Quantity")
ax.set_ylabel("Items")

plt.tight_layout()
plt.show()




