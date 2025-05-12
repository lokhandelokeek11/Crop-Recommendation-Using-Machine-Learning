import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Load dataset
crop = pd.read_csv("Crop_recommendation.csv")

# Mapping labels to numbers
crop_dict = {name: i+1 for i, name in enumerate(crop['label'].unique())}
crop['label'] = crop['label'].map(crop_dict)

# Save crop labels
import json
with open("model/crop_labels.json", "w") as f:
    json.dump({str(v): k for k, v in crop_dict.items()}, f)

# Split dataset
X = crop.drop('label', axis=1)
y = crop['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize data
minmax_scaler = MinMaxScaler()
X_train = minmax_scaler.fit_transform(X_train)
X_test = minmax_scaler.transform(X_test)

standard_scaler = StandardScaler()
X_train = standard_scaler.fit_transform(X_train)
X_test = standard_scaler.transform(X_test)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and scalers
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(minmax_scaler, open("minmaxscaler.pkl", "wb"))
pickle.dump(standard_scaler, open("standardscaler.pkl", "wb"))
