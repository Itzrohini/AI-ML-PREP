import pandas as pd
class DataLoader:
    """
    Class to load data from different sources
    """

    def __init__(self, file_path: str):
        """
        Initialize with the file path
        """
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        """
        Load Excel data into pandas DataFrame
        """
        try:
            df = pd.read_excel(self.file_path)
            print("Data loaded successfully")
            return df
        except Exception as e:
            print(f"Error loading data: {e}")        
            return None
       
       # Used OOPS (CLASS)
       # used constructor (__init__)
       # used exception handling (try-except)
       #used type hinting (-> pd.DataFrame)mport pandas as pd
 