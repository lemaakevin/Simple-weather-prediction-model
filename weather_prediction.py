import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Load sample weather data (or use your own dataset)
# Example data structure:
data = {
    'temperature': [22, 25, 18, 15, 20, 23, 19, 17, 21, 24],
    'humidity': [65, 70, 80, 75, 68, 72, 78, 82, 67, 71],
    'pressure': [1012, 1010, 1015, 1018, 1011, 1009, 1014, 1017, 1013, 1010],
    'wind_speed': [10, 8, 12, 15, 9, 7, 11, 14, 8, 6],
    'rainfall': [0, 0, 5, 8, 0, 0, 3, 6, 0, 0]
}

df = pd.DataFrame(data)

# Create target variable (predict next day's temperature)
df['next_day_temp'] = df['temperature'].shift(-1)
df = df.dropna()

# Prepare features and target
X = df[['temperature', 'humidity', 'pressure', 'wind_speed', 'rainfall']]
y = df['next_day_temp']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae:.2f}°C")

# Feature importance
importances = model.feature_importances_
features = X.columns
plt.barh(features, importances)
plt.title('Feature Importance')
plt.show()