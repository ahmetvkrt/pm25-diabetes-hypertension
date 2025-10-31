# Project Proposal
DSA210 – Introduction to Data Science (Fall 2025–2026)

## 1. Motivation

Air pollution has become one of the most significant environmental determinants of human health, contributing to millions of premature deaths globally each year. Among its components, fine particulate matter (PM2.5) has been shown to cause chronic diseases such as diabetes and hypertension.

This project aims to explore, at the county level across the United States, whether long-term exposure to PM2.5 correlates with higher prevalence of diabetes and hypertension. Behavioral and lifestyle risk factors such as obesity, smoking, and physical inactivity will be included as control variables. The goal is to integrate environmental and public health data to reveal potential population-level associations and evaluate how much environmental exposure contributes beyond individual behaviors.

## 2. Datasets

### a. CDC PLACES: County-Level Health Indicators

**Source:** Centers for Disease Control and Prevention (CDC) – PLACES Project

**URL:** https://www.kaggle.com/datasets/cdc/500-cities/data

**Description:**
The dataset provides county-level estimates of health outcomes, risk factors, and preventive measures across all U.S. counties. Each variable represents the age-adjusted prevalence (percentage) of a given condition.

**Key Variables to Be Used:**

- DIABETES_AdjPrev: Age-adjusted prevalence of diabetes
- BPHIGH_AdjPrev: Age-adjusted prevalence of high blood pressure (hypertension)
- OBESITY_AdjPrev: Prevalence of obesity
- CSMOKING_AdjPrev: Prevalence of current smoking
- LPA_AdjPrev: Prevalence of leisure-time physical inactivity
- ACCESS2_AdjPrev: Percentage of adults without health insurance
- CountyFIPS: County-level FIPS code used for merging

### b. EPA Air Quality System (AQS): Annual PM2.5 Concentrations

**Source:** United States Environmental Protection Agency (EPA) – AirData Portal

**URL:** https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual

**Description:**
Contains annual mean concentrations of PM2.5 for each U.S. county, along with corresponding state and county codes, measurement counts, and summary statistics.

## 3. Data Integration Plan

Both datasets include geographic identifiers that allow them to be matched at the county level. The EPA dataset contains State Code and County Code, while the CDC PLACES dataset includes a unified CountyFIPS identifier.

**Integration Steps:**

1. Create a 5-digit FIPS key in the EPA dataset by combining state and county codes.

2. Calculate the average PM2.5 exposure for each county (single-year or multi-year average).

3. Merge the EPA and CDC datasets on their common FIPS codes.

4. Retain relevant columns for analysis: air pollution levels (PM2.5), disease prevalence (diabetes, hypertension), and behavioral factors (obesity, smoking, inactivity).

The merged dataset will provide a comprehensive view of how environmental and lifestyle variables align with public health outcomes across U.S. counties.

## 4. Hypotheses

### Main Hypothesis (H₁)

Counties with higher long-term exposure to fine particulate matter (PM2.5) have higher prevalence of diabetes and hypertension, even after controlling for obesity, smoking, and physical inactivity.

### Null Hypothesis (H₀)

There is no statistically significant relationship between PM2.5 exposure and the prevalence of diabetes or hypertension.

## 5. Expected Outcomes

- Identification of statistically significant correlations between PM2.5 concentration and the prevalence of chronic diseases (diabetes and hypertension).

- Quantitative estimation of how much air pollution contributes to disease prevalence compared to behavioral factors.

- Visualizations showing spatial patterns of pollution and disease burden across U.S. counties.

- An interpretable regression or machine learning model demonstrating the predictive influence of environmental variables relative to behavioral ones.
