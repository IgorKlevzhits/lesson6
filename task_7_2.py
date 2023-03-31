def print_operation_table(operation, num_rows=6, num_columns=6):
    # Напечатать заголовок таблицы
    print("  ", end="")
    for j in range(1, num_columns + 1):
        print(j, end=" ")
    print()
    
    # Напечатать разделительную строку
    print(" +" + "-+" * num_columns)
    
    # Напечатать таблицу
    for i in range(1, num_rows + 1):
        print(i, end="|")
        for j in range(1, num_columns + 1):
            print(operation(i, j), end=" ")
        print()

# Определение функции, которая перемножает номера строк и столбцов
def mult(x, y):
    return x * y

# Печать таблицы умножения
print_operation_table(mult)

print()
# Печать таблицы сложения размером 4x4
print_operation_table(lambda x, y: x + y, num_rows=4, num_columns=4)

