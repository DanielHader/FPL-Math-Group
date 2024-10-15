from colour import Color

import timeit
import random
import functools

import numpy as np
import matplotlib.pyplot as plt

from sympy import gcd

def benchmark(funcs, inputs, random_seed=42):
    random.seed(random_seed) # seed random generator for duplicating runs

    # number of times to repeat each input timing
    NUM_REPEATS = 3

    # extract and sort input sizes and func names
    input_sizes = list(sorted(inputs.keys()))
    func_names = list(sorted(funcs.keys()))

    # generate a color for each func name
    colors = {}
    for i, func_name in enumerate(func_names):
        hue = i / len(func_names)
        sat = 0.5
        lum = 0.5
        colors[func_name] = Color(hsl=(hue, sat, lum))
    
    # create plots
    fig, ax = plt.subplots(figsize=(15,8))

    plt.ion()
    
    timings = {name: { size: [] for size in input_sizes } for name in func_names}

    worsts = {name: [] for name in func_names}
    averages = {name: [] for name in func_names}
    bests = {name: [] for name in func_names}

    x_data = []

    for input_size in input_sizes:
        print(f' - benchmarking input size {input_size}')
        inp_list = inputs[input_size]

        ax.clear()
        x_data.append(input_size)
        
        for func_name in func_names:
            func = funcs[func_name]
            
            for (a,b) in inp_list:
                try:
                    if func(a,b) != gcd(a,b):
                        raise ValueError
                    t = timeit.timeit(lambda: func(a, b), number=NUM_REPEATS) / NUM_REPEATS
                    
                except ValueError:
                    print(f'func "{func_name}" failed to calculate correct answer:')
                    print(f'  input a: {a}')
                    print(f'  input b: {b}')
                    print(f'  calculated gcd: {func(a, b)}')
                    print(f'  correct gcd: {gcd(a,b)}')
                    t = float('nan')
                except Exception:
                    t = float('nan')
                timings[func_name][input_size].append(t)

            worsts[func_name].append(np.max(timings[func_name][input_size]))
            averages[func_name].append(np.average(timings[func_name][input_size]))
            bests[func_name].append(np.min(timings[func_name][input_size]))

            rgb = colors[func_name].rgb

            ax.plot(x_data, averages[func_name], label=func_name, color=rgb)
            ax.fill_between(x_data, worsts[func_name], bests[func_name], alpha=0.5, color=rgb)

        ax.set_xlabel('input size [bits]')
        ax.set_ylabel('run time [seconds]')
        ax.legend()
        
        plt.pause(0.0001)

    input('press enter to continue')
    #plt.show(block=True)
            
def generate_inputs(size_range, inputs_per_size, random_seed=42):
    random.seed(random_seed)

    inputs = {}
    
    for input_size in size_range:
        inputs[input_size] = []
        for i in range(inputs_per_size):
            a = random.randint(0, 2**input_size - 1)
            b = random.randint(0, 2**input_size - 1)
            inputs[input_size].append((a, b))

    return inputs
            
import daniel_gcd as daniel
import EA_RieckV2 as yoav

def main():

    INPUT_GROWTH_RATE = 1.02
    MAX_INPUT = 50000
    MIN_INPUT = 4
    
    input_sizes = [MAX_INPUT]
    inp = int(MAX_INPUT / INPUT_GROWTH_RATE)
    while inp != input_sizes[0] and inp > MIN_INPUT:
        input_sizes = [inp] + input_sizes
        inp = int(inp / INPUT_GROWTH_RATE)
    
    print(f'generating inputs for {len(input_sizes)} different input sizes')
    inputs = generate_inputs(input_sizes, 10)

    print(f'registering gcd functions')
    funcs = {
        'daniel': daniel.gcd,
        'yoav': yoav.GCD,
    }

    print(f'beginning benchmark')
    benchmark(funcs, inputs)
    
if __name__ == "__main__":

    main()
