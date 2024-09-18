def add_employee(employees: dict) ->dict:
        login = input("Введіть логін для користувача: ")
        position = input("Введіть посаду працівника: ")
        salary = input("Введіть ЗП для користувача: ")
        start_date = input("Введіть дату старту роботи у форматі '01.01.2024': ")
        name = input("Введіть ім'я працівника: ")
        password = input("Введіть пароль для користувача: ")

        EMPLOYEES[login] = {
            "posititon": position,
            "salary": salary,
            "start_date": start_date,
            "name": name,
            "password": password
        }
        print("Користуча успішно додано")
        return employees



def del_employee(employees: dict) ->None:
        login = input("Введіть логін користувача для видалення співробітника: ")
     

        if login in employees:
            del employees[login]
            input("Користувача успішно видалено")
        else:
            input("Такого користувача не знайдено")
        return employees
    


def show_employees(employees: dict) ->None:
        for employee in employees:
            print(f"Інформація про користувача з логіном {employee}\n")
            for key, val in employees[employee].items():
                print(f"{key}: {val}")
            print("\n\n")


def palindromes(reviews: list) ->None:
         for review in reviews:
              print(review)       




def change_salary(employees: dict) ->dict:
         login = input("Ведіть логін користувача: ")

         if login in employees:
           salary = input("Ведіть нову зп:")
           employees[login]["salary"] = salary

         else:
          input("Такого користувача не знайдено\nНатисніть 'enter' для продовження ")
         return employees



def show_log(log: list) -> None:
        pprint(log, width = 100)   


def change_position(employees: dict) ->dict:
         login = input("Ведіть логін користувача:")

         if login in employees:
             position = input("Ведіть нову посаду користувача: ")
             EMPLOYEES[login]["position"] = position
             input("Посаду користувача успішно змінено: ")
         else:
            input("Такого користувача не знайдено\nНатисніть 'enter' для продовження") 
         return employees


def show_using_commands(using_commands: dict) ->None:
        for command, count in USING_COMMANDS.items():
            print(f"Команда '{command}' використана {count} разів")
       

