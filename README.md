İlk olarak programı oluşturulurken pyhon da grafiksel kullancı arayüzleri için kullanılan tkinter kütüphanesi kullanıldı. Kullanıcı giriş arayüzünde kullanıcı adı ve şifre yazısı için label, kullanıcı adı ve şifre bilgileri girişi için entry, girilen şifreyi göstermek veya gizlemek için check button ve pencereler arası geçiş için ise giris ve kayıt ol adında 2 buton oluşturuldu.

 

Eğer kullanıcı sisteme kayıt olmamışsa kayıt ol butonuna tıklayarak sisteme kayıt olabilir. Eğer sisteme kayıtlı ise kullanıcı ve şifre bilgilerini girerek sisteme giriş yapar.
 
Kullanıcı sistemi ile defa kulanacaksa kayıt olmak zorundadır. Kullanıcı bilgilerini sqlite3 veritabanını kullanarak saklamaktadır. Kullanıcı, bilgilerini girerek sifreYonetim.db veritabanında tbl_user tablosuna kayıt edilir.
Kayıt edilen şifre bilgisi veritabanına şifreli olarak gönderilir. Şifreleme için fernet kütüphanesi kullanıldı.
Kullanıcı, geri butonu ile giriş sayfasına yönlendirilir.
 

Giris sayfasında kullanıcı girdiği şifreyi görmek isterse check button ile bol fonsiyonu çağırılarak şifre göster, sifre sil işlemleri yapılır.
 

Kullanıcının girdiği bilgiler veritabanından sorugulanır ve eğer kullanıcı bilgileri veribanında yoksa kullanıcıya hata mesajı gönderilir. Mesaj box özelliği tkinter kütüphanesinden import edilmiştir. Kullanıcı bilgileri doğru girdiğinde ise arayuz dosyası import edilir ve yeni bir python dosyası açılır.
 

Kullanıcı, sisteme girdiği window penceresi oluşturulur. Kullanıcının gireceği site adı, adres ve şifresi sifreYonetim.db veritanında tbl_site tablosunda saklanmaktadır. Kullanıcının kullanıcının veritanından bilgilerini görmesi için bir listbox oluşturulmuştur.

 

Kullanıcı, site adı ,adres ve şifre bilgilerini girerek ekle butonuna bastığında insert işlemi ile kullanıcı bilgileri veritabanına kayıt edilir. Kullanıcının şifresi ise veritanına şifreli olarak gönderilir.
 

Kullanıcı tüm kayıtları gör butonuna tıkladığında ise kullanıcıya ait bilgiler select sorgusu ile veritanından çekilir.

 

Kullanıcı listbox içindeki bilgilere tıklayarak giriş yapılan kısımlara o bilgiler getirilir ve veritabanındaki şifreli olan şifre bilgiside çözülerek şifre kullanıcıya gösterilir.


 

Kullanıcı arama işleminde şifresini öğrenmek istediği side adını yazar. Yazdığı site adresi veritanına sorgulanır ve kayıt varsa veritabanından çekilir. Kullanıcı listbox içindeki bilgiye tıklayarak şifresini öğrenmiş olur.

 

Kullanıcı daha önceden girmiş olduğu google123 şifresini google olarak değiştirir ve şifresini güncellemiş olur. 
Kullanıcı formu temizle butonuna tıklayarak formu temizler ve tekrar giriş gerçekleştirebilir. Son olarak kullanıcı çıkış butonu ile giriş sayfasına yönlendirilir.
