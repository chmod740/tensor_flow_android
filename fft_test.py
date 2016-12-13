import numpy as np


def fft(str):
    #数据切片处理致int——list
    str = str.split(' ')
    int_range = []
    for i in str:
        if i!="":
            int_range.append(int(i))
    fft_final = np.fft.fft(int_range)
    #矩阵内元素虚数转实数
    temp = fft_final.tolist()
    temp_final = temp[0:161:1]
    num=0
    for i in temp_final:
        temp_final[num] = np.sqrt(i.real*i.real+i.imag*i.imag)
        num = num+1
    fft_final = np.mat(temp_final)

    # print(fft_final)
    return fft_final