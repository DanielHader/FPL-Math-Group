
def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while a != 0:
        a, b = b % a, a
    return b

