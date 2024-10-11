import timeit
import random
import functools

import numpy as np
import matplotlib.pyplot as plt

from sympy import gcd

def gcd_1(a, b):
    if a == 0:
        return b
    return gcd_1(b%a, a)

def gcd_2(a, b):
    return gcd(a, b)

def my_gcd(a, b):
    if b == 0:
        return a
    while a != 0:
        a, b = b % a, a
    return b

def param_gen(input_sizes, samples):
    for input_size in input_sizes:
        for _ in range(samples):
            a = functools.reduce(lambda a, x: a * 2 + x, random.choices([0,1], k=input_size), 0)
            b = functools.reduce(lambda a, x: a * 2 + x, random.choices([0,1], k=input_size), 0)
            yield ((a, b), input_size)
            

def benchmark(func, param_gen, input_sizes, random_seed):
    random.seed(random_seed)
    N = 10

    data = {i: [] for i in input_sizes}
    
    for params in param_gen(input_sizes, 10):
        p, input_size = params
        t = timeit.timeit(lambda: func(*p), number=N) / N

        data[input_size].append(t)

    worsts = []
    avgs = []
    bests = []
        
    for input_size in input_sizes:

        times = data[input_size]
        
        best = times[0]
        avg = times[0]
        worst = times[0]
        
        for time in times[1:]:
            if time < best:
                best = time
            avg += time
            if time > worst:
                worst = time
        avg /= len(times)

        worsts.append(worst)
        avgs.append(avg)
        bests.append(best)

    fig, ax = plt.subplots()
    
    ax.plot(input_sizes, worsts, color='r', label='worst case')
    ax.plot(input_sizes, avgs, color='y', label='average case')
    ax.plot(input_sizes, bests, color='g', label='best case')

    ax.set_xlabel('input size [bits]')
    ax.set_ylabel('run time [seconds]')
    ax.legend()
    
    plt.show()


def main():
    benchmark(gcd_2, param_gen, [x for x in range(100, 10000, 100)], 42069)
    benchmark(my_gcd, param_gen, [x for x in range(100, 10000, 100)], 42069)
    
    
import time
    
if __name__ == "__main__":

    main()
