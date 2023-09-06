# Тестовое задание (EffectiveMovile)

+ Реализован телефонный справочник со следующими возможностями:
  
  + Вывод постранично записей из справочника на экран

    + Открывает файл data.txt для чтения и печатает данные на экран:
    
        ```python
        def show_entries(filename: str) -> None:
      """Данная функция выводит на экран данные которые содержатся в файле data.txt"""
  
      with open(filename, "r", encoding="utf-8") as data:
          if phone_book := data.read():
              print("№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона")
              print(phone_book)
          else:
              print(f"Файл {filename} пуст")
  
    + Данные справочника:
      
       >  ``` 
       > №   | ФИО                         | Организация | Рабочий номер телефона | Личный номер телефона
       > 1.  | Иванов Иван Иванович        | HomeBank    | 8754612658             | 8741646135
       > 2.  | Петров Петр Петрович        | Школа       | 8454545454             | 8700344523
       > 3.  | Николаев Николай Николаевич | Детсад      | 87565445612            | 896452622336
       > 4.  | Мясников Егор Александрович | Kaspi       | 875454165461           | 75568741265
       > 5.  | Иванов Иван Иванович        | HomeBank    | 8754612658             | 8741646135
       > 6.  | Петров Петр Петрович        | Школа       | 8454545454             | 8700344523
       > 7.  | Николаев Николай Николаевич | Детсад      | 87565445612            | 896452622336
       > 8.  | Мясников Егор Александрович | Kaspi       | 875454165461           | 75568741265
       > 9.  | Егоров Антон Антонович      | Автоцентр   | 8546561225             | 456531546
       > 10. | Александров Петр Евгенивич  | Музей       | 8756684566             | 558458784
     

  + Добавление новой записи в справочник
    + Открывает файл data.txt для чтения, № строки сохраняются в переменную `contact_num`:

      ```python
      def export_entries(filename: str) -> None:
          """Данная функция записывает данные введенные пользователем, после сохраняет их в файл data.txt"""
          try:
              with open(filename, "r", encoding="utf-8") as data:
                  phone_book = data.read()
          except FileNotFoundError:
              print(f"File not found: {filename}")
              return
          contact_num = len(phone_book.split("\n"))
      ```
    + Открывает файл data.txt для записи, переменная `data` записывает в файл данные введеные пользователем:
    
      ```python
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
      ```
    
  + Возможность редактирования записей в справочнике
 
    + Открывает файл data.txt для чтения, данные из файла сохраняются в переменную `phone_book_data`:
       
      ```python
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
      ```
         
    + Данные из файла преобразуются в список, переменная `edit_phone_book_lines` сохраняет данные выбранной для изменения строки, если пользователь во время редактирования оставил поля пустыми, то данные останутся прежними:

         ```python
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
         
                
    + Изменённые данные сохраняются в переменную `edited_line`, а после преобразуются из списка в строку. Открывает файл для записи и заменяют данные в файле data.txt:
    
        ```python
        edited_line = f"{contact_num} | {contact_name} | {company_name} | {work_phone_number} | {self_phone_number}"
        phone_book_lines[index_edit_data] = edited_line
        print(f"Запись — {edit_phone_book_lines}, изменена на — {edited_line}\n")
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("\n".join(phone_book_lines))
        except FileNotFoundError:
            print(f"File not found: {filename}")
             ```

  + Поиск записей по одной или нескольким характеристикам

    + Открывает файл data.txt для чтения:

      ```python
      
      def search_entries(filename: str) -> None:
            """Данная функция ищет данные в файле data.txt по параметрам которые ввёл пользователь."""
            try:
                with open(filename, "r", encoding="utf-8") as data:
                    phone_book = data.readlines()
            except FileNotFoundError:
                print(f"File not found: {filename}")
                return
      ```
    + Данные файла преобразуются из строки в список, в цикле `for` данные которые ввел пользователь, перебираются пока не найдется совпадение:

      ```python
        flag = False
        data_search = input('Введите данные для поиска: ').title()
        print("№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона\n")
    
        for line in phone_book:
            if data_search in line:
                flag = True
                print(line)
    
        if not flag:
            print('Контакт не найден!\n')
  
      ```
    + Словарь для хранения опций меню
    
      ```python   
         MENU_OPTIONS = {
            1: show_entries,
            2: export_entries,
            3: edit_entries,
            4: search_entries, 
    + В функции `main` находится цикл который, вызывает функции опций в зависимости от введенной пользователем опции:
      ```python
       def main():
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

    + Функция `print_menu`:
      ```python
          def print_menu():
              print("\nВыберите одну из опций:")
              print("1 – Вывести справочник на экран")
              print("2 – Добавить данные в справочник")
              print("3 – Изменить данные в справочнике")
              print("4 – Поиск данных в справочнике")
              print("0 – Выход из программы\n")
    
    + Функция `get_menu_option`:
      ```python
          def get_menu_option():
              while True:
                  try:
                      return int(input("Опция: "))
                  except ValueError:
                      print("Введите номер опции!")
      
+ Требования к программе:
  + Реализация интерфейса через консоль (без веб- или графического интерфейса)
  + Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
  + В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)

