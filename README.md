# PROJECT 2:  DISASTER RESPONSE PIPELINE PROJECT

This project will use a machine learning pipeline to categorize emergency messages.  The data comes from Figure Eight, which we will use to build our model for the emergency messages API.

## Required Files:
- Data
  - process_data.py:  This Python script shall read in the input data from the required CSV files, clean the data in the files, and store the cleaned data in an SQLite database.
  - disaster_categories.csv, disaster_messages.csv:  The required CSV files
  - DisasterResponse.db:  The SQLite database created from process_data.py 
- Models
  - train_classifier.py:  This Python script shall load the data from the DisasterResponse.db database and call the downstream system GridSearchCV to run and train the machine learning model.  The model shall be saved in a Pickle file.
  - classifier.pkl:  The pickle file (not available due to file size limitations in Github; the file exceeded over 100 MB)
- App
  - run.py:  This Python script is the main script that shall run the web app on any web broswer.  In the IDE terminal, the user will be directed to /home/workspace; this directory must be changed to /home/workspace/app via a "cd app" command, to access and run the run.py file.
  - templates folder:  Contains the HTML template files (these files must not be modified)

## Screenshots:

Main Interface
![Alt text](https://github.com/mhuda040/PROJECT-2---Disaster-Response-Pipeline/blob/main/Screenshot%201%20-%20Main%20Interface%2001.png?raw=true "Screenshot 1")

Genre Interface displaying the training dataset and the appropriate categories
![Alt text](https://github.com/mhuda040/PROJECT-2---Disaster-Response-Pipeline/blob/main/Screenshot%202%20-%20Genre%20Interface%2001.png?raw=true "Screenshot 2")

Analyze Message Interface that takes the user input
![Alt text](https://github.com/mhuda040/PROJECT-2---Disaster-Response-Pipeline/blob/main/Screenshot%203%20-%20Message%2001.png?raw=true "Screenshot 3")

Analyze Message Interface that displays the results
![Alt text](https://github.com/mhuda040/PROJECT-2---Disaster-Response-Pipeline/blob/main/Screenshot%204%20-%20Results%2001.png?raw=true "Screenshot 4")

