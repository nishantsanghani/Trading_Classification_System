📝 Trading Classification Dashboard

🚀 Overview
•	The Trading Classification Dashboard is a machine learning project designed to classify the prevailing market sentiment (Fear, Greed, Neutral, etc.) by combining historical trade execution data with the Fear & Greed Index. The system builds a robust, end-to-end Scikit-learn Pipeline and deploys the resulting model as an interactive web application using Streamlit.


📊 Dataset
•	The classification model relies on a merged dataset:
o	Trade History = historical_data.csv (https://drive.google.com/file/d/1fJYLpWqt123MbIblOjmHyuFDZFx-FQae/view?usp=sharing)
o	Market Sentiment = fear_greed_index.csv (https://drive.google.com/file/d/1ILczutp8NWAywtslZaTWy0cMEFzb95Li/view?usp=sharing)

🔧 Data Preprocessing
•	All preprocessing steps are encapsulated and automated within the final ML Pipeline:
•	Data Integration: Trade data is merged with sentiment data on a normalized date column.
•	Missing Value Imputation: Missing values in the sentiment classification and value are filled using the mode of the target column (predominantly 'Fear').
•	Feature Transformation:
  o	Numeric Features (Execution Price, Closed PnL, value, Fee): Standardized using StandardScaler.
  o	Categorical Features (Account, Coin, Side, Direction, Crossed): Encoded using OneHotEncoder.

🤖 Modeling (with Scikit-learn Pipeline)
👉 LogisticRegression → 0.99
👉 RandomForestClassifier → 1.0
👉 Random Forest → 1.0

⚖️ Performance Evaluation
👉 Training Accuracy → 1.0 (100.0%)
👉 Test Accuracy → 1.0 (100.0%)

📌 Conclusion
•	The project successfully builds an integrated ML solution for classifying market sentiment. The Tree-Based Classifier, wrapped in a comprehensive Scikit-learn Pipeline, achieves 100% accuracy on the test set, demonstrating excellent performance. The application is deployed via Streamlit, making the model easily accessible for real-time predictions.

🛠️ Tools & Technologies
•	Python
•	Libraries:
•	Scikit-learn: Machine Learning pipeline, model training, and preprocessing.
•	Pandas / NumPy: Data handling and numerical operations.
•	Streamlit: Interactive web dashboard deployment (main.py).
•	joblib: Model serialization (model.pkl).

