import pandas as pd
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump

print(sklearn.__version__)

# Load data
data = pd.read_csv("sample_data.csv")
X = data[['feature1', 'feature2']]
y = data['target']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the trained model
dump(model, 'model.pkl')
print("Model trained and saved as 'model.pkl'")
