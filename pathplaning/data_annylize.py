import pandas as pd

from A_star_search import *

from set_Map import *

from pandas import DataFrame as df

rate = pd.read_csv('In_situMeasurementforTraining_201712.csv')

rate = rate.values

wall = {}

for i in rate:
    x,y,date,hour,wind = i
    if wind>=15.0:
        wall[(x,y,date,hour)] = 1

import numpy as np
import matplotlib.pyplot as plt



