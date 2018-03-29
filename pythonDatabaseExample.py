import sqlite3 as sql



while True:
    con = sql.connect("new_db.db")
    crsr = con.cursor()
    print("\niscileri goruntulemek icin : 1")
    print("isci eklemek icin : 2")
    print("isci ucret guncelleme : 3")
    print("programi kapatmak icin : 0")
    secim = input('Seciminiz : ')
    if secim == '1':
        for jobs in con.execute("SELECT * From job"):
            print(jobs[0] + "\t" + jobs[1] + "\n")
    elif secim == '2':
        name = input('isim giriniz : ')
        price = input('ücret giriniz : ')
        if name and str(price) != '':
            con.execute(("""insert into job VALUES ('{}','{}')""").format(name, str(price)))
            con.commit()
            print(('{} iscisi {} ucreti ile veritabanina eklendi.\n').format(name, price))
            con.close()
    elif secim == '3':
        name = input('isim giriniz : ')
        if (con.execute("select name from job WHERE '{}'".format(name))):
            price = input('yeni ucreti giriniz : ')
            con.execute("update job set name = '{}', price='{}' WHERE name='{}'".format(name,price,name))
            con.commit()
            con.close()
    else:
        break