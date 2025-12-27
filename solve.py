from sudoku_solver.helper import read_sudoku_csv, print_sudoku_matrix
from sudoku_solver.solver import (
    find_unique_intersections,
    get_missing_numbers_in_columns,
    get_missing_numbers_in_rows,
)

sudoku_matrix = read_sudoku_csv("sudoku.csv")

# Print the sudoku matrix
print_sudoku_matrix(sudoku_matrix)

# Get missing numbers in each row
missing_numbers = get_missing_numbers_in_rows(sudoku_matrix)
# Display missing numbers for each row
print("Missing numbers per row:")
for row_index, missing in enumerate(missing_numbers):
    print(f"Row {row_index}: {missing}")

# Get missing numbers in each column
missing_numbers_in_columns = get_missing_numbers_in_columns(sudoku_matrix)
# Display missing numbers for each column
print("Missing numbers per column:")
for col_index, missing in enumerate(missing_numbers):
    print(f"Column {col_index}: {missing}")

# Find unique intersections
unique_intersections = find_unique_intersections(sudoku_matrix)
# Display unique intersections
print("Unique intersections:")
for row_index, col_index, value in unique_intersections:
    print(f"Row {row_index}, Column {col_index}: {value}")
