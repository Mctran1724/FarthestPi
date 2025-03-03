import random
import math

import multiprocessing
import time

class PiEstimator:
    def __init__(self):
        pass

    def timer(self, t: int, func: callable):
        """
        :param t: time in seconds that we want to compute for
        :return: None

        This function will terminate the target function after t seconds and give back the value
        """
        pi = multiprocessing.Value('pi', 0)
        p = multiprocessing.Process(target=func, args=(pi, ))
        p.start()
        time.sleep(t)
        p.terminate()
        return pi.value

    def buffon_needle(self):
        pass

    def square_circle_mc(self):
        pass

    def basel_series(self):
        pass

    def leibniz_series(self):
        pass

    def lattice_points(self):
        pass



def loop_forever():

    i = 0
    while True:
        # do something
        print("Looping...")
        i += 1

    return i

def main():
    # Create a new process for the loop
    p = multiprocessing.Process(target=loop_forever)

    # Start the process
    p.start()

    # Wait for 5 seconds
    time.sleep(5)

    # Terminate the process
    p.terminate()

    print("Loop stopped")

if __name__ == "__main__":
    main()
    