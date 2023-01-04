def greet():
    print(" Добро пожаловать")
    print("      в игру     ")
    print("КРЕСТИКИ - НОЛИКИ!")
    print("Ввод: x, y")
    print("x - номер строки")
    print("y - номер столбца")

game_field = [[" ", " ", " "] for i in range(3)]


def game():
    print(" ")
    print("   | 0 | 1 | 2 |")
    print("  _______________")
    for i, row in enumerate(game_field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("  _______________")
    print()


def ask():
    while True:
        cords = input("Можете сделать ход: ").split()
        if len(cords) != 2:
            print("Дружище, нужны только 2 числа! ")
            continue
        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Числами, будьте добры. ")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Вне поля играть нельзя! ")
            continue
        if game_field[x][y] != " ":
            print("Место занято! ")
            continue

        return x, y

num = 0
while True:
    num += 1

    game()

    if num % 2 == 1:
        print("Ход крестик: ")
    else:
        print("Ход нолик: ")

    x, y = ask()

    if num % 2 == 1:
        game_field[x][y] = "x"
    else:
        game_field[x][y] = "0"

    if num == 9:
        print("Ничья! ")
        break

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (2, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(game_field[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print("Победа КРЕСТИКА!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победа НОЛИКА!")
            return True
    return False

greet()
count = 0
game_field = [[" ", " ", " "] for i in range(3)]
while True:
    count += 1
    game()
    if count % 2 == 1:
        print("Ходит крестик! ")
    else:
        print("Ходит нолик! ")

    x, y = ask()

    if count % 2 == 1:
        game_field[x][y] = "x"
    else:
        game_field[x][y] = "0"

    if check_win():
        break


    if count == 9:
        print("Ничья!")
        break



