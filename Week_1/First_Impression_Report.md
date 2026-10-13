# First Impression Report — Airline Flight Delay Analysis

## 1. Dataset Overview

- **Dataset:** Flight Data 2024
- **Total records:** 3,538,856
- **Total columns:** 35
- **Date range:** January 1, 2024 – July 4, 2024
- **Duplicate rows:** 0

The dataset contains flight schedules, operating carriers, origin and destination information, departure and arrival delays, cancellation and diversion indicators, flight duration, distance, and delay causes.

## 2. Initial Data Quality Assessment

- **Total missing cells:** 3,976,567
- **Cancellation code:** 3,489,749 missing values (98.61%)
- **Arrival delay:** 49,107 missing values (1.39%)
- **Departure delay:** 47,390 missing values (1.34%)
- **Delay-cause columns:** No missing values detected.

The missing cancellation codes appear consistent with flights that were not cancelled. Missing arrival-delay values coincide with the cancelled-flight count and require further investigation alongside diverted flights.

## 3. Flight Status

- **Non-cancelled flights:** 3,489,749
- **Cancelled flights:** 49,107
- **Non-diverted flights:** 3,529,555
- **Diverted flights:** 9,301

No duplicate rows were detected during the initial inspection.

## 4. Initial Statistical Findings

- **Mean arrival delay:** 8.10 minutes
- **Median arrival delay:** -5 minutes
- **Standard deviation:** Approximately 59.69 minutes
- **Minimum arrival delay:** -117 minutes
- **Maximum arrival delay:** 3,359 minutes

The difference between the mean and median suggests that large positive delays influence the average.

## 5. Scope and Limitations

The available dataset covers January 1 through July 4, 2024, rather than the complete calendar year. Missing values will be investigated before deciding whether to retain, exclude, or impute them. Outliers will be examined before any treatment is applied.

## 6. Next Steps

1. Validate missing values against cancellation and diversion status.
2. Examine distributions and potential outliers.
3. Perform univariate and bivariate exploratory data analysis.
4. Document cleaning decisions and findings.
