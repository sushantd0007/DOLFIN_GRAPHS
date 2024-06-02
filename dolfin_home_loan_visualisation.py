# -*- coding: utf-8 -*-
"""DolFin - Home Loan Visualisation

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PPrhDjbS_hIowqkYtRbW5Rv31HY45UkG
"""

import pandas as pd # type: ignore # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
import matplotlib.dates as mdates # type: ignore

def visualise_loan_balance(csv_file_path):
    # Set DolFin branding colour palette
    sns.set_palette(['#343a40', '#0077bb', '#d9d9d9', '#fafafe', '#abb5be'])

    # Load in users home loan data
    df = pd.read_csv(csv_file_path)

    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Specify custom fonts and styles according to DolFin brand style guide
    font_heading = {'weight': 'extra bold', 'size': 48, 'color': '#0077BB'}
    font_body = {'weight': 'medium', 'size': 24, 'color': '#1E1E1E'}

    # Create plot using Seaborn
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Date', y='Total')

    # Adjust X-axis date format and frequency
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # Display every 3rd month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format as Year-Month

    # Reduce Y-axis labels frequency
    plt.gca().yaxis.set_major_locator(plt.MaxNLocator(8))

    # Add labels and title with custom fonts and styles
    plt.xlabel('Date', **font_body)
    plt.ylabel('Total Loan Balance', **font_body)
    plt.title('Loan Balance Over Time', **font_heading)

    # Show plot
    plt.tight_layout()
    plt.show()

# Load in user home loan data
visualise_loan_balance("/content/user7_homeloandata.csv")