from typing import List

def printPascal(n: int) -> List[List[int]]:
    if n <= 0:
        return []

    ans = []
    prev_row = [1]

    ans.append(prev_row)  # Add the first row with a single element

    for row in range(1, n):
        curr_row = [1]  # First element of each row is always 1

        for col in range(1, row):
            curr_row.append(prev_row[col - 1] + prev_row[col])

        curr_row.append(1)  # Last element of each row is always 1

        ans.append(curr_row)
        prev_row = curr_row

    return ans
