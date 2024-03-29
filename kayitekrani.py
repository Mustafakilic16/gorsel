from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 692)
        MainWindow.setStyleSheet("#centralwidget{\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(9, 172, 869, 371))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(230, 180, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(230, 0, 111, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(230, 90, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(230, 270, 71, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 30, 261, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 120, 261, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_isim = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_isim.setGeometry(QtCore.QRect(230, 210, 261, 41))
        self.lineEdit_isim.setObjectName("lineEdit_isim")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 300, 261, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(565, 101, 321, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(9, 557, 869, 121))
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(600, 13, 131, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 13, 141, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(9, 9, 869, 151))
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(parent=self.widget_3)
        self.label.setGeometry(QtCore.QRect(370, 79, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "   isim"))
        self.label_3.setText(_translate("MainWindow", "T.C Kimlik Numarası"))
        self.label_4.setText(_translate("MainWindow", "Telefon Numarası"))
        self.label_5.setText(_translate("MainWindow", "Araç Plakası"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "isim"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "plaka"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "numara"))
        self.pushButton.setText(_translate("MainWindow", "GİRİŞ"))
        self.pushButton_2.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.label.setText(_translate("MainWindow", "MUSPARK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
