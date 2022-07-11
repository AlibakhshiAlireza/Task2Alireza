# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TRMQyZ_QyOnJrpmCfQmSIQXCITM13lZz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = pd.read_csv("D:/Downloads/Data Analyst - Commercial/data_analysis_task_q2.csv")

df

plt.rcParams['figure.figsize'] = [20, 20] 
plt.scatter(x=df['origin_lng'], y=df['origin_lat'],color = "r")
plt.scatter(x=df['destination_lng'], y=df['destination_lat'],color = "g")
x_values = [51.381725	, 51.458588]
y_values = [35.743465	,35.768105]
plt.plot(x_values, y_values)
plt.show()

id_list = list(range(1,31))

origin_dots = {}
for i in id_list:
  f = df[df['id'] == i]
  y = f.iloc[0,1]
  x = f.iloc[0,2]
  origin_dots[i] = []
  origin_dots[i].append(x)
  origin_dots[i].append(y)

origin_dots

destination_dots = {}
for i in id_list:
  f = df[df['id'] == i]
  y = f.iloc[0,3]
  x = f.iloc[0,4]
  destination_dots[i] = []
  destination_dots[i].append(x)
  destination_dots[i].append(y)

Best_Due = {}
for i in id_list:
    globals()[f"dues_for_{i}"] = {}
    for j in id_list:
        if i == j:
            pass
        else:
            a = math.dist(origin_dots[i], destination_dots[j])
            b = math.dist(origin_dots[j], destination_dots[j])
            c = math.dist(origin_dots[i], destination_dots[i])
            d = math.dist(origin_dots[j], destination_dots[i])
            e = math.dist(origin_dots[i], origin_dots[j])
            f = math.dist(destination_dots[i],destination_dots[j])
            optimized_route_between = min([a,b,c,d])
            total_destination = optimized_route_between + e + f
            globals()[f"dues_for_{i}"][j] = total_destination

h = min(dues_for_15.values())
dues_for_15

#dues_for_15
list(dues_for_15.keys())[list(dues_for_15.values()).index(h)]

Best_Due = {}
for i in id_list:
    h = min(globals()[f"dues_for_{i}"].values())
    f = list(globals()[f"dues_for_{i}"].keys())[list(globals()[f"dues_for_{i}"].values()).index(h)]
    Best_Due[i] = []
    Best_Due[i].append(f)
    Best_Due[i].append(h)

Best_Due

Destination_for_ind_dest = {}
for i in id_list:
    h = math.dist(origin_dots[i], destination_dots[i])
    Destination_for_ind_dest[i] = h

TripsDistin = pd.DataFrame()

TripsDistin["id"] = id_list
TripsDistin["Distin"] = ""

index = 0
for i in TripsDistin["id"]:
    TripsDistin.iloc[index,1] = Destination_for_ind_dest[i]
    index = index + 1

TripsDistin.sort_values(by=['Distin'],inplace = True)

Best_Due

TripsDistin_Duo = pd.DataFrame()

TripsDistin_Duo["id"] = id_list
TripsDistin_Duo["best duo"] = ""
TripsDistin_Duo["Distin"] = ""

index = 0
for i in TripsDistin_Duo["id"]:
    TripsDistin_Duo.iloc[index,1] = Best_Due[i][0]
    TripsDistin_Duo.iloc[index,2] = Best_Due[i][1]
    index = index + 1

TripsDistin_Duo.sort_values(by=['Distin'],inplace = True,ascending=False)

drivers_df = pd.DataFrame()
drivers_df["driverid"] = list(range(1,26))
drivers_df["passenger"] = ""

drivers_df

ids = list(range(1,31))
[int(i) for i in ids]

drivers_df

index = 0
passenger_mounted = []
for index_df, i in enumerate(drivers_df["driverid"]):
    if index < 5:
        x = int(TripsDistin_Duo.iloc[index_df,0])
        y = int(TripsDistin_Duo.iloc[index_df,1])
        count_x = passenger_mounted.count(x)
        count_y = passenger_mounted.count(y)
        if ((count_x == 0) and (count_y == 0)):
            passenger_mounted.append(x)
            passenger_mounted.append(y)
            drivers_df.iloc[index,1] = str(x) + "+" + str(y)
            try:
                ids.remove(x)
                ids.remove(y)
            except:
                pass
            index = index + 1
    else:
        break
for h in ids:
    drivers_df.iloc[index,1] = h
    index = index + 1

len(ids)

drivers_df

TripsDistin_Duo.sort_values(by=['Distin'],inplace = True,ascending=True)

index = 0
passenger_mounted = []
for index_df, i in enumerate(drivers_df["driverid"]):
    if index < 5:
        x = int(TripsDistin_Duo.iloc[index_df,0])
        y = int(TripsDistin_Duo.iloc[index_df,1])
        count_x = passenger_mounted.count(x)
        count_y = passenger_mounted.count(y)
        if ((count_x == 0) and (count_y == 0)):
            passenger_mounted.append(x)
            passenger_mounted.append(y)
            drivers_df.iloc[index,1] = str(x) + "+" + str(y)
            try:
                ids.remove(x)
                ids.remove(y)
            except:
                pass
            index = index + 1
    else:
        break
for h in ids:
    drivers_df.iloc[index,1] = h
    index = index + 1

drivers_df

id_list = list(range(1,31))