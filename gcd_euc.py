def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
# a = int(input('Podaj a: '))
# b = int(input('Podaj b: '))
# gcd = gcd(a, b)


print(gcd(84, 18))
