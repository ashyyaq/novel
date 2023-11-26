import random
import json

students = ["студ1", "студ2", "студ3"]

situations = {
    "лекция": "У вас есть выбор: [1] прийти на лекцию, [2] прогулять",
    "экзамен": "Через месяц уже начнутся экзамены: [1] готовиться к экзаменам, [2] отложить все последнего",
    "проект": "Нужно выполнить групповой проект, сколько работы возьмете на себя?: [1] взять на себя больше работы, [2] скинуть все на других"
}

completed_situations = set()

def get_choice(situation):
    print(situation)
    choice = input("Ваш выбор: ")
    return choice

def lecture():
    choice = get_choice(situations["лекция"])
    if choice == "1":
        print("Вы пришли на лекцию, но проспали практически все")
    elif choice == "2":
        print("Вы выбрали быть счастливым и прогуляли лекцию")

def exam():
    choice = get_choice(situations["экзамен"])
    if choice == "1":
        print("Вы успешно сдали экзамены")
    elif choice == "2":
        print("Вы отложили подготовку до последнего момента, сдали так себе")

def project():
    choice = get_choice(situations["проект"])
    if choice == "1":
        print("Вы взяли на себя больше работы, очень устали, зато проект выглядит блестяще")
    elif choice == "2":
        print("Вы переложили все свои обязанности на других, проект выполнен, результаты не самые лучшие, но зато у вас есть халявная оценка")


def save_game():
    with open('save_data.json', 'w') as file:
        save_data = {
            'completed_situations': list(completed_situations),
        }
        json.dump(save_data, file)

def load_game():
    try:
        with open('save_data.json', 'r') as file:
            save_data = json.load(file)
            return save_data['completed_situations']
    except FileNotFoundError:
        return []

def main():
    print("Добро пожаловать в игру 'выживание в мпт'")

    def delete_save():
        confirmation = input("Вы уверены, что хотите удалить сохранение? (yes/no): ")
        if confirmation.lower() == 'yes':
            with open('save_data.json', 'w') as file:
                file.write('')
            print("Сохранение удалено.")
        else:
            print("Удаление отменено.")

    delete_option = input("Хотите удалить сохранение? (yes/no): ")
    if delete_option.lower() == 'yes':
        delete_save()

    loaded_situations = load_game()
    completed_situations.update(loaded_situations)

    while len(completed_situations) < len(situations):
        current_situation = random.choice(list(situations.keys()))

        while current_situation in completed_situations:
            current_situation = random.choice(list(situations.keys()))

        if current_situation == "лекция":
            lecture()
        elif current_situation == "экзамен":
            exam()
        elif current_situation == "проект":
            project()

        completed_situations.add(current_situation)

        save_game()

    print("Игра завершена. Спасибо за участие!")

if __name__ == "__main__":
    main()
