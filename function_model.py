def print_arr(arr):
    for i in arr:
        print(i)


def nine_avr(arr, x, y):
    x_map = [1, 0, 1, 0, -1, -1, 1, -1]
    y_map = [1, 1, 0, -1, 0, -1, -1, 1]
    arr_sum = arr[x][y]
    tmp = 1
    for i in range(8):
        x_tmp = x + x_map[i]
        y_tmp = y + y_map[i]
        if (0 <= x_tmp < len(arr)) and (0 <= y_tmp < len(arr)):
            arr_sum += arr[x_tmp][y_tmp]
            tmp += 1
    return arr_sum / tmp


def nine_sum(arr, x, y):
    x_map = [1, 0, 1, 0, -1, -1, 1, -1]
    y_map = [1, 1, 0, -1, 0, -1, -1, 1]
    arr_sum = arr[x][y]
    for i in range(8):
        x_tmp = x + x_map[i]
        y_tmp = y + y_map[i]
        if (0 <= x_tmp < len(arr)) and (0 <= y_tmp < len(arr)):
            arr_sum += arr[x_tmp][y_tmp]
    return arr_sum


def arr_2d_max(arr):
    max_value = 0
    for i in arr:
        max_value = max(max_value, max(i))
    return max_value


def arr_2d_min(arr):
    min_value = arr[0][0]
    for i in arr:
        min_value = min(min_value, min(i))
    return min_value


def arr_2d_average(arr):
    arr_sum = 0
    for i in arr:
        arr_sum += sum(i) / len(i)
    return arr_sum / len(arr)


def arr_2d_variance(arr):
    arr_avr = arr_2d_average(arr)
    var_sum = 0
    for i in arr:
        sum_tmp = 0
        for j in i:
            sum_tmp += (j - arr_avr) ** 2
        var_sum += sum_tmp / len(i)
    return var_sum / len(arr)


def arr_2d_sum(arr):
    arr_sum = 0
    for i in arr:
        arr_sum += sum(i)
    return arr_sum


def arr_2d_min_max_normalization(arr):
    arr_min = arr_2d_min(arr)
    arr_max = arr_2d_max(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = (arr[i][j] - arr_min) / (arr_max - arr_min)
    return arr


def arr_2d_z_score_normalization(arr):
    arr_avr = arr_2d_average(arr)
    arr_var = arr_2d_variance(arr)
    for i in range(arr):
        for j in range(arr[i]):
            arr[i][j] = (arr[i][j] - arr_avr) / arr_var
    return arr
