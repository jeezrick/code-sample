def generate_array(size, shape, random=False):
    import numpy as np
    arr = np.linspace(1, size, size)
    arr = arr.reshape(shape)
    if random:
        np.random.shuffle(arr)
    return arr
