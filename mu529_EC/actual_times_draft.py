# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:10:29 2015

@author: murbanek
"""

import pandas as pd
import numpy as np
import os
from datetime import timedelta
import pylab as pl
import pickle
from scipy import stats
import warnings
warnings.simplefilter(action = "ignore", category = RuntimeWarning)

stopfile = 'data/gtfs-bus/m60_stops.csv'
busline = 'MTA NYCT_M60+'

beginstop = pd.read_csv(stopfile).loc[1][0]
endstop = pd.read_csv(stopfile).loc[16][0]


with open(busline + '_stoparrays.pkl', 'rb') as input:
    stoparrays = pickle.load(input)

begintimes = stoparrays['MTA_'+str(beginstop)][['vehicle_id','arrival_target']]
endtimes = stoparrays['MTA_'+str(endstop)][['vehicle_id','arrival_target']]
times = pd.concat([begintimes,endtimes],keys=[0,1])
times.index.names = ['begin_end_ind','index']
times.reset_index(level=0,inplace=True)

times.sort(columns=['vehicle_id','arrival_target'],inplace=True)
times['elapsed'] = times['arrival_target'].diff()
actual_times = times[times['begin_end_ind'].diff()==1][['arrival_target','elapsed']]
actual_times['hour'] = actual_times.arrival_target.dt.hour
actual_times['dow'] = actual_times.arrival_target.dt.weekday + 1

subset_actual = actual_times[(actual_times['dow'] <= 5) & (actual_times['hour'] >= 10) & (actual_times['hour'] < 16)]

stats.percentileofscore(subset_block['elapsed'],np.percentile(subset_actual['elapsed'],50.0))
np.percentile(subset_actual['elapsed'],50.0)