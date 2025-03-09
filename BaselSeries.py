from utils.PiEstimator import PiEstimator

"""
The solution to the Basel problem is a famous result by Euler.
The Basel problem is the sum of reciprocals of squares of natural numbers.
The result is that the series converges to pi**2/6. 
Therefore, pi = sqrt(6 * basel_sum)
"""

def basel_series(queue):
    i = 0
    basel_sum = 0
    while True:
        i += 1
        basel_sum += 1 / (i**2)
        queue.put((6 * basel_sum)**0.5)
    
    return


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    
    calculator = PiEstimator(10)
    estimates = calculator.timer(basel_series)
    elements = []
    while not estimates.empty():
        elements.append(estimates.get())
    plt.plot(range(5, len(elements)),elements[5:])
    plt.title("Basel Sum Method for Computing Pi")  
    plt.hlines([3.141592653589793], 0, len(elements), colors="red", linestyles="dashed")
    plt.show()