# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:46:28 2022

@author: albye
"""

import pandas as pd
from prophet import Prophet
import os


data_dir = 'C:/Users/albye/Documents/Data Science Portfolio/nyc taxi/Data'
files = os.listdir(data_dir)
os.chdir(data_dir)

model_data = pd.DataFrame(columns = ['ds', 'y'])

#used to record the total number of missing values from all columns
total_nas = 0
for file in files:
    #extract month based on the name of the file
    month = int(file.split('-')[1][:2])
    
    data = pd.read_parquet(file)
    data = data[data['PULocationID'] == 113]
    data = data[['VendorID', 'tpep_pickup_datetime']]
    data = data.rename(columns = {'VendorID':'id',
                        'tpep_pickup_datetime':'datetime'})
    
    data['hour'] = data['datetime'].dt.round('H')
    
    total_nas += data.isna().sum().sum()
    
    summaries = data.groupby(['hour']).size().reset_index(name='total')
    
    summaries = summaries.rename(columns = {'hour':'ds',
                                                               'total':'y'})
    
    #each file is named based on the month of data, so removing records which don't belong to that month
    #this will remove duplicates
    summaries = summaries[summaries['ds'].dt.month == month]
    
    model_data = model_data.append(summaries)
    
    
#check for duplicates
dupes_idx = model_data.duplicated(subset = 'ds', keep = False)

dupes = model_data[dupes_idx]
    
model_data.to_parquet('C:/Users/albye/Documents/Data Science Portfolio/nyc taxi/Summarised Data/model_data.parquet')


