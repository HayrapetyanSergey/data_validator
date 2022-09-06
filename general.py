from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import validator_window
import functions

class StartWindow(QMainWindow, validator_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.text = None
        self.check_type = None
        
        self.btn_check.clicked.connect(self.press)

    def press(self):
        self.text = self.line_edit.text()
        self.type = self.multy_botton.currentText()
        if self.type == 'Email':  
            valid = functions.is_email(self.text)
        elif self.type == 'URL':
            valid = functions.is_website_URL(self.text)
        elif self.type == 'Date (year-month-day)':
            valid = functions.is_Date(self.text)
        elif self.type == 'Number':
            valid = functions.is_number(self.text)
        elif self.type == 'Credit Card':
            valid = functions.is_CreditCard(self.text)
        elif self.type == 'Armenian Phone Number(write together)':
            valid = functions.is_mobile(self.text)

        if valid:
            message = f'Your {self.type} is valid'
        else:
            message = f'Your {self.type} is not valid'
        QMessageBox.about(self, "", message)
        
app = QApplication([])

widget = StartWindow()
widget.show()

app.exec()