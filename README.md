# 🎯 Sudoku Solver 🧩

## 📖 About This Project

This is a special project that I created **with my dad on December 25th** 🎄✨. It started on December 25th as a fun coding adventure where I taught my dad the basics of Python programming!

### 🎓 The Story

My dad has always been interested in algorithms and theory, and he bought several Sudoku books that he couldn't solve. Together, we decided to explore whether **any Sudoku puzzle can be solved** using an algorithm that **he created**! 

This project combines:
- 🤓 My dad's algorithmic thinking and theory
- 💻 My Python programming skills
- 🧩 The challenge of solving Sudoku puzzles from his books

### 🎯 Project Goal

The goal is to create a Python program that:
1. 📊 Takes an initial Sudoku grid (sheet) containing the numbers of the Sudoku game
2. 🔍 Applies my dad's custom algorithm
3. ✅ Attempts to solve the puzzle
4. 📊 Shows the results

We want to test if **any Sudoku can be solved** using this algorithm!

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.8 or higher
- UV package manager

### 🔧 Installation

1. **Install UV** (if you haven't already):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install the project dependencies**:
   ```bash
   uv sync
   ```

3. **Activate the virtual environment**:
   ```bash
   source .venv/bin/activate  # On Linux/Mac
   # or
   .venv\Scripts\activate  # On Windows
   ```

### 🏃 Running the Project

```bash
# Run the Sudoku solver
uv run python -m sudoku_solver
```

## 📁 Project Structure

```
sudoku_solver/
├── src/
│   └── sudoku-solver/
│       └── __init__.py
├── pyproject.toml
└── README.md
```

## 🧩 How It Works

1. **Input**: A Sudoku grid (sheet) with initial numbers
2. **Processing**: Apply the custom algorithm created by my dad
3. **Output**: Solved Sudoku puzzle (if solvable)

## 👨‍👦 A Special Collaboration

This project represents a beautiful collaboration between:
- **Dad**: Algorithm design and theory 🧠
- **Me**: Python implementation and teaching 💻

It's been an amazing experience teaching my dad Python while working together on something we both enjoy! 🎉

## 📝 Notes

- Started: December 25th
- Purpose: Test if any Sudoku can be solved with the custom algorithm
- Fun fact: This project helped my dad learn Python basics! 🐍

---

Made with ❤️ by Rafael and Dad on December 25th 🎄

