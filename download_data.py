import requests
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# URL of the dataset
url = 'https://raw.githubusercontent.com/gscdit/Breast-Cancer-Detection/refs/heads/master/data.csv'

# Download the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the file
    with open('data/breast_cancer_data.csv', 'wb') as f:
        f.write(response.content)
    print('Dataset downloaded successfully!')
else:
    print(f'Failed to download dataset. Status code: {response.status_code}')