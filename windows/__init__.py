# -*- coding: UTF-8 -*-
from PySide2.QtWidgets import QMainWindow
from windows.ui import mainwindow

class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)