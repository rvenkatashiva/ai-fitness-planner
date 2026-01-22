# train_calorie_model.py
# ML model to predict daily calorie needs for students

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset (can be expanded)
data = {
    'age': [18, 20, 22, 25, 30, 28, 24, 21],
    'height': [160, 165, 170, 175, 180, 172, 168, 166],
    'weight': [55, 60, 65, 70, 80, 75, 62, 58],
    'activity': [1.2, 1.55, 1.55, 1.75, 1.75, 1.55, 1.2, 1.2],
    'calories': [1800, 2100, 2200, 2600, 3000, 2700, 2000, 1900]
}

# Create DataFrame
df = pd.DataFrame(data)

X = df[['age', 'height', 'weight', 'activity']]
y = df['calories']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open('calorie_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print('Calorie prediction model trained and saved!')
