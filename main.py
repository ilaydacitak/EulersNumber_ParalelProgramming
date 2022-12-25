import multiprocessing
import random
import numpy as np
import os
import time

class EulerEsimatorProcess(multiprocessing.Process):
    def __init__(self, iterations, array: multiprocessing.Array, array_start_index: int):
        super().__init__()
        self.n = []
        self.iterations = iterations;
        self.array = array
        self. array_start_index = array_start_index

    def run(self) -> None:
        for _ in range(self.iterations):
            s = 0
            i = 0
            while True:
                number = random.random()
                i +=1
                s += number
                if s>1:
                    break
            self.n.append(i)
        summation = np.average(self.n)
        self.array[self.array_start_index] = summation

def main():
    time_start = time.time()
    cpu_count = os.cpu_count()
    guessing_number = 10000000
    array = multiprocessing.Array('f', range(cpu_count))
    processes = []
    for cpu in range(cpu_count):
        process = EulerEsimatorProcess(iterations=guessing_number, array=array, array_start_index=cpu)
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    average = 0
    for i in range(len(array)):
        average += array[i]

    average = average/len(array)

    time_end = time.time()

    print(f"Time took running script: {time_end-time_start:.2f} seconds!")
    print(f"Simulated {guessing_number * cpu_count} numbers!")
    print(f"Euler Number is {average}")

if __name__ == '__main__':
    main()