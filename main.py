import random
import json
import csv

situations = {
    "лекция": "У вас есть выбор: [1] прийти на лекцию, [2] прогулять",
    "экзамен": "Через месяц уже начнутся экзамены: [1] готовиться к экзаменам, [2] отложить все последнего",
    "проект": "Нужно выполнить групповой проект, сколько работы возьмете на себя?: [1] взять на себя больше работы, [2] скинуть все на других"
}

completed_situations = set()
csv_file = 'save_data.csv'

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


def save_game_to_json():
    with open('save_data.json', 'w') as file:
        save_data = {
            'completed_situations': list(completed_situations),
        }
        json.dump(save_data, file)

def save_game_to_csv():
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['completed_situation'])
        for situation in completed_situations:
            writer.writerow([situation])

def load_game_from_json():
    try:
        with open('save_data.json', 'r') as file:
            save_data = json.load(file)
            return save_data['completed_situations']
    except FileNotFoundError:
        return []

def load_game_from_csv():
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                completed_situations.add(row[0])
    except FileNotFoundError:
        pass

def main():
    print("Добро пожаловать в игру 'выживание в мпт'")

    def delete_save():
        confirmation = input("Вы уверены, что хотите удалить сохранение? (yes/no): ")
        if confirmation.lower() == 'yes':
            if csv_file:
                open(csv_file, 'w').close()  # Clear the CSV file
            with open('save_data.json', 'w') as file:
                file.write('')
            print("Сохранение удалено.")
        else:
            print("Удаление отменено.")

    delete_option = input("Хотите удалить сохранение? (yes/no): ")
    if delete_option.lower() == 'yes':
        delete_save()

        load_game_from_csv()

    loaded_situations = load_game_from_json()
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

        save_game_to_json()
        save_game_to_csv()

    print("Игра завершена. Спасибо за участие!")

if __name__ == "__main__":
    main()
