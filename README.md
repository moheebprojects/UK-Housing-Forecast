# UK Housing Market Analysis & Forecasting

This project explores and forecasts UK housing prices using publicly available UK housing transaction data, sourced from HM Land Registry. It covers housing sales across England, Wales, Scotland, and Northern Ireland from 1995 to 2023. It includes an exploratory data analysis (EDA) followed by time-series forecasting utilising ARIMA model.

The project is broken into three clear modules:
1) Data Cleaning
2) Data Exploratory Analysis
3) Time Series Forecasting (ARIMA)

## Project Overview

- Goal: Understand trends in UK housing prices and forecast future prices.
- Data: Cleaned UK property transaction dataset with fields like Price, District, Date_of_Transfer, Property_Type, etc.
- Techniques Used: Exploratory data analysis, feature engineering, ARIMA forecasting, confidence interval estimation, RMSE evaluation.

## Dataset
The dataset is available on Kaggle.
🔗 UK Housing Dataset on Kaggle (https://www.kaggle.com/datasets/burhanimtengwa/uk-housing-cleaned).

![image](https://github.com/user-attachments/assets/2f18b1b5-5bac-435c-ba0c-047d4c042863)


## Tools & Libraries

- Python (Pandas, NumPy)
- Matplotlib / Seaborn / Plotly – for visualization
- Statsmodels (ARIMA, ADF Test) – for time series forecasting
- Scikit-learn – RMSE evaluation

## Module 1: Data Cleaning & Exploratory Analysis (uk_housing_eda.py)

- Converted dates to datetime format
- Removed duplicates and dropped unnecessary columns
- Filtered outliers using 5th–95th percentiles
- Extracted Sale_Year, Sale_Month, and Sale_Month_Name
- Visualized trends in:
- Yearly average house prices
- Prices by property type and old/new status
- Monthly seasonality in price and sales count
- Top and bottom 10 districts by average price
- Price distributions via boxplots

Example Insights:
📈 Detached homes have consistently higher prices than other property types

🆕 New builds tend to be more expensive than older properties

📅 Transactions peak during summer months (May–August)

🏘️ Wide variation in district-level pricing, with clear regional disparities

## Module 2: Forecasting UK House Prices (uk_housing_forecast.py)

- Conducted stationarity testing using the Augmented Dickey-Fuller (ADF) test
- Fit an ARIMA(1,1,1) model to average yearly housing prices
- Forecasted house prices 5 years into the future
- Plotted confidence intervals for forecast estimates
- Evaluated model performance with Root Mean Squared Error (RMSE)
- Compared predictions against a held-out test set

Forecasting Output:
A plot showing actual historical prices vs. future forecast

95% confidence interval shaded area to represent model uncertainty

