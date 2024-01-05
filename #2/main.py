import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('dataset.csv')

# Explore the dataset
print(df.head())

# Preprocess the data (fill missing values for Feature_1)
df['Feature_1'] = df['Feature_1'].fillna(df['Feature_1'].mean())

# Select features and target variable
X = df[['Feature_1', 'Feature_2']]
y = df['Target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f'Model Accuracy: {accuracy}')
