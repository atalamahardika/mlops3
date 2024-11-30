import os
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def main():
    # Load the trained model
    models_dir = './models'
    model_path = os.path.join(models_dir, 'trained_model.pkl')
    if not os.path.exists(model_path):
        print("Error: Trained model not found. Please run 'make train' first.")
        return
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Load the testing dataset
    dataset = pd.read_csv('./data/data.csv')
    X_test = dataset.drop('target', axis=1)
    y_test = dataset['target']

    # Make predictions on the testing dataset
    y_pred = model.predict(X_test)
    # Evaluate the model
    # Add more evaluation metrics and code here
    # Calculate the evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Print the results
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-score:", f1)
    print('Model evaluation complete.')

if __name__ == '__main__':
    main()