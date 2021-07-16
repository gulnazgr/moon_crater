def calculate(matrix: list) -> int:
    # счётчик краторов
    count = 0
    m = matrix

    for i in range(len(m)):
        for j in range(len(m[i])):
            c = m[i][j]  # текущая ячейка
            # получем ячейку матрицы справа от текущей ячейки,если не вышли за границу
            if j < len(m[i]) - 1:
                right_c = m[i][j + 1]
            # если вышли за границу ,то ячейка справа равна=0
            else:
                right_c = 0
            # получаем ячейкуснизу от текущей ячейки,если не вышли за границу матрицы
            if i < len(m) - 1:
                down_c = m[i + 1][j]
            # если вышли,то ячейка снизу равна=0

            else:
                down_c = 0
            if c == 1 and right_c == 0 and down_c == 0:
                # мы нашли кратер и прибавляем 1
                count += 1

    return count


def main() -> None:
    # загрузить файл
    with open('matrix.txt', 'rt') as fd:
        matrix = []

        # преобразовываем строки в списки и добавляем в матрицу
        for line in fd:
            matrix.append([int(lit) for lit in line.strip()])

        # получаем количество кратаров
        count = calculate(matrix)

        print(count)


if __name__ == "__main__":
    main()
