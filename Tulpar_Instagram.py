#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json


class Tulpar_Instagram():

    def __init__(self, main_gui):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

        self.gui = main_gui

        """
        with open('users.txt') as f:
            self.content = f.readlines()
        self.content = [x.strip() for x in self.content]
        for url in self.content:
            self.getinfo(url)
        """

    def getinfo(self, username):
        try:
            url = "https://www.instagram.com/" + username

            html = urllib.request.urlopen(url, context=self.ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            data = soup.find_all('meta', attrs={'property': 'og:description'
                                 })
            text = data[0].get('content').split()
            user = '%s %s %s' % (text[-3], text[-2], text[-1])
            followers = text[0]
            following = text[2]
            posts = text[4]

            self.gui.user_label.setText(user)
            self.gui.followers_label.setText(followers)
            self.gui.following_label.setText(following)
            self.gui.post_label.setText(posts)

            print ('User:', user)
            print ('Followers:', followers)
            print ('Following:', following)
            print ('Posts:', posts)
            print ('---------------------------')
        except:
            self.gui.user_label.setText("####")
            self.gui.followers_label.setText("####")
            self.gui.following_label.setText("####")
            self.gui.post_label.setText("####")