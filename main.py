from datetime import datetime
from pprint import pprint

from src.password import generate_password
from src.animals import(
     animals_undergoing_treatment,
add_animals_to_the_list,
animal_healths,
list_of_healthy,
delete_accidentally_added_animal,
remove_animal_by_name,
sort_by_name,
change_name,
change_number_by_name,
symbols_that_are_repeated_in_the_comments
)

from src.reviews import (
     show_reviews
)

from src.employees import (
palindromes,
add_employee,
del_employee,
show_employees,
change_salary,
change_position,
show_log,
)
from src import files
from files.list_files import HELP

def exit():
         
        c = input("ви точно хочете вийти? ")  
        if c == "так":
            quit()
        else:
             print("")



def help(path: str ="files/help.txt") -> None:
     with open(path,"r",encodig="UTF=8") as file:
          print(file.read())



def show_log(log: list) -> None:
        pprint(log, width = 100)       



def show_using_commands(using_commands: dict) ->None:
        for command, count in USING_COMMANDS.items():
            print(f"Команда '{command}' використана {count} разів")
       


def main():
     
     animals = files.open_animals()

     animals_cured = files.open_animals_cured()
     reviews = []


     log = []         
     using_commands = {} 

     employees = {                 
    "andrew": {
        "position": "Менеджер",
        "salary": 3900,
        "start_date": "22.02.2024",
        "name": "andrew",
        "password": "123987654k"
    },
    "Artem": {
        "position": "Продавець",
        "salary": 30000,
        "start_date": "24.05.2024",
        "name": "Artem",
        "password": "987123456g"
    }
}
     login_Global = input("Введіть свій логін користувача:")
     password = employees.get(login_Global, {}).get("password")
     
     if not password:
        position = input("Введіть свою посаду:")
        salary = input("Введіть свою зарплату:")
        name = input("Введіть своє ім'я:")
        start_date = datetime.now().strftime("%d.%m.%Y")

        employees[login_Global] = {
            "posiotion": position,
            "salary": salary,
            "start_date": start_date,
            "name": name,
        }

        password = generate_password()
        employees[login_Global]["password"]  = password
   
     
        input(f"\nПароль успішно створено: '{password}'. Запам'ятайте його ")

        password_input = input("\nВведіть пароль для входу у систему: ")

      
     command = ""
     while password_input == password:
         if not command:
              log.append(f"Користувач с логіном '{login_Global}'війшов до системи: {datetime.now()} ")
         
              print("Доброго дня в нашій системі")
    
    
         command = input("Введіть номер команди: ")
         log.append(f"Користувач с логіном '{login_Global}' в вів команду '{command}': {datetime.now()}")
         using_commands[command] = using_commands.get(command, 0) +1
    
         match command:
              case "animals undergoing treatment":
                   animals_undergoing_treatment(animals)
              case "animal health":
                   animal_healths(animals)
              case "list of healthy":
                   list_of_healthy(animals_cured)
              case "add animals":
                   add_animals_to_the_list(animals)      
              case "delete accidentally added animal":
                   delete_accidentally_added_animal(animals, animals_cured)
              case "remove animal by name":
                   remove_animal_by_name(animals, animals_cured) 
              case "sort by name":
                   sort_by_name(animals)
              case "change name":
                   change_name(animals)
              case "change number by name":
                   change_number_by_name(animals)
              case "exit":
                   exit()
              case "show reviews":
                   show_reviews(reviews)
              case "symbols that are repeated in the comments":
                   symbols_that_are_repeated_in_the_comments(animals)
              case "palindromes":
                   palindromes(employees)
              case "add employee":
                   add_employee(employees)
              case "del employee":
                   del_employee(employees)
              case "show employees":
                   show_employees(employees)
              case "change salary":
                   change_salary(employees)
              case "change position":
                   change_position(employees)
              case "show log":
                   show_log(employees)
              case "show using commands":
                  show_using_commands(employees)
              case "help":
                  help()
              case _:
                   print("Невідома команда. Спробуйте ще раз...")

     else:
          print("Пароль введено не вірно. Доступ заборонено!")
   
if __name__=="__main__":
    main()
     



