def cal_amall(x, p):
    ans = []
    sum_tmp = 0
    for k in range(122):
        sum_tmp += x ** 2
        ans.append(sum_tmp)
    a = sum_tmp / p
    ans = [(ii / a) for ii in ans]
    return ans
