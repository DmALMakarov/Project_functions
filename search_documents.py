print('Команды:\np – поиск человека по номеру документа;\ns – поиск номера полки по номеру документа;\nl – поиск всех данных (документ, номер полки, ФИО);\na – добавить новый документ в каталог;\nq - выход;')

documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

def user_name(): 
  number = input('Введите номер документа: ')
  for document in documents:  
    if number == document["number"]:
      name = document["name"]
      return name
  else:
    print('Такого документа не существует')

def shelf(): 
  number = input('Введите номер документа: ')  
  for key, document in directories.items():
    for i in document:
      if number == i:
        name = key
        return name
  else:
    print('Такого документа не существует') 

def data():
  for document in documents: 
    print (f'{document["type"]} {document["number"]} {document["name"]}')

def access(): 
  type = input('Введите тип документа: ')  
  number = input('Введите номер документа: ')
  name = input('Введите ФИО: ')
  shelf = input(int('На какую полку добавить документ?: '))
  for document in documents:
    document['type'] = type
    document['number'] = number
    document['name'] = name
    print(document)
  return name

def add_user():
  type = input('Введите тип документа: ')  
  number = input('Введите номер документа: ')
  name = input('Введите ФИО: ')
  shelf = input('На какую полку добавить документ?: ')
  for document in documents:
    document["type"] = type
    document["number"] = number
    document["name"] = name
  for box, val in directories.items():
    if box == shelf:
      val.append(number)
      print(f'Добавлен новый документ: {type} {number} {name} на полку № {box}') 
      break
  else:
    print('Такой полки не существует')      

def main():
  while True:
    user = input('Введите команду: ')
    if user == 'p':
      print(user_name())
    elif user == 's':
      print(f'Документ находится на полке: {shelf()}')
    elif user == 'l':  
      print(data())
    elif user == 'a':
      print(add_user())
    elif user == 'q':
      break
    else:
      print('Данная команда неверна')
main()