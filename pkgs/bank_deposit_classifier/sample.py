# from ast import Call
from collections import Counter
import math
import pandas as pd

def print_hi():
    return print('hi baby')

def oversample_minority_class(data, outcome, p_minority):
    '''
    Function used to oversample the minority class.

    Parameters
    ----------
    data = pandas dataframe
        dataframe to be resampled
    outcome: str
        name of the outcome column
    p_minority: float
        propotyion of the rows that we want the minority class
        to make up after we are done resampling.
    '''
    # Define functions

    def check_p_minority_bounds(p_minority, p_minority_pre):
        '''
        Checks if p_minority is between 0 and 1
        
        Parameters
        ----------
        p_minority: float
        p_minority_pre:
        '''
        if (p_minority > 1) or (p_minority < p_minority_pre):
            msg = f'Proportion out of bounds ! p_minority must be between 0 and 1, but value passed was {p_minority}.'
            raise ValueError(msg)

    def check_outcome_binary(data, outcome):
        '''
        checks if the outcome has 2 and only 2 categories

        Parameters:
        ----------
        data: pandas dataframe
        outcome: str
            name of the outcome column in the dataset
        '''
        outcome_counts = Counter(data[outcome])
        n_outcomes = len(outcome_counts.keys())
        if (n_outcomes != 2):
            msg = f'Binary outcome expected but specified outcome has {n_outcomes} classes'
            raise ValueError(msg)

    # Call functions
    # check_p_minority_bounds(p_minority)
    check_outcome_binary(data,outcome)

    # Oversample data
    outcome_counts = Counter(data[outcome])
    majority_class, majority_count = outcome_counts.most_common()[0]
    minority_class, minority_count = outcome_counts.most_common()[-1]
    p_minority_pre = minority_count / data.shape[0]
    desired_total_count = math.ceil(majority_count/(1-p_minority))
    check_p_minority_bounds(p_minority, p_minority_pre)
    n_samples = desired_total_count - majority_count - minority_count
    samples = data.loc[data[outcome] == minority_class].sample(n_samples, replace=True)
    oversampled_data = pd.concat([data, samples])
    return oversampled_data