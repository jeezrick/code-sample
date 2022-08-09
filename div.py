def div_loop(d, r):
    '''
    Accessing the diviend and divisor by parameter D and R.
    >>> a, b = div_loop(11, 3)
    >>> a
    3
    >>> b
    2
    '''
    temp = r
    while d > (r << 1):
        r <<= 1
    q = 0
    while r >= temp: # while R can still represent one or more divisors
        q <<= 1    
        if d >= r:
            d -= r
            q += 1
        r >>= 1
    if d >= temp:
        q += 1
        d -= temp
    return q, d

if __name__ == "__main__":
    import numpy as np
    for i in range(100):
        a, b = np.random.randint(1, 1000), np.random.randint(1, 1000)
        c, d = div_loop(a, b)
        if c == a // b and d == a % b:
            pass
        else:
            print("False at: ", a, b)
