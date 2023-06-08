def zeroMatrix(matrix):
    zero_rows = set()
    zero_cols = set()

    n = len(matrix)
    m = len(matrix[0])

    # Traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set rows to zero
    for row in zero_rows:
        for j in range(m):
            matrix[row][j] = 0

    # Set columns to zero
    for col in zero_cols:
        for i in range(n):
            matrix[i][col] = 0

    return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    ans = zeroMatrix(matrix)

    print("The Final matrix is:")
    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()
