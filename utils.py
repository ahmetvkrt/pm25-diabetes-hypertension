import pandas as pd
import numpy as np


def weighted_average(group, value_column, weight_column):
    """
    Calculate the weighted average of a value column using a weight column within a group.
    Args:
        group (pd.DataFrame): The group of data to calculate the weighted average for.
        value_column (str): The name of the column containing the values to average.
        weight_column (str): The name of the column containing the weights.
    Returns:
        float: The weighted average.
    """
    d = group[value_column]
    w = group[weight_column]
    return (d * w).sum() / w.sum()


def build_dataset(csv_path="places_pm25_merged.csv", population_threshold=3000):
    """
    Load merged dataset from CSV file and group the tract level data to county level by weighted averaging according to population.
    The function filters out tracts with total population less than the specified threshold before grouping to eliminate noise from small populated tracts.
    Args:
        csv_path (str): Path to the CSV file containing the merged dataset.
        population_threshold (int): Minimum population required for a tract to be included in the grouping.
    Returns:
        pd.DataFrame: Grouped dataset at county level.
    """
    
    df = pd.read_csv(csv_path, index_col="ctfips")

    # Filter out tracts with population less than the threshold and drop rows with missing values
    df = df[df["total_population"] >= population_threshold].dropna()

    cols_to_be_used = [
        "diabetes",
        "hypertension",
        "avg_pm25",
        "smoking",
        "obesity",
        "no_lt_physical_activity",
        "binge_drinking",
        "lack_of_health_insurance",
        "routine_checkup",
        "food_insecurity",
        "housing_insecurity",
        "urbanization_level",
        "total_population",
    ]

    grouped_df = df.groupby(["state_name", "county_name"])[cols_to_be_used].apply(
        lambda x: pd.Series({
            "diabetes": weighted_average(x, "diabetes", "total_population"),
            "hypertension": weighted_average(x, "hypertension", "total_population"),
            "avg_pm25": weighted_average(x, "avg_pm25", "total_population"),
            "smoking": weighted_average(x, "smoking", "total_population"),
            "obesity": weighted_average(x, "obesity", "total_population"),
            "no_lt_physical_activity": weighted_average(x, "no_lt_physical_activity", "total_population"),
            "binge_drinking": weighted_average(x, "binge_drinking", "total_population"),
            "lack_of_health_insurance": weighted_average(x, "lack_of_health_insurance", "total_population"),
            "routine_checkup": weighted_average(x, "routine_checkup", "total_population"),
            "food_insecurity": weighted_average(x, "food_insecurity", "total_population"),
            "housing_insecurity": weighted_average(x, "housing_insecurity", "total_population"),
            "urbanization_level": x["urbanization_level"].iloc[0],
            "total_population": x["total_population"].sum(),
        })
    ).reset_index()

    # Eliminate any rows with values that are 0 after grouping
    grouped_df = grouped_df[(grouped_df[["diabetes", "hypertension", "avg_pm25"]] != 0).all(axis=1)]

    return grouped_df

def ols_summary(model):
    """
    Generate a summary table for an OLS regression model including coefficients, standard errors, p-values, and confidence intervals.
    Args:
        model: A fitted statsmodels OLS regression model.
    Returns:
        pd.DataFrame: Summary table with R^2 values, MSE, coefficients, standard errors, p-values, and confidence intervals.
    """
    ci = model.conf_int()
    coef_table = pd.concat([model.params, model.bse, model.pvalues, ci], axis=1)
    coef_table.columns = ['coef','std_err','pvalue','ci_lower','ci_upper']
    r_squared = model.rsquared
    adj_r_squared = model.rsquared_adj
    mse = model.mse_resid
    summary_df = pd.DataFrame({
        'R_squared': [r_squared],
        'Adj_R_squared': [adj_r_squared],
        'MSE': [mse],
        'RMSE': [np.sqrt(mse)]
    })
    
    return summary_df, coef_table