# ЗАДАНИЕ 22.9.1 (HW-03)

array = list(map(int, input('Введите последовательность чисел через пробел: ').split()))


array.sort()

print(f'Отсортированная последовательность по возрастанию чисел: {array}')
element = int(input('Введите число в рамках данной последовательности : '))

if element not in  array:
    print('Число не входит в данную последовательность, повторите ввод числа!')
    element = int(input('Введите число из данной последовательности : '))
    
    

        



def binary_search(array, element, left, right):
    if left > right:                                            
        return False                                            

    middle = (right + left) // 2                                
    if array[middle] == element:                                
        return middle                                          
    elif element < array[middle]:                               
                                                                
        return binary_search(array, element, left, middle - 1)
    else:                                                       
        return binary_search(array, element, middle + 1, right)


element_index= binary_search(array, element, 0, len(array) - 1)

if element_index == 0:
    print('Введеное число первое в последовательности и перед ним нет числа и нет индекса числа.')
    print('Индекс введеного элемента :', (element_index))
    print(f'Индекс элемента, после введенного числа : {(element_index) + 1}')
else:
    print(f'Индекс элемента, пред введеным числом : {(element_index) - 1}')

    print('Индекс введеного элемента :', (element_index))
    print(f'Индекс элемента, после введенного числа : {(element_index) + 1}')
