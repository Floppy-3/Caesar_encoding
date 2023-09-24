ukr = [
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
    'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я','а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
    'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

#Інсталяція змінних для циклів
i = 0
b = 0
d = 0
inputedstr = 0

#Інсталяція списків
iin = []
iin2 = []
out = []
outlist = []
inputedlist = []


#Вхід за допомогою 1 команди
inputedstr = input("example: cript ідея 4 4")
inputedlist = inputedstr.split()

#Вхідні данні
inputfunc = inputedlist[0]

#Перевірка вхідної функції данних
if inputfunc == 'cript' or 'decript':
    print('Function Confirmed')
else:
    #Закінчує код↓
    exit('Function Failure')
inputedtext = str(inputedlist[1])
ic = int(inputedlist[2]) - 1
inputedcode = int(inputedlist[3])

#Перевіряє та Розбирає вхідний текст на індекси
while i <= ic:
    if inputedtext[i] in ukr:
        iin.append(ukr.index(inputedtext[i]))
        i = i + 1
        ii = i
    else:
        #Завершення коду з помилкою
        exit("DATA Failure")

#Кодування, Декодування індексів
if inputfunc == 'cript':
    while b <= ic:
        iin2.append(iin[b]+inputedcode)
        b = b+1
else:
    while b <= ic:
        iin2.append(iin[b]-inputedcode)
        b = b + 1

#Переведення індексів в текст
while d <= ic:
    outlist.append(str(ukr[iin2[d]]))
    d = d+1
out = outlist

#Виведення
print(out)
input('Press ENTER To exit')

#Більше в файлі прочитай_мене.txt