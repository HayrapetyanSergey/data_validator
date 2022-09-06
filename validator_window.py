from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 70, 495, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_edit.setText("")
        self.line_edit.setObjectName("line_edit")
        self.horizontalLayout.addWidget(self.line_edit)
        self.multy_botton = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.multy_botton.addItem("Email")
        self.multy_botton.addItem("URL")
        self.multy_botton.addItem("Date (year-month-day)")
        self.multy_botton.addItem("Number")
        self.multy_botton.addItem("Credit Card")
        self.multy_botton.addItem("Armenian Phone Number(write together)")
        self.multy_botton.setObjectName("multy_botton")
        self.horizontalLayout.addWidget(self.multy_botton)
        self.btn_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check.setGeometry(QtCore.QRect(387, 160, 111, 32))
        self.btn_check.setObjectName("btn_check")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Validator"))
        self.btn_check.setText(_translate("MainWindow", "Check"))