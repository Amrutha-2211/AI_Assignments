# Air Quality Index (AQI) Analysis

## Objective

The objective of this assignment is to calculate the Air Quality Index (AQI) for Hyderabad using the given historical air-quality dataset and classify the AQI according to standard AQI categories.

## Dataset

The dataset used in this project is `air quality dataset.csv`.

It contains historical air-quality information including:

- PM2.5
- PM10
- Carbon Monoxide
- Nitrogen Dioxide
- Sulphur Dioxide
- Ozone
- US AQI
- European AQI

For this analysis, the `us_aqi` column is used.

## Methodology

The following steps are performed:

1. Load the dataset using Pandas.
2. Calculate the average AQI using the `us_aqi` column.
3. Compare the calculated AQI with the standard AQI ranges.
4. Classify the air quality.

## AQI Classification

AQI Range	Category

0–50	  Good
51–100	Moderate
101–150	Unhealthy for Sensitive Groups
151–200	Unhealthy
201–300	Very Unhealthy
301–500	Hazardous

## Result

The calculated average AQI is:

87.13

## AQI Category

Moderate

## Conclusion

The calculated AQI for Hyderabad is 87.13, which falls under the Moderate category.

This indicates that the overall air quality represented by the dataset is acceptable, although some sensitive individuals may experience effects from air pollution.

## Technologies Used
Python
Pandas
GitHub

## How to Run

Clone the repository and install the required library:

pip install -r requirements.txt

Run the Python file:

python aqi_analysis.py

Expected output:

Air Quality Index (AQI): 87.13
AQI Category: Moderate
