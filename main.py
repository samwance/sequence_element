def main1():
    n = int(input('Введите количество чисел, которое вы хотите вывести из последовательности:\n'))
    sequence = ''

    if n <= 0:
        print("Пожалуйста, введите число больше нуля")
    else:
        while len(sequence) < n:
            for num in range(1, n + 1):
                sequence += str(num) * num

        print(f"Полученная последовательность: {sequence[:n]}")


def main2():
    n = int(input('Введите количество чисел, которое вы хотите вывести из последовательности:\n'))
    sequence = []

    if n <= 0:
        print("Пожалуйста, введите число больше нуля")
    else:
        while len(sequence) < n:
            for num in range(1, n + 1):
                sequence.extend([str(num)] * num)

        print(f"Полученная последовательность: {''.join(sequence[:n])}")


if __name__ == "__main__":
    choice = input('Выберите вариант решения: \n1. Через строку\n2. Через список\n')
    if choice == '1':
        main1()
    elif choice == '2':
        main2()
