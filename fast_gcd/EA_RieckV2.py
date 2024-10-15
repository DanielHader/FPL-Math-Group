def GCD_evens(a, b):
    k=0
    while((a%2 == 0) & (b%2 == 0)):
        k += 1
        a = a >> 1
        b = b >> 1
    return a, b, k

def GCD_oneEven(a, b):
    while(a%2 == 0):
        a = a >> 1
    while(b%2 == 0):
        b = b >> 1
    return a, b


def GCD(a, b):
    if b>a:
        a, b = b, a
    a, b, k = GCD_evens(a, b)
    while(b>0):
        a, b = GCD_oneEven(a, b)
        if b >= a:
            a = b-a
        else:        
            a = a-b
        if b>a:
            a, b = b, a
    return a * 2**k

a_in = 150
b_in = 22
print(GCD(a_in, b_in))
