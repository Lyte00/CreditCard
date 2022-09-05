import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
import pyluhn
from pyluhn import verify

class frontpage(QDialog):
    def __init__(self):
        super(frontpage, self).__init__()
        loadUi("CreditCardEz.ui",self)
        self.VerifyButton.clicked.connect(self.validate)

    def validate(self):

        Input = self.NumberBox.text()

        if len(Input) != 16:
            error = QMessageBox()
            error.setWindowTitle("ERROR")
            error.setText("The input must contain 16 digits")

            x = error.exec_()

        if Input.isnumeric() == False:
            error = QMessageBox()
            error.setWindowTitle("ERROR")
            error.setText("The input must be numeric")

            x = error.exec_()

        if Input == "":
            error = QMessageBox()
            error.setWindowTitle("ERROR")
            error.setText("The input was empty")

            x = error.exec_()

        else:
            verification = verify(Input)
            if verification == True:
                success = QMessageBox()
                success.setWindowTitle("SUCCESS")
                success.setText("The card is valid :)")

                x = success.exec_()

            else:
                error = QMessageBox()
                error.setWindowTitle("ERROR")
                error.setText("The card is invalid :(")

                x = error.exec_()


app = QApplication(sys.argv)
window = frontpage()
window.show()

app.exec()

