import sqlite3 as sl

conn = sl.connect('contactbook.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, phone_number TEXT)')

conn.commit()
conn.close()

def show_contacts():
   conn = sl.connect('contactbook.db')
   cursor = conn.cursor()
   
   cursor.execute('SELECT * FROM contacts')
   contacts = cursor.fetchall()
   
   for contact in contacts:
      print(f'ID: {contact[0]}, Имя: {contact[1]}, Номер телефона: {contact[2]}')
   
   conn.close()

def add_contact(name, phone_number):
   conn = sl.connect('contactbook.db')
   cursor = conn.cursor()
   
   cursor.execute('INSERT INTO contacts (name, phone_number) VALUES (?, ?)', (name, phone_number))
   
   conn.commit()
   conn.close()

def search_contacts(keyword):
   conn = sl.connect('contactbook.db')
   cursor = conn.cursor()
   
   cursor.execute('SELECT * FROM contacts WHERE name LIKE ? OR phone_number LIKE ?', ('%' + keyword + '%', '%' + keyword + '%'))
   contacts = cursor.fetchall()
   
   for contact in contacts:
       print(f'ID: {contact[0]}, Имя: {contact[1]}, Номер телефона: {contact[2]}')
   
   conn.close()

def delete_contact(contact_id):
   conn = sl.connect('contactbook.db')
   cursor = conn.cursor()
   
   cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
   
   conn.commit()
   conn.close()

def update_contact(contact_id, name, phone_number):
   conn = sqlite3.connect('contactbook.db')
   cursor = conn.cursor()
   
   cursor.execute('UPDATE contacts SET name = ?, phone_number = ? WHERE id = ?', (name, phone_number, contact_id))
   
   conn.commit()
   conn.close()