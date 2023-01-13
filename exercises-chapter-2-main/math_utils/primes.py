def isprime(n):
    if n == 1:
        return False
    b = 1
    m = int(n ** (1 / 2)) + 1
    i = 2
    while b and i < m:
        b = int(n % i)
        i += 1
        if not b:
            return False
    return True