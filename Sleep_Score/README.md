# Sleep Health and Mental Health Prediction

## Objective

The objective of this assignment is to calculate a Sleep Score based on various sleep and lifestyle factors and predict the Mental Health Category using Sleep Score and Stress Level.

## Dataset

The dataset used in this project is `Sleep_health_and_lifestyle_dataset.csv`.

It contains information including:

- Sleep Duration
- Quality of Sleep
- Physical Activity Level
- Stress Level
- BMI Category
- Heart Rate
- Daily Steps
- Sleep Disorder

## Methodology

The following steps are performed:

1. Load the dataset using Pandas.
2. Preprocess the required sleep and lifestyle factors.
3. Calculate a Sleep Score based on the relevant factors.
4. Use Sleep Score and Stress Level as input features.
5. Train machine learning models to predict Mental Health Category.
6. Compare the performance of different models using accuracy.

## Machine Learning Models

The following models are used:

- Decision Tree
- Random Forest
- Logistic Regression

## Mental Health Categories

The predicted mental health category is classified as:

- Good
- Moderate
- Poor

## Result

The trained models are evaluated using test data and their accuracies are compared to understand their performance.

The Random Forest model is also used to predict the mental health category for new Sleep Score and Stress Level values.

## Conclusion

The project demonstrates how sleep and stress-related factors can be used with machine learning to estimate a mental health category. The prediction is only a data-based estimate and is not a medical diagnosis.

## Technologies Used

Python  
Pandas  
NumPy  
Scikit-learn  
Matplotlib  
GitHub

## How to Run

Clone the repository and install the required libraries:

```bash
pip install -r requirements.txt
