# Flight Operations & Delay Analysis — 2024

## 1. Dashboard Objective

The Flight Operations & Delay Analysis Dashboard is designed to provide an overview of flight activity and operational performance. It focuses on flight volume, airline performance, delays, major causes of delays, route activity, cancellations, and diversions.

The dashboard will help users identify patterns in flight operations and compare performance across airlines, airports, and routes.

---

## 2. Key Performance Indicators (KPIs)

| KPI | Purpose |
|---|---|
| **Total Flights** | Shows the overall number of flight records in the dataset. |
| **Average Departure Delay** | Measures the average delay experienced before departure. |
| **Average Arrival Delay** | Measures the average delay experienced at arrival. |
| **Cancellation Rate** | Shows the percentage of flights that were cancelled. |
| **Diversion Rate** | Shows the percentage of flights that were diverted. |

---

## 3. Dashboard Filters

The dashboard should provide filters that allow users to explore specific parts of the dataset.

- **Airline**
- **Origin Airport**
- **Destination Airport**
- **Day of Week**

---

## 4. Dashboard Sections

### A. Flight Overview

This section provides a high-level view of flight activity.

**Planned visualizations:**
- Flights by Airline
- Top Origin Airports

**Purpose:** Identify airlines and airports with the highest flight activity.

---

### B. Delay Analysis

This section focuses on flight delays and airline operational performance.

**Planned visualizations:**
- Average Delay by Airline
- Departure Delay vs Arrival Delay
- Delay Distribution

**Purpose:** Compare airline delay performance and understand the overall distribution of flight delays.

---

### C. Delay Causes

The dataset contains several categories of delay causes.

**Planned visualization:**
- Delay Causes

The analysis will consider:
- Carrier Delay
- Weather Delay
- NAS Delay
- Security Delay
- Late Aircraft Delay

**Purpose:** Identify the major factors contributing to flight delays.

---

### D. Route Analysis

This section examines flight activity and delay patterns across routes.

**Planned visualizations:**
- Top Flight Routes
- Average Delay by Route

**Purpose:** Identify frequently used routes and routes associated with higher average delays.

---

### E. Cancellations & Diversions

This section focuses on operational disruptions.

**Planned visualizations:**
- Cancellation Reasons
- Cancelled vs Diverted Flights

**Purpose:** Understand the frequency and reasons for cancellations and diversions.

---

## 5. Proposed Dashboard Layout

```text
┌──────────────────────────────────────────────────────────────┐
│              ✈️ FLIGHT OPERATIONS & DELAY ANALYSIS           │
├──────────────────────────────────────────────────────────────┤
│ Filters: Airline | Origin | Destination | Day of Week       │
├──────────────┬──────────────┬──────────────┬─────────────────┤
│ TOTAL        │ AVG DEP      │ AVG ARR      │ CANCELLATION    │
│ FLIGHTS      │ DELAY        │ DELAY        │ RATE            │
├──────────────┴──────────────┴──────────────┴─────────────────┤
│                                                              │
│  FLIGHTS BY AIRLINE          │  TOP ORIGIN AIRPORTS          │
│                              │                               │
├──────────────────────────────┼───────────────────────────────┤
│                              │                               │
│  AVERAGE DELAY BY AIRLINE    │  DELAY DISTRIBUTION           │
│                              │                               │
├──────────────────────────────┴───────────────────────────────┤
│                                                              │
│                       DELAY CAUSES                            │
│                                                              │
├──────────────────────────────┬───────────────────────────────┤
│                              │                               │
│  TOP FLIGHT ROUTES           │  AVERAGE DELAY BY ROUTE       │
│                              │                               │
├──────────────────────────────┼───────────────────────────────┤
│  CANCELLATION REASONS        │  CANCELLED VS DIVERTED        │
│                              │                               │
└──────────────────────────────┴───────────────────────────────┘
```

---

## 6. Planned Visualizations Summary

| # | Visualization | Dashboard Section |
|---|---|---|
| 1 | Flights by Airline | Flight Overview |
| 2 | Top Origin Airports | Flight Overview |
| 3 | Average Delay by Airline | Delay Analysis |
| 4 | Departure Delay vs Arrival Delay | Delay Analysis |
| 5 | Delay Distribution | Delay Analysis |
| 6 | Delay Causes | Delay Causes |
| 7 | Top Flight Routes | Route Analysis |
| 8 | Average Delay by Route | Route Analysis |
| 9 | Cancellation Reasons | Cancellations & Diversions |
| 10 | Cancelled vs Diverted Flights | Cancellations & Diversions |

---

## 7. Main Dashboard Questions

The dashboard should help users answer the following questions:

1. How many flights are present in the dataset?
2. Which airlines operate the most flights?
3. Which airports have the highest flight activity?
4. Which airlines have higher average delays?
5. Is departure delay associated with arrival delay?
6. What does the overall delay distribution look like?
7. What are the major causes of flight delays?
8. Which routes have the highest flight volume?
9. Which routes experience higher average delays?
10. What are the main reasons for flight cancellations?
11. How many flights were cancelled or diverted?

---

## 8. Dataset Consideration

The current cleaned dataset contains **96,711 flight records**. The dataset currently has `month = 1`, so time-based analysis across multiple months should not be presented as a full-year trend unless additional months are added to the dataset.
This dashboard plan is intended to guide the implementation of the final visualization/dashboard and can be updated if the dataset scope changes.
