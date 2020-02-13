import os
import shelve
import string
import random
import pyperclip

data = shelve.open('userpasswords')

def randomPassword():
    password = ''
    for x in range(12):
        password += random.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+')
    return password

answer = '0'
while answer == '0':
    print("""Wybierz operację:
1 - Wygenerowanie nowego hasla dla nowego lub istniejacego uzytkownika
2 - Wyswietlenie aktualnych uzytkownikow posiadajacych hasla
3 - Kasowanie istniejącego użytkownika""")
    answer = input()
    if answer == '1':
        print('Podaj nazwe uzytkownika:\n')
        try:
            username = input()
            userpassword = randomPassword()
            data[username] = userpassword
            print('\nPomyslnie wygenerowano haslo\n')
        except:
            print('Cos poszlo nie tak\n\n')
        answer = '0'
    elif answer == '2':
        for key in (data.keys()):
            print(key)
        print("\nWybierz uzytkownika aby skopiowac haslo do schowka")
        try:
            userChoice = input()
            pyperclip.copy(data[userChoice])
            print('\nPomyslnie skopiowano haslo\n')
        except:
            print('Cos poszlo nie tak\n\n')
        answer = '0'
    elif answer == '3':
        print('\nWybierz uzytkownika do EKSTERMINACJI\n')
        for key in (data.keys()):
            print(key)
        try:
            delChoice = input()
            del data[delChoice]
            print('\nPomyślnie usunięto użytkownika\n')
        except:
            print('Cos poszlo nie tak\n\n')
        answer = '0'
    else:
        print('Niewlasciwy wybor. Wracam do menu')
        answer = '0'
