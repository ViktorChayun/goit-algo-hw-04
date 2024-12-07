"""
    https://www.edu.goit.global/uk/learn/26850204/19951493/19951578/homework
    
    завдання:
        * Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка  і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. 
        * Створіть віртуальне оточення Python для ізоляції залежностей проєкту
        * Скрипт має отримувати шлях до директорії як аргумент при запуску.  шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
        * Використати бібліотеки colorama для реалізації кольорового виведення.
        * Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
        * Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.
        * Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.
"""
import sys
from pathlib import Path
from colorama import Fore

#функція що відмальовує елемент в залежності від типу + задані префікси
def draw_element(path, folder_prefix, element_prefix):
    icon = "🖼️" if path.is_file() else "📂"
    elem_color = Fore.GREEN if path.is_file() else Fore.MAGENTA
    print(f"{Fore.BLUE}{folder_prefix}{element_prefix}{icon} {elem_color}{path.name}{Fore.RESET}")

def draw_folder_tree(path:Path, folder_prefix:str="", element_prefix:str=""):
    draw_element(path, folder_prefix, element_prefix)
    
    #якщо це файл, то немає сенсу дивитися в середині, зупинка рекурсії
    if path.is_file():
        return
    
    #це папка, будуємо відсортований список всіх елементів папки
    lst = sorted(path.iterdir())
    
    for p in lst:
        # це останій елемент папки чи проміжний?
        isLast = (p==lst[-1])
        element_prefix = " ┗━" if isLast else " ┣━"
        # якщо це корінь (перший виклик) - додаємо відступ,
        # інакше це вже вкладені в папку виклики, ствимо вертикальну риску (з верхнього рівня вкладеності)
        ext = " " if folder_prefix == ""  else " ┃"

        draw_folder_tree(p, folder_prefix + ext, element_prefix)
    
def main():
    if len(sys.argv)==1:
        print(f"{Fore.RED}Не заданий параметр (шляж до папки/файлу)!{Fore.RESET}")
        sys.exit(1) #помилка 1
        
    path_str = sys.argv[1]
    path = Path(path_str)
    
    if not path.exists():
        print(f"{Fore.RED}{path_str} не існує{Fore.RESET}")
        sys.exit(2) #помилка 2
    
    #print(path)
    draw_folder_tree(path)

# program start
if __name__ =="__main__":
    main()
    sys.exit(0) #успішний вихід з програми