# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:39:28 2022

@author: albye
"""

import pandas as pd
from prophet import Prophet
import os
import matplotlib.pyplot as plt

model_data = pd.read_parquet('C:/Users/albye/Documents/Data Science Portfolio/nyc taxi/Summarised Data/model_data.parquet')


#keeping july-semptember 2022 as an unseen test set
train_data = model_data[(model_data['ds'].dt.year == 2021) | (model_data['ds'].dt.month <= 6)]
test_data = model_data[(model_data['ds'].dt.year == 2022) & (model_data['ds'].dt.month > 6)]



m = Prophet()
m.fit(train_data)

#making predictions for every hour in july - september plus every hour for first 3 days of October
future = m.make_future_dataframe(periods = 2280, 
                                 freq = 'H', 
                                 include_history = True)

forecast = m.predict(future)

forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]





