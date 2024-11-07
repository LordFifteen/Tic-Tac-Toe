#Устанавливаем размер поля
field_size = 3
#Делаем поле с номерами клеток
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]


#Функция для отрисовки игрового поля
def draw_field():
    #Рисуем верхнюю границу
    print("_" * 4 * field_size)
    #Проходим по строкам поля
    for i in range(field_size):
        #Рисуем вертикальные границы
        print((" " * 3 + "|") * 3)
        #Печатаем текущую строку с числами или символами
        print("", field[i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        #Рисуем нижнюю границу
        print(("_" * 3 + "|") * 3)
    pass


#Функция для обработки хода игрока
def steps(number, char):
    #Проверяем, корректен ли ввод и не занята ли клетка
    if number > 9 or number < 1 or field[number - 1] in ("X", "O"):
        return False
    #Записываем символ игрока в поле
    field[number - 1] = char
    return True


#Функция для проверки на выигрыш
def check_for_win():
    combinations_for_win = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  #Горизонтальные линии
        (0, 4, 8), (2, 4, 6),  #Диагонали
        (0, 3, 6), (1, 4, 7), (2, 5, 8)  #Вертикальные линии
    )
    #Проверяем, есть ли совпадения по текущей комбинации
    for position in combinations_for_win:
        if field[position[0]] == field[position[1]] == field[position[2]]:
            return field[position[0]]  #Возвращаем выигравший символ


#Функция для запуска игры
def start_game():
    current_player = "X"  #Начинает игрок X
    step = 1  #Счетчик ходов
    draw_field()  #Рисуем поле

    #Цикл продолжается, пока не сделано 9 ходов
    while step < 9:
        while True:
            #Запрашиваем номер клетки от текущего игрока
            number = input("Player's turn: " + current_player + ". Enter field's number(0-9): ")
            #Проверяем корректность ввода
            if number.isdigit() and (0 <= int(number) <= 9):
                number = int(number)  #Преобразуем ввод в целое число
                break
            else:
                print("Try Again!")  #Если ввод некорректен, запрашиваем снова

        #Проверка на выход из игры
        if number == 0:
            print("Game Over!")  #Сообщение о завершении игры
            return

        #Обрабатываем ход игрока
        if steps(number, current_player):
            step += 1  #Увеличиваем счетчик ходов
            draw_field()  #Отрисовываем обновленное поле
            winner = check_for_win()  #Проверяем, есть ли победитель
            if winner:
                print(winner, "Wins!")  #Сообщаем о победе
                print("Game Over!")  #Сообщение о завершении игры
                return

            # Меняем текущего игрока
            current_player = "0" if current_player == "X" else "X"
        else:
            print("Wrong number! Try Again!")  #Если ход некорректный

    #Если все ходы сделаны, и нет победителя
    print("Game Over! Draw!")


#Приветствие
print("Welcome to the Tic Tac Toe!")
start_game()  #Запускаем игру
