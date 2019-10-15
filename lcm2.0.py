def remove_values_from_list(list, val):
    return [value for value in list if value != val]


def prime_factorization(value):
    factors = []
    while(value != 1):
        if value % 2 == 0:
            factors.append(2)
            value /= 2
        else:
            n = 2
            while(value % n != 0):
                n += 1
            factors.append(n)
            value /= n
    return factors


def lcm(a, b):
    factors_a = prime_factorization(a)
    factors_b = prime_factorization(b)
    output = 1

    while len(factors_a) != 0:
        if factors_a.count(factors_a[0]) >= factors_b.count(factors_a[0]):
            output = output * factors_a[0]**factors_a.count(factors_a[0])
            factors_b = remove_values_from_list(factors_b, factors_a[0])
            factors_a = remove_values_from_list(factors_a, factors_a[0])
        else:
            factors_a = remove_values_from_list(factors_a, factors_a[0])

    while len(factors_b) != 0:
        output = output * factors_b[0]**factors_b.count(factors_b[0])
        factors_b = remove_values_from_list(factors_b, factors_b[0])

    return output


print(lcm(192, 348))
