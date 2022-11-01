import os
import game


#вызывает меню
def main_menu():
    """
    Показывает главное меню
    Из него начинается игра или заканчивается программа
    TODO:
        Настройки: цвет текста
        Сохранение/загрузка
    """
    # главный цикл меню, завершается правильным выбором
    while True:
        os.system("cls")
        print(" Меню:\n")
        print("1 - Начать новую игру")
        print("2 - Выйти\n")
        answer = input("Введите номер ответа и нажимите ENTER: ")
        if answer == "1":
            game.start_game()
        elif answer == "2":
            print("Выходим из игры")
            break
    print("Пока!")

if __name__ == "__main__":
    main_menu() # запуск программы
