import math

n = 100
prime_numbers = [1] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if prime_numbers[i] == 1:
        for j in range(2 * i, n, i):
            prime_numbers[j] = 0

for i in range(2, n):
    if prime_numbers[i] == 1:
        print(i)
