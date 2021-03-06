# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
from PyQt5.QtCore import QUrl


import sys

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitscreen_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.splitscreen_button.setFont(font)
        self.splitscreen_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.splitscreen_button.setObjectName("splitscreen_button")
        self.gridLayout_3.addWidget(self.splitscreen_button, 1, 1, 1, 1)
        self.quickWidget_3 = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget_3.setObjectName("quickWidget_3")
        self.gridLayout_3.addWidget(self.quickWidget_3, 0, 1, 1, 1)

        self.quickWidget_3.setSource(QUrl('navigationAndInformation.qml')) #add qml to quickwidget

        self.horizontalLayout_5.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.quickWidget_2 = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget_2.setObjectName("quickWidget_2")
        self.gridLayout_6.addWidget(self.quickWidget_2, 0, 0, 1, 1)

        self.quickWidget_2.setSource(QUrl('offline.qml')) #add qml to quickwidget

        self.offline_map_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.offline_map_button.setFont(font)
        self.offline_map_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.offline_map_button.setObjectName("offline_map_button")
        self.gridLayout_6.addWidget(self.offline_map_button, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.quickWidget_4 = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget_4.setObjectName("quickWidget_4")
        self.gridLayout_2.addWidget(self.quickWidget_4, 1, 0, 1, 1)
        
        self.quickWidget_4.setSource(QUrl('information.qml')) #add qml to quickwidget

        self.information_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.information_button.setFont(font)
        self.information_button.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.information_button.setObjectName("information_button")
        self.gridLayout_2.addWidget(self.information_button, 2, 0, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setStyleSheet("")
        self.quickWidget.setObjectName("quickWidget")
        self.gridLayout_7.addWidget(self.quickWidget, 0, 0, 1, 1)

        self.quickWidget.setSource(QUrl('online.qml')) #add qml to quickwidget

        self.online_map_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.online_map_button.setFont(font)
        self.online_map_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.online_map_button.setObjectName("online_map_button")
        self.gridLayout_7.addWidget(self.online_map_button, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.splitscreen_button.setText(_translate("MainWindow", "Push"))
        self.offline_map_button.setText(_translate("MainWindow", "Push"))
        self.information_button.setText(_translate("MainWindow", "Push"))
        self.online_map_button.setText(_translate("MainWindow", "Push"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
