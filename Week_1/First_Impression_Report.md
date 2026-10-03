# First Impression Report

## 1. Dataset Overview

The project uses a cleaned flight dataset containing flight records from January 1–6, 2024. The cleaned CSV file was provided by a team member and is stored at:

`data/cleaned/flight_data_2024_cleaned.csv`

The dataset contains **96,711 rows and 35 columns**.

The dataset will be explored to understand flight activity, delays, cancellations, and other relevant variables.

**Note:** The original dataset source and citation still need to be confirmed.

## 2. Dataset Structure

The cleaned dataset contains:

- **Rows:** 96,711
- **Columns:** 35
- **File format:** CSV

Each row represents a flight record, while the columns contain information about flight details and operational outcomes.

During the initial inspection:
- The `fl_date` column was found to contain one missing value.
- The available records cover January 1–6, 2024.

## 3. Main Variable Categories

The dataset contains variables related to the following areas:

- **Date and calendar details:** `year`, `month`, `day_of_month`, `day_of_week`, `fl_date`
- **Airline information:** `op_unique_carrier`, `op_carrier_fl_num`
- **Flight locations:** `origin`, `origin_city_name`, `origin_state_nm`, `dest`, `dest_city_name`, `dest_state_nm`
- **Flight timings:** Scheduled and actual departure and arrival times, along with taxi and wheels-off/wheels-on times
- **Flight delays:** `dep_delay`, `arr_delay`
- **Cancellations:** `cancelled`, `cancellation_code`
- **Delay causes:** `carrier_delay`, `weather_delay`, `nas_delay`, `security_delay`, `late_aircraft_delay`

These variables can help examine flight activity, delay patterns, cancellations, and possible factors associated with delays.

## 4. Initial Data-Quality Check

The initial inspection of the cleaned dataset found:

- **Missing values:** One missing value in `fl_date`; all other columns have no missing values.
- **Duplicate rows:** No duplicate rows were detected.

These checks provide an initial understanding of the dataset's completeness and consistency.

## 5. Initial Observations and Scope

- The dataset contains 96,711 flight records.
- The available records cover January 1–6, 2024.
- The dataset includes flight details, departure and arrival delays, cancellations, and delay-cause variables.
- Since the available data covers only six days, findings should not be generalized to the entire year without additional data.

These observations describe the available cleaned file and its current scope.