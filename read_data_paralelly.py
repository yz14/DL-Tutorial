""" Load Data Paralelly """

import multiprocessing as mtp
import numpy as np
import glob
import ray

##############################
#########  example 1 #########
##############################
def f(x):
    return x**2

if __name__ == '__main__':
    num_work = 4
    with mtp.Pool(num_work) as P:
        x = P.map(f, np.arange(4))
    print(x)


##############################
#########  example 2 #########
##############################
def loadtxt_parallelly(files, num_work):
    """files: file names."""
    with mtp.Pool(num_work) as P:
        x = P.map(np.loadtxt, files)
    return np.array(x)

if __name__ == '__main__':
    files = glob.glob('path_to_your_data/*.txt')
    num_work = 4
    data = loadtxt_parallelly(files, num_work)


##############################
#########  example 3 #########
##############################
ray.init()

@ray.remote
def f(x):
    return x**2

y = [f.remote(x) for x in range(4)]
y = ray.get(y)
print(y)


##############################
#########  example 4 #########
##############################
ray.init()
@ray.remote
def loadtxt(file):
    return np.loadtxt(file)

files = glob.glob('path_to_your_data/*.txt')
data = [loadtxt.remote(file) for file in files]
data = ray.get(data)