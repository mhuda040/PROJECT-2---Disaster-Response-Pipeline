# PROJECT 2:  DISASTER RESPONSE PIPELINE PROJECT

This project will use a machine learning pipeline to categorize emergency messages.  The data comes from Figure Eight, which we will use to build our model for the emergency messages API.

## Required Files:
- App
  - run.py:  This Python script is the Flask file that shall run the app on any web broswer (e.g. Firefox, Microsoft Edge, Google Chrome, etc.  For this project, the Flask app was run on Google Chrome).  In the IDE terminal, the user will be directed to /home/workspace; this directory must be changed to /home/workspace/app via a "cd app" command, to access and run the run.py file.
  - templates folder:  Contains the HTML template files
    - master.html is the main page of the emergency messages API, or web app.  go.html is the classification result page of web app.  These HTML files must not be modified.
  - A second terminal browser shall be opened and the following commands executed on the terminal screen:  env|grep WORK.  The user shall see the parameters for both SPACEID and SPACEDOMAIN.  SPACEID is automatically generated; SPACEDOMAIN is:  udacity-student-workspaces.com
  - To see the Flask app in action, the user shall type the following in the browser URL:  http://[SPACE-ID]-3001.SPACEDOMAIN (example:  http://viewa4a5284b-3001.udacity-student-workspaces.com/)

- Data
  - process_data.py:  This Python script shall read in the input data from the required CSV files, clean the data in the files, and store the cleaned data in an SQLite database
  - disaster_categories.csv:  Required CSV file
  - disaster_messages.csv:  Required CSV file
  - DisasterResponse.db:  The SQLite database created from process_data.py that shall store the cleaned data

- Models
  - train_classifier.py:  This Python script shall load the data from the DisasterResponse.db database and call the downstream system GridSearchCV to run and train the machine learning model.  The model shall be saved in a Pickle file.
  - classifier.pkl:  The saved model stored in a pickle file (not available due to file size limitations in Github; max file size allowed in Github is 40 MB.  The pickle file exceeded over 100 MB)


## Screenshots:

Main Interface
![Alt text](https://github.com/mhuda040/PROJECT-2---Disaster-Response-Pipeline/blob/main/Screenshot%201%20-%20Main%20Interface%2001.png?raw=true "Screenshot 1")

Genre Interface displaying the training dataset and the appropriate categories
![Alt text](https://github.com/mhuda040/PROJECT-2---Disaster-Response-Pipeline/blob/main/Screenshot%202%20-%20Genre%20Interface%2001.png?raw=true "Screenshot 2")

Analyze Message Interface that takes the user input
![Alt text](https://github.com/mhuda040/PROJECT-2---Disaster-Response-Pipeline/blob/main/Screenshot%203%20-%20Message%2001.png?raw=true "Screenshot 3")

Analyze Message Interface that displays the results
![Alt text](https://github.com/mhuda040/PROJECT-2---Disaster-Response-Pipeline/blob/main/Screenshot%204%20-%20Results%2001.png?raw=true "Screenshot 4")

