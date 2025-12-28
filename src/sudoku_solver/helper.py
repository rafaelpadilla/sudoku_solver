"""
Helper functions for Sudoku solver.
"""

import csv
from pathlib import Path
from typing import List


def read_sudoku_csv(file_path: str = "sudoku.csv") -> List[List[int]]:
    """
    Read a Sudoku puzzle from a CSV file and store it in a 9x9 matrix.

    The matrix is indexed from [0][0] to [8][8], where:
    - First index is the row (0-8)
    - Second index is the column (0-8)

    Args:
        file_path: Path to the CSV file containing the Sudoku puzzle.
                   Defaults to "sudoku.csv" in the current directory.

    Returns:
        A 9x9 matrix (list of lists) containing integers from 0-9.
        - 0 represents an empty cell
        - 1-9 represent filled cells with the corresponding number

    Raises:
        FileNotFoundError: If the CSV file doesn't exist.
        ValueError: If the CSV doesn't have exactly 9 rows or 9 columns,
                   or if any cell contains a value outside the valid range (0-9).

    Empty Cell Handling:
        Empty cells in the CSV can be represented as:
        - Empty string (""): Converted to 0
        - String "0": Converted to 0
        Both represent empty/unfilled cells in the Sudoku puzzle.

    Value Validation:
        - Valid values: 0-9 (0 for empty, 1-9 for filled cells)
        - Values outside this range (e.g., 10, -1, or non-numeric strings)
          will raise a ValueError

    Example CSV format:
        5,3,0,0,7,0,0,0,0
        6,0,0,1,9,5,0,0,0
        0,9,8,0,0,0,0,6,0
        ...
    """
    csv_path = Path(file_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Arquivo CSV do Sudoku não encontrado: {file_path}")

    matrix = []

    with open(csv_path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        for row_index, row in enumerate(reader):
            if row_index >= 9:
                raise ValueError(
                    f"Arquivo CSV tem mais de 9 linhas. Linha encontrada no índice {row_index}"
                )

            # Ensure we have exactly 9 columns
            if len(row) != 9:
                raise ValueError(
                    f"Linha {row_index} tem {len(row)} colunas, esperado 9. Encontrado: {row}"
                )

            # Convert each cell to integer (empty strings become 0)
            matrix_row = []
            for col_index, cell in enumerate(row):
                cell = cell.strip()  # Remove whitespace
                if cell == "" or cell == "0":
                    matrix_row.append(0)
                else:
                    try:
                        cell_value = int(cell)
                        # Validate that the value is in the valid range (0-9)
                        if cell_value < 0 or cell_value > 9:
                            raise ValueError(
                                f"Valor fora do intervalo na linha {row_index}, coluna {col_index}: '{cell}'. "
                                f"Esperado um número de 0-9 (0 para vazio, 1-9 para células preenchidas)."
                            )
                        matrix_row.append(cell_value)
                    except ValueError as e:
                        # Re-raise if it's our custom validation error
                        if "Valor fora do intervalo" in str(e):
                            raise
                        # Otherwise, it's a conversion error
                        raise ValueError(
                            f"Valor inválido na linha {row_index}, coluna {col_index}: '{cell}'. "
                            f"Esperado um número de 0-9 (0 para vazio, 1-9 para células preenchidas)."
                        ) from e

            matrix.append(matrix_row)

    # Ensure we have exactly 9 rows
    if len(matrix) != 9:
        raise ValueError(f"Arquivo CSV tem {len(matrix)} linhas, esperado 9")

    return matrix


def print_sudoku_matrix(matrix: List[List[int]]) -> None:
    """
    Print a 9x9 Sudoku matrix in a visually appealing format.

    The matrix is displayed with:
    - Borders around the entire grid
    - Separators for 3x3 boxes
    - Empty cells (0) displayed as dots

    Args:
        matrix: A 9x9 matrix (list of lists) containing integers from 0-9.
    """
    print("\n" + "═" * 37)
    print(" " * 12 + "QUEBRA-CABEÇA SUDOKU")
    print("═" * 37)

    for row_index, row in enumerate(matrix):
        if row_index % 3 == 0 and row_index > 0:
            print("├" + "─" * 7 + "┼" + "─" * 7 + "┼" + "─" * 7 + "┤")

        # Print row with borders
        row_str = "│ "
        for col_index, cell in enumerate(row):
            if col_index % 3 == 0 and col_index > 0:
                row_str += "│ "

            # Display 0 as a dot, other numbers as themselves
            if cell == 0:
                row_str += "· "
            else:
                row_str += f"{cell} "

        row_str += "│"
        print(row_str)

    print("═" * 37 + "\n")


def is_valid_sudoku(matrix: List[List[int]]) -> bool:
    """
    Verify if the input 9x9 Sudoku matrix is valid.

    A valid Sudoku matrix must satisfy:
    1. All rows must not have repeated values (empty/0 values are allowed and ignored)
    2. All columns must not have repeated values (empty/0 values are allowed and ignored)
    3. All 9 3x3 boxes must not have repeated values (empty/0 values are allowed and ignored)

    Args:
        matrix: A 9x9 matrix (list of lists) containing integers from 0-9.
                Indexed from [0][0] to [8][8].
                0 represents empty cells, 1-9 represent filled cells.

    Returns:
        True if the matrix is valid (no duplicates in rows, columns, or 3x3 boxes).
        False if any duplicates are found.

    Example:
        >>> matrix = [
        ...     [5, 3, 0, 0, 7, 0, 0, 0, 0],
        ...     [6, 0, 0, 1, 9, 5, 0, 0, 0],
        ...     ...
        ... ]
        >>> is_valid_sudoku(matrix)
        True
    """
    # Validate rows
    for row_index, row in enumerate(matrix):
        non_zero_values = [cell for cell in row if cell != 0]
        if len(non_zero_values) != len(set(non_zero_values)):
            return False

    # Validate columns
    for col_index in range(9):
        column = [matrix[row_index][col_index] for row_index in range(9)]
        non_zero_values = [cell for cell in column if cell != 0]
        if len(non_zero_values) != len(set(non_zero_values)):
            return False

    # Validate 3x3 boxes
    for box_row in range(3):
        for box_col in range(3):
            box_values = []
            # Get all values in this 3x3 box
            for row_offset in range(3):
                for col_offset in range(3):
                    row_index = box_row * 3 + row_offset
                    col_index = box_col * 3 + col_offset
                    box_values.append(matrix[row_index][col_index])

            # Check for duplicates (ignoring 0)
            non_zero_values = [cell for cell in box_values if cell != 0]
            if len(non_zero_values) != len(set(non_zero_values)):
                return False

    return True


def is_solved_sudoku(matrix: List[List[int]]) -> bool:
    """
    Verify if the input 9x9 Sudoku matrix is solved.

    A solved Sudoku matrix must satisfy:
    - All rows must have no repeated values (empty/0 values are allowed and ignored)
    - All columns must have no repeated values (empty/0 values are allowed and ignored)
    - All 9 3x3 boxes must have no repeated values (empty/0 values are allowed and ignored)
    """
    return is_valid_sudoku(matrix) and all(
        all(cell != 0 for cell in row) for row in matrix
    )
