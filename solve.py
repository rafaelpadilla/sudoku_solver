from sudoku_solver.helper import (
    is_solved_sudoku,
    is_valid_sudoku,
    read_sudoku_csv,
    print_sudoku_matrix,
)
from sudoku_solver.solver import (
    find_unique_intersections,
)

sudoku_matrix = read_sudoku_csv("sudoku.csv")

if not is_valid_sudoku(sudoku_matrix):
    print("Matriz de Sudoku inválida")
    exit(1)

# Print the sudoku matrix
print_sudoku_matrix(sudoku_matrix)

while True:
    # Find unique intersections
    unique_intersections = find_unique_intersections(sudoku_matrix)

    # Check condition after first iteration - if no intersections found, break
    if not unique_intersections:
        print("Não há mais interseções únicas")
        break

    # Fill unique intersections in the sudoku matrix
    for row_index, col_index, value in unique_intersections:
        sudoku_matrix[row_index][col_index] = value

    # Print the sudoku matrix
    print_sudoku_matrix(sudoku_matrix)

# Check if the sudoku matrix is solved
if is_solved_sudoku(sudoku_matrix):
    print("Sudoku resolvido! Sua teoria está correta!")
else:
    print("Sudoku não resolvido! Sua teoria está errada!")
