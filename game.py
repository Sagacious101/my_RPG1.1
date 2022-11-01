import os
import shop #импортируем файл shop.py





def start_game():
    """
    Создаёт персонажа:
        player_name - имя игрока
        player_money - деньги игрока
        player_xp - опыт игрока
        player_hp - жизни игрока, >= 0 иначе игра заканчивается
        player_mp - мана персонажа
        player_damage - урон игрока
        player_potions - зелья лечения здоровья
            Doto:
        player_items - вещи игрока
    Запускает игру
    Игра контролируется переменной is_game
    """
    os.system("cls")
    player_money = 5
    player_xp = 0
    player_hp = 20
    player_mp = 20
    player_damage = 3
    player_potions = 3
    player_name = input("Введите имя игрока и нажмите ENTER: ")
    if not player_name: player_name = "Богатырь"
    os.system("cls")

    #главный цикл игры
    is_game = True
    while is_game:
        os.system("cls")
        print("Персонаж: ")
        print(f"Имя: {player_name}")
        print(f"Деньги: {player_money}")
        print(f"Опыт: {player_xp}")
        print(f"HP: {player_hp}")
        print(f"MP: {player_mp}")
        print(f"АТК: {player_damage}")
        print(F"Зелья: {player_potions}\n")
        # показываем вариант
        print(f"{player_name} приехал в стартовый город.")
        print("0 - Выйти в главное меню")
        print("1 - Поехать в магический лес")
        print("2 - Поехать играть в кости")
        print("3 - поехать в лавку снаряжения\n")
        answer = input("Введите номер ответа и нажмите ENTER: ")

        #проверяем ответ
        if answer == "0":
            break
        elif answer == "1":
            print("Вы прибыли в магический лес")
        elif answer == "2":
            print("Вы приехали играть в кости")
        elif answer == "3":
            shop.in_shop(player_name, player_money, player_xp, player_hp, player_mp, player_damage, player_potions)
            player_money == shop(player_money)
            player_potions == shop(player_potions)

if __name__ == "__main__":
    print("Этот модуль запустили не посредственно")
