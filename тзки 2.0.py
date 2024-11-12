def create_matrix(text, rows, cols):
    """Создает матрицу для текста."""
    matrix = [[""] * cols for _ in range(rows)]
    index = 0
    for r in range(rows):
        for c in range(cols):
            if index < len(text):
                matrix[r][c] = text[index]
                index += 1
    return matrix

def encrypt(text, row_order, col_order):
    """Шифрование текста методом двойной перестановки."""
    rows, cols = len(row_order), len(col_order)
    text = text.ljust(rows * cols, "_")  # Дополнение символами, чтобы матрица была полной
    matrix = create_matrix(text, rows, cols)

    # Перестановка строк
    matrix = [matrix[i] for i in row_order]
    # Перестановка столбцов
    matrix = [[row[i] for i in col_order] for row in matrix]

    # Преобразование обратно в строку
    return "".join("".join(row) for row in matrix)

def decrypt(text, row_order, col_order):
    """Дешифрование текста методом двойной перестановки."""
    rows, cols = len(row_order), len(col_order)
    matrix = create_matrix(text, rows, cols)

    # Обратная перестановка столбцов
    reverse_col_order = [col_order.index(i) for i in range(len(col_order))]
    matrix = [[row[i] for i in reverse_col_order] for row in matrix]
    # Обратная перестановка строк
    reverse_row_order = [row_order.index(i) for i in range(len(row_order))]
    matrix = [matrix[i] for i in reverse_row_order]

    # Преобразование обратно в строку
    return "".join("".join(row) for row in matrix).rstrip("_")

if __name__ == "__main__":
    # Входные данные
    text = "ПРИВЕТМИР"
    row_order = [2, 0, 1]  # Порядок перестановки строк
    col_order = [3, 0, 2, 1]  # Порядок перестановки столбцов

    print(f"Исходный текст: {text}")

    # Шифрование
    encrypted = encrypt(text, row_order, col_order)
    print(f"Зашифрованный текст: {encrypted}")

    # Дешифрование
    decrypted = decrypt(encrypted, row_order, col_order)
    print(f"Расшифрованный текст: {decrypted}")
