import os
import pickle
import joblib

def main():
    # Load the trained model
    models_dir = './models'
    model_path = os.path.join(models_dir, 'trained_model.pkl')
    if not os.path.exists(model_path):
        print("Error: Trained model not found. Please run 'make train' first.")
        return
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Save the model to a serialized format
    deployed_model_path = os.path.join(models_dir, 'deployed_model.joblib')
    joblib.dump(model, deployed_model_path)

    print('Model deployed.')

if __name__ == '__main__':
    main()