
delimeter = "-" * 28
tamplate = "|{:<5}|{:<20}|"



def animals_undergoing_treatment(animals: list) ->None:
    print(animals)



def  add_animals_to_the_list(animals: list) ->list:
     animal = input("як зваті вашу тварину? ")
     if animal in animals:
          print(animals)
     else:
           animals.append(animal)     
           print("дякую за вибір цієі кліники")
     return animals



def animal_healths(animals: list) -> list:
            a = input("яку тварну вилыкувано? ")
            animals_lower = [animals.lswer() for animal in animals]
            if animals.lower() in animals_lower:
                 animals.remove(animal.lower().title())
                 animals_cured.append(animal.lower().title())
                 print(f"{animal}")
            return animals



def list_of_healthy(animals_cured: list) -> list:
         print(animals_cured)
         return animals_cured


def delete_accidentally_added_animal(animals_cured: list, animals: list) ->tuple[list]:
         gta = input("який список здорові - хворі   ")
         neme = input("назву тварини:")
         
         if gta == 'здорові':
              animals_cured.remove(neme)
              print(animals_cured)
              
         elif gta == 'хворі':
              animals.remove(neme)
              print(animals)
              
         else:
              print("ееее брат я хз но в списках такого нет и небыло!  ")
                 
         return animals, animals_cured     



def remove_animal_by_name(animals_cured: list, animals: list) ->tuple[list]:
         ga = input("який список здорові - хворі ")
         ggwp = input("індикс тварини:")
         ggwp = int(ggwp)
         
         if ga == 'здорові':
             animals_cured.pop(ggwp)
             print(animals_cured)
             
                  
             print(animals_cured)
             

         elif ga == 'хворі':           
              animals.pop(ggwp)
              print(animals)
              
         else:
              print("штото не сроботало")  
              
         return animals_cured, animals



def sort_by_name(animals: list) ->None:
         animas = sorted(animals)

         for i, animal in enumerate(animas, start=1):
            print(f"{i}: {animal}")

         print("\nСписок тварин відсортовано")

def change_name(animals: list) ->list:
         ass = input("ведіть номет тварини якій треба змінити ім'я:")
         ass = int(ass)
         ass -= 1
         sa = input("введіть нове ім'я:")
         animals[ass] = sa
         print(animals)
         return animals



def change_number_by_name(animals: list) ->None:
         
         hdhdh = input("введіть назву тварини")

         dd = animals.index(hdhdh) 
         dd += 1
         print(dd)
         input("")

def symbols_that_are_repeated_in_the_comments(animals: list) ->None:
         palin_app = []
         for animals in animals:
              if animals.lower() == animals.lower()[::1]:
                   palin_app.append(animals)
         input(f"{palin_app}")      
         