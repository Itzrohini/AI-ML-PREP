import pandas as pd

class Preprocessor:
    """
    Class for data preprocessing
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def check_nulls(self):
        print("\nNull Values:")
        print(self.df.isnull().sum())

    def check_dtypes(self):
        print("\nData Types:")
        print(self.df.dtypes)

    def save_data(self, path: str):
        """
        Save dataframe as pickle file
        """
        self.df.to_pickle(path)
        print(f"\nData saved to {path}")