def calculate_pi(n):
    approximation = 1
    for i in range(1, n + 1):
        output_text = 'Iteracja nr: {} | przybliżenie {}'
        approximation *= (4*i*i)/((2*i - 1)*(2*i + 1))
        pi = approximation*2
        print(output_text.format(i, pi))


try:
    n = int(input('Wybierz ilość przybliżeń: '))
except ValueError:
    print('Niepoprawna wartość')
    exit()

calculate_pi(n) if n != 0 else print('Wartość nie może być zerem')
