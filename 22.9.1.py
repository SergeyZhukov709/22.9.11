
# Сортировка по возрастанию
def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

    return array

# Двоичный поиск входного числа
def binary_search(array, element, left, right):
    try:
        if left > right:  # если левая граница превысила правую,
            return False  # значит элемент отсутствует

        middle = (right + left) // 2  # находимо середину
        if array[middle] == element:  # если элемент в середине,
            return middle  # возвращаем этот индекс
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        print('Число выходит за диапазон списка, введите меньшее число.')

# Ввод данных
#_list = list(map(int, input("Введите последовательность чисел через пробел").split()))

array = (str(input("Введите последовательность чисел через пробел")))
# Проверка введенных данных

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

if " " not in array:
    print("\nНА ВХОДЕ ОТСУТСТВУЮТ ПРОБЕЛЫ (введите числа, согласно условиям ввода или продожите работу с одним числом.)")
    array = (str(input("Введите последовательность чисел через пробел")))
if not is_int(array):
    print('\nНА ВХОДЕ ДОЛЖНЫ БЫТЬ ТОЛЬКО ЦЕЛЫЕ ЧИСЛА '
          '\nПерезапустите программу')
    raise SystemExit(0)

while True:
    try:
        num = int(input("Введите одно число для поиска: "))  #Ввод элемента поиска
    except ValueError:
        continue
    break


# Преобразование в список и Вывод полученных данных
array_of_strings = array.split() # список строковых представлений чисел
array_list = list(map(int, array_of_strings)) # список чисел

# Вывод отсортированного списка
array_list_sort = qsort(array_list, 0, len(array_list)-1)
print(array_list_sort)

fnd = binary_search(array_list_sort, num, 0, len(array_list_sort)-1)

if not fnd:
    rI = min(array_list_sort, key=lambda x: (abs(x - num), x))
    ind = array_list_sort.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if num < array_list_sort[0]:
        print(f'''Элемент {num} меньше значений в списке
Ближайший меньший элемент: {array_list_sort[0]}, его индекс: {0}''')
    elif num > array_list_sort[len(array_list_sort)-1]:
        print(f'''Элемент {num} больше значений в списке
Ближайший больший элемент: {array_list_sort[len(array_list_sort)-1]}, его индекс: {len(array_list_sort)-1}''')
    elif rI < num:
        print(f'''В списке нет введенного элемента {num}
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {array_list_sort[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента {num}
Ближайший больший элемент: {rI}, его индекс: {array_list_sort.index(rI)}
В списке нет меньшего элемента''')
    elif rI > num:
        print(f'''В списке нет введенного элемента {num}
Ближайший больший элемент: {rI}, его индекс: {array_list_sort.index(rI)}
Ближайший меньший элемент: {array_list_sort[min_ind]} его индекс: {min_ind}''')
    elif array_list_sort.index(rI) == 0:
        print(f'Индекс введенного элемента: {array_list_sort.index(rI)}')
else:
    print(f'Индекс введенного элемента: {fnd}')

