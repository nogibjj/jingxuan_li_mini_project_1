import pandas as pd
import matplotlib.pyplot as plt
def load_and_preview_data(file_path):
    """
    Loads the data from the specified CSV file and prints the first few rows.
    """
    df = pd.read_csv(file_path)
    print(df.head())
    return df

def calculate_summary_statistics(df):
    """
    Calculates and prints summary statistics for the data.
    """
    summary_statistics = df.describe()
    print(summary_statistics)
    return summary_statistics

def calculate_descriptive_statistics(df):
    """
    Calculates and prints the descriptive statistics for Age and Salary.
    """
    age_mean = df['Age'].mean()
    age_median = df['Age'].median()
    age_std = df['Age'].std()

    salary_mean = df['Salary'].mean()
    salary_median = df['Salary'].median()
    salary_std = df['Salary'].std()

    print("Age descriptive statistics:")
    print(f"Average age: {age_mean:.2f}")
    print(f"Median age: {age_median}")
    print(f"Standard Deviation of age: {age_std:.2f}")

    print("\nSalary descriptive statistics:")
    print(f"Average salary: {salary_mean:.2f}")
    print(f"Median salary: {salary_median}")
    print(f"Standard Deviation of salary: {salary_std:.2f}")

def plot_age_distribution(df):
    """
    Plots the distribution of Age.

    """
    plt.hist(df['Age'], bins=10, color='blue', alpha=0.7)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True)
    # plt.show()
    plt.savefig("age.png")

# Define a function to plot the gender distribution across departments

def plot_gender_distribution_by_department(df):
    gender_dept_counts = df.groupby(['Department', 'Gender']).size().unstack()
    gender_dept_counts.plot(kind='bar', stacked=True, figsize=(10, 6), 
                            color=['lightblue', 'lightgreen', 'lightcoral'])
    plt.title('Gender Distribution by Department')
    plt.xlabel('Department')
    plt.ylabel('Number of Employees')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.legend(title='Gender')
    plt.tight_layout()
    plt.savefig("department.png")


