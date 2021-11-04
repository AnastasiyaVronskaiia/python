# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file = open('example.txt','r')
content = file.read()
poz = file.tell()
print(f'Текст в файле: \n {content}')
print(f'Текущая позиция:{poz}')
file = open('example.txt','r')
cnt = file.readlines()
print(f'Кол-во строк в файле:\n {len(cnt)}')
file = open('example.txt', 'r')
content = file.readlines()
for i in range(len(content)):
    print(f'количество слов {i + 1} - ой строки {len(content[i])}')
file = open('example.txt', 'r')
content = file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
