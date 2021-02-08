import random
import function_model as fm


def init_map(n, m):
    return [[m for i in range(n)] for ii in range(n)]


def map_inoculation(arr, k):
    random_x = random.randint(0, len(arr) - 1)
    random_y = random.randint(0, len(arr[0]) - 1)
    arr[random_x][random_y] = k
    return arr


def competition_start(arr1, arr2, a, b):  # arr1 win arr2
    n = len(arr1)
    for i in range(n):
        for j in range(n):
            # if a == 0 and b == 0:
            tmp1 = max(arr1[i][j] - arr2[i][j] * (b / (a + b)), 0)
            tmp2 = max(arr2[i][j] - arr1[i][j] * (a / (a + b)), 0)
            arr1[i][j] = tmp1
            arr2[i][j] = tmp2
    return arr2


def competition_start_equal(arr1, arr2):
    n = len(arr1)
    for i in range(n):
        for j in range(n):
            if (arr1[i][j] != 0) and (arr2[i][j] != 0):
                arr1[i][j] *= 0.5
                arr2[i][j] *= 0.5
                # tmp = random.randint(0, 1)
                # if tmp == 0:
                #     arr2[i][j] = 0
                # else:
                #     arr1[i][j] = 0
    return arr1, arr2


def fungal_competition(fungi_map):
    for i in range(len(fungi_map)):
        for j in range(i + 1, len(fungi_map)):
            if fungi_map[i]['rank'] > fungi_map[j]['rank']:
                fungi_map[j]['map'] = competition_start(fungi_map[i]['map'], fungi_map[j]['map'],
                                                        fungi_map[i]['rank'], fungi_map[j]['rank'])
            elif fungi_map[i]['rank'] < fungi_map[j]['rank']:
                fungi_map[i]['map'] = competition_start(fungi_map[j]['map'], fungi_map[i]['map'],
                                                        fungi_map[j]['rank'], fungi_map[i]['rank'])
            else:
                fungi_map[i]['map'], fungi_map[j]['map'] = \
                    competition_start_equal(fungi_map[i]['map'], fungi_map[j]['map'])
    return fungi_map


def fungal_increase_model(arr, rate, N):
    n = len(arr)
    tmp_arr = [[0 for ii in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = arr[i][j]
            if tmp == 0:
                tmp_arr[i][j] = fm.nine_avr(arr, i, j)
            else:
                tmp_arr[i][j] = rate * tmp * (1 - (tmp / N)) + tmp
    return tmp_arr


def fungal_increase(fungi_map, N):
    for k in range(len(fungi_map)):
        fungi_map[k]['map'] = fungal_increase_model(fungi_map[k]['map'], fungi_map[k]['increase_rate'], N)
    return fungi_map


def fungi_map_draw(fungi_map):
    k = len(fungi_map)
    n = len(fungi_map[0]['map'])
    tmp_map = [[0 for i in range(n)] for ii in range(n)]
    tmp_number = 0
    for i in range(k):
        tmp_number = max(fungi_map[i]['rank_number'], tmp_number)
    for i in range(k):
        for x in range(n):
            for y in range(n):
                if fungi_map[i]['map'][x][y] != 0:
                    tmp_map[x][y] = max(tmp_number - fungi_map[i]['rank_number'], tmp_map[x][y])
    return tmp_map


def fungi_map_draw_2(fungi_map):
    k = len(fungi_map)
    n = len(fungi_map[0]['map'])
    tmp_map = [[0 for i in range(n)] for ii in range(n)]
    # tmp_number = 0
    # for i in range(k):
    #     tmp_number = max(fungi_map[i]['rank_number'], tmp_number)
    for i in range(k):
        for x in range(n):
            for y in range(n):
                if fungi_map[i]['map'][x][y] != 0:
                    tmp_map[x][y] = max(fungi_map[i]['map'][x][y], tmp_map[x][y])
    return tmp_map


def fungi_temp_cal(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] *= 0.5
    return arr


def fungi_temp(fungi_map, now_temp):
    for k in range(len(fungi_map)):
        left = fungi_map[k]['temp_niche_low']
        right = fungi_map[k]['temp_niche_high']
        if left < now_temp < right:
            continue
        fungi_map[k]['map'] = fungi_temp_cal(fungi_map[k]['map'])
    return fungi_map


def fungi_water(fungi_map, now_water):
    for k in range(len(fungi_map)):
        left = fungi_map[k]['water_niche_low']
        right = fungi_map[k]['water_niche_high']
        if left < now_water < right:
            continue
        fungi_map[k]['map'] = fungi_temp_cal(fungi_map[k]['map'])
    return fungi_map
