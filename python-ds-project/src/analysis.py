import pandas as pd

class Analyzer:
    """
    Class for data analysis
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary_statistics(self):
        """
        Display summary statistics
        """
        print("\nSummary Statistics:")
        print(self.df.describe())

    def count_categories(self):
        """
        Count unique categories
        """
        print("\nCategory Counts:")
        print("Product Categories:", self.df['Product_Category'].nunique())


    def profit_by_category(self):
        """ 
        Find most and least profitable product category
        """
        print("\nProfit by Category:")

        profit_data = self.df.groupby('Product_Category')['Profit'].sum()
        print(profit_data)

        most_profitable = profit_data.idxmax()
        least_profitable = profit_data.idxmin()

        print(f"\nMost Profitable Category: {most_profitable}")
        print(f"Least Profitable Category: {least_profitable}")

    def profit_margin(self):
        """
        Calculate profit margin per row
        """
        print("\nProfit Margin:")
        self.df['Profit_Margin'] = self.df['Profit'] / self.df['Revenue']
        print(self.df[['Product_Category', 'Profit_Margin']])

    def sub_category_analysis(self):
        """
        Analyze total Revenue and Profit per Product Category, optionally by Gender
        """
        print("\nSub-Category Analysis:")

        grouped = self.df.groupby(['Product_Category', 'Gender']).agg({
            'Revenue': 'sum',
            'Profit': 'sum'
        }).reset_index()

        print(grouped)