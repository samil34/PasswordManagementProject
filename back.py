from cryptography.fernet import Fernet

import sqlite3


def connect():
    conn=sqlite3.connect("sifreYonetim.db")
    if(conn):
        print("Bağlantı Başarılı")
    else:
        print("Bağlantı Başarısız")
    cur = conn.cursor() 
    cur.execute('''CREATE TABLE IF NOT EXISTS tbl_site(id INTEGER PRIMARY KEY , site_name TEXT, site_address TEXT , site_password TEXT)''')
    conn.commit()
    conn.close()

def insert(site_name,site_address,site_password):
    from back import encrypt_message
    conn=sqlite3.connect("sifreYonetim.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_site VALUES (NULL,?,?,?)",(site_name,site_address, encrypt_message(site_password)))
    conn.commit()
    conn.close()
    view()



def view():
    conn=sqlite3.connect("sifreYonetim.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_site")
    row=cur.fetchall()
    conn.close()
    return row

def search(site_name="",site_address="",site_password=""):
    conn=sqlite3.connect("sifreYonetim.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_site WHERE site_name=? or site_address=? or site_password=?",(site_name,site_address,site_password))
    row=cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn=sqlite3.connect("sifreYonetim.db")
    cur = conn.cursor()
    cur.execute('DELETE FROM tbl_site WHERE id=?',(id,))
    conn.commit()
    conn.close()

def update(id,site_name,site_address,site_password):
    from back import encrypt_message
    conn=sqlite3.connect("sifreYonetim.db")
    cur = conn.cursor()
    cur.execute('''UPDATE tbl_site SET site_name=?, site_address=?, site_password=? WHERE id=?''',(site_name,site_address,encrypt_message(site_password),id))
    conn.commit()
    conn.close()


    


def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message
    #print(encrypted_message)

   

connect()

    
    
