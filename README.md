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

###P3: Working With Data Workflow
1. Set up the project
    * Set up repo datafun-03-analytics in GitHub
    * Cloned repo down to my machine
    * Opened folder in VS Code
    * Added .gitignore file
    * Added requirements.txt
    * Installed required packages via requirements.txt

2. Run the Examples
    * Copied example data and process files from example repo
    * Read, reviewed, and ran each example script

3. Create and run my own data fetchers
    * Searched for files on the web for CSV, Excel, JSON, and text and saved to my machine
    * Set up new repo, test_datasets, to house data files in order to easily retrieve URLs
    * Added files to test_datasets via git add-commit-push
    * Set up scripts to fetch data from test_datasets
    * Fetched data for each file type
    * Git add-commit-push between each fetch

