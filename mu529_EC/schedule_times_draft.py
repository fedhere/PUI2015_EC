# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 01:48:29 2015

@author: murbanek
"""

import pandas as pd
import numpy as np
import os
import pylab as pl
import datetime as dt
# from datetime import timedelta

os.chdir('C:/Users/murbanek/CUSP/ADS/LGA')
stoptimesfile = 'data/gtfs-bus/stop_times.txt'
tripfile = 'data/gtfs-bus/trips.txt'
stopfile = 'data/gtfs-bus/m60_stops.csv'
busline = 'M60+'

beginstop = pd.read_csv(stopfile).loc[1][0]
endstop = pd.read_csv(stopfile).loc[16][0]

trips = pd.read_csv(tripfile)
trips = trips[trips['route_id']==busline][['trip_id','service_id']]
# trips.set_index('trip_id',inplace=True)

myparser = lambda texttime: dt.datetime.strptime(texttime, '%H:%M:%S')

stoptimes = pd.read_csv(stoptimesfile)
stoptimes = stoptimes[stoptimes['arrival_time']<'23:59:59']
stoptimes['arrival_time'] = stoptimes['arrival_time'].apply(myparser)
# stoptimes.set_index('trip_id',inplace=True)

joined = pd.merge(trips.set_index('trip_id'),stoptimes.set_index('trip_id'),how='inner',left_index=True,right_index=True)
# joined.set_index('stop_id',inplace=True)

times = pd.concat([joined[joined['stop_id']==beginstop],joined[joined['stop_id']==endstop]],keys=[0,1])
times.index.names = ['begin_end_ind','trip_id']
times.reset_index(level=0,inplace=True)
times.reset_index(inplace=True)

times.sort(columns=['trip_id','arrival_time'],inplace=True)
times['elapsed'] = times['arrival_time'].diff()
block_times = times[times['begin_end_ind'].diff()==1][['arrival_time','elapsed','service_id']]
block_times['time_dec'] = block_times.arrival_time.dt.hour + block_times.arrival_time.dt.minute/60
# block_times['arrival_time'] = block_times.arrival_time.dt.time

colordict = {1:'red',2:'green',3:'yellow',4:'blue',5:'cyan',6:'pink'}
figure, ax = pl.subplots(figsize=(10,10))
c = 0
legend = {}
for name, group in block_times.groupby('service_id'):
    c = c + 1
    ax.scatter(group.time_dec, group.elapsed/np.timedelta64(1, 's')/60, color=colordict[c])
    legend[colordict[c]]=name

subset_block = block_times[(block_times['service_id']==legend['cyan']) & (block_times['time_dec']>=10.0)& (block_times['time_dec']<16)]
np.percentile(subset_block['elapsed'],50.0)