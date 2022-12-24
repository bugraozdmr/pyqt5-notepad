import sys
import os
from PyQt5.QtWidgets import *


class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazialani = QTextEdit()
        self.temizle = QPushButton("TEMİZLE")
        self.ac = QPushButton("DOSYA AÇ")
        self.kaydet = QPushButton("KAYDET")

        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.yazialani)

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.temiz)
        self.kaydet.clicked.connect(self.dosyala)
        self.ac.clicked.connect(self.open)
        self.setWindowTitle("Notepad x+")


    def open(self):  # 3 değer alıyor pencere objem,pencere ismi,alınacak dosya   ÖNEMLİ FONK        #demet şeklinde döndürüyor  getOpenFileName doğrusu     getOpenFileNames değil
        dosya_isim = QFileDialog.getOpenFileName(self,"DOSYA AÇ",os.getenv("HOME"))
        print(dosya_isim)
        with open(dosya_isim[0],"r",encoding="utf-8") as file:
            self.yazialani.setText(file.read())
    def dosyala(self):
        print("ewqe")
        dosya_isim = QFileDialog.getSaveFileName(self,"KAYDET",os.getenv("HOME"))
        with open(dosya_isim[0],"w",encoding="utf-8") as file:
            file.write(self.yazialani.toPlainText())
    def temiz(self):
        self.yazialani.clear()

class menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencere = pencere()
        self.setCentralWidget(self.pencere)

        self.menuler()

        self.setWindowTitle("NOTEPAD +X")
        self.show()
    def menuler(self):
        menu = self.menuBar()
        dosya = menu.addMenu("Dosya")

        dosya_ac = QAction("Dosya aç",self)
        dosya_ac.setShortcut("CTRL+R")
        dosya.addAction(dosya_ac)

        dosya_kaydet = QAction("Dosya kaydet",self)
        dosya_kaydet.setShortcut("CTRL+O")
        dosya.addAction(dosya_kaydet)

        temizle = QAction("Temizle",self)
        temizle.setShortcut("Ctrl+Q")
        dosya.addAction(temizle)

        cikis = QAction("Çıkış",self)
        cikis.setShortcut("CTRL+u")
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)

        self.setWindowTitle("Metin editörü")
        self.show()

    def response(self,action):
        if action.text() == "Dosya aç":
            self.pencere.open()     #nesneye yönelik programlamanın getirileri
        elif action.text() == "Dosya kaydet":
            self.pencere.dosyala()
        elif action.text() == "Temizle":
            self.pencere.temiz()
        elif action.text() == "Çıkış":
            QApplication.exit()
        else:
            print("hata aldın !")

app = QApplication(sys.argv)
menu1 = menu()
sys.exit(app.exec_())