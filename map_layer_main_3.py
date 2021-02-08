import json
import random
import function_model as fm
import csv
import map_layer_function as mlf
import process_bar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

data = []
with open('fungi_data/map_layer_data.csv') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)

# data = data[1:]
map_length = 100  # The map size of each layer is 100 * 100
N = 100000  # Maximum environmental capacity of each grid
fungi_map = []  # Define a map to store fungal traits and information
now_temp = 26  # Initialize current temperature
now_water = 1  # Initializes the current water niche
for sub_data in data[1:]:  # Read data
    dict_data = {
        'name': sub_data[0],
        'rank': float(sub_data[1]),
        'increase_rate': float(sub_data[2]) / 2,
        'rank_number': int(sub_data[3]),
        'temp_niche_low': float(sub_data[4]),
        'temp_niche_high': float(sub_data[5]),
        'water_niche_low': float(sub_data[6]),
        'water_niche_high': float(sub_data[7]),
        'map': mlf.init_map(map_length, 0)
    }
    fungi_map.append(dict_data)

for i in range(len(fungi_map)):
    for j in range(5):  # Initial random inoculation 5 squares
        fungi_map[i]['map'] = mlf.map_inoculation(fungi_map[i]['map'], 2)
        # Each grid was inoculated with 2 corresponding fungi

y1 = [[] for i in range(len(fungi_map))]
n = 244
for k in range(n):  # iteration
    # For the question 1
    fungi_map = mlf.fungal_increase(fungi_map, N)  # The propagation and expansion of fungi were calculated layer by layer

    # For the question 2 (add)
    fungi_map = mlf.fungal_competition(fungi_map)  # The results of competition among fungi were calculated

    # For the question 3 (add)
    now_temp_tmp = now_temp + random.uniform(-5.0, 5.0)  # Random temperature change
    now_water_tmp = now_water + random.uniform(-2.0, 2.0)  # Random change of water niche
    fungi_map = mlf.fungi_temp(fungi_map, now_temp_tmp)  # Calculate the effect of current temperature on fungi
    fungi_map = mlf.fungi_water(fungi_map, now_water_tmp)  # The effect of water niche on fungi was calculated

    for index in range(len(fungi_map)):
        y1[index].append(fm.arr_2d_sum(fungi_map[index]['map']))  # Record preparation drawing
    process_bar.bar_print(k, n)

x1 = [i for i in range(1, n + 1)]
# X, Y = np.meshgrid([i for i in range(map_length)], [i for i in range(map_length)])

k = 0
plt.title('5-2')
for y_tmp in y1:  # mapping
    plt.plot(x1, y_tmp, label=fungi_map[k]['name'])
    k += 1
#
# with open('fungi_temp_water_com_244_fungimap_5-2.json', 'w') as f:
#     f.write(json.dumps(fungi_map))
#
# with open('fungi_temp_water_com_244_y1_5-2.json', 'w') as f:
#     f.write(json.dumps(y1))

plt.show()
