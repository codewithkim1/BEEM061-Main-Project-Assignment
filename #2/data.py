import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate random data
num_samples = 1000

# Features
feature_1 = np.random.normal(loc=0, scale=1, size=num_samples)
feature_2 = np.random.normal(loc=5, scale=2, size=num_samples)

# Target variable (binary: 0 or 1)
target = np.random.choice([0, 1], size=num_samples)

# Create a DataFrame
data = pd.DataFrame({'Feature_1': feature_1, 'Feature_2': feature_2, 'Target': target})

# Save the DataFrame to a CSV file
data.to_csv('dataset.csv', index=False)

# Display the first few rows of the generated dataset
print(data.head())
