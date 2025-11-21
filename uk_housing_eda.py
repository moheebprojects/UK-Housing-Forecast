from uk_housing_cleaning import *
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Average house prices over-time graph

filtered_df["Sale_Date"] = pd.to_datetime(filtered_df["Date_of_Transfer"])
filtered_df["Sale_Year"] = filtered_df["Sale_Date"].dt.year
avg_price_per_year = filtered_df.groupby("Sale_Year")["Price"].mean().reset_index()

plt.plot(avg_price_per_year["Sale_Year"], avg_price_per_year["Price"])

# graph title and labels
plt.xlabel("Year")
plt.ylabel("Average Housing Price")
plt.title("UK Housing Prices Over Time")

# prinitng graph
plt.show()

# Average house type (grouped) prices over-time

avg_price_by_type = (
    filtered_df.groupby(["Property_Type", "Sale_Year"])["Price"].mean().reset_index()
)

# Check the result to ensure the grouping is correct
print(avg_price_by_type.head())

# Setting the plot style for better visuals
sns.set(style="whitegrid")

# Creating the line plot for average prices by Property_Type
plt.figure(figsize=(12, 6))
sns.lineplot(
    x="Sale_Year", y="Price", hue="Property_Type", data=avg_price_by_type, marker="o"
)

# graph title and labels
plt.xlabel("Year")
plt.ylabel("Average Housing Price")
plt.title("Average Housing Prices by Property Type Over Time")
plt.legend(title="Property Type")
plt.grid(True)

# generating the graph
plt.show()

# Average house price of "Old" and "New" houses over-time graph

# Grouping by Old_New and Sale_Year, then calculating the mean price
avg_price_by_old_new = (
    filtered_df.groupby(["Old_New", "Sale_Year"])["Price"].mean().reset_index()
)

# ensuring the grouping is correct
print(avg_price_by_old_new.head())

# Creating the line plot for average prices by "Old" and "New" property status
plt.figure(figsize=(12, 6))
sns.lineplot(
    x="Sale_Year", y="Price", hue="Old_New", data=avg_price_by_old_new, marker="o"
)

#  grapht tile and labels added
plt.xlabel("Year")
plt.ylabel("Average Housing Price")
plt.title("Average Housing Prices: Old vs New Properties Over Time")
plt.legend(title="Property Status")
plt.grid(True)

# generating the graph
plt.show()

# Average house price sold each month

# Ensuring date is in datetime format
filtered_df["Sale_Date"] = pd.to_datetime(filtered_df["Date_of_Transfer"])

# Creating a 'Sale_Month' column (1 = January, ..., 12 = December)
filtered_df["Sale_Month"] = filtered_df["Sale_Date"].dt.month

# For month names like 'Jan', 'Feb', etc.
filtered_df["Sale_Month_Name"] = filtered_df["Sale_Date"].dt.strftime("%b")

# Group by month and calculate average price
avg_price_per_month = (
    filtered_df.groupby("Sale_Month_Name")["Price"]
    .mean()
    .reindex(
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
    )
)

# bar graph
plt.figure(figsize=(10, 5))
avg_price_per_month.plot(kind="bar", color="skyblue")

plt.title("Average House Price by Month")
plt.xlabel("Month")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Number of houses sold each month

# Counting number of sales per month
sales_count_per_month = (
    filtered_df["Sale_Month_Name"]
    .value_counts()
    .reindex(
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
    )
)

# bar graph
plt.figure(figsize=(10, 5))
sales_count_per_month.plot(kind="bar", color="orange")

plt.title("Number of Sales by Month")
plt.xlabel("Month")
plt.ylabel("Number of Sales")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Identifying the 10 most expensive districts

# Calculating average price by District
avg_price_by_district = (
    filtered_df.groupby("District")["Price"].mean().sort_values(ascending=False)
)

# Selecting top 10
top_districts = avg_price_by_district.head(10)

# bar chart
plt.figure(figsize=(12, 6))
top_districts.plot(kind="bar", color="mediumseagreen")

plt.title("Top 10 Districts by Average House Price")
plt.ylabel("Average Price")
plt.xlabel("District")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis="y")
plt.show()


# Identifying the 10 cheapest districts

# Calculate average price by District
avg_price_by_district = filtered_df.groupby("District")["Price"].mean().sort_values()

# selecting bottom 10
bottom_districts = avg_price_by_district.head(10)

# bar chart
plt.figure(figsize=(12, 6))
bottom_districts.plot(kind="bar", color="salmon")

plt.title("Bottom 10 Districts by Average House Price")
plt.ylabel("Average Price")
plt.xlabel("District")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis="y")
plt.show()

# districts with the most transactions (sales)

# obtaining the top 10 districts with most transactions
top_districts = filtered_df["District"].value_counts().head(10).index

# Filtering the DataFrame
top_df = filtered_df[filtered_df["District"].isin(top_districts)]

# boxplot graph
plt.figure(figsize=(12, 6))
sns.boxplot(data=top_df, x="District", y="Price", palette="Set2")

plt.title("Price Distribution in Top 10 Districts by Number of Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()


# districts with the least transactions (sales)

# Filtering the DataFrame for bottom 10 transactons by districts
low_df = filtered_df[filtered_df["District"].isin(bottom_districts.index)]

# boxplot graph
plt.figure(figsize=(12, 6))
sns.boxplot(data=low_df, x="District", y="Price", palette="Reds")

plt.title("Price Distribution in Bottom 10 Districts by Average Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
