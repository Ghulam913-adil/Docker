import pandas as pd
from sklearn.ensemble import IsolationForest

def predict_new_data(new_data_path):
    # Load data
    new_data = pd.read_csv(new_data_path)

    # Train an Isolation Forest for prediction
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(new_data)

    # Predict
    predictions = model.predict(new_data)
    predictions
    predictions = ["Anomaly" if x == -1 else "Normal" for x in predictions]

    # Output
    new_data['Prediction'] = predictions
    new_data.to_csv('./data/processed/predictions.csv', index=False)
    print("Predictions saved to './data/processed/predictions.csv'")

if __name__ == "__main__":
    predict_new_data('./data/processed/test.csv')
