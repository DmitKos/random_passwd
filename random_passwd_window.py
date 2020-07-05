from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random
import string
from random_password import random_passwd


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(700, 400, 600, 300)
        self.setWindowTitle("Password Generator")
        self.initUI()

    def initUI(self):
        self.label_spin = QtWidgets.QLabel(self)
        self.label_spin.setText("Выберите длину пароля: ")
        self.label_spin.setGeometry(QtCore.QRect(180, 50, 150, 16))

        self.spin = QtWidgets.QSpinBox(self)
        self.spin.setProperty("value", 8)
        self.spin.move(250, 80)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Сгенерированный пароль: ")
        self.label.setGeometry(QtCore.QRect(180, 135, 170, 16))

        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.setGeometry(QtCore.QRect(180, 160, 200, 60))
        self.text_edit.setPlaceholderText("Сгенерированный пароль")

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Сгенерировать!")
        self.b1.clicked.connect(self.clicked_btn)
        self.b1.move(260, 230)

    def clicked_btn(self):
        r = random_passwd(int(self.spin.value()))
        self.text_edit.setText(str(''.join(map(str, r))))


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
