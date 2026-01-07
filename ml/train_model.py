import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
data = pd.read_csv('../data/house_data.csv')

X = data[['area', 'bedrooms', 'bathrooms']]
y = data['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'house_price_model.pkl')

print("Model trained and saved successfully")
