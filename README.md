# 🌾 Crop Recommendation Using Machine Learning

A smart machine learning-based system that helps farmers select the most suitable crop based on soil nutrients and weather conditions, aimed at enhancing agricultural productivity and sustainability.

## 📖 Overview

With the world facing challenges like climate change, limited natural resources, and growing population, agriculture needs innovative solutions. This project presents a data-driven crop recommendation system that helps farmers make informed decisions by analyzing soil and environmental parameters. The system uses various machine learning models to predict the best crop for given input conditions, thereby increasing yield, reducing risks, and supporting sustainable agriculture.

## 🎯 Objectives

-  Recommend optimal crops for a given land based on pH, rainfall, humidity, temperature, and soil nutrients (N, P, K).
-  Integrate multiple machine learning algorithms to enhance accuracy and reliability.
-  Assist farmers in reducing crop selection risks and maximizing profits.
-  Minimize agricultural losses by enabling data-informed crop planning.

## 🗃️ Dataset

- **Source**: [Kaggle - Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
- **Size**: 2200 records
- **Features**: `N`, `P`, `K`, `temperature`, `humidity`, `ph`, `rainfall`
- **Target**: Crop type (22 crop varieties)

## 🔍 Methodology

1. **Data Collection**: Acquired dataset from Kaggle including 22 crop varieties.
2. **Preprocessing**: Cleaned data by removing noise, filling missing values, and normalizing features.
3. **Feature Selection**: Selected relevant attributes for training to improve model performance.
4. **Model Training**: Applied multiple ML algorithms:
   - Decision Tree (90%)
   - Naïve Bayes (99%)
   - SVM (96%)
   - Logistic Regression (95%)
   - Random Forest (99%)
   - XGBoost (94%)
5. **Recommendation System**: Predicts the most suitable crop for given conditions.
6. **Evaluation**: Models evaluated using metrics like accuracy, precision, recall, and F1-score.

## 📊 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn, XGBoost
- Matplotlib, Seaborn
- Streamlit (for UI)

## 🚀 How to Run

```bash
git clone https://github.com/lokhandelokeek11/Crop-Recommendation-Using-Machine-Learning.git
cd Crop-Recommendation-Using-Machine-Learning
pip install -r requirements.txt
streamlit run app.py
```

## Screenshots
![1744466530147](https://github.com/user-attachments/assets/ab922e2c-d67b-408b-8b1d-1aeea9c34df1)

## 🧠 Key Features
1. Supports real-time crop prediction based on user input
2. User-friendly web interface built using Streamlit
3. High prediction accuracy using ensemble and boosting techniques
4. Helps achieve eco-friendly, data-supported farming decisions

## 🌱 Future Scope
1. Integrate real-time weather API for live data predictions
2. Mobile application support for wider accessibility
3. Soil image-based recognition using deep learning
4. Regional language support for better adoption
