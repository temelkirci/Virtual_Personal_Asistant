from Tulpar_Firebase import Tulpar_Firebase
from Tulpar_Web import Tulpar_Web
from Tulpar_Media import Tulpar_Media
from Tulpar_Instagram import Tulpar_Instagram

import sqlite3
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import threading
import requests
from os import startfile
import time

from threading import Thread

class MyApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("Tulpar.ui", self)

        self.tulpar_db = Tulpar_Firebase()
        self.tulpar_web = Tulpar_Web(self.frame)
        self.tulpar_media = Tulpar_Media(self)
        self.tulpar_insta = Tulpar_Instagram(self)

        self.picture_size.clear()
        self.picture_size.addItem("icon")
        self.picture_size.addItem("medium")
        self.picture_size.addItem("large")
        self.picture_size.addItem(">2MP")
        self.picture_size.addItem("<2MP")
        self.picture_size.addItem(">8MP")
        self.picture_size.addItem("<8MP")

        self.search_image_button.clicked.connect(self.download_image)
        self.instagram_search_button.clicked.connect(self.insta_search)

        self.pushButton.clicked.connect(self.save_data)

    def download_image(self):
        if self.image_textbox.text() == "" or self.download_number.text() == "" or int(self.download_number.text()) == 0 or self.picture_size.currentText() == "":
            pass
        else:
            x = threading.Thread(target=self.tulpar_media.downloadImage, args=(self.image_textbox.text(), int(self.download_number.text()), self.picture_size.currentText(), True,))
            x.start()

            self.image_textbox.setText("")
            self.download_number.setText("")

    def insta_search(self):
        if self.instagram_username_textbox.text() == "":
            pass
        else:
            x = threading.Thread(target=self.tulpar_insta.getinfo, args=(self.instagram_username_textbox.text(),))
            x.start()


    def save_data(self):
        try:
            self.tulpar_db.save_english_data(self.lineEdit.text(), self.lineEdit_2.text())
            self.showMessageBox("ENGLISH", "Sentence was added")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
        except:
            self.showMessageBox("Error", "Your sentence was not added")
            self.lineEdit.clear()
            self.lineEdit_2.clear()

    def showMessageBox(self, title, message):
        buttonReply = QMessageBox.question(self, title, message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')


if __name__ == "__main__":
    app = QApplication([])

    window = MyApp()
    window.show()

    app.exec_()
