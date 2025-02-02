# datafun-03-analytics
Module 3 Assignments

Follow the below outline for beginning a new project:  
*Note: steps in project initialization only need performed once per project*

## Start with project initialization:
1. EITHER Create a new repository from Scratch or Copy an Existing Project

2. ALWAYS use Git to clone the new repository to local machine
    * git clone https://github.com/kjleopold/datafun-03-analytics

3. IF starting from scratch only: Add files such as .gitignore and requirements.txt
    * Create new files in the root project folder

4. IF starting from scratch only: Use Git to add, commit, and push new files to GitHub
    * `git add .`
    * `git commit -m "Add meaningful comment"`
    * `git push -u origin main`  
    *After subsequent changes, may be able to use `git push`*

5. ALWAYS Create a local Python Virtual Environment for the project
    * Run `py -m venv .venv` from the project root directory

## Continue with the repeatable project work flow:
1. Pull the latest changes from GitHub
    * `git pull origin main`

2. Activate the Project Virtual Environment
    * `.venv\Scripts\activate`
    * Confirm activation by checking that the terminal shows the environment name (e.g.,  (venv))

3. Install dependencies as needed
    * Ensure .venv is active
    * Update key packages
    * Install dependencies from the requirements.txt file
    * `py -m pip install --upgrade pip setuptools wheel`
    * `py -m pip install -r requirements.txt`

4. Run Scripts.
    * Open the Command Palette: Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (Mac).
    * Search for "Python: Select Interpreter":
    * Type Python: Select Interpreter in the Command Palette search bar and select it from the dropdown
    * Choose an Interpreter - A list of available Python environments will appear. Look for the local .venv option
    * Once selected, check the Python version displayed in the bottom-left corner of the VS Code window in the status bar
    * Make sure Autosave is on
    * Activate/Execute with `py myfile.py` (change the name of the file to the actual file name and it must exist in the root project folder)

5. Modify code and test functionality
    * Do not git add-commit-push if code doesn't run

6. Save work with git add-commit-push frequently to commit small sets of well-labeled changes to the repo (see step 4 under project initialization section)

Run through this repeatable workflow as the project develops. 

## P3: Working With Data Workflow

### 1. Set up the project as data-03-analytics in GitHub

### 2. Installed required packages via requirements.txt
* pip
* loguru
* requests
* openpyxl
* pandas

### 3. Copied example data and process files from example repo

### 4. Read, reviewed, and ran each example script

### 5. Searched for files on the web in CSV, Excel, JSON, and text format

### 6. Created, ran, and git add-commit-pushed data fetchers 
- **`kleopold_get_csv.py`**  
Fetches a CSV file with Spotify streaming data for 2023  
- **`kleopold_get_excel.py`**  
Fetches an excel file with movie titles and their box office earnings data  
- **`kleopold_get_json.py`**  
Fetches a JSON file with Super Bowl data from 1967 to 2024  
- **`kleopold_get_txt.py`**  
Fetches a text file with the full script for the Broadway Musical Wicked

### 7. Created and ran data processors
- **`kleopold_process_csv.py`**  
The script returns the most streamed track and artist  
- **`kleopold_process_excel.py`**  
The script returns the movie title and amount of the max and min box office earnings and the average earnings over all  
- **`kleopold_process_json.py`**  
The script returns the highest scoring Super Bowl, the team that has made the most appearances, and the average point spread  
- **`kleopold_process_txt.py`**  
The script returns how many times the word "Oz" occurs in the play  

### Fetchers:
py kleopold_get_csv.py  
py kleopold_get_excel.py  
py kleopold_get_json.py  
py kleopold_get_txt.py  

### Processors:
py kleopold_process_csv.py  
py kleopold_process_excel.py  
py kleopold_process_json.py  
py kleopold_process_txt.py  

### 8. Saved work with git add-commit-push frequently

### 9. Updated README.md to Describe Work

