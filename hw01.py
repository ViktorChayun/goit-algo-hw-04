"""
    https://www.edu.goit.global/uk/learn/26850204/19951493/19951578/homework 
    
    текстовий файл містить інформацію про місячні заробітні плати
	    * Кожен рядок вказує на одного розробника
        * Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

    параметри
        * один аргумент - шлях до текстового файлу (path).
    
    завдання - розробити функцію total_salary(path)
	    * яка аналізує файл повертає загальну та середню суму заробітної плати
        * Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.
"""
def total_salary(path) -> tuple[float, float]:
    try:
        with open(path, mode='r', encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]
    except Exception:
        return (None, None)
            
    lst=[]
    for str in lines:
        try:
            name, salary = str.split(sep=',')
            lst.append({'name':name.strip(), 'salary':float(salary.strip())})
        except ValueError:
            print(f"Некоректний формат рядка: {str}")

    total = sum(val["salary"] for val in lst)
    cnt = len(lst)
    avg = total/cnt if cnt else None
    
    return (total, avg)

total, average = total_salary(".\\salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")