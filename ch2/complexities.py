# this is problem 1.1 comparision of running times of different functions
# given an f(n), f(n) 1e-6 seconds is spent for size n

# times in microseconds
from math import e
from numpy import log


times = [1e6, 1e6*60, 1e6*60*60, 1e6*60*60*24, 1e6*60 *
         60*24*30, 1e6*60*60*24*30*365, 1e6*60*60*24*30*365*100]
# 1. log_2 (n)
# for what n does it take 1 second, 1 minute... so on
# lgn = 1e6, n = e^(1e6) = e^t


def f(n):
    return log(n)


# def
for t in times:
    print(f"{t}s".format(t/1e6), f(e**t), end=" |")
