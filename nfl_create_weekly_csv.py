import nfl_data_py as nfl
import pandas as pd 

def create_nfl_weekly_csv(start_year: int, end_year: int, output_file: str) -> None:
    """
    Creates a CSV file containing all the NFL boxscore stats from start_year to end_year.

    Args:
        start_year (int): start year for the data pulled from nfl_data_py
        end_year (int): end year for the data pulled from nfl_data_py
        output_file (str): path to the output CSV file
    """
    # Fetch NFL boxscore data for the specified years
    nfl_data = nfl.import_weekly_data(years=list(range(start_year, end_year + 1)))
    
    # Save the data to a CSV file
    nfl_data.to_csv(output_file, index=False)
    
if __name__ == "__main__":
    for i in range(2000, 2025):
        create_nfl_weekly_csv(i, i, f"nfl_boxscore_stats_{i}.csv")
    # create_nfl_csv(2000, 2024, "nfl_boxscore_stats_2000_2023.csv")
    """
    This will create a CSV file named 'nfl_boxscore_stats_xxxx.csv' for each year from 2000 to 2024,
    containing all the NFL boxscore stats for that year.
    """

