import os


def in_shop(player_name, player_money, player_xp, player_hp, player_mp, player_damage, player_potions):
    while True:
        os.system("cls")
        #печатаем персонажа
        print("Состояние персонажа:")
        print(f"Имя: {player_name}")
        print(f"Деньги: {player_money}")
        print(f"Опыт: {player_xp}")
        print(f"HP: {player_hp}")
        print(f"MP: {player_mp}")
        print(f"АТК: {player_damage}")
        print(F"Зелья: {player_potions}\n")

        #печатаем ситуацию
        print(f"{player_name} приехал в лавку снаряжения\n")

        #печатаем выборы
        print("1 - Купить зелье лечения за 3 монеты")
        print("2 - Выйти из лавки обратно в город\n")

        # проверяем выбор
        answer = input("Введите номер варианта и нажмите ENTER: ")
        if answer == "1":
            if player_money >= 3:
                player_money -= 3
                player_potions += 1
                return(player_money, player_potions)

            else:
                print("Недостаточно монет!")
        elif answer == "2":
            break



