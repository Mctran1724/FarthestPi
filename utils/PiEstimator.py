import multiprocessing
import time

class PiEstimator:
    def __init__(self, t: int = 1):
        self._runtime = t

    def timer(self, func: callable) -> multiprocessing.Queue:
        """
        :param func: estimator function
        :return: a multiprocessing queue that holds successive pi estimates

        This function will terminate the target function after t seconds and return the pi estimates achieved
        """
        pi_estimates = multiprocessing.Queue()
        p = multiprocessing.Process(target=func, args=(pi_estimates, ))
        p.start()
        time.sleep(self._runtime)
        p.terminate()
        return pi_estimates

    def buffon_needle(self):
        pass

    def leibniz_series(self):
        pass

    def lattice_points(self):
        pass


if __name__ == "__main__":
    pass    