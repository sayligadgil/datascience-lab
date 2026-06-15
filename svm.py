import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# 1. Load the dataset
df = sns.load_dataset("iris")

# 2. Separate features (X) and target label (y)
X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df["species"]

# 3. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Create and train the SVM model
model = SVC(kernel="linear")
model.fit(X_train, y_train)

# 5. Make predictions on the test data
predictions = model.predict(X_test)

# 6. Map text predictions to numbers (0, 1, 2) for pure Matplotlib coloring
# This replaces the need for 'hue' entirely!
mapping = {"setosa": 0, "versicolor": 1, "virginica": 2}
colors = [mapping[pred] for pred in predictions]

# 7. DATA PRESENTATION: Pure Matplotlib Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(
    X_test["sepal_length"], X_test["sepal_width"], c=colors, cmap="brg"
)

plt.title("SVM Predictions (Test Data)")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()
