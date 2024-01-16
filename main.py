import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import QtWidgets
from python_deneme1 import Ui_MainWindow
from pymongo import MongoClient

class LoginWindow(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.main_window = main_window

        self.ui.pushButton.clicked.connect(self.login_clicked)

        # MongoDB bağlantısı
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['giris']
        self.collection = self.db['kullanicilar']

    def login_clicked(self):
        # Kullanıcı adı ve şifre
        correct_username = "admin"
        correct_password = "123"

        # Kullanıcının girdiği değerler
        entered_username = self.ui.lineEdit_isim.text()
        entered_password = self.ui.lineEdit_2.text()

        # Kullanıcı adı ve şifre kontrolü
        if entered_username == correct_username and entered_password == correct_password:
            QMessageBox.information(self, "Başarılı", "Giriş Başarılı!")

            # Kullanıcıyı MongoDB'ye ekle
            self.collection.insert_one({'username': entered_username, 'password': entered_password})

            # Giriş başarılı, ana pencereyi göster
            self.main_window.show_main_window()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.login_window = LoginWindow(self)
        self.ui.pushButton.clicked.connect(self.show_login_window)

        # MongoDB bağlantısı
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['giris']
        self.collection = self.db['veriler']

    def show_login_window(self):
        self.login_window.show()

    def show_main_window(self):
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = MainWindow()
    
    pencere.show()
    sys.exit(app.exec())
