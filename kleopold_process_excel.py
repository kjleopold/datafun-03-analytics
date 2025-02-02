"""
Process an Excel file to calculate the min, max, and average earnings of a data set.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import statistics
import pandas as pd


# Import from external packages
import openpyxl

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

def box_office_data(file_path: pathlib.Path) -> int:
    """Analyze the Gross column to calculate min, max, and average earnings."""
    try:
        # Load the workbook and select the first sheet
        workbook = openpyxl.load_workbook(file_path, data_only=True)
        sheet = workbook.active 

        # Find column indices for "Movie" and "Gross"
        headers = {cell.value: idx for idx, cell in enumerate(sheet[1])}

        if "Gross" not in headers or "Movie" not in headers:
                logger.error ("Headers not found.")
                return {}
        
        gross_col = headers["Gross"]
        movie_col = headers["Movie"]

        # Initialize an empty list to store the scores
        earnings_list = []
        movie_list = []

        # Skip headers
        for row in sheet.iter_rows(min_row=2, values_only=True):
            try:
                movie = str(row[movie_col]).strip() if row[movie_col] else "Unkown"  # Extract gross earnings
                amount = float(row[gross_col]) if row[gross_col] else 0  # Extract movie titles

                # Append the gross earnings and movie titles to their respective lists
                earnings_list.append(amount)
                movie_list.append((amount, movie))

            except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")

        # Ensure the data is valid
        if not earnings_list:
             logger.warning("No valid earnings data found.")
             return {}

        # Find the highest and lowest grossing movies
        highest_grossing_movie = max(movie_list, key=lambda x: x[0])  # Sort by earnings
        lowest_grossing_movie = min(movie_list, key=lambda x: x[0])  # Sort by earnings

        # Calculate statistics
        stats = {
            "highest_grossing_movie": {"movie": highest_grossing_movie[1], "earnings": highest_grossing_movie[0]},
            "lowest_grossing_movie": {"movie": lowest_grossing_movie[1], "earnings": lowest_grossing_movie[0]},
            "min": min(earnings_list),
            "max": max(earnings_list),
            "average": round(statistics.mean(earnings_list), 2)
        }

        return stats
    
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}
    

def process_csv_file():
    """Read a Excel file, analyze box office data, and save the results."""
    input_file = pathlib.Path(fetched_folder_name, "box_office_data.xlsx")
    output_file = pathlib.Path(processed_folder_name, "box_office_gross_earnings.txt")
    
    stats = box_office_data(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Box Office Statistics:\n")
        file.write(f"Highest Grossing Movie: {stats['highest_grossing_movie']['movie']} with earnings of {stats['max']:,.2f}\n")
        file.write(f"Lowest Grossing Movie: {stats['lowest_grossing_movie']['movie']} with earnings of {stats['min']:,.2f}\n")
        file.write(f"Average Box Office Earnings: {stats['average']:,.2f}\n")
    
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")