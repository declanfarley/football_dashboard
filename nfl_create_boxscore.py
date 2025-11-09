import pandas as pd 
import os

def create_weekly_boxscore_csv(year: int, week: int, output_file: str) -> None:
    """Creates a CSV file containing the NFL boxscore data for a specific game. 
    This will process a week at a time, a single run will result in the creation of many CSV files, one for each game within the week.

    Args:
        year (int): year for which the data represents
        week (int): week for which the data represents of the provided year
        output_file (str): file name for the output CSV file, root of the overall file name, extra will be game_id
    """
    # using pbp data here instead of weekly since weekly does not include kicking stats 
    data_dir = "data/pbp_data"
    csv_file = f"nfl_pbp_{year}.csv"
    # fetch the appropriate yearly data from our own CSV files
    yearly_data = pd.read_csv(os.path.join(data_dir, csv_file))
    # filter the data for the specified week
    weekly_data = yearly_data[yearly_data['week'] == week]
    # now we are going to create the boxscore stats for the overall team based off the play by play data
    # group by team and aggregate relevant statistics
    boxscore_stats = {
        'passing_yards': 'sum',
        'rushing_yards': 'sum',
        'receiving_yards': 'sum',
        'touchdown': 'sum',
        'interception': 'sum',
        'fumble_lost': 'sum',
        'field_goal_result': 'sum',
        'field_goal_attempt': 'sum',
        'extra_point_result': 'sum',
        'extra_point_attempt': 'sum'
    }
    weekly_data = weekly_data.groupby(['home_team', 'away_team']).agg(boxscore_stats).reset_index()
    # save the weekly boxscore data to a CSV file
    weekly_data.to_csv(output_file, index=False)
    
    print(weekly_data.head())   
    
if __name__ == "__main__":
    
    """
    This will create a CSV file named 'nfl_boxscore_xxxx_week_yy.csv' for each week from 1 to 18
    for each year from 2000 to 2024, containing all the NFL boxscore data for that week.
    """
    output_filename = "nfl_boxscore_sample.csv"
    create_weekly_boxscore_csv(2023, 1, output_filename)
    # for year in range(2000, 2025):
    #     for week in range(1, 19):
    #         if year < 2021 and week > 17:
    #             continue  # Skip weeks beyond 17 for years before 2021
    #         output_filename = f"nfl_boxscore_{year}_{week}.csv"
    #         create_weekly_boxscore_csv(year, week, output_filename)
    #         break
    #     break