# UK Housing Market Analysis & Forecasting

This project explores and forecasts UK housing prices using publicly available UK housing transaction data, sourced from HM Land Registry. It covers housing sales across England, Wales, Scotland, and Northern Ireland from 1995 to 2023. It includes an exploratory data analysis (EDA) followed by time-series forecasting utilising ARIMA model.

## Project Overview

- Goal: Understand trends in UK housing prices and forecast future prices.
- Data: Cleaned UK property transaction dataset with fields like Price, District, Date_of_Transfer, Property_Type, etc.
- Techniques Used: Exploratory data analysis, feature engineering, ARIMA forecasting, confidence interval estimation, RMSE evaluation.

## Dataset
The dataset is available on Kaggle.
🔗 UK Housing Dataset on Kaggle (https://www.kaggle.com/datasets/burhanimtengwa/uk-housing-cleaned).

Note: Due to GitHub's file size restrictions, the dataset is not included in this repository.
After downloading, place the CSV file in the data/ folder before running the scripts.



## Tools & Libraries

- Python (Pandas, NumPy)
- Matplotlib / Seaborn / Plotly – for visualization
- Statsmodels (ARIMA, ADF Test) – for time series forecasting
- Scikit-learn – RMSE evaluation

## Key Exploratory Insights

- Yearly trend of average housing prices (increasing over time)
- Differences in price trends by Property_Type and Old_New status
- Seasonal patterns in sales frequency and average monthly prices
- Most and least expensive districts by average price
- Price distributions in top and bottom districts using boxplots

## Forecasting Highlights

- Applied ADF test to ensure stationarity of the time series
- Fit an ARIMA(1,1,1) model on historical average yearly prices
- Forecasted housing prices for the next 5 years
- Evaluated performance using RMSE
- Included confidence intervals around predictions
