# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%matplotlib inline
import numpy as np
import pandas as pd
import requests

#Check if the string is a floating point number
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def fred(series,frequency,units, start_date,end_date):
    result = []
#Selection parameters
    selection = { 'api_key' : '770130e3e272d1085975a8e920dd6aa1',
                  'file_type' : 'json',
                  'series_id' : series, 
                  'frequency' : frequency,
                  'units' : units,
                  'observation_start' : start_date,
                  'observation_end' : end_date }
    
    r = requests.get('http://api.stlouisfed.org/fred/series/observations?', params=selection)
    result = r.json()
    obs = dict()
#Storing the observations
    for i,x in enumerate(result["observations"]):
        key = x["date"]
        if is_float(x["value"]):
            obs[key] = float(x["value"])
#Convert the observations into a series
    result = pd.Series(obs)
    return result

obs_1 = fred("GDPC1", "a","ch1", "1990-01-01", "2013-01-01")
obs_2 = fred("SP500", "a", "ch1", "1990-01-01", "2013-01-01")
obs_1.plot()
obs_2.plot()

# <codecell>


