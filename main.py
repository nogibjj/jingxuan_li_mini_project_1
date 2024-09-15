"""
Main cli or app entry point
"""

from mylib.lib import *
import click

def g_describe(file):
    g = load_and_preview_data(file)
    return g
def save_to_md():
    with open("test.md","a") as file:
        file.write("test")
if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    file_path = './Employee.csv'
    df = g_describe(file_path)
    save_to_md()

    # Calculate and display summary statistics
    calculate_summary_statistics(df)

    # Calculate and display descriptive statistics for Age and Salary
    calculate_descriptive_statistics(df)

    # Plot the Age distribution
    plot_age_distribution(df)
