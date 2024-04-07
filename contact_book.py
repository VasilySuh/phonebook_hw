import sqlite3

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL)''')

# Добавление контакта
def add_contact(name, phone_number):
    cursor.execute("INSERT INTO phonebook (name, phone_number) VALUES (?, ?)", (name, phone_number))
    conn.commit()
    print("Контакт успешно добавлен")

# Просмотр всех контактов
def view_contacts():
    cursor.execute("SELECT * FROM phonebook")
    contacts = cursor.fetchall()
    for contact in contacts:
        print(contact)

# Поиск контакта по id
def search_contact(id_contact):
    cursor.execute("SELECT * FROM phonebook WHERE id=?", (id_contact))
    contact = cursor.fetchone()
    if contact:
        print(contact)
    else:
        print("Контакт не найден")

# Удаление контакта
def delete_contact(id_contact):
    cursor.execute("DELETE FROM phonebook WHERE id=?", (id_contact))
    conn.commit()
    print("Контакт успешно удален")

# Изменение контакта
def edit_contact(id_contact, new_name, new_phone_number):
    cursor.execute("UPDATE phonebook SET name = ?, phone_number = ? WHERE id = ?", (new_name, new_phone_number, id_contact))
    conn.commit()
    print("Контакт успешно изменен")

while True:
    print('Что вы хотите сделать?')
    user_choice = input('\
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
    elif user_choice == '0':
        print('До свидания!')
        print()
        break
    else:
        print('Неправильно выбрана команда!')
        print()
    continue
