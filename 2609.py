from math import gcd

def lcm(a,b):
    return a*b//gcd(a,b)
a, b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b)) 
