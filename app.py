# Устанавливаем размер поля для игры в "Крестики-нолики"
field_size = 3
# Делаем поле с номерами клеток
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Функция для отрисовки игрового поля
def draw_field():
    print("_" * 4 * field_size) # Рисуем верхнюю границу
    for i in range(field_size):
        print((" " * 3 + "|") * 3) # Рисуем вертикальные границы
        print("", field[i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|") # Печатаем текущую строку с числами или символами
        print(("_" * 3 + "|") * 3) # Рисуем нижнюю границу
    pass
# Функция для обработки хода игрока
def steps(number, char):
    # Проверяем, корректен ли ввод и не занята ли клетка
    if number > 10 or number < 1 or field[number - 1] in ("X", "O"):
        return False
    field[number - 1] = char # Записываем символ игрока в поле
    return True

# Функция для проверки на выигрыш
def check_for_win():
    # Все возможные выигрышные комбинации
    win_or_lose = False
    combinations_for_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8),
                            (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
    # Проверяем, есть ли совпадения по текущей комбинации
    for position in combinations_for_win:
        if field[position[0]] == field[position[1]] and field[position[1]] == field[position[2]]:
            win_or_lose = field[position[0]] # Возвращаем выигравший символ


    return win_or_lose
# Функция для запуска игры
def start_game():
    current_player = "X" # Начинает игрок "X"
    step = 1 # Счетчик ходов
    draw_field() # Рисуем поле

    while step < 10 and (check_for_win() == False): # Игра продолжается, пока не сделано 9 ходов
        verify = 0
        while verify != 1:
            number = input("Player's turn: " + current_player + ". Enter field's number(0-9): ")
            if str(number).isdigit():
                verify = 1
            else:
                print("Try Again!")
        # Проверка на выход из игры
        if number == 0:
            break
        if steps(int(number), current_player):
            if current_player == "X": # Меняем текущего игрока
                current_player = "O"
            else:
                current_player = "X"
            draw_field()
            step += 1 # Увеличиваем счетчик ходов
        else:
            print("Wrong number! Try Again!") # Если ход некорректный
    if step == 10:
        print("Game Over! Draw!") # Если все ходы сделаны, и нет победителя
    else:
        print(check_for_win() + " Wins!") # Объявляем победителя
        print("Game Over!")

print("Welcome to the Tic Tac Toe!")
start_game()