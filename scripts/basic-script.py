# Imports
import os
# from pathlib import path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder


# <codecell> Read data
def get_data(path, sep=','):        
    df = pd.read_csv(path, sep)
    return df

# <codecell> preprocess
def standardize_columns(dataframe):
    '''
    Transform columns names into lowercaseseparated with underscores

    Parameters
    ----------
    dataframe : pandas dataframe

    Returns
    -------
    dataframe: pandas dataframe

    '''
    dataframe.columns = dataframe.columns.str.lower() \
        .str.replace(' ', '_').str.replace('.', '_')
        
    return dataframe

def split_feature_target(dataframe):

    target = dataframe.y
    features = dataframe.drop('y', axis='columns')
    return target, features

def split_column_dtypes(dataframe):
    categorical = list(dataframe.select_dtypes(include='object'))
    numerical = list(dataframe.select_dtypes(exclude='object'))
    
    return categorical, numerical

# <codecell>

def clean_categorical_columns(dataframe, columns):
    for column in columns:
        dataframe[column] = dataframe[column].str.lower().str.replace(' ', '_') \
            .str.replace('.', '_')
            
    return dataframe

# <codecell> split
def traintestsplit(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True, stratify=target)
    train_df = pd.concat([X_train, y_train], axis='columns')
    test_df = pd.concat([X_test, y_test], axis='columns')
    
    return train_df, test_df
# <codecell>
def save_data(data, filename):
    data.to_csv(f'./data/input/{filename}.csv', index=False)
# <codecell>
def drop_columns(dataframe, columns):
    
    for column in columns:
        df.drop(column, inplace=True, axis='columns')
    
    return dataframe

# <codecell>
def encode_data(data):
    
    train_dict = data[categorical + numerical].to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    dv.fit(train_dict)
    X_train = dv.transform(train_dict)
    
    return X_train

# <codecell>

df = get_data('../data/input/bank-additional-full.csv', ';')
standardize_columns(df)
target, features = split_feature_target(df)
categorical, numerical = split_column_dtypes(features)
clean_categorical_columns(df, categorical)

# <codecell>
train_df, test_df = traintestsplit(df[categorical+numerical], df['y'])

# <codecell>
save_data(train_df, 'train_df')
save_data(test_df, 'test_df')

# <codecell>
get_data('./data/input/train_df.csv')
X_train = encode_data(train_df.drop('y', axis='columns'))

