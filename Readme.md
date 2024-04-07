# Contact_book
Эта программа представляет собой консольный телефонный справочник с локальной БД, которую программа создаёт самостоятельно. 
Возможности на данный момент:
1. Добавление контактов.
2. Просмотр контактов.
3. Поиск контактов по id.
4. Удаление контактов.
5. Редактирование контактов по  id.

**В планах:**
1. Прописать возможность добавления нескольких номеров телефона к одному контакту,
электронной почты и адресов.
2. Добавить возможность редактирования параметров перечисленных в пункте 1.

Реализация программы:

1. Импорт СУБД SQLite 3 и создание локальную БД:

```
import sqlite3
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()
```


2.  Создание таблицы:

```

cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL)''')
#создаём таблицу phonebook состоящую из столбцов id, name и phone_number
```
3. Функция для добавления контакта:

```
def add_contact(name, phone_number):
    cursor.execute("INSERT INTO phonebook (name, phone_number) VALUES (?, ?)", (name, phone_number)) # Вставляем в таблицу данные в соответствующие столбцы
    conn.commit() 
    print("Контакт успешно добавлен") # Оповещаем пользователя
```
4. Функция просмотра всех контактов:

```
def view_contacts():
    cursor.execute("SELECT * FROM phonebook")
    contacts = cursor.fetchall()
    for contact in contacts:
        print(contact) # выводим всю информацию из таблицы
```
5. Функция для поиска контакта по id:

```
def search_contact(id_contact):
    cursor.execute("SELECT * FROM phonebook WHERE id=?", (id_contact)) # ищем строку с соответсвующим id
    contact = cursor.fetchone()
    if contact:
        print(contact) # выводим, если такой контакт есть
    else:
        print("Контакт не найден") #сообщаем пользователю, если такого контакта нет.
```
6. Функция для удаления контакта:

```
def delete_contact(id_contact):
    cursor.execute("DELETE FROM phonebook WHERE id=?", (id_contact)) #удаляем строку с соответсвующим id
    conn.commit()
    print("Контакт успешно удален") #сообщаем пользователю
```

7. Функция для изменения контакта:

```
def edit_contact(id_contact, new_name, new_phone_number):
    cursor.execute("UPDATE phonebook SET name = ?, phone_number = ? WHERE id = ?", (new_name, new_phone_number, id_contact)) #ищем контакт по id и меняем данные
    conn.commit()
    print("Контакт успешно изменен") #сообщаем пользователю о том, что провели изменения
```

8. Реализация меню программы:

```
while True:    #запускаем цикл программы
    print('Что вы хотите сделать?') 
    user_choice = input('\  #считываем выбор пользователя
    1 - Посмотреть контакты\n\
    2 - Найти контакт\n\
    3 - Добавить контакт\n\
    4 - Изменить контакт\n\
    5 - Удалить контакт\n\
    0 - Выйти из приложения\n')
    print()
    if user_choice == '1':
        print(view_contacts())
        print()
    elif user_choice == '2':
        search_contact(id_contact = input("Введите id контакта: "))
        print()
    elif user_choice == '3':
        add_contact(name = input("Введите имя контакта: "), phone_number = input("Введите номер телефона контакта: "))
        print()
        pass
    elif user_choice == '4':
        edit_contact(id_contact = input("Введите id контакта: "), new_name = input("Введите новое имя контакта: "), new_phone_number = input("Введите номер телефона контакта: "))
        print()
        pass
    elif user_choice == '5':
        delete_contact(id_contact = input("Введите id контакта: "))
        print()
        pass
    elif user_choice == '0' # данный выбор пользователя завершает программу
        print('До свидания!')
        print()
        break
    else:
        print('Неправильно выбрана команда!') 
        print()
    continue # Продолжаем цикл пока пользователь его не прервёт elif user_choice == '0'
```