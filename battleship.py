from random import randint
# tworzenie funckji potrzebnych do gry i ustawien domyslnych
moves = 4
size_board = 5
number = 1
temp_board = []
def print_board(board):
  for row in board:
    print " ".join(row)
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)
def placing_ships(number):
    for x in range(size_board):
        temp_board.append(["O"] * size_board)

    ran_row = 0
    ran_col = 0
    count = 0
    for x in range(number):
        while count < number:
            ran_row = randint(0, len(temp_board) - 1)
            ran_col = randint(0, len(temp_board) - 1)
            print ran_row,
            print ran_col
            if temp_board[ran_row][ran_col] == "X" or temp_board[ran_row][ran_col] == "Z":
                continue
            else:
                temp_board[ran_row][ran_col] = "X"
                count = count + 1
                if ran_row == 0:
                    if ran_col == 0:
                        temp_board[ran_row + 1][ran_col] = "Z"
                        temp_board[ran_row][ran_col + 1] = "Z"
                        temp_board[ran_row + 1][ran_col + 1] = "Z"
                    elif ran_col == len(temp_board) - 1:
                        temp_board[ran_row + 1][ran_col] = "Z"
                        temp_board[ran_row][ran_col - 1] = "Z"
                        temp_board[ran_row + 1][ran_col - 1] = "Z"
                    else:
                        temp_board[ran_row][ran_col - 1] = "Z"
                        temp_board[ran_row][ran_col + 1] = "Z"
                        temp_board[ran_row + 1][ran_col] = "Z"
                        temp_board[ran_row + 1][ran_col + 1] = "Z"
                        temp_board[ran_row + 1][ran_col - 1] = "Z"
                elif ran_row == len(temp_board) - 1:
                    if ran_col == 0:
                        temp_board[ran_row - 1][ran_col] = "Z"
                        temp_board[ran_row][ran_col + 1] = "Z"
                        temp_board[ran_row - 1][ran_col + 1] = "Z"
                    elif ran_col == len(temp_board) - 1:
                        temp_board[ran_row - 1][ran_col] = "Z"
                        temp_board[ran_row][ran_col - 1] = "Z"
                        temp_board[ran_row - 1][ran_col - 1] = "Z"
                    else:
                        temp_board[ran_row - 1][ran_col] = "Z"
                        temp_board[ran_row][ran_col + 1] = "Z"
                        temp_board[ran_row][ran_col - 1] = "Z"
                        temp_board[ran_row - 1][ran_col - 1] = "Z"
                        temp_board[ran_row - 1][ran_col + 1] = "Z"
                elif ran_col == 0:
                    temp_board[ran_row - 1][ran_col] = "Z"
                    temp_board[ran_row + 1][ran_col] = "Z"
                    temp_board[ran_row][ran_col + 1] = "Z"
                    temp_board[ran_row + 1][ran_col + 1] = "Z"
                    temp_board[ran_row - 1][ran_col + 1] = "Z"
                elif ran_col == len(temp_board) - 1:
                    temp_board[ran_row - 1][ran_col] = "Z"
                    temp_board[ran_row + 1][ran_col] = "Z"
                    temp_board[ran_row][ran_col - 1] = "Z"
                    temp_board[ran_row + 1][ran_col - 1] = "Z"
                    temp_board[ran_row - 1][ran_col - 1] = "Z"
                else:
                    temp_board[ran_row + 1][ran_col] = "Z"
                    temp_board[ran_row - 1][ran_col] = "Z"
                    temp_board[ran_row][ran_col + 1] = "Z"
                    temp_board[ran_row][ran_col - 1] = "Z"
                    temp_board[ran_row + 1][ran_col + 1] = "Z"
                    temp_board[ran_row + 1][ran_col - 1] = "Z"
                    temp_board[ran_row - 1][ran_col + 1] = "Z"
                    temp_board[ran_row - 1][ran_col - 1] = "Z"

    return temp_board
# tworzenie menu gry

menu_default = 0

while menu_default == 0:
    temp_board = []
    moves_2 = moves
    board = []
    for x in range(size_board):
        board.append(["O"] * size_board)
    menu_a = 1
    menu_b = 2
    choose = raw_input("""Witaj w grze statki.
1 - Start gry
2 - Opcje
Rozmiar planszy - """ + str(size_board) + 'x' + str(size_board) + ', ilosc tur - ' + str(moves) + ', ilosc statkow - ' + str(number))
    if int(choose) == 2:
        opt_a = 1
        opt_b = 2
        opt_c = 3
        choose_opt = raw_input("""Wybierz jedna z opcji:
1 - rozmiar planszy
2 - ilosc statkow
3 - ilosc tur gry
Dowolny inny klawisz - powrot do menu startowego
""")
        if int(choose_opt) == opt_a:
            size_board = raw_input("Wybierz rozmiar planszy")       #tu cos zrobic zeby nie wywalalo bledu
            if int(size_board) > 0:
                size_board = int(size_board)
            else:
                print "Niewlasciwy rozmiar planszy"
        elif int(choose_opt) == opt_c:
            moves = int(raw_input("Wybierz ilosc tur gry"))         #tu to samo, blad wywala zdebugowac
            if moves > 0:
                continue
            else:
                print "Niewlasciwa ilosc ruchow"
        elif int(choose_opt) == opt_b:
            print "wtf"
            number = int(raw_input("Podaj ilosc statkow"))
    elif int(choose) == 1:
        placing_ships(number)
        print_board(temp_board)
        print " "
        print_board(board)
        ships_left = number

        while moves_2 > 0 and ships_left > 0:
            print "You have " + str(moves_2) + " turns to guess where i put the battleship ;P"
            guess_col = int(raw_input("Guess Col: "))
            guess_row = int(raw_input("Guess Row: "))
            guess_col -= 1
            guess_row -= 1
            if (board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
                moves_2 -= 1
            elif temp_board[guess_row][guess_col] == "X":
                board[guess_row][guess_col] = "X"
                ships_left -= 1
                if ships_left == 0:
                    print "Gratulacje! Zwyciestwo."
                    break
                else:
                    print "Trafiony! Strzelaj dalej"
            else:
                if moves_2 == 1:
                    print "Game Over"
                    break
                elif (guess_row < 0 or guess_row > len(board)) or (guess_col < 0 or guess_col > len(board)):
                    print "Oops, that's not even in the ocean."
                    moves_2 -= 1
                else:
                    print "You missed my battleship!"
                    board[guess_row][guess_col] = "X"
                    moves_2 -= 1

            print_board(board)
    else:
        print "Nie wybrales zadnej opcji lub niewlasciwa. Wracam do menu"
