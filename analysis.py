import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
df.head()

df.info()
df = df.dropna()

plt.figure(figsize=(12, 6))
counts = df["Model Year"].value_counts().sort_index()

sns.barplot(x=counts.index, y=counts.values)
plt.title("EV Adoption Over Time")
plt.xticks(rotation=45)
plt.show()


ev_types = df["Electric Vehicle Type"].value_counts()

sns.barplot(x=ev_types.values, y=ev_types.index)
plt.title("EV Type Distribution")
plt.show()

top_makes = df["Make"].value_counts().head(10)

sns.barplot(x=top_makes.values, y=top_makes.index)
plt.title("Top EV Manufacturers")
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(df["Electric Range"], kde=True)
plt.title("Electric Range Distribution")
plt.xlabel("Range (miles)")
plt.show()

from scipy.optimize import curve_fit

def exp_growth(x, a, b):
    return a * np.exp(b * x)

# actual data
year_counts = df["Model Year"].value_counts().sort_index()
year_counts = year_counts[year_counts.index <= 2023]

x = year_counts.index - year_counts.index[0]
y = year_counts.values

params, _ = curve_fit(exp_growth, x, y)
a, b = params

# forecast future (2024–2029)
future_years = np.arange(2024, 2030)
future_x = future_years - year_counts.index[0]
future_y = exp_growth(future_x, a, b)

# plot results
plt.figure(figsize=(12, 6))
plt.plot(year_counts.index, year_counts.values, label="Actual")
plt.plot(future_years, future_y, '--', label="Forecast")
plt.title("EV Market Forecast (2024–2029)")
plt.xlabel("Year")
plt.ylabel("EV Registrations")
plt.legend()
plt.show()