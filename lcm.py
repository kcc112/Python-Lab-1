def lcm(a, b):
    output = a * b
    output /= gcd(a, b)
    return output


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(int(lcm(192, 348)))
