from uk_housing_eda import *
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error

# forecasting using ARIMA LIBRARY
# ARIMA stationarity test

result = adfuller(avg_price_per_year["Price"])
print("ADF Statistic:", result[0])
print("p-value:", result[1])

# forecasting library ARIMA

# Setting 'Sale_Year' as the index
avg_price_per_year.set_index("Sale_Year", inplace=True)

# checking the data
print(avg_price_per_year)

# Fitting ARIMA model
model = ARIMA(avg_price_per_year["Price"], order=(1, 1, 1))  # (p,d,q) values
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())

# Forecasting the next 5 steps (years)
forecast = model_fit.forecast(steps=5)

print(forecast)


# Plotting historical data
plt.plot(avg_price_per_year.index, avg_price_per_year["Price"], label="Observed")

# Plotting the forecast
future_years = range(avg_price_per_year.index[-1] + 1, avg_price_per_year.index[-1] + 6)
plt.plot(future_years, forecast, label="Forecast", linestyle="--")

# groah title and labels
plt.xlabel("Year")
plt.ylabel("Average Housing Price")
plt.title("Housing Price Forecast with ARIMA")
plt.legend()
plt.grid(True)
plt.show()

# Train-Test Split & Forecast Evaluation

# Splitting the data
train = avg_price_per_year.iloc[:-5]
test = avg_price_per_year.iloc[-5:]

# Modelling the data
model = ARIMA(train["Price"], order=(1, 1, 1))
model_fit = model.fit()

# Forecasting the data
forecast = model_fit.forecast(steps=len(test))

# Evaluating the data
rmse = np.sqrt(mean_squared_error(test["Price"], forecast))
print("RMSE:", rmse)


# Forecasting next 5 years
forecast = model_fit.get_forecast(steps=5)
conf_int = forecast.conf_int()
predicted_mean = forecast.predicted_mean

# Defining future years
last_year = avg_price_per_year.index[-1]
future_years = range(last_year + 1, last_year + 6)

# Plotting historical data
plt.plot(avg_price_per_year.index, avg_price_per_year["Price"], label="Observed")

# Ploting forecasted values
plt.plot(future_years, predicted_mean, label="Forecast", linestyle="--")

# Plot confidence interval as shaded area
plt.fill_between(
    future_years,
    conf_int.iloc[:, 0],
    conf_int.iloc[:, 1],
    color="pink",
    alpha=0.3,
    label="95% Confidence Interval",
)

# graph title and labels
plt.xlabel("Year")
plt.ylabel("Average Housing Price")
plt.title("Housing Price Forecast with Confidence Interval (ARIMA)")
plt.legend()
plt.grid(True)
plt.show()
