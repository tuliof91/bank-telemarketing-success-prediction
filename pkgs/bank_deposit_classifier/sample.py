# from ast import Call
from collections import Counter
import math
import yaml

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder



def print_hi():
    return print('hi baby')


class DataPrep:
    def __init__(self, features=None, categorical_features=None, encoder=None):
        #self._outcome = outcome
        self._features=features
        self._categorical_features=categorical_features
        self._encoder=encoder
        
    def get_data(self, path, sep=','):        
        # self.df = pd.read_csv(path, sep)
        #if self._features:
            #self.df = self.df[self._features]
        #else:
            #self.df = pd.read_csv(path, sep)
            
        self.data = pd.read_csv(path, sep)
        print(f'Data read from {path}')
    
    def standardize_columns(self, dataframe):
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
            
        self.data = dataframe
        # return dataframe
    
    def split_feature_target(self, dataframe):
    
        self.target = dataframe.y
        self.features_df = dataframe.drop('y', axis='columns')
        
        #return target, features
    
    def split_column_dtypes(self, dataframe):
        self.categorical = list(dataframe.select_dtypes(include='object'))
        self.numerical = list(dataframe.select_dtypes(exclude='object'))
        
        # return self.categorical, self.numerical
    
    def clean_categorical_columns(self, dataframe, columns):
        for column in columns:
            dataframe[column] = dataframe[column].str.lower().str.replace(' ', '_') \
                .str.replace('.', '_')
        
        self.data = dataframe
        # return dataframe
    
    def traintestsplit(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True, stratify=self.target)
        self.train_df = pd.concat([X_train, y_train], axis='columns')
        self.test_df = pd.concat([X_test, y_test], axis='columns')
        
        # return train_df, test_df
    
    def save_data(self, data, filename):
        data.to_csv(f'./data/input/{filename}.csv', index=False)
        
    def drop_columns(self, dataframe, columns):
        
        for column in columns:
            dataframe.drop(column, inplace=True, axis='columns')
        
        self.data = dataframe
        # return dataframe
    
    def encode_train_data(self, dataframe):
        
        self.train_dict = self.data[self.categorical + self.numerical].to_dict(orient='records')
        self.encoder = DictVectorizer(sparse=False)
        self.encoder.fit(self.train_dict)
        self.X_train = self.encoder.transform(self.train_dict)
        
    # def transform_data(self, dictionary):
        # self.X_train = dv.transform(dictionary)
        
        # return X_train
        
    @classmethod
    def from_yaml(cls, filename):
        path = './config/' + f'{filename}'
        with open(path, 'r') as file:
            params = yaml.load(file, Loader=yaml.FullLoader)
        return cls(**params)



# <codecell>
# def oversample_minority_class(data, outcome, p_minority):
#     '''
#     Function used to oversample the minority class.

#     Parameters
#     ----------
#     data = pandas dataframe
#         dataframe to be resampled
#     outcome: str
#         name of the outcome column
#     p_minority: float
#         propotyion of the rows that we want the minority class
#         to make up after we are done resampling.
#     '''
#     # Define functions

#     def check_p_minority_bounds(p_minority, p_minority_pre):
#         '''
#         Checks if p_minority is between 0 and 1
        
#         Parameters
#         ----------
#         p_minority: float
#         p_minority_pre:
#         '''
#         if (p_minority > 1) or (p_minority < p_minority_pre):
#             msg = f'Proportion out of bounds ! p_minority must be between 0 and 1, but value passed was {p_minority}.'
#             raise ValueError(msg)

#     def check_outcome_binary(data, outcome):
#         '''
#         checks if the outcome has 2 and only 2 categories

#         Parameters:
#         ----------
#         data: pandas dataframe
#         outcome: str
#             name of the outcome column in the dataset
#         '''
#         outcome_counts = Counter(data[outcome])
#         n_outcomes = len(outcome_counts.keys())
#         if (n_outcomes != 2):
#             msg = f'Binary outcome expected but specified outcome has {n_outcomes} classes'
#             raise ValueError(msg)

#     # Call functions
#     # check_p_minority_bounds(p_minority)
#     check_outcome_binary(data,outcome)

#     # Oversample data
#     outcome_counts = Counter(data[outcome])
#     majority_class, majority_count = outcome_counts.most_common()[0]
#     minority_class, minority_count = outcome_counts.most_common()[-1]
#     p_minority_pre = minority_count / data.shape[0]
#     desired_total_count = math.ceil(majority_count/(1-p_minority))
#     check_p_minority_bounds(p_minority, p_minority_pre)
#     n_samples = desired_total_count - majority_count - minority_count
#     samples = data.loc[data[outcome] == minority_class].sample(n_samples, replace=True)
#     oversampled_data = pd.concat([data, samples])
#     return oversampled_data

