# Project Proposal
DSA210 – Introduction to Data Science (Fall 2025–2026)

## 1. Motivation

Air pollution has become one of the most significant environmental determinants of human health, contributing to millions of premature deaths globally each year. Among its components, fine particulate matter ($\text{PM}_{2.5}$) is particularly dangerous due to its ability to enter the bloodstream, potentially triggering chronic conditions like diabetes and hypertension.

This project aims to explore, at the county level across the United States, whether long-term exposure to PM2.5 correlates with a higher prevalence of diabetes and hypertension. Unlike simpler studies that use broad county averages, this research begins at the census tract level—a much finer geographic scale—to capture local variations in pollution and health and combines this finer data to generate more precise county-level estimates. Behavioral and lifestyle risk factors such as obesity, smoking, and physical inactivity will be included as control variables. The goal is to integrate environmental and public health data to reveal potential population-level associations and evaluate how much environmental exposure contributes beyond individual behaviors.

## 2. Datasets

### a. CDC PLACES: County-Level Health Indicators

**Source:** Centers for Disease Control and Prevention (CDC) – PLACES Project

**URL:** https://www.kaggle.com/datasets/cdc/500-cities/data

**Description:**
The dataset provides census tract-level estimates of health outcomes, risk factors, and preventive measures across all U.S. counties. Each variable represents the age-adjusted prevalence (percentage) of a given condition.

### b. EPA Air Quality System (AQS): Annual PM2.5 Concentrations

**Source:** United States Environmental Protection Agency (EPA) 

**URLs:** https://healthdata.gov/CDC/Daily-Census-Tract-Level-PM2-5-Concentrations-2011/wwnf-fvrd/about_data | https://healthdata.gov/CDC/Daily-Census-Tract-Level-PM2-5-Concentrations-2016/k9st-jhz8/about_data

**Description:**
High-resolution daily PM2.5 estimates for every census tract in the United States. The 10-year data will be averaged across years to create a stable "chronic exposure" metric for each tract.

### c. NCHS Urban-Rural Classification Scheme

**Source:** National Center for Health Statistics (NCHS)

**URL:** https://www.cdc.gov/nchs/data-analysis-tools/urban-rural.html

**Description:**
This dataset classifies U.S. counties into urbanization levels (e.g., large central metro, medium metro, small metro, micropolitan, noncore) based on population size and density. This variable will be used to control for urban-rural differences in pollution exposure and health outcomes.


## 3. Data Integration Plan

The integration process follows a "Tract-to-County" pipeline to ensure the final county values are weighted by where people actually live.

1. Tract-Level Processing: PM2.5 daily data is first averaged by year for each census tract. These annual averages are then combined to create a long-term (multi-year) mean for each tract.

2. Initial Merge: The PLACES health data and PM2.5 data are merged using the 11-digit Census Tract FIPS code.

3. Population-Weighted Aggregation: To reduce the 50,000+ data points to a county-level dataset without losing accuracy, population weighting is used. Instead of a simple average, the county value for each variable is calculated as:

$$
	\text{County Value} = \frac{\sum\bigl(\text{Tract Value} \times \text{Tract Population}\bigr)}{\sum \text{Tract Population}}
$$

This ensures that a highly populated, polluted tract has a greater impact on the county score than a sparsely populated one.

4. Urbanization Mapping: The 6-level NCHS codes are joined using the 5-digit County FIPS (the first 5 digits of the ctfips).

The merged dataset will provide a comprehensive view of how environmental and lifestyle variables align with public health outcomes across U.S. counties.

**Final Dataset Variables:**
ctfips, avg_pm25, state_abbreviation, state_name, county_name, total_population, total_population_18_plus, diabetes, hypertension, smoking, obesity, no_lt_physical_activity, binge_drinking, lack_of_health_insurance, routine_checkup, food_insecurity, housing_insecurity, urbanization_level.

## 4. Hypotheses

### Main Hypothesis (H₁)

Counties with higher long-term exposure to fine particulate matter (PM2.5) have a higher prevalence of diabetes and hypertension, even after controlling for key behavioral risk factors, and socioeconomic variables.

### Null Hypothesis (H₀)

There is no statistically significant relationship between PM2.5 exposure and the prevalence of diabetes or hypertension.

### Secondary Hypothesis (H₂)

Advanced machine learning algorithms, (such as Random Forest and Gradient Boosting), will significantly outperform traditional Linear Regression and K-Nearest Neighbors (KNN) in predicting county-level chronic disease prevalence, demonstrating that environmental and behavioral risks have complex, non-linear interactions.

### Third Hypothesis (H₃)

The strength of the association between PM2.5 and chronic disease varies significantly based on urbanization levels, with urban counties showing a stronger association due to higher pollution levels.

## 5. Expected Outcomes

- A refined dataset that correctly reflects population-level exposure through weighted aggregation.

- Identification of statistically significant correlations between PM2.5 concentration and the prevalence of chronic diseases (diabetes and hypertension).

- Quantitative estimation of how much air pollution contributes to disease prevalence compared to behavioral factors.

- Interaction plots showing how urbanization (H₃) steepen the "slope" of the pollution-health relationship.

- An interpretable regression or machine learning model demonstrating the predictive influence of environmental variables relative to behavioral ones.

## 6. Findings

The findings can be found in the final report included in this repository, named `DSA210_FinalReport.pdf`.