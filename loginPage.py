from tkinter import * 
from tkinter import messagebox as ms
from cryptography.fernet import Fernet
import sqlite3

def baglanti(): #veritabanı bağlantısı
    conn=sqlite3.connect("sifreYonetim.db")
    if(conn):
        print("Bağlantı Başarılı")
    else:
        print("Bağlantı Başarısız")
        
    cur = conn.cursor() 
    cur.execute('''CREATE TABLE IF NOT EXISTS tbl_users(id INTEGER PRIMARY KEY , ad VARCHAR(50), soyad VARCHAR(50) , kul_adi VARCHAR(50) , email VARCHAR(50), sifre TEXT )''')
    conn.commit()
    conn.close()



def kontrol(): #kullanıcı adı ve şifre kontrol edilir
    kont_ad = kul_adi.get() # get ile kutu içindeki bilgiler alınır
    kont_sifre = kul_sifre.get()

    print(kont_ad,kont_sifre)

    """
    a = encrypt_message(kont_sifre)
    s = encrypt_message(kont_sifre)
    print(type(a))
    print(s)

    b= decrypt_message(a)
    f= decrypt_message(s)

    print(b.decode())
    print(f.decode())
    """


    #print(decrypt_message(kont_sifre))
    
    #kontSifreli = #veritabanına şifreli gönderildi
    #print(kontSifreli)
    
    conn=sqlite3.connect("sifreYonetim.db")
    cur = conn.cursor()

    find_user = ('SELECT sifre FROM tbl_users WHERE kul_adi=?')
    cur.execute(find_user,[kont_ad])
    result = cur.fetchone()
    try:
        print(result[0])
    except TypeError:
        ms.showerror('Hata!','Kullanıcı adı veya şifre hatalı')
        return 0;
        
    
    conn.close()
    
    

    
    sifreAc = decrypt_message(result[0])
    
    print(sifreAc.decode())
    sde = sifreAc.decode()
    
    if sde == kont_sifre:
        pencere.destroy()
        import arayuz
        
        
    else:
        print("false")
        ms.showerror('Hata!','Kullanıcı adı veya şifre hatalı')
       


def bol():
    
    if var.get() == 1:
        entry2.configure(show = "")
    elif var.get() == 0:
        entry2.configure(show = "*")
        
        


def Giris():
    global kul_adi,kul_sifre,var,entry2 # diğer fonksiyonlarda kullanabilmek için global yaptık
    global pencere
    
    pencere=Tk()
    pencere.title("Şifre Saklama/Yönetim Uygulaması")
    pencere.geometry("600x400+500+100") 
    
    label1 = Label(text="Kullanıcı Girişi",width=20,font=("bold",20))
    label1.place(x=90,y=53)
    
    label2=Label(text="Kullanıcı Adı:",width=20,font=("bold",10))
    label2.place(x=80,y=130)
  
    label3=Label(text="Şifre:",width=20,font=("bold",10))
    label3.place(x=56,y=180)

    kul_adi = StringVar()
    entry1=Entry(textvar=kul_adi,width=25)
    entry1.place(x=240,y=130)

    kul_sifre = StringVar()
    entry2 = Entry(pencere,textvar=kul_sifre,width=25,show="*")
    entry2.place(x=240,y=180)
    
    var = IntVar()
    bt = Checkbutton(pencere,text ="Şifre Göster" ,command=bol,offvalue=0,onvalue=1,variable= var)
    bt.place(x=235,y=200)
    
         

    Button(text='Giriş Yap',command=kontrol,width=20,bg='brown',fg='white').place(x=130,y=250)
    
    
    Button(text='Kayıt Ol',command=kayitOl,width=20,bg='brown',fg='white').place(x=300,y=250)




def kaydet():
    #kullanıcı bilgileri veritabanına eklenecek
        
    kul_adi1 = kul_adim.get()
    sifrele = sifre.get()
    
    print(kul_adi1,sifrele) #şifelenmiş yazıyı ekrana yazar
    print(encrypt_message(sifrele))
    
    conn=sqlite3.connect("sifreYonetim.db")
    cur = conn.cursor()

    find_user = ('SELECT kul_adi FROM tbl_users WHERE kul_adi=? ')
    cur.execute(find_user,[(kul_adi1)])
    
    if cur.fetchall():
        ms.showerror("Hata","Sistemde aynı kullanıcı adı mevcut")
        print("Sistemde aynı kullanıcı adı mevcut")
    else:
        ms.showinfo("Başarılı","Kayıt başarılı bir şekilde oluşturuldu")
        print("Bir kayıt oluşturuldu")
        kayit.destroy()
        Giris()
    cur.execute("INSERT INTO tbl_users VALUES (NULL,?,?,?,?,?)",(adi.get(),soyadi.get(),kul_adi1,email.get(), encrypt_message(sifrele)))
    conn.commit()
    conn.close()
    

def reEnter():
    kayit.destroy()
    Giris()
    

def kayitOl():
    pencere.destroy()

    global kayit
    
    kayit=Tk()
    kayit.title("Kayıt Ol")
    kayit.geometry("600x400+500+100")


    global kullanici_ad,sifre,adi,soyadi,kul_adim,email,sifre # diğer fonksiyonlarda kullanabilmek için global yaptık

    label1 = Label(text="Kullanıcı Kaydı",width=20,font=("bold",20))
    label1.place(x=90,y=25)

    
    lbadi=Label(text="Ad:",width=20,font=("bold",10))
    lbadi.place(x=53,y=100)

    lbsoyadi=Label(text="Soyad:",width=20,font=("bold",10))
    lbsoyadi.place(x=63,y=140)

    lbkul_adi=Label(text="Kullanıcı Adı:",width=20,font=("bold",10))
    lbkul_adi.place(x=80,y=180)

    lbemail=Label(text="E-mail:",width=20,font=("bold",10))
    lbemail.place(x=64,y=220)
    
    lbsifreLabel=Label(text="Şifre:",width=20,font=("bold",10))
    lbsifreLabel.place(x=58,y=260)

    
    adi = StringVar()
    ad=Entry(textvariable=adi,width=25)
    ad.place(x=240,y=100)

    soyadi = StringVar()
    soyad=Entry(textvariable=soyadi,width=25)
    soyad.place(x=240,y=140)

    kul_adim = StringVar()
    kullanici_ad=Entry(textvariable=kul_adim,width=25)
    kullanici_ad.place(x=240,y=180)

    email = StringVar()
    Email=Entry(textvariable=email,width=25)
    Email.place(x=240,y=220)    

    sifre = StringVar()
    sifre=Entry(textvariable=sifre,width=25,show="*")
    sifre.place(x=240,y=260)    


    
    Button( text='Kaydol',command=kaydet,width=20,bg='brown',fg='white').place(x=240,y=345)
    Button( text='Geri',command=reEnter,width=10,bg='brown',fg='white').place(x=0,y=0)

    


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
    #print("fon içi: ",decrypted_message.decode())
    return decrypted_message



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


baglanti()
Giris() # program buradan başlıyor

mainloop()
