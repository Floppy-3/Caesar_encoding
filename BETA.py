ukr = [
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
    'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

#Вхідні данні
inputfunc = input("cript - шифрування, decript - розшифровування")
#Перевірка вхідної функції данних
if inputfunc == 'cript' or 'decript':
    print('Function Confirmed')
else:
    #Закінчує код↓
    exit('Function Failure')
inputedtext = list(str(input('Введіть текст')))
ic = int(input("Кількість букв в слові(Обовязково для роботи)")) - 1
inputedcode = int(input('Введіть зміщення'))

#Інсталяція змінних для циклів
i = 0
b = 0
d = 0

#Інсталяція списків
iin = []
iin2 = []
out = []

#Перевіряє та Розбирає вхідний текст на індекси
while i <= ic:
    if inputedtext[i] in ukr:
        iin.append(ukr.index(inputedtext[i]))
        i = i + 1
        ii = i
        print('буква №' + str(ii) + ' э')
    else:
        #Завершення коду з помилкою
        exit("ERROR DATA")

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
    out.append(ukr[iin2[d]])
    d = d+1

#Виведення
print(out)

#Більше в файлі прочитай_мене.txt