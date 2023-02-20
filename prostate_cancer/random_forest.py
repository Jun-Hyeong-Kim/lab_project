import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset into a Pandas DataFrame
df = pd.read_excel("C:/Users/tommy/OneDrive/바탕 화면/lab_project/prostate_cancer/prostate_data2.xlsx")

# Split the dataset into features (X) and target (y)
X = df.drop("Sample", axis=1) # assuming "outcome" is the name of the column containing the target variable
y = df["Sample"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest classifier on the training data
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

'''
# Use the model to make predictions on novel input data
novel_input = ... # Replace this with your novel input data
novel_prediction = model.predict([novel_input])
print("Novel prediction:", novel_prediction)'''
