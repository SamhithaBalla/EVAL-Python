# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atbt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 471, 31))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 13pt \"Rockwell\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 100, 471, 31))
        self.pushButton_2.setStyleSheet("font: 75 13pt \"Rockwell\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 160, 471, 31))
        self.pushButton_3.setStyleSheet("font: 75 13pt \"Rockwell\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 220, 471, 31))
        self.pushButton_6.setStyleSheet("font: 75 13pt \"Rockwell\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("dsBuffer.bmp.png"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EVAL"))
        self.pushButton.setText(_translate("MainWindow", "Enter Bloom\'s Levels into DB"))
        self.pushButton_2.setText(_translate("MainWindow", "Enter Bloom\'s Keywords into DB"))
        self.pushButton_3.setText(_translate("MainWindow", "Accept and Evaluate Question paper"))
        self.pushButton_6.setText(_translate("MainWindow", "Generate Report"))

