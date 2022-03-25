from typing import List
import math


def zcount(list: List[float]) -> float:
    return len(list)


def zmean(list: List[float]) -> float:
    return sum(list) / zcount(list)


def zmode(list: List[float]) -> float:
    return max(set(list), key=list.count)


def zmedian(list: List[float]) -> float:
    sorted_list = sorted(list)
    n = len(list)
    index = (n - 1) // 2
    return sorted_list[index]


def zvariance(list: List[float]) -> float:
    n = zcount(list) - 1
    mean = zmean(list)  # mean of data mean=sum(data) / n
    deviations = [abs(mean - xi) ** 2 for xi in list]  # square deviations
    variance = sum(deviations) / n  # varience
    return variance


def zstddev(list: List[float]) -> float:
    return math.sqrt(zvariance(list))


def zstderr(list: List[float]) -> float:
    std_err = zstddev(list) / (math.sqrt(zcount(list)))
    return std_err


def zcorr(listx: List[float], listy: List[float]) -> float:
    statx = zstddev(listx)
    staty = zstddev(listy)
    cov = zcov(listx, listy)
    return cov / (statx * staty)


def cov(listx: List[float], listy: List[float]) -> float:
    sum = 0
    if len(listx) == len(listy):
        for i in range(len(listx)):
            sum += ((listx[i] - zmean(listx)) * (listy[i] - zmean(listy)))
        cov = sum / (len(listx) - 1)
        return cov


def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data


def readDataFile(file_name):
    x, y = [], []
    with open(file_name) as f:
        first_line = f.readline()
        for line in f:
            row = line.split(',')
            x.append(float(row[0]))
            y.append(float(row[1]))
    return x, y
