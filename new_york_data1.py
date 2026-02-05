import pandas as pd
def load_new_york_data(file_path):
    """
    Load New York City data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing New York City data.

    Returns:
    pd.DataFrame: A DataFrame containing the New York City data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error parsing the file.")
        return None
    data = pd.read_csv("datasets.csv")
    data.head()