"""
    https://www.edu.goit.global/uk/learn/26850204/19951493/19951578/homework
    
    завдання:
	    - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.
         
    текстовий файл:
	    - містить інформацію про котів. 
	    - Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.

    Вимоги:
	    - Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
	    - Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
	    - Функція має повертати список словників, де кожен словник містить інформацію про одного кота.
"""
def get_cats_info(path) -> list[list[str, str, str]]:
    try:
        with open(path, mode='r', encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]
    except Exception:
        print("Помилка роботи з файлом.")
        return None

    lst=[]
    for str in lines:
        try:
            id, name, age = str.split(sep=',')
            lst.append({"id":id.strip(), "name":name.strip(), "age":age.strip()})
        except ValueError:
            print(f"Некоректний формат рядка: {str}")

    return lst

cats_info = get_cats_info(".\\cats_file.txt")
print(cats_info)