from utils.PiEstimator import PiEstimator


def wallis_product(queue):
    i = 2
    result = 1

    while True:
        gt_1 = i/(i-1)
        lt_1 = i/(i+1)
        i += 2
        result *= gt_1 * lt_1
        queue.put(2 * result)

    return


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    
    calculator = PiEstimator(10)
    estimates = calculator.timer(wallis_product)
    elements = []
    while not estimates.empty():
        elements.append(estimates.get())
    plt.plot(range(len(elements)), elements)
    plt.title("Wallis Product Method for Computing Pi")  
    plt.hlines([3.141592653589793], 0, len(elements), colors="red", linestyles="dashed")
    plt.show()