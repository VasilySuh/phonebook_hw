import sqlite3
import easygui 
from easygui import*
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL, extra_phone_number TEXT NOT NULL, email TEXT NOT NULL, address TEXT NOT NULL)''')

# Добавление контакта
def add_contact():
    name = easygui.enterbox("Введите имя контакта: ")
    phone_number = easygui.enterbox("Введите номер телефона контакта: ")
    extra_phone_number = easygui.enterbox("Введите дополнительный номер телефона контакта: ")
    email = easygui.enterbox("Введите электронную почту контакта: ")
    address = easygui.enterbox("Введите адрес контакта: ")
    cursor.execute("INSERT INTO phonebook (name, phone_number, extra_phone_number, email, address) VALUES (?, ?, ?, ?, ?)", (name, phone_number, extra_phone_number, email, address))
    conn.commit()
    msgbox("Контакт успешно добавлен")

# Просмотр всех контактов
def view_contacts():
    cursor.execute("SELECT * FROM phonebook")
    contacts = cursor.fetchall()
    contacts_str = ""
    for contact in contacts:
        contacts_str += "ID: {} \nИмя: {} \nНомер телефона: {} \nДополнительный номер: {} \nEmail: {} \nАдрес: {} \n\n".format(contact[0], contact[1], contact[2], contact[3], contact[4], contact[5])
    easygui.msgbox(contacts_str, title="Contacts")
    
# Поиск контакта по id
def search_contact_id():
    id_contact = easygui.enterbox("Введите id контакта: ")
    cursor.execute("SELECT * FROM phonebook WHERE id=?", (id_contact))
    contact = cursor.fetchone()
    if contact:
        msgbox(contact)
    else:
        msgbox("Контакт не найден")

# Поиск контакта по адресу электронной почты
# def search_contact_email():
#     email_contact = easygui.enterbox("Введите электронную почту контакта: ")
#     cursor.execute("SELECT * FROM phonebook WHERE email=?", (email_contact))
#     contact = cursor.fetchone()
#     if contact:
#         msgbox(contact)
#     else:
#         msgbox("Контакт не найден")

# Удаление контакта
def delete_contact():
    id_contact = easygui.enterbox("Введите id контакта: ")
    cursor.execute("DELETE FROM phonebook WHERE id=?", (id_contact))
    conn.commit()
    msgbox("Контакт успешно удален")

# Изменение контакта
def edit_contact():
    id_contact = easygui.enterbox("Введите id контакта: ")
    cursor.execute("SELECT * FROM phonebook WHERE id=?", (id_contact))
    contact = cursor.fetchone()
    if contact:
        new_name = easygui.enterbox("Введите новое имя контакта: ")
        new_phone_number = easygui.enterbox("Введите новый номер контакта: ")
        new_extra_phone_number = easygui.enterbox("Введите новый  дополнительный номер контакта: ")
        new_email = easygui.enterbox("Введите новую электронную почту контакта: ")
        new_address = easygui.enterbox("Введите новый адрес контакта: ")
        cursor.execute("UPDATE phonebook SET name = ?, phone_number = ?, extra_phone_number = ?, email = ?, address = ? WHERE id = ?", (new_name, new_phone_number,new_extra_phone_number, new_email, new_address, id_contact))
        conn.commit()
        msgbox("Контакт успешно изменен")
    else:
        msgbox("Контакт не найден")
    

while True:
    choice = easygui.choicebox("Что вы хотите сделать?", choices = ["Посмотреть контакты", "Найти контакт", "Добавить контакт", 
                                                                    "Удалить контакт", "Изменить контакт", "Выход"])
    if choice == "Посмотреть контакты":
        view_contacts()
    elif choice == "Найти контакт":
        search_contact_id()
    # elif choice == "Найти контакт по электронной почте":
    #     search_contact_email()
    elif choice == "Добавить контакт":
        add_contact()
    elif choice == "Изменить контакт":
        edit_contact()
    elif choice == "Удалить контакт":
        delete_contact()
    elif choice == "Выход":
        break