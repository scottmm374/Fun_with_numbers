

def main():
    matrix = [[0] * 10 for x in range(0, 10)]

    num = 0
    for y in range(len(matrix)):
            for x in range(10):
                num +=1
                matrix[y][x] = num

    print(matrix)

def digit_root_row():
    digit_roots = []

    # each row, first reduce each int to one digit, then sum row, and reduce to digit_root for row (can do cols too, but same result)


if __name__ == "__main__":
    main()