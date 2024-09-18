import string
import random


def is_verify_password(passwords: str) -> bool:
     if len(passwords) >=8:
          is_len_pass = True
     else:
          is_len_pass = False


     is_have_digit = False
     is_have_char =False



     for char in passwords:
          if char.isalpha():  
                 is_len_pass = True  
          elif char.isdigit():
                  s_have_digit = True   

     if is_len_pass and is_have_digit and is_have_char:
          return True
     else:
          return False



def generate_password() -> str:
     while True:
          commands = input("Потрібно створити пароль для можливості працювати в системі.\n"
                    "Введіть 1 - для введення свого паролю.\n"
                    "Введіть 2 - для автоматичної генерації паролю\n-> ")

 


          if commands == "1":
              passwords = input("Введіть свій пароль. Довжина паролю має бути не менше 8 символіd, містити мінім одна буква та одну цифру.\n->")

              if is_verify_password(passwords):      
                 return passwords 
               
              else:
                   input("Ваш пароль не пройшов перевірку. Спробуйте ще раз. 'Enter' для проовження")

          elif commands == "2":
               string_password = string.ascii_lowercase + string.digits

               len_password = input("Введіть довжину паролю, мінім 8 символів:")
               if len_password and len_password.isdigit() and int(len_password) >=8:
                   len_password = int(len_password)
               else:
                    len_password = 8     

               is_upper = ("Чи використовувати великі літери для генерації паролю: 1 - так, будь який інший символ - ні ->") 
               if is_upper == "1":
                  string_password += string.ascii_uppercase

               is_punktuation = input("Чи використовувати спецсимволи для генерації паролю: 1 - так, будь який інший символ - ні ->")
               if is_punktuation == "1":
                   string_password += string.punctuation
        
               is_repeart = input("Чи можуть символи у паролю повторюватись. 1 - так, будь який інший символ - ні -> ")
               if is_repeart == "1":
                  password = random.choices(string_password, k=len_password)
               else:
                    password = random.sample(string_password, k=len_password)
               
               return "".join(password)
     
              