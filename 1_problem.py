from dask import delayed  # DON'T CHANGE (explained later)
import time
import math

def func(i):
    """A dummy CPU-bound function."""
    print(f'Function {i} starting...')
    # ***INSERT CODE HERE*** (should take about 1 second to execute)
    for i in range (800000000):
        i += math.sqrt(2) 
    print(f'Function {i} done')
    return i


start = time.time()

lazy = [delayed(func)(i) for i in range(4)]  # DON'T CHANGE (explained later)

end = time.time()
print("it took {} seconds".format(end - start))
