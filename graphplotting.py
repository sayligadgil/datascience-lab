import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load dataset (Replace with 'titanic.csv' or examiner's file)
df = sns.load_dataset("iris")

# Pick numerical columns dynamically for plotting
num_cols = df.select_dtypes(include=["number"]).columns
cat_cols = df.select_dtypes(include=["object", "category"]).columns

# A. X–Y Graph (Line Plot)
# Sort the dataframe by the X-axis variable so the line doesn't zigzag
df_sorted = df.sort_values(by=num_cols[0])

plt.figure(figsize=(6, 4))
plt.plot(
    df_sorted[num_cols[0]], df_sorted[num_cols[1]], color="blue", marker="o"
)
plt.title(f"X-Y Graph: {num_cols[0]} vs {num_cols[1]}")
plt.xlabel(num_cols[0])
plt.ylabel(num_cols[1])
plt.show()

# B. Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(df[num_cols[0]], df[num_cols[1]], color="purple", alpha=0.7)
plt.title(f"Scatter Plot: {num_cols[0]} vs {num_cols[1]}")
plt.xlabel(num_cols[0])
plt.ylabel(num_cols[1])
plt.show()

# C. Bar Chart (Aggregated counts of a categorical variable)
plt.figure(figsize=(6, 4))
df[cat_cols[0]].value_counts().plot(kind="bar", color="orange")
plt.title(f"Bar Chart of {cat_cols[0]}")
plt.ylabel("Count")
plt.show()

# D. Pie Chart
plt.figure(figsize=(6, 4))
df[cat_cols[0]].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title(f"Pie Chart of {cat_cols[0]}")
plt.ylabel("")  # Hides the default sidebar label
plt.show()
