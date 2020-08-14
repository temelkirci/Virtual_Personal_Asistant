from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class Tulpar_Web():
    def __init__(self, page):
        self.web = QWebEngineView(page)
        self.web.setGeometry(5,10,1800,600)

        self.loadWebPage("https://www.google.com/")

    def loadWebPage(self, page_url):
        self.web.load(QUrl(page_url))
        self.web.show()
