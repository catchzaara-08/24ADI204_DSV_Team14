import pandas as pd
import os

file_path = r"C:\Users\ashun\Downloads\flight_data_2024_final_cleaned.csv"

print("File exists:", os.path.exists(file_path))
print("File size (MB):", round(os.path.getsize(file_path) / (1024 * 1024), 2))

print("\nLoading dataset... Please wait.")
df = pd.read_csv(file_path, low_memory=False)

print("\n========== DATASET OVERVIEW ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== DATE RANGE ==========")
print("Start date:", df["fl_date"].min())
print("End date:", df["fl_date"].max())

print("\n========== DATA QUALITY ==========")
print("Total missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())
print("\n========== MISSING VALUES BY COLUMN ==========")

missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

print(missing.to_string())

print("\n========== MISSING VALUE PERCENTAGE ==========")
print(((missing / len(df)) * 100).round(2).to_string())
print("\n========== FLIGHT STATUS ==========")

print("Cancelled flights:")
print(df["cancelled"].value_counts(dropna=False))

print("\nDiverted flights:")
print(df["diverted"].value_counts(dropna=False))

print("\nCancellation codes:")
print(df["cancellation_code"].value_counts(dropna=False))

print("\nMissing arrival delay by cancellation status:")
print(df.groupby("cancelled")["arr_delay"].apply(
    lambda x: x.isnull().sum()
))
print("\n========== DELAY CAUSE ANALYSIS ==========")

delay_columns = [
    "carrier_delay",
    "weather_delay",
    "nas_delay",
    "security_delay",
    "late_aircraft_delay"
]

print("\nMissing values in delay causes:")
print(df[delay_columns].isnull().sum())

print("\nNon-missing values in delay causes:")
print(df[delay_columns].notnull().sum())

print("\nArrival delay summary:")
print(df["arr_delay"].describe())

print("\nInspection complete!")