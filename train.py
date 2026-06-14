# Step 1 - Import libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Step 2 - Load the data
df = pd.read_csv('data.csv')
print("Data loaded successfully!")
print(df)

# Step 3 - Separate inputs and output
X = df[['age', 'monthly_salary', 'job_satisfaction', 
        'years_at_company', 'work_life_balance', 
        'promotions_last_3years']]
y = df['left']

# Step 4 - Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print(f"\nTraining on {len(X_train)} employees")
print(f"Testing on {len(X_test)} employees")

# Step 5 - Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("\nModel trained successfully!")

# Step 6 - Test the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy * 100:.1f}%")

# Step 7 - Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("\nModel saved as model.pkl")