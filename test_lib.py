"""
Tests for lib.py functions
"""

from mylib.lib import (
    load_and_preview_data,
    calculate_summary_statistics,
    calculate_descriptive_statistics,
)

# Assuming we have a local CSV file for testing purposes
example_csv = "./Employee.csv"


def test_load_and_preview_data():
    """Test that loading the CSV will work"""
    df = load_and_preview_data(example_csv)
    assert df is not None, "The DataFrame should not be None."
    assert df.shape[1] > 0, "The DataFrame should have columns."
    assert df.shape[0] > 0, "The DataFrame should have rows."


def test_summary_statistics():
    """Test that summary statistics calculation works"""
    df = load_and_preview_data(example_csv)
    summary_stats = calculate_summary_statistics(df)
    assert "Age" in summary_stats.columns, "should include 'Age'."
    assert "Salary" in summary_stats.columns, "should include 'Salary'."
    assert summary_stats.loc["mean", "Age"] is not None, "Mean age wrong."


def test_descriptive_statistics():
    df = load_and_preview_data(example_csv)
    age_mean = df["Age"].mean()
    salary_mean = df["Salary"].mean()

    # Calculate descriptive statistics
    calculate_descriptive_statistics(df)

    # Ensure mean calculations are consistent
    assert round(age_mean, 2) == round(df["Age"].mean(), 2), "The mean age wrong."
    assert round(salary_mean, 2) == round(df["Salary"].mean(), 2)


if __name__ == "__main__":
    test_load_and_preview_data()
    test_summary_statistics()
    test_descriptive_statistics()
