# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'antiplugiat.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import difflib
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 201, 17))
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 801, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(230, 0, 581, 26))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Антиплагиат v0.0001"))
        self.label.setText(_translate("MainWindow", "Порог срабатывания (%)"))
        self.label_2.setText(_translate("MainWindow", "Текст 1"))
        self.label_3.setText(_translate("MainWindow", "Текст 2"))
        self.pushButton.setText(_translate("MainWindow", "Сравнить"))
        self.pushButton.clicked.connect(self.cl_bn)

    def cl_bn(self):
        text1 = self.textEdit.toPlainText().split('\n')
        text2 = self.textEdit_2.toPlainText().split('\n')
        threshold = self.doubleSpinBox.text()
        flag = False
        proc_one = 100 / len(text1)
        count = 0
        for i in range(len(text1)):
            try:
                matcher = difflib.SequenceMatcher(None, text1[i], text2[i])
                if float(float(matcher.ratio()) * 100) >= float(threshold.split(',')[0]):
                    count += proc_one
            except IndexError:
                self.add_count_to_statusBar(round(count, 2))
                flag = True
                break
        if not flag:
            self.add_count_to_statusBar(round(count, 2))

    def add_count_to_statusBar(self, num):
        self.statusbar.showMessage(f'Код похож на {str(num)}%')
        if num > 50:
            self.statusbar.setStyleSheet('background: red;')
        else:
            self.statusbar.setStyleSheet('background: green;')


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
