def nwd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
# a = int(input('Podaj a: '))
# b = int(input('Podaj b: '))
# nwd = nwd(a, b)


print(nwd(84, 18))
