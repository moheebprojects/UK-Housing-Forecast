import pandas as pd
import numpy as np

uk_housing_df = pd.read_csv("data/UK_Housing_(Cleaned).csv")

# Preview column types
print(uk_housing_df.dtypes)

# Removing 2 columns
uk_housing_df = uk_housing_df.drop(columns=["PAON", "SAON"])

# See missing value summary

print(uk_housing_df.isna().sum())

# Removing duplicates

uk_housing_df = uk_housing_df.drop_duplicates()

# Identifying Number of Unique values for each columns
print(uk_housing_df.nunique())

# Confident Interval, 5% and 95% quantile (removing Outliers)

lower_bound = uk_housing_df["Price"].quantile(0.05)
upper_bound = uk_housing_df["Price"].quantile(0.95)

# Keep only data within the 5%-95% range
filtered_df = uk_housing_df[
    (uk_housing_df["Price"] >= lower_bound) & (uk_housing_df["Price"] <= upper_bound)
]

print(filtered_df)
