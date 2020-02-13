import random
import time
from logoo import logoPrinting
import menu

logo_Printing

table = [['B','O',' ','O',' '],[' ','O','O',' ',' '],['O','O',' ',' ',' '],[' ','O','O','O',' '],[' ','O',' ','O','M']]
print("""Sterowanie:
W - gora
S - doł
A - lewo
D - prawo

Twoim celem jest doprowadzenie buldozera (B) do mety (M) przesuwajac po drodze skaly tak aby sie nie zablokowac.

""")

def tablePrint(table):
    for x in range(len(table)):
        print(table[0][x] + '|', end='')
    print("\n----------")
    for x in range(len(table)):
        print(table[1][x] + '|', end='')
    print("\n----------")
    for x in range(len(table)):
        print(table[2][x] + '|', end='')
    print("\n----------")
    for x in range(len(table)):
        print(table[3][x] + '|', end='')
    print("\n----------")
    for x in range(len(table)):
        print(table[4][x] + '|', end='')
    print("\n----------")

def moving(table):
    x = 0
    y = 0
    while x != 4 or y != 4:
        tablePrint(table)
        table[x][y] = ' '
        ruch = input().lower()
        if ruch == 'd': #prawo
            try:
                y += 1
                if y == len(table):
                    y -= 1
                    print('Nie wychodz za plansze')
                elif table[x][y] == "O" and table[x][y + 1] == "O":
                    y -= 1
                    print("Dwa kamyczki to za duzo dla takiego malego buldozerka")
                elif table[x][y] == 'O':
                    table[x][y + 1] = 'O'
            except:
                y -= 1
                print("Nie mozna wypchac kamyczka")

        elif ruch == 'a': #lewo
            try:
                y -= 1
                if y == -1:
                    y += 1
                    print('Nie wychodz za plansze')
                elif table[x][y] == "O" and table[x][y - 1] == "O":
                    y += 1
                    print("Dwa kamyczki to za duzo dla takiego malego buldozerka")
                elif table[x][y] == 'O' and y == 0:
                    print('Nie mozna wypchac kamyczka')
                    table[x][y] = 'O'
                    y += 1
                elif table[x][y] == 'O':
                    table[x][y - 1] = 'O'
            except:
                y += 1
                print('Nie mozna wypchac kamyczka')
        elif ruch == 'w': #gora
            try:
                x -= 1
                if x == -1:
                    x += 1
                    print('Nie wychodz za plansze')
                elif table[x][y] == "O" and table[x - 1][y] == "O":
                    x += 1
                    print("Dwa kamyczki to za duzo dla takiego malego buldozerka")
                elif table[x][y] == "O" and x == 0:
                    print('Nie mozna wypchac kamyczka')
                    table[x][y] = "O"
                    x += 1
                elif table[x][y] == "O":
                    table[x - 1][y] = 'O'
            except:
                x += 1
                print('Nie mozna wypchac kamyczka')
        elif ruch == 's': #dol
            try:
                x += 1
                if x == len(table):
                    x -= 1
                    print('Nie wychodz za plansze')
                elif table[x][y] == 'O' and table[x + 1][y] == 'O':
                    x -= 1
                    print("Dwa kamyczki to za duzo dla takiego malego buldozerka")
                elif table[x][y] == "O":
                    table[x + 1][y] = 'O'
            except:
                x -= 1
                print('Nie mozna wypchac kamyczka')
        else:
            print("Nieprawidlowy klawisz")
        table[x][y] = 'B'


moving(table)

tablePrint(table)
print("Gratulacje, doczlapales sie do mety")

time.sleep(30)
