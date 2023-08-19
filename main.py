def show_data(filename: str):
    """Данная функция выводит на экран данные которые содержатся в файле data.txt"""

    with open(filename, "r", encoding="utf-8") as data:
        data_read = data.read()
        if len(data_read) != 0:
            print("\n№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона")
            print(data_read)
        else:
            print(f"Файл {filename} пуст")


def export_data(filename: str):
    """Данная функция записывает данные введенные пользователем, после сохраняет их в файл data.txt"""

    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()

    num = len(tel_file.split("\n"))

    with open(filename, "a", encoding="utf-8") as data:
        fio: str = input("Введите ФИО: ").title()
        company_name = input("Введите название организации: ").title()
        work_phone_number = input("Введите рабочий номер телефона: ")
        self_phone_number = input("Введите личный номер телефона: ")

        try:
            data.write(f"{num} | {fio} |  {company_name} | {work_phone_number} | {self_phone_number}\n")
        except Exception:
            print("Не удалось добавить запись")
            return

        print(f"Добавлена запись : {num} | {fio} | {company_name} | {work_phone_number} | {self_phone_number}\n")


def edit_data(filename: str):
    """Данная функция изменяет данные в файле data.txt на те что ввёл пользователь."""

    print("\n№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
    print(tel_book)

    try:
        index_edit_data = int(input("Введите номер строки для редактирования: ")) - 1
    except Exception:
        return print("Введен некорректный номер строки!!!")

    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_edit_data]
    elements = edit_tel_book_lines.split(" | ")

    fio: str = input("Введите ФИО: ").title()
    company_name = input("Введите название организации: ").title()
    work_phone_number = input("Введите рабочий номер телефона: ")
    self_phone_number = input("Введите личный номер телефона: ")

    num = elements[0]

    if not fio:
        fio = elements[1]
    if not company_name:
        company_name = elements[2]
    if not work_phone_number:
        work_phone_number = elements[3]
    if not self_phone_number:
        self_phone_number = elements[4]

    edited_line = f"{num} | {fio} | {company_name} | {work_phone_number} | {self_phone_number}"
    tel_book_lines[index_edit_data] = edited_line
    print(f"Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(tel_book_lines))


def delete_data(filename: str):
    """Данная функция удаляет выбранный контакт из файла data.txt"""

    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
    print("\n№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона")
    print(tel_book)

    try:
        index_delete_data = int(input("Введите номер строки для удаления: \n")) - 1
    except Exception:
        print("\nВведен некорректный номер строки!!!\nПопробуйте ещё раз.")
        return delete_data(filename)

    tel_book_lines = tel_book.split("\n")

    try:
        del_tel_book_lines = tel_book_lines[index_delete_data]
    except Exception:
        print("Номер не найден")
        return

    tel_book_lines.pop(index_delete_data)

    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(filename, "w", encoding="utf-8") as data:
        data.write("\n".join(tel_book_lines))


def search_data(filename: str):
    """Данная функция ищет данные в файле data.txt по параметрам которые ввёл пользователь."""

    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()

    flag = 1
    data_search = input('Введите данные для поиска: ').title()
    tel_book_lines = tel_book.split("\n")
    print("\n№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона\n")

    for line in tel_book_lines:
        if data_search in line:
            flag = 0
            print(line)
    if flag:
        print('Контакт не найден!\n')


def main():
    """Основная функция main в которой создается файл data.txt, если он ещё не был  создан. Также в ней находится
    цикл который вызывает все другие функции."""

    my_choice = -1
    file_tel = "data.txt"

    with open(file_tel, "a", encoding="utf-8") as file:
        file.write("")
    while my_choice != 0:
        print("\n Выберите одну из опций:")
        print("1 — Вывести справочник на экран")
        print("2 — Добавить данные в справочник")
        print("3 — Изменить данные в справочнике")
        print("4 — Поиск данных в справочнике")
        print("5 — Удалить данные из справочника")
        print("0 — Выход из программы\n")

        try:
            action = int(input("Опция: "))
        except Exception:
            print("Введите номер опции!")
            return main()

        if action == 1:
            show_data(file_tel)
        elif action == 2:
            export_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            search_data(file_tel)
        elif action == 5:
            delete_data(file_tel)
        else:
            my_choice = 0


if __name__ == "__main__":
    main()