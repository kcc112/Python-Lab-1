def calculate_pi(n):
    approximation = 1
    for i in range(1, n + 1):
        output_text = 'Iteracja nr: {} | przybliżenie {}'
        approximation *= (4 * i ** 2) / (4 * i ** 2 - 1)
        pi = approximation * 2
        print(output_text.format(i, pi))


n = 10
calculate_pi(n)
