import sys

# Функция проверки принадлежит ли точка треугольнику
def is_triangle_own(triangle, point):
    q1 = (triangle[0][0] - point[0]) * (triangle[1][1] - triangle[0][1]) - (triangle[1][0] - triangle[0][0]) * (triangle[0][1] - point[1])
    q2 = (triangle[1][0] - point[0]) * (triangle[2][1] - triangle[1][0]) - (triangle[2][0] - triangle[1][0]) * (triangle[1][1] - point[1])
    q3 = (triangle[2][0] - point[0]) * (triangle[0][1] - triangle[2][1]) - (triangle[0][0] - triangle[2][0]) * (triangle[2][1] - point[1])

    for q in [q1, q2, q3]:
        if q == 0:
            return 0

    if sum([
        True if str(q)[0] == '-' else False for q in [q1, q2, q3]
    ]) in [0, 3]:
        return 1

    return -1


def main():
    # Считывание входных данных, наполнение списков точек
    quadrangle_points = []
    selected_points = []

    with open(sys.argv[1], 'r') as file:
        for line in file:
            line = line.strip().split(' ')
            quadrangle_points.append([
                float(line[0]),
                float(line[1])
            ])

    with open(sys.argv[2], 'r') as file:
        for line in file:
            line = line.strip().split(' ')
            selected_points.append([
                float(line[0]),
                float(line[1])
            ])

    # Вычисление вершин двух равных треугольников, полученных делением прямоугольника
    triangles = [
        [
            quadrangle_points[0],
            quadrangle_points[1],
            quadrangle_points[3]
        ],
        [
            quadrangle_points[2],
            quadrangle_points[1],
            quadrangle_points[3]
        ]
    ]

    for point in selected_points:
        done = False

        # Есть ли искомая точка в списке вершин прямоугольника
        if point in quadrangle_points:
            print(0)
            continue

        # Перебор двух треугольников, принадлежит ли точка им
        for triangle in triangles:
            q = is_triangle_own(
                triangle,
                point
            )

            if q == 0:
                print(1)
                done = True
            elif q == 1:
                print(2)
                done = True

        # Если во время выполнения цикла переменная done осталась ложной, значит точка находится снаружи
        if not done: print(3)

if __name__ == '__main__':
    main()
