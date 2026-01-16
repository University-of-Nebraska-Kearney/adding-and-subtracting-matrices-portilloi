# Isac Portillo
# Adding Matrices
# 1/15/26

def main():
    matrix1 = get_matrix()
    matrix2 = get_matrix()
    sum = add_matrix(matrix1, matrix2)
    print(sum)


# Create a matrix given user specifications and values
def get_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of cols: "))

    A = [[0 for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):
            value = int(input(f"Enter value at A[{row}][{col}]: "))
            A[row][col] = value

    return A


# verify that matrices can be added and return their sum
def add_matrix(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    if rows != len(matrix2) | cols != len(matrix2[0]):
        print("Matrices cannot be added")
        return

    A = [[0 for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):
            A[row][col] = matrix1[row][col] + matrix2[row][col]

    return A


if __name__ == '__main__':
    main()
