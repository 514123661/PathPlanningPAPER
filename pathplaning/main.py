from A_star_search import *
from set_Map import *
import pandas as pd
import numpy as np
import tqdm
if __name__ == '__main__':

    rate = pd.read_csv('In_situMeasurementforTraining_201712.csv')

    rate = rate.values

    wall = {}
    for i in tqdm.tqdm(rate):
        x, y, date, hour, wind = i
        if wind >= 15.0:
            wall[(x, y, date, hour)] = wind

    citydata = pd.read_csv('CityData (1).csv')

    start = (citydata.iloc[0].xid, citydata.iloc[0].yid)
    goal = (citydata.iloc[9].xid, citydata.iloc[9].yid)

    print(start)
    print(goal)

    path = []
    location = start
    path.append(location)
    time =0
    date = 1 #日期
    Map = Map()
    while location != goal:
        Map.wall = set_Map(current=location, time=time, date=1, rate=wall)
        came_from,cost_so_far =  A_Star(Map, location, goal)
        if came_from == cost_so_far =='fuck' :
            time = time+60
            continue
        father = 0
        h = goal
        while father != location:
            father = came_from[h]
            if father == location:
                time += 2
                next_step = h

            h = father

        location = next_step

        path.append(location)

        print(path)

        file = open('data1.txt', 'w')
        file.write(str(path))
        file.close()




