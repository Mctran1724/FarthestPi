from utils.PiEstimator import PiEstimator
import random

"""
This implements a Square-Circle Monte Carlo method for computing the mathematical constant pi.
This arises directly from the area of a circle.

Consider a circle with radius 1 centered at the origin. Then, the area of the circle is pi.
Consider also a circumscribed square with side length 2 centered at the origin. Then, the area of the square is 4.
Because the diameter of the circle and the side of the square are equal, the ratio of the areas is pi/4.
Suppose we were to choose a point at random from within the square with uniform distribution.
Then, the probability of any given point falling within the circle is pi/4.

The experimental probability will converge toward the theoretical pi/4, and so iteration
allows us to converge the value of pi as 4 * experimental probability.
pi = 4 * (count_of_points_in_circle / num_points)
"""

def compute(queue):
    num_points = 0
    in_circle = 0
    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            in_circle += 1
        num_points += 1
        queue.put(4 * (in_circle / num_points))
            
    return queue



if __name__ == "__main__":
    from matplotlib import pyplot as plt
    
    calculator = PiEstimator(100)
    estimates = calculator.timer(compute)
    elements = []
    while not estimates.empty():
        elements.append(estimates.get())
    plt.plot(range(len(elements)),elements)
    plt.title("Square-Circle Monte Carlo Method for Computing Pi")  
    plt.hlines([3.141592654], 0, len(elements), colors="red", linestyles="dashed")
    plt.show()