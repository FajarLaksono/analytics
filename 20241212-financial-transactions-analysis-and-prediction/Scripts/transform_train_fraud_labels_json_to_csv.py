import pandas as pd
import os

input_path = input("Enter data source location: ")
train_fraud_labels_location = os.path.join(input_path, "train_fraud_labels.json")
print("data source path is :", train_fraud_labels_location)

# Load JSON and convert to DataFrame
df = pd.read_json(train_fraud_labels_location)
df = pd.DataFrame(df['target'].items(), columns=['id', 'status'])

# Save DataFrame to CSV
output_path = os.path.join(input_path, 'train_fraud_labels.csv')
df.to_csv(output_path, index=False)
print("Output path is : ", output_path)
