import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import zipfile

zip_path = "air quality  dataset.zip"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("air_quality_data")

df = pd.read_csv(
    "air_quality_data/air_quality_historical.csv"
)

df['date'] = pd.to_datetime(df['date'])

# AQI classification
def classify_aqi(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

# Apply classification
df['AQI_Category'] = df['us_aqi'].apply(classify_aqi)

# Basic AQI analysis
print("Average AQI:", df['us_aqi'].mean())
print("Minimum AQI:", df['us_aqi'].min())
print("Maximum AQI:", df['us_aqi'].max())

# Best day
best_day = df.loc[df['us_aqi'].idxmin()]

print("\nBest Air Quality Day:")
print("Date:", best_day['date'])
print("AQI:", best_day['us_aqi'])
print("Category:", best_day['AQI_Category'])

# Worst day
worst_day = df.loc[df['us_aqi'].idxmax()]

print("\nWorst Air Quality Day:")
print("Date:", worst_day['date'])
print("AQI:", worst_day['us_aqi'])
print("Category:", worst_day['AQI_Category'])

# Latest day
latest = df.sort_values('date').iloc[-1]

print("\nLatest Observation:")
print("Date:", latest['date'])
print("AQI:", latest['us_aqi'])
print("Category:", latest['AQI_Category'])

# Category counts
print("\nAQI Category Counts:")
print(df['AQI_Category'].value_counts())
