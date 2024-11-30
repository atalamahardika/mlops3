import os
import pandas as pd
from sklearn.datasets import load_iris

def main():
    # Load the Iris dataset
    iris = load_iris()
    dataset = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    dataset['target'] = iris.target

    # Create the data directory if it doesn't exist
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Save the dataset to a CSV file in the data directory
    dataset.to_csv(os.path.join(data_dir, 'data.csv'), index=False)
    # # Save the dataset to a CSV file
    # dataset.to_csv('data.csv', index=False)

if __name__ == '__main__':
    main()