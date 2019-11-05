from google_images_download import google_images_download

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import glob, os

class Tulpar_Media():
    def __init__(self, page):
        self.response = google_images_download.googleimagesdownload()  # class instantiation
        self.page = page

        #self.downloadImage("Silvia saint", 5, False)


    def downloadImage(self, keyword, limit, size, print_url):

        """
        "format": "jpg"
        "size": "medium"  -> ">2MP"
        "aspect_ratio: "panoramic"
        "time": "past-24-hours"
        "output_directory": "c:/"
        "specific_site": "www.facebook.com"

        """
        print(size)
        arguments = {
                        "keywords": keyword,
                        "size": size,
                        "limit": limit, #limit max 100
                        "print_urls": print_url
                     }
        # creating list of arguments

        paths = self.response.download(arguments)  # passing the arguments to the function

        print(paths)  # printing absolute paths of the downloaded images

        download_url = r"C:/Users/temel/Desktop/Tulpar/downloads/" + keyword
        file_list = os.listdir(download_url)

        for x in file_list:
            if int(os.path.getsize(download_url + "/" + x)) < 10000:
                os.remove(download_url + "/" + x)


        #self.page.label_3.setPixmap(QPixmap("C:/Users/temel/PycharmProjects/Tulpar/downloads/" + keyword + "/" + file_list[0]))
        image_path = download_url + keyword + "/" + file_list[0]

        image_profile = QImage(image_path)  # QImage object
        image_profile = image_profile.scaled(600,300, aspectRatioMode=Qt.KeepAspectRatio,
                                             transformMode=Qt.SmoothTransformation)  # To scale image for example and keep its Aspect Ration
        self.page.label_3.setPixmap(QPixmap.fromImage(image_profile))

