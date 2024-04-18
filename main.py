from termcolor import colored

# Чтение данных из файлов
with open("HUMECTANTS.txt", "r") as file:
    filter1 = file.readlines()
filter1 = [word.replace('\n', '').strip().lower() for word in filter1]  # Удаляем \n, преобразуем в нижний регистр

with open("SUPPORT_POINTS.txt", "r") as file:
    filter2 = file.readlines()
filter2 = [word.replace('\n', '').strip().lower() for word in filter2]  # Удаляем \n, преобразуем в нижний регистр

# Чтение input_string из файла
with open("COMPOSITION.txt", "r") as file:
    input_string = file.read().strip()

# Разделяем строку на список слов
words = input_string.strip().replace('\n', '').strip().lower().split(',')  # Удаляем \n, преобразуем в нижний регистр

i = -1
for word in words:
    i = i + 1
    words[i] = word.strip()

i = -1
for word in filter1:
    i = i + 1
    filter1[i] = word.strip()

i = -1
for word in filter2:
    i = i + 1
    filter2[i] = word.strip()
result1 = []
result2 = []
# Проверяем совпадения с filter1 и выводим на экран совпадающие слова синим цветом
for word in words:
    if word in filter1:
        #print(colored(word, 'red'), end=',')
        result1.append(word)
   # else:
        #print(word, end=',')
#print()

# Проверяем совпадения с filter2 и выводим на экран совпадающие слова красным цветом
for word in words:
    if word in filter2:
       # print(colored(word, 'blue'), end=',')
        result2.append(word)
    #else:
       # print(word, end=',')
#print()





for word in words:
    if word in result1:
        print(colored(word, 'blue'), end=',')
    elif word in result2:
        print(colored(word, 'red'), end=',')
    else:
        print(word, end=',')
print()



