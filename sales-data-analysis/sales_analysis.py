"""
Sales Data Analysis Script
Mehul J. Chaudhary
Description:
This script loads, cleans, analyzes sales data
and prints a summary report using Pandas.
"""

import pandas as pd


def load_data(file_path):
    """Load dataset from CSV file"""
    return pd.read_csv(file_path)


def clean_data(df):
    """Clean dataset by handling missing values and duplicates"""
    numeric_cols = df.select_dtypes(include="number").columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    df = df.drop_duplicates()
    return df


def analyze_sales(df):
    """Compute core sales metrics"""
    return {
        "Total Revenue": df["Total_Sales"].sum(),
        "Average Sales Value": round(df["Total_Sales"].mean(), 2),
        "Best Selling Product": (
            df.groupby("Product")["Total_Sales"].sum().idxmax()
        ),
        "Total Transactions": len(df),
    }


def product_contribution(df):
    """Calculate product-wise contribution percentage"""
    contribution = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )
    return (contribution / contribution.sum() * 100).round(2)


def main():
    df = load_data("sales_data.csv")
    df = clean_data(df)

    summary = analyze_sales(df)
    contribution = product_contribution(df)

    print("\n=== SALES SUMMARY ===")
    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\n=== PRODUCT CONTRIBUTION (%) ===")
    print(contribution)


if __name__ == "__main__":
    main()
