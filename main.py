import random
import tkinter as tk


# Zamienia wartości dwóch kolumn w wierszu board
def swap(board, row, col1, col2):
    board[row][col1], board[row][col2] = board[row][col2], board[row][col1]
    return board


# Symuluje board przez wyznaczoną liczbę iteracji
def simulate_board(board, iterations):
    # Pobiera ilość wierszy i kolumn
    rows = len(board)
    cols = len(board[0])
    for iteration in range(iterations):
        for row in range(rows):
            col1 = random.randint(0, cols - 1)  # losuje indeks pierwszej kolumny
            col2 = random.randint(0, cols - 1)  # losuje indeks drugiej kolumny
            board = swap(board, row, col1, col2)  # zamienia wartości kolumn
    return board


# Wyswietla plansze
# noinspection PyShadowingNames
def display_board(board):
    # noinspection PyShadowingNames
    root = tk.Tk()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                block = tk.Canvas(root, height=50, width=50, bg="yellow")
                block.grid(row=i, column=j)
                label = tk.Label(root, text="Orzeł", bg="yellow", fg="black")
                label.grid(row=i, column=j)
            else:
                block = tk.Canvas(root, height=50, width=50, bg="blue")
                block.grid(row=i, column=j)
                label = tk.Label(root, text="Reszka", bg="blue", fg="white")
                label.grid(row=i, column=j)
    root.mainloop()


# Pobiera dane wejsciowe od użytkownika (liczba wierszy, kolumn i iteracji) i wywołuje funkcję simulate_board
def get_input():
    rows = int(rows_entry.get())
    cols = int(cols_entry.get())
    iterations = int(iterations_entry.get())
    board = [[1 if j < 2 else 0 for j in range(cols)] for _ in range(rows)]
    board = simulate_board(board, iterations)
    display_board(board)


root = tk.Tk()  # Tworzy okno
root.title("Projekt Symulacja orzel-reszka")
# Dodaje etykiete i pole tekstowe dla liczby wierszy
rows_label = tk.Label(root, text="Wprowadź liczbę wierszy")
rows_label.grid(row=0, column=0)
rows_entry = tk.Entry(root)
rows_entry.grid(row=0, column=1)
cols_label = tk.Label(root, text="Wprowadź liczbę kolumn:")
# Umieszczamy label w oknie aplikacji na wierszu 1 i kolumnie 0
cols_label.grid(row=1, column=0)
# Tworzymy Entry widget do wprowadzenia ilości kolumn
cols_entry = tk.Entry(root)
# Umieszczamy widget w oknie aplikacji na wierszu 1 i kolumnie 1
cols_entry.grid(row=1, column=1)
# Tworzymy label do wprowadzenia liczby powtórzeń
iterations_label = tk.Label(root, text="Wpisz liczbę powtórzeń algorytmu:")
# Umieszczamy label w oknie aplikacji na wierszu 2 i kolumnie 0
iterations_label.grid(row=2, column=0)
# Tworzymy Entry widget do wprowadzenia liczby powtórzeń
iterations_entry = tk.Entry(root)
# Umieszczamy widget w oknie aplikacji na wierszu 2 i kolumnie 1
iterations_entry.grid(row=2, column=1)
# Tworzymy przycisk do wysłania danych
submit_button = tk.Button(root, text="Zatwierdź", command=get_input)
# Umieszczamy przycisk w oknie aplikacji na wierszu 3 i kolumnie 1
submit_button.grid(row=3, column=1)
# Uruchamiamy pętlę okna
root.mainloop()
