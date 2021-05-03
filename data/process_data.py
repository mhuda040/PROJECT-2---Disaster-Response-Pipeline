import sys
import pandas as pd
import numpy as np
import re
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    
    '''
    Loads data sets from the following *.csv files:
    - disaster_categories.csv
    - disaster_messages.csv
    and merges them into one dataframe.
    
    Input:  messages_filepath, categories_filepath
    Output:  The merged dataframe df    
    '''
    messages_df = pd.read_csv(messages_filepath)
    categories_df = pd.read_csv(categories_filepath)
    df = pd.merge(messages_df, categories_df, on="id", how='inner')
    return df


def clean_data(df):
    
    '''
    This function will take the newly created
    datafrme from load_data and clean it.
    
    '''

    #Create a dataframe of individual columns using ';' as the delimiter
    categories = df['categories'].str.split(';', expand = True)
    row = categories.iloc[0].str.split('-', expand = True)
    categories.columns = list(row[0])

    # iterate through the category columns in the dataframe to keep
    # only the last character of the string 
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str.split('-').str.get(-1)
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
        #set numerical values other than 0 and 1 as 1 by default
        for n, i in enumerate(categories[column]):
            if i > 1:
                categories[column][n] = 1


    #Drop duplicate entries
    df.drop(['categories'], axis = 1, inplace = True)
    df = pd.concat([df, categories], axis=1, join="inner").drop_duplicates()

    return df


def save_data(df, database_filename):
    
    '''
    Save the cleaned dataframe in an SQLite database
    '''
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('disaster_messages', engine, index=False, if_exists = 'replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()