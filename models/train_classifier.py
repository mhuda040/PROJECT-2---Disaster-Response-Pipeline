import sys
import nltk
import warnings
warnings.filterwarnings('ignore')  # "error", "ignore", "always", "default", "module" or "once"

nltk.download('punkt')
nltk.download('wordnet')

import pandas as pd
import numpy as np
import re
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import confusion_matrix
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import GridSearchCV
import pickle


def load_data(database_filepath):
    
    '''
    Loads data from SQLite database created from process_data.py
    
    Input: Filepath of SQLite database
    Output:
    - X:  Features
    - Y:  Target
    '''
    
    engine = create_engine('sqlite:///'+ database_filepath)
    df = pd.read_sql("SELECT * FROM disaster_messages", engine)

    X = df['message']
    Y = df.iloc[:,4:]
    category_names = Y.columns.values
    
    return  X, Y, category_names


def tokenize(text):
    '''
    Tokenizes and lemmatizes text.
    
    Input:  Text to be tokenized
    Output:  Cleaned tokens
    '''

    # Remove punctuation
    text = re.sub(r'[^a-zA-Z0-9]', ' ',text)
    
    # Tokenize text
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    # Iterate through each token, lemmatize text
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok, pos='n').strip()
        clean_tok = lemmatizer.lemmatize(clean_tok, pos='v')
        
        clean_tokens.append(clean_tok)
    
    
    return clean_tokens


def build_model():
    '''
    Function to build our model using GridSearchCV
    
    Input:  None
    Output:  ML Model
    '''

    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])


    parameters = {'tfidf__norm': ['l1','l2'],
              'clf__estimator__criterion': ["gini", "entropy"]    
             }
    
    cv = GridSearchCV(pipeline, param_grid=parameters)

    return cv





def evaluate_model(model, X_test, Y_test, category_names):
    
    '''
    Cleaning The Data And Tokenizing Text. 
  
    Parameters:
    model:  Classified ML Model
    X_test:  Test Dataset
    Y_test:  Labels Dataset
    category_names:  Category Names List
    '''

    Y_pred = model.predict(X_test)
    report= classification_report(Y_pred,Y_test, target_names=category_names)


    temp=[]
    for item in report.split("\n"):
        temp.append(item.strip().split('     '))
    clean_list=[ele for ele in temp if ele != ['']]
    report_df=pd.DataFrame(clean_list[1:],columns=['group','precision','recall', 'f1-score','support'])


    return report
    




def save_model(model, model_filepath):
    
    '''
    Saving our model as a pickle file
    
    Input:  Trained ML Model
    Output:  Destination .pkl file
    '''

    with open(model_filepath, 'wb') as file:
        pickle.dump(model, file)



def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()