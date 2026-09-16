import pandas as pd

# Load the dataset
df = pd.read_csv("data/air_quality_dataset.csv")

# Calculate the average AQI
aqi = df["us_aqi"].mean()

print("Air Quality Index (AQI):", round(aqi, 2))

# Classification of AQI
if aqi <= 50:
    category = "Good"
elif aqi <= 100:
    category = "Moderate"
elif aqi <= 150:
    category = "Unhealthy for Sensitive Groups"
elif aqi <= 200:
    category = "Unhealthy"
elif aqi <= 300:
    category = "Very Unhealthy"
else:
    category = "Hazardous"

print("AQI Category:", category)
