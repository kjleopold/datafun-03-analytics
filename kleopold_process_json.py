"""
Process a JSON file to count the NFL team that has won the most the Super Bowls and 
made the most appearances, and then average the point spread across all games.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json
import statistics
import pandas as pd

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "kleopold_data"
processed_folder_name: str = "kleopold_data_processed"

#####################################
# Define Functions
#####################################

def analyze_super_bowl_data(file_path: pathlib.Path) -> dict:
    """Analyze Super Bowl data to determine:
        - The team with me most wins and how many
        - The team with the most appearances and how many
        - The average point spread across all games
    """
    try:
        with file_path.open('r', encoding='utf-8') as file:
            data = json.load(file)  # Load JSON data

        # Initialize dictionaries
        winning_team = {}  # Dictionary
        most_bowls = {}  # Dictionary
        point_spreads = []  # List

        for game in data:
            winner = game["Winning team"]
            loser = game["Losing team"]
            winning_score = game["Winning Team Points"]
            losing_score = game["Losing Team Points"]

            # Calculate the spread manually
            spread = winning_score - losing_score
            point_spreads.append(spread)

            # Count wins
            winning_team[winner] = winning_team.get(winner, 0) + 1

            # Count appearances (using both winner and loser)
            most_bowls[winner] = most_bowls.get(winner, 0) + 1
            most_bowls[loser] = most_bowls.get(loser, 0) + 1
            
        # Determine the team with the most wins
        most_wins_team = max(winning_team, key=winning_team.get)
        most_wins_count = winning_team[most_wins_team]
        
        # Determine the team with the most appearances
        most_appearances_team = max(most_bowls, key=most_bowls.get)
        most_appearances_count = most_bowls[most_appearances_team]
        
        # Calculate average point spread
        avg_point_spread = round(statistics.mean(point_spreads))
        
        # Return analysis as dictionary
        return {
            "most_wins": {"team": most_wins_team, "wins": most_wins_count},
            "most_appearances": {"team": most_appearances_team, "appearances": most_appearances_count},
            "average_point_spread": {"average_point_spread": avg_point_spread}
            }

    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count wins and appearances, calculate average spread, and save the result."""
    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, "super_bowl.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, "super_bowl_analysis.txt")
    
    stats = analyze_super_bowl_data(input_file)  # Get analysis results
    win_count = stats.get('most_wins',{})  # Get win count from stats
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Super Bowl Analysis:\n")

        file.write(f"Most Super Bowl Wins: {stats['most_wins']['team']} with {win_count['wins']}\n"),
        file.write(f"Most Super Bowl Appearances: {stats['most_appearances']['team']} with {stats['most_appearances']['appearances']} appearances.\n"),
        file.write(f"Average Point Spread: {stats['average_point_spread']['average_point_spread']} points.\n"),
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")
