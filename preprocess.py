from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def preprocess_data():
    # Load dataset
    iris = load_iris(as_frame=True)
    data = iris.data
    target = iris.target

    # Treat one class as anomalous
    data['label'] = (target == 2).astype(int)  # Class '2' as anomalous (1 = anomaly)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        data.iloc[:, :-1], data['label'], test_size=0.2, random_state=42
    )

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Save to CSV
    train_df = pd.DataFrame(X_train_scaled, columns=data.columns[:-1])
    train_df['label'] = y_train.values
    test_df = pd.DataFrame(X_test_scaled, columns=data.columns[:-1])
    test_df['label'] = y_test.values

    train_df.to_csv('./data/processed/train.csv', index=False)
    test_df.to_csv('./data/processed/test.csv', index=False)
    print("Preprocessing complete. Data saved to './data/processed/'")

if __name__ == "__main__":
    preprocess_data()
