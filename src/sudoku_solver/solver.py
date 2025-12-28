"""
Sudoku solver functions implementing the custom algorithm.
"""

# All valid numbers in a Sudoku puzzle (1-9)
VALID_SUDOKU_NUMBERS = set(range(1, 10))


def get_missing_numbers_in_rows(matrix: list[list[int]]) -> list[list[int]]:
    """
    Analyze each row of the Sudoku matrix and return missing numbers for each row.

    For each row, finds which numbers from 1-9 are missing (not present in that row).
    Empty cells (represented as 0) are ignored when checking for present numbers.

    Args:
        matrix: A 9x9 matrix (list of lists) containing integers from 0-9.
                Indexed from [0][0] to [8][8].

    Returns:
        A list of 9 lists, where each list contains the missing numbers (1-9)
        for the corresponding row. Each inner list is sorted in ascending order.

        Example:
            If row 0 has [5, 3, 0, 0, 7, 0, 0, 0, 0],
            the missing numbers are [1, 2, 4, 6, 8, 9]
            (since 3, 5, 7 are present)
    """
    missing_per_row = []

    for row in matrix:
        # Get all non-zero numbers present in this row
        present_numbers = {cell for cell in row if cell != 0}

        # Find missing numbers by subtracting present numbers from all numbers
        missing_numbers = sorted(list(VALID_SUDOKU_NUMBERS - present_numbers))

        missing_per_row.append(missing_numbers)

    return missing_per_row


def get_missing_numbers_in_columns(matrix: list[list[int]]) -> list[list[int]]:
    """
    Analyze each column of the Sudoku matrix and return missing numbers for each column.

    For each column, finds which numbers from 1-9 are missing (not present in that column).
    Empty cells (represented as 0) are ignored when checking for present numbers.

    Args:
        matrix: A 9x9 matrix (list of lists) containing integers from 0-9.
                Indexed from [0][0] to [8][8].

    Returns:
        A list of 9 lists, where each list contains the missing numbers (1-9)
        for the corresponding column. Each inner list is sorted in ascending order.
        The index of each inner list corresponds to the column index (0-8).

        Example:
            If column 0 has [5, 6, 0, 8, 4, 7, 0, 0, 0],
            the missing numbers are [1, 2, 3, 9]
            (since 4, 5, 6, 7, 8 are present)
    """
    missing_per_column = []

    for col_index in range(9):
        # Get all non-zero numbers present in this column
        column = [matrix[row_index][col_index] for row_index in range(9)]
        present_numbers = {cell for cell in column if cell != 0}

        # Find missing numbers by subtracting present numbers from all numbers
        missing_numbers = sorted(list(VALID_SUDOKU_NUMBERS - present_numbers))

        missing_per_column.append(missing_numbers)

    return missing_per_column


def find_unique_intersections(matrix: list[list[int]]) -> list[tuple[int, int, int]]:
    """
    Find cells where the intersection of missing row and column numbers has exactly one element.

    For each empty cell (value 0), this function:
    1. Gets the missing numbers in that cell's row
    2. Gets the missing numbers in that cell's column
    3. Finds the intersection of these two sets
    4. If the intersection has exactly one element, that value can be placed in that cell

    Args:
        matrix: A 9x9 matrix (list of lists) containing integers from 0-9.
                Indexed from [0][0] to [8][8].
                0 represents empty cells, 1-9 represent filled cells.

    Returns:
        A list of tuples, where each tuple contains (row_index, col_index, value):
        - row_index (int): The row index (0-8)
        - col_index (int): The column index (0-8)
        - value (int): The unique value that is missing in both the row and column

        Only cells where the intersection has exactly one element are included.
        Only empty cells (value 0) are considered.

    Example:
        If row 0 is missing [1, 2, 4] and column 0 is missing [1, 3, 4],
        the intersection is [1, 4]. Since it has 2 elements, this cell is not included.

        If row 0 is missing [1, 2] and column 0 is missing [1, 3],
        the intersection is [1]. Since it has exactly 1 element,
        the result includes (0, 0, 1).
    """
    # Get missing numbers for all rows and columns
    missing_in_rows = get_missing_numbers_in_rows(matrix)
    missing_in_columns = get_missing_numbers_in_columns(matrix)

    result = []

    # Outer loop: iterate over columns
    for col_index in range(9):
        # Inner loop: iterate over rows
        for row_index in range(9):
            # Only process empty cells (value 0)
            if matrix[row_index][col_index] == 0:
                # Get missing numbers for this row and column
                missing_row = set(missing_in_rows[row_index])
                missing_col = set(missing_in_columns[col_index])

                # Find the intersection (numbers missing in both row and column)
                intersection = missing_row & missing_col

                # If intersection has exactly one element, add it to results
                if len(intersection) == 1:
                    unique_value = intersection.pop()
                    print(
                        f"Interseção única encontrada na linha {row_index}, coluna {col_index}: {unique_value}"
                    )
                    result.append((row_index, col_index, unique_value))

    return result
