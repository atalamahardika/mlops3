import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    # Load the dataset
    dataset = pd.read_csv('./data/data.csv')

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(dataset.drop('target', axis=1), dataset['target'], test_size=0.2, random_state=42)

    # Train the Decision Tree model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')

    # Save the trained model
    import pickle
    models_dir = './models'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    with open(os.path.join(models_dir, 'trained_model.pkl'), 'wb') as f:
        pickle.dump(model, f)

if __name__ == '__main__':
    main()