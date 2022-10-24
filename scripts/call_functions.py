#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:03:16 2022

@author: tulio
"""
# <codecell> imports

# import os
import bank_deposit_classifier.sample as s
s.print_hi()

# <codecell>
config_path = 'data_prep.yaml'
input_path = './data/input/bank-aditional-full.csv'
train_path = './data/input/train_df.csv'
test_path = './data/input/test_df.csv'

# <codecell>

# create an instance
dp = s.DataPrep.from_yaml(config_path)
# <codecell>
dp.get_data(path='./data/input/bank-additional-full.csv', sep=';')


 # <codecell>
dp.standardize_columns(dp.data)
dp.split_feature_target(dp.data)
dp.split_column_dtypes(dp.features_df)
dp.clean_categorical_columns(dp.data, dp.categorical)

# <codecell>
dp.traintestsplit(dp.data[dp.categorical+dp.numerical], dp.target)

# <codecell>
dp.save_data(dp.train_df, 'train_df')
dp.save_data(dp.test_df, 'test_df')

# <codecell>
#dp.get_data('./data/input/train_df.csv')
X_train = dp.encode_train_data(dp.train_df.drop('y', axis='columns'))

