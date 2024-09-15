import os
from mylib.lib import (
    calculate_summary_statistics,
    calculate_descriptive_statistics,
    plot_age_distribution,
    plot_gender_distribution_by_department,
)
from main import g_describe, save_to_md, insert_image_to_md

# Assuming we have a local CSV file for testing purposes
example_csv = "./Employee.csv"


def test_g_describe():
    """Test that g_describe correctly loads and returns data."""
    df = g_describe(example_csv)
    assert df is not None, "The DataFrame should not be None."
    assert df.shape[1] > 0, "The DataFrame should have columns."
    assert df.shape[0] > 0, "The DataFrame should have rows."


def test_save_to_md():
    """Test that text is correctly written to the markdown file."""
    test_md_file = "test.md"
    save_to_md("# Test Heading", test_md_file)

    with open(test_md_file, "r") as file:
        content = file.read()

    assert "# Test Heading" in content, "Markdown file should contain the heading."

    # Clean up
    os.remove(test_md_file)


def test_insert_image_to_md():
    """Test that image references are correctly added to the markdown file."""
    test_md_file = "test.md"
    insert_image_to_md("age.png", test_md_file)

    with open(test_md_file, "r") as file:
        content = file.read()

    assert "![age.png](age.png)" in content, "not contain the image reference."

    # Clean up
    os.remove(test_md_file)


def test_calculate_summary_statistics():
    """Test that summary statistics are correctly calculated."""
    df = g_describe(example_csv)
    summary_stats = calculate_summary_statistics(df)
    assert "Age" in summary_stats.columns, "Summary statistics should include 'Age'."
    assert "Salary" in summary_stats.columns, "should include 'Salary'."
    assert summary_stats.loc["mean", "Age"] is not None


def test_calculate_descriptive_statistics():
    df = g_describe(example_csv)
    age_mean = df["Age"].mean()
    salary_mean = df["Salary"].mean()

    # Calculate descriptive statistics
    calculate_descriptive_statistics(df)

    # Ensure mean calculations are consistent
    assert round(age_mean, 2) == round(df["Age"].mean(), 2)
    assert round(salary_mean, 2) == round(df["Salary"].mean(), 2)


def test_plot_age_distribution():
    """Test that the age distribution plot is generated and saved as a file."""
    df = g_describe(example_csv)
    plot_age_distribution(df)
    assert os.path.exists("age.png")

    # Clean up
    os.remove("age.png")


def test_plot_gender_distribution_by_department():
    df = g_describe(example_csv)
    plot_gender_distribution_by_department(df)
    assert os.path.exists("department.png")

    # Clean up
    os.remove("department.png")


if __name__ == "__main__":
    test_g_describe()
    test_save_to_md()
    test_insert_image_to_md()
    test_calculate_summary_statistics()
    test_calculate_descriptive_statistics()
    test_plot_age_distribution()
    test_plot_gender_distribution_by_department()
