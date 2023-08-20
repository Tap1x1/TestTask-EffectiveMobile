def show_entries(filename: str) -> None:
    """Данная функция выводит на экран данные которые содержатся в файле data.txt"""

    with open(filename, "r", encoding="utf-8") as data:
        if phone_book := data.read():
            print("№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона")
            print(phone_book)
        else:
            print(f"Файл {filename} пуст")


def export_entries(filename: str) -> None:
    """Данная функция записывает данные введенные пользователем, после сохраняет их в файл data.txt"""
    try:
        with open(filename, "r", encoding="utf-8") as data:
            phone_book = data.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return
    contact_num = len(phone_book.split("\n"))
    try:
        with open(filename, "a", encoding="utf-8") as data:
            contact_name = input("Введите ФИО: ").title()
            company_name = input("Введите название организации: ").title()
            work_phone_number = input("Введите рабочий номер телефона: ")
            self_phone_number = input("Введите личный номер телефона: ")

            data.write(f"{contact_num} | {contact_name} |  {company_name} | {work_phone_number} "
                       f"| {self_phone_number}\n")
            print(f"Добавлена запись : {contact_num} | {contact_name} | {company_name} | {work_phone_number} "
                  f"| {self_phone_number}\n")
    except Exception as e:
        print("Не удалось добавить запись", e)
        return


def edit_entries(filename: str) -> None:
    """Данная функция изменяет данные в файле data.txt на те что ввёл пользователь."""

    try:
        with open(filename, "r", encoding="utf-8") as data:
            phone_book_data = data.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    print("№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона")
    print(phone_book_data)

    try:
        index_edit_data = int(input("Введите номер строки для редактирования: ")) - 1
    except ValueError:
        print("Введен некорректный номер строки!!!")
        return

    phone_book_lines = phone_book_data.split("\n")
    edit_phone_book_lines = phone_book_lines[index_edit_data]
    elements = edit_phone_book_lines.split(" | ")

    contact_name = input("Введите ФИО: ").title() or elements[1]
    company_name = input("Введите название организации: ").title() or elements[2]
    work_phone_number = input("Введите рабочий номер телефона: ") or elements[3]
    self_phone_number = input("Введите личный номер телефона: ") or elements[4]
    contact_num = elements[0]

    edited_line = f"{contact_num} | {contact_name} | {company_name} | {work_phone_number} | {self_phone_number}"
    phone_book_lines[index_edit_data] = edited_line
    print(f"Запись — {edit_phone_book_lines}, изменена на — {edited_line}\n")
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(phone_book_lines))
    except FileNotFoundError:
        print(f"File not found: {filename}")


def search_entries(filename: str) -> None:
    """Данная функция ищет данные в файле data.txt по параметрам которые ввёл пользователь."""
    try:
        with open(filename, "r", encoding="utf-8") as data:
            phone_book = data.readlines()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    flag = False
    data_search = input('Введите данные для поиска: ').title()
    print("№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона\n")

    for line in phone_book:
        if data_search in line:
            flag = True
            print(line)

    if not flag:
        print('Контакт не найден!\n')


"""Словарь для хранения опций меню"""
MENU_OPTIONS = {
    1: show_entries,
    2: export_entries,
    3: edit_entries,
    4: search_entries,
}


def main():
    """Основная функция main в которой создается файл data.txt, если он ещё не был создан. Также в ней находится
    цикл который, вызывает функции в зависимости от выбранной пользователем опции."""

    file_phone = "data.txt"
    initialize_file(file_phone)

    while True:
        print_menu()
        action = get_menu_option()

        if action in MENU_OPTIONS:
            func = MENU_OPTIONS[action]
            func(file_phone)
        elif action == 0:
            break
        else:
            print("Неверный вариант. Пожалуйста, введите правильный вариант меню")


def initialize_file(file_name):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("")


def print_menu():
    print("\nВыберите одну из опций:")
    print("1 – Вывести справочник на экран")
    print("2 – Добавить данные в справочник")
    print("3 – Изменить данные в справочнике")
    print("4 – Поиск данных в справочнике")
    print("0 – Выход из программы\n")


def get_menu_option():
    while True:
        try:
            return int(input("Опция: "))
        except ValueError:
            print("Введите номер опции!")


if __name__ == "__main__":
    main()
