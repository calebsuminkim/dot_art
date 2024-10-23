def ceil_trunc(n):
    if n % 10 < 5:
        n -= (n % 10)
    else:
        n += 10 - (n % 10)
    return n
