from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

from random import *
import string


class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.generate_btn.clicked.connect(self.generate)

    def generate(self):
        symbols = string.ascii_letters + string.digits
        password = ""
        for i in range(8):
            password += choice(symbols)

        self.ui.password_label.setText(password)



app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
