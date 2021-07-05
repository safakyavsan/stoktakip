import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="stoktakip"

)
mycursor = mydb.cursor()
def kategorilist(q2):
    sql = "SELECT kategori FROM kategori "
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        q2.append(x[0])


def urunekle(kategori,isim,adet):
    sql = "INSERT INTO urunler (kategori, isim,adet) VALUES (%s, %s, %s)"
    val = (kategori, isim,adet)
    mycursor.execute(sql, val)
    mydb.commit()

def urunlistele(kategori,q):
    sql = "SELECT isim,adet FROM urunler WHERE kategori = %s"
    adr = (kategori,)

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()

    for x in myresult:
      q.append(x)

def urunsil(isim):
    sql = "DELETE FROM urunler WHERE isim = %s"
    adr=(isim,)
    mycursor.execute(sql,adr)

    mydb.commit()

def stokduzenle(adet,isim):
    sql = "UPDATE urunler SET adet = %s WHERE isim = %s"
    adr=(adet,isim,)
    mycursor.execute(sql,adr)
    mydb.commit()

def satis(isim,adet):
    sql = "UPDATE urunler SET adet = adet - %s WHERE isim = %s"
    adr=(adet,isim,)
    mycursor.execute(sql,adr)
    mydb.commit()


