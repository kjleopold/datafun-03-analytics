"""
Process a CSV file to calculate what artist and track had the most streams on Spotify in 2023. 
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
import pandas as pd
from collections import Counter

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "kleopold_data"
processed_folder_name: str = "test_data_processed"

#####################################
# Define Functions
#####################################

def analyze_spotify_data(file_path: pathlib.Path) -> dict:
    """Analyze the artist, track, and stream columns from Spotify data to calculate what track was the most played in 2023."""
    try:
        # Initialize an empty list to store artist names, track names, and number of streams.
        artist_list = []
        track_list = []
        stream_list = []

        # Open the file for reading
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  #Read the CSV as a dictionary
            for row in dict_reader:
                try:
                    artist = str(row["artist(s)_name"])  # Extract artist name
                    track = str(row["track_name"]) # Extract track name
                    streams = int(row["streams"]) # Convert the streams to integer

                    # Append the artist, track, and streams to their respective lists
                    artist_list.append(artist)
                    track_list.append((track, artist, streams)) # Store track name, artist name, and stream count
                    stream_list.append(streams)

                except KeyError as e:
                    logger.warning(f"Skipping row due to missing key: {row} ({e})")
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Find the most streamed track (the track with the highest number of streams)
        most_streamed_track = max(track_list, key=lambda x: x[2])  # Find the track with the highest streams

        # Count the occurrences of each artist using Counter
        artist_counter = Counter(artist_list)

        # Find the most streamed artist (the one with the most occurrences)
        most_streamed_artist = artist_counter.most_common(1)[0]

        # Return a dictionary with the results
        return { 
            "most_streamed_track": {"track": most_streamed_track[0], "streams": most_streamed_track[2], "artist": most_streamed_track[1]},
            "most_streamed_artist": {"artist": most_streamed_artist[0], "appearance": most_streamed_artist[1]}
        }
  
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {"most_stremed_track":{}, "most_streamed_artist": {}}

def process_csv_file():
    """Read a CSV file, analyze artist and track data, and save the results."""
    input_file = pathlib.Path(fetched_folder_name, "spotify_data.csv")
    output_file = pathlib.Path(processed_folder_name, "spotify_data_2023.txt")
    
    stats = analyze_spotify_data(input_file)

    if not stats or 'most_streamed_track' not in stats or 'most_streamed_artist' not in stats: 
        logger.error("No statistics to write. Skipping file output.")
        return
    
    # Ensure the output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Save the results to a text file
    with output_file.open('w') as file:
        file.write("Spotify Streaming Analysis (2023):\n")

        track_data = stats.get('most_streamed_track',{})
        
        file.write(f"Most Streamed Track: {stats['most_streamed_track']['track']} by {track_data['artist']}\n"),
        file.write(f"Most Streamed Artist: {stats['most_streamed_artist']['artist']}\n"),
    
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")
