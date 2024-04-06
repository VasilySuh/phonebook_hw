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

# Поиск контакта по имени
def search_contact(name):
    cursor.execute("SELECT * FROM phonebook WHERE name=?", (name,))
    contact = cursor.fetchone()
    if contact:
        print(contact)
    else:
        print("Контакт не найден")

# Удаление контакта
def delete_contact(name):
    cursor.execute("DELETE FROM phonebook WHERE name=?", (name,))
    conn.commit()
    print("Контакт успешно удален")

# Изменение номера телефона
def edit_contact(name, new_phone_number):
    cursor.execute("UPDATE phonebook SET phone_number=? WHERE name=?", (new_phone_number, name))
    conn.commit()
    print("Номер телефона успешно изменен")

while True:
    print('Что вы хотите сделать?')
    user_choice = input('\
    1 - Посмотреть контакты\n\
    2 - Найти контакт\n\
    3 - Добавить контакт\n\
    4 - Изменить контакт\n\
    5 - Удалить контакт\n\
    0 - Выйти из приложения\n')
#     #6 - Просмотреть все контакты\n\
    print()
    if user_choice == '1':
        print(view_contacts())
        print()
    elif user_choice == '2':
        search_contact(name = input("Введите имя контакта: "))
        print()
    elif user_choice == '3':
        add_contact(name = input("Введите имя: "))
        print()
        pass
    elif user_choice == '4':
        edit_contact(name = input("Введите имя контакта: "), phone_number = input("Введите номер телефона контакта: "))
        print()
        pass
    elif user_choice == '5':
        delete_contact(name = input("Введите имя контакта: "))
        print()
        pass
#     # elif user_choice == '6':
#     #     #show_phonebook(phonebook)
#     #     pass
    elif user_choice == '0':
        print('До свидания!')
        print()
        break
    else:
        print('Неправильно выбрана команда!')
        print()
    continue
