def start_game():
    print("Выживание в МПТ.(Часть 3)")

    while True:
        print_menu(["Начать", "Выйти"])
        choice = input("Выберите действие (1 или 2): ")

        if choice == "1":
            game_state = episode_1()
        elif choice == "2":
            print("\nХорошее решение, до свидания!")
            break
        else:
            print("\nВыберите действие 1 или 2.\n")

def episode_1():
    print("\n5 утра, Вы спокойно спите, но тут же ваш блаженный сон перебивает будильник, Вы встаете с пониманием того, что поездка на пары неизбежна, иначе вас отчислят\n")
    print("Доброе утро, Вы уже собрались для того, чтобы поехать на пару к Кудякову, которую он, возможно, отменит\n")

    while True:
        print_menu(["Спать дальше", "Поехать на пары", "Не пойти на пару к Кудякову", "Вернуться в главное меню"])
        choice = input("Выберите действие (1, 2 или 3): ")

        if choice == "1":
            print("\nВы проигнорировали будильник и решили, что сон важнее. Вас отчислили за большое количество пропущенных часов.")
            return {}
        elif choice == "2":
            print("\nВы поехали к первой паре, но Кудяков её отменил, Вам пришлось просто сидеть всю пару.")
            return {"part_1_choice": "Поехать на пары"}
        elif choice == "3":
            print("\nВместо пары информатики Вы решили пойти поесть, как оказалось препод все равно отменил пару.")
            return {"part_1_choice": "Не пойти на пару к Кудякову"}
        elif choice =="4":
            print("\nВы вернулись в главное меню")
            return {}
        else:
            print("\nПожалуйста, выберите действие 1, 2 или 3.\n")

def print_menu(menu_items):
    for i, item in enumerate(menu_items, start=1):
        print(f"{i}. {item}")

start_game()
