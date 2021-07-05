import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox,QVBoxLayout
from PyQt5.uic import loadUi
import sql

class Giris(QDialog):
    def __init__(self):
        super(Giris, self).__init__()
        loadUi("login.ui",self)
        self.girisbutton.clicked.connect(self.girisfonksiyonu)
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
    def girisfonksiyonu(self):
        kadi=self.kadi.text()
        sifre= self.sifre.text()

        if kadi=="Satış" and sifre=="12345":
            satis = Satis()
            widget.addWidget(satis)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            widget.setFixedWidth(1128)
            widget.setFixedHeight(893)
        elif kadi=="Depo" and sifre=="qwerty":
            depo = Depo()
            widget.addWidget(depo)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            widget.setFixedWidth(1128)
            widget.setFixedHeight(893)
        else :
            msgBox=QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Hatalı Giriş")
            msgBox.setWindowTitle("Hata")
            returnValue = msgBox.exec()
class Satis(QDialog):
    def __init__(self):
        super(Satis, self).__init__()
        loadUi("satis.ui",self)
        q2 = []
        sql.kategorilist(q2)
        for i in q2:
            self.kategorilist.addItem(i)
        self.kategorilist.itemClicked.connect(self.kategoriitem_click)
        self.urunlist.itemClicked.connect(self.urunitem_click)
        self.satisbutton.clicked.connect(self.satisclick)
    def kategoriitem_click(self,item):
        self.urunlist.clear()
        global q
        q=[]
        global kategori
        kategori=item.text()
        sql.urunlistele(str(kategori),q)

        for i in q:
            self.urunlist.addItem(i[0])
    def urunitem_click(self,item):
        global urun
        urun=item.text()
        print(urun)
        for i in q:
            if i[0]==str(urun):
             global stokadeti
             stokadeti=str(i[1])
             self.stokadet.setText(stokadeti)

    def satisclick(self):
        satilacakadet=self.satilacakadetx.text()
        sql.satis(urun,int(satilacakadet))
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Satış Yapıldı")
        msgBox.setWindowTitle("Satış")
        returnValue = msgBox.exec()
        sql.urunlistele(str(kategori), q)
        for i in q:
            if i[0]==str(urun):
             global stokadeti
             stokadeti=str(i[1])
             self.stokadet.setText(stokadeti)











class Depo(QDialog):
    def __init__(self):
        super(Depo, self).__init__()
        loadUi("depo.ui",self)
        q2 = []
        sql.kategorilist(q2)
        for i in q2:
            self.kategorilist.addItem(i)
        self.kategorilist.itemClicked.connect(self.kategoriitem_click)
        self.urunlist.itemClicked.connect(self.urunitem_click)
        self.stokduzenle.clicked.connect(self.stokekle)
        self.urunekleformbutton.clicked.connect(self.urunekleformu)
        self.urunusil.clicked.connect(self.urunsil)
    def kategoriitem_click(self,item):
        self.urunlist.clear()
        global q
        q=[]
        global kategori
        kategori=item.text()
        sql.urunlistele(str(kategori),q)

        for i in q:
            self.urunlist.addItem(i[0])
    def urunitem_click(self,item):
        global urun
        urun=item.text()
        print(urun)
        for i in q:
            if i[0]==str(urun):
             global stokadeti
             stokadeti=str(i[1])
             self.stokadet.setText(stokadeti)
    def stokekle(self):
        eklenecekadet=self.eklenecekstokadetint.text()
        sql.stokduzenle(int(eklenecekadet),urun)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Stok Düzenleme")
        msgBox.setWindowTitle("Stok Düzenlendi")
        returnValue = msgBox.exec()
        sql.urunlistele(str(kategori), q)
        for i in q:
            if i[0]==str(urun):
             global stokadeti
             stokadeti=str(i[1])
             self.stokadet.setText(stokadeti)
    def urunekleformu(self):
        urunekle = Urunekle()
        widget.addWidget(urunekle)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(356)
        widget.setFixedHeight(391)
    def urunsil(self):
        if str(urun)=="":


            self.urunlist.clear()
            self.stokadet.setText("")
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Lütfen Ürün Seçiniz")
            msgBox.setWindowTitle("Hata!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            sql.urunsil(str(urun))
            self.urunlist.clear()
            self.stokadet.setText("")
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Ürün Silindi")
            msgBox.setWindowTitle("Ürün Silme")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()



class Urunekle(QDialog):
    def __init__(self):
         super(Urunekle, self).__init__()
         loadUi("urunekle.ui",self)
         q2 = []
         sql.kategorilist(q2)
         for i in q2:
             self.kategoribox.addItem(str(i))
         self.uruneklebutton.clicked.connect(self.urunekle)


    def geridon(self):
        depo = Depo()
        widget.addWidget(depo)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedWidth(1128)
        widget.setFixedHeight(893)
    def urunekle(self):
        x = str(self.kategoribox.currentText())
        yeniurunismi = self.urunismiekleme.text()
        yeniurunadet = self.stokadetiekleme.text()
        sql.urunekle(x, str(yeniurunismi), int(yeniurunadet))
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Yeni Ürün Eklendi")
        msgBox.setWindowTitle("Ürün Ekleme")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.buttonClicked.connect(self.geridon)
        returnValue = msgBox.exec()












app=QApplication(sys.argv)
mainwindow=Giris()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()

