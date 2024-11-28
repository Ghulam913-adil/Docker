import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

def train_model():
    # Load data
    train_data = pd.read_csv('./data/processed/train.csv')
    test_data = pd.read_csv('./data/processed/test.csv')

    # Separate features and labels
    X_train, y_train = train_data.iloc[:, :-1], train_data['label']
    X_test, y_test = test_data.iloc[:, :-1], test_data['label']

    # Train model
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(X_train)

    # Predict
    y_pred = model.predict(X_test)
    y_pred = [1 if x == -1 else 0 for x in y_pred]  # Map -1 to anomaly

    # Evaluate
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    train_model()
