# PROJECT 2:  DISASTER RESPONSE PIPELINE PROJECT

This project will use a machine learning pipeline to categorize emergency messages.  The data comes from Figure Eight, which we will use to build our model for the emergency messages API.

## Required Files:

- Jupyter Notebook
  - ETL Pipeline Preparation.ipynb:  Required for the process_data.py python script (see file details below under Data section)
  - ML Pipeline Preparation.ipynb:  Required for the train_classifier.py python script (see file details below under Models section)

- Data
  - process_data.py:  This Python script shall read in the input data from the required CSV files, clean the data in the files, and store the cleaned data in an SQLite database
  - disaster_categories.csv:  Required CSV file
  - disaster_messages.csv:  Required CSV file
  - DisasterResponse.db:  The SQLite database created from process_data.py that shall store the cleaned data

- Models
  - train_classifier.py:  This Python script shall load the data from the DisasterResponse.db database and call the downstream system GridSearchCV to run and train the machine learning model.  The model shall be saved in a Pickle file.
  - classifier.pkl:  The saved model stored in a pickle file (not available due to file size limitations in Github; max file size allowed in Github is 40 MB.  The pickle file exceeded over 100 MB)

- App
  - run.py:  This Python script is the Flask file that shall run the app on any web broswer (e.g. Firefox, Microsoft Edge, Google Chrome, etc.  For this project, the Flask app was run on Google Chrome).  In the IDE terminal, the user will be directed to /home/workspace; this directory must be changed to /home/workspace/app via a "cd app" command, to access and run the run.py file.
  - templates folder:  Contains the HTML template files.
    - master.html:  Main page of the emergency messages API, or web app
    - go.html:  Classification result page of web app
  - A second terminal browser shall be opened and the following commands executed on the terminal screen:  env|grep WORK.  No change to the app directory necessary.  The user shall see the parameters for both SPACEID and SPACEDOMAIN.  SPACEID is automatically generated; SPACEDOMAIN is:  udacity-student-workspaces.com
  - To see the Flask app in action, the user shall type the following in the browser URL:  http://[SPACE-ID]-3001.SPACEDOMAIN (example:  http://view6914b2f4-3001.udacity-student-workspaces.com/).  Do not access the URL http://0.0.0.0:3001/ generated from the first terminal screen.


## Screenshots:

Main application interface:
![Screenshot 1 - Main Interface 01](https://user-images.githubusercontent.com/39567971/116820035-f4e77c00-ab40-11eb-864b-1fb1a2a6b351.png)

Overview of Training Dataset:
![Screenshot 2 - Genre Interface 01](https://user-images.githubusercontent.com/39567971/116820036-f4e77c00-ab40-11eb-9232-e340f3141fcd.png)

Analyzing message data for disaster response:
![Screenshot 3 - Message 01](https://user-images.githubusercontent.com/39567971/116820038-f4e77c00-ab40-11eb-88c3-11ab03f3432e.png)

Results:
![Screenshot 4 - Results 01](https://user-images.githubusercontent.com/39567971/116820039-f4e77c00-ab40-11eb-953a-d1204be62809.png)


## About

This project was prepared as part of the Udacity Data Scientist nanodegree program.  Data provided by Figure Eight.
