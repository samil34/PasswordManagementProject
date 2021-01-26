from tkinter import *
from cryptography.fernet import Fernet

import back

if __name__ == "__main__":
    import loginPage
    

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0] #seçilen satırın indisini alır
    selected_tuple=list1.get(index)
    entry1.delete(0,END)
    entry1.insert(END,selected_tuple[1])
    entry2.delete(0,END)
    entry2.insert(END,selected_tuple[2])
    entry3.delete(0,END)
    entry3.insert(END,decrypt_message(selected_tuple[3]))
    #print("tip: ",type(selected_tuple[3]))
    #print(index," index") listedeki seçilen satırın indisini ekrana yazar
    
def view_command():
    list1.delete(0,END)
    for row in back.view():
        list1.insert(END,row)    

def search_command():
    list1.delete(0,END)
    for row in back.search(site_adi.get(),site_adres.get(),site_sifre.get()):
        list1.insert(END,row)


def add_command():
    back.insert(site_adi.get(),site_adres.get(),site_sifre.get())
    list1.delete(0,END)
    list1.insert(END,(site_adi.get(),site_adres.get(),site_sifre.get()))

def delete_command():
    back.delete(selected_tuple[0])
    view_command()

def update_command():
    #print(selected_tuple[0],site_adi.get(),site_adres.get(),site_sifre.get())
    back.update(selected_tuple[0],site_adi.get(),site_adres.get(),site_sifre.get())
    view_command()

def form_clear():
    site_adi.set("")
    site_adres.set("")
    site_sifre.set("")

def Form_exit():
    window.destroy()
    import loginPage
    loginPage.Giris()
    
window = Tk()
window.title("Şifre Saklama/Yönetim Uygulaması")
window.geometry("750x450+500+100") 

label1 = Label(window,text="Hoşgeldiniz")
label1.grid(row=0,column=2)

label2 = Label(window,text="Site Adı:")
label2.grid(row=1,column=0)

label3 = Label(window,text="Adres:")
label3.grid(row=2,column=0)

label4 = Label(window,text="Sifre:")
label4.grid(row=3,column=0)

site_adi = StringVar()
entry1=Entry(window,textvariable=site_adi)
entry1.grid(row=1,column=1)

site_adres = StringVar()
entry2=Entry(window,textvariable=site_adres)
entry2.grid(row=2,column=1)

site_sifre = StringVar()
entry3=Entry(window,textvariable=site_sifre)
entry3.grid(row=3,column=1)


list1 =Listbox(window,height=20,width=59)
list1.grid(row=1,column=3,rowspan=6, columnspan=2)

#scrl=Scrollbar(window)
#scrl.grid(row=1,column=2,sticky='ns',rowspan = 6)

#list1.configure(yscrollcommand=scrl.set)
#scrl.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window,text="Tüm Kayıtları Gör",width=15,bg='brown',fg='white',command=view_command)
b1.grid(row=7,column=0)

b2 = Button(window,text="Ekle",width=15,bg='brown',fg='white',command=add_command)
b2.grid(row=7,column=1)

b3 = Button(window,text="Sil",width=15,bg='brown',fg='white',command=delete_command)
b3.grid(row=7,column=2)


b4 = Button(window,text="Ara",width=15,bg='brown',fg='white',command=search_command)
b4.grid(row=8,column=0)

b5 = Button(window,text="Güncelle",width=15,bg='brown',fg='white',command=update_command)
b5.grid(row=8,column=1)

b6 = Button(window,text="Formu Temizle",width=15,bg='brown',fg='white',command=form_clear)
b6.grid(row=8,column=2)

b6 = Button(window,text="Çıkış",width=15,bg='brown',fg='white',command=Form_exit)
b6.grid(row=9,column=0)

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
    #print(encrypted_message)
    return encrypted_message
    


def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    print(decrypted_message.decode())
    return decrypted_message
    
    

window.mainloop()

