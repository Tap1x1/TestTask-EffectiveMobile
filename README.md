# Тестовое задание (EffectiveMovile)

+ Реализован телефонный справочник со следующими возможностями:
  
  + Вывод постранично записей из справочника на экран

    + Открывает файл data.txt для чтения и печатает данные на экран:
    
        ```python
        def show_data(filename: str):
        """Данная функция выводит на экран данные которые содержатся в файле data.txt"""
     
        with open(filename, "r", encoding="utf-8") as data:
            data_read = data.read()
            if len(data_read) != 0:
                print("\n№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона")
                print(data_read)
            else:
                print(f"Файл {filename} пуст")
            ```
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
    + Открывает файл data.txt для чтения, № строки сохраняются в переменную `num`:

      ```python
      
       def export_data(filename: str):
       """Данная функция записывает данные введенные пользователем, после сохраняет их в файл data.txt"""
   
       with open(filename, "r", encoding="utf-8") as data:
           tel_file = data.read()
   
       num = len(tel_file.split("\n"))
      ```
    + Открывает файл data.txt для записи, переменная `data` записывает в файл данные введеные пользователем:
    
      ```python
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
      ```
    
  + Возможность редактирования записей в справочнике
 
    + Открывает файл data.txt для чтения, данные из файла сохраняются в переменную `tel_book`:
       
         ```python
             def edit_data(filename: str):
            """Данная функция изменяет данные в файле data.txt на те что ввёл пользователь."""
        
            print("\n№ | ФИО | Организация | Рабочий номер телефона | Личный номер телефона")
            with open(filename, "r", encoding="utf-8") as data:
                tel_book = data.read()
            print(tel_book)
         
    + Данные из файла преобразуются в список, переменная `edit_tel_book_lines` сохраняет данные выбраной для изменения строки:

       ```python
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
        ```
       
     + Условие, если пользователь во время редактирования оставил поля пустыми, то данные остануться прежними:
         
          ```python
              num = elements[0]
          
              if not fio:
                  fio = elements[1]
              if not company_name:
                  company_name = elements[2]
              if not work_phone_number:
                  work_phone_number = elements[3]
              if not self_phone_number:
                  self_phone_number = elements[4]
         ```
          
      + Изменённые данные сохраняются в переменную `edited_line`, а после преобразуются из списка в строку. Открывает файл для записи и заменют данные в файле data.txt:
    
        ```python
                edited_line = f"{num} | {fio} | {company_name} | {work_phone_number} | {self_phone_number}"
                tel_book_lines[index_edit_data] = edited_line
                print(f"Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n")
            
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("\n".join(tel_book_lines))  
             ```

  + Поиск записей по одной или нескольким характеристикам

    + Открывает файл data.txt для чтения:

      ```python
      
      def search_data(filename: str):
      """Данная функция ищет данные в файле data.txt по параметрам которые ввёл пользователь."""
      
      with open(filename, "r", encoding="utf-8") as data:
          tel_book = data.read()
      ```
    + Данные файла преобразуются из строки в список, в цикле `for` данные которые ввел пользователь, перебираются пока не найдется совпадение:

      ```python
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
  
      ```
    
+ Требования к программе:
  + Реализация интерфейса через консоль (без веб- или графического интерфейса)
  + Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
  + В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)

