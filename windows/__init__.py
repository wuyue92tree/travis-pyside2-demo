# -*- coding: UTF-8 -*-
from PySide2.QtWidgets import QMainWindow
from windows.ui import mainwindow, browserwindow
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide2.QtWebChannel import QWebChannel
from PySide2.QtCore import QUrl


class BrowserWindow(QMainWindow, browserwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(BrowserWindow, self).__init__(parent)
        self.setupUi(self)
        self.browserView = QWebEngineView()
        self.browserPage = QWebEnginePage()
        self.browserChannel = QWebChannel()
        self.browserView.resize(500, 200)
        self.browserPage.setWebChannel(self.browserChannel)
        self.browserView.setPage(self.browserPage)


class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.browser = BrowserWindow(self)
        self.pushButton.clicked.connect(self.open_browser)

    def open_browser(self):
        print('browser called.')
        url = QUrl('https://www.antio.top')
        self.browser.browserView.load(url)
        self.browser.browserView.show()

