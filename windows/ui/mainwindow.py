# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Project\travis-pyside2-demo\ui\mainwindow.ui',
# licensing of 'D:\Project\travis-pyside2-demo\ui\mainwindow.ui' applies.
#
# Created: Wed Nov 27 16:46:18 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 178)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "travis-pyside2-demo", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "travis-pyside2-demo", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Hello world!</span></p></body></html>", None, -1))

