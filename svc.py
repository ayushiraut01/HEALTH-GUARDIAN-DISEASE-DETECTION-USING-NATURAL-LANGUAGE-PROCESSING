import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load your dataset
training_df = pd.read_csv('Datasets\\Training.csv')  # Replace with the correct path

# Prepare the data
X = training_df.drop(columns=['prognosis'])
y = training_df['prognosis']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the SVM model
svc_model = SVC(kernel='linear')
svc_model.fit(X_train, y_train)

# Make predictions
y_pred = svc_model.predict(X_test)

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print accuracy to console

print("Model Accuracy:", accuracy)
