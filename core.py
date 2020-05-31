from PIL import Image
from io import BytesIO
from math import *
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
from time import sleep
from urllib.request import urlopen
import speech_recognition as sr
from bs4 import BeautifulSoup
import threading
from googlesearch import search
import os
from selenium import webdriver
import os
import time
from youtube_search import YoutubeSearch
import sys
import wikipedia
from pydub import AudioSegment
from django.http.response import StreamingHttpResponse
from django.shortcuts import render
import random
import smtplib
from django.views import generic
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import json
import pyrebase
from googletrans import Translator
import urllib.request
import urllib.parse
import youtube_dl
import re
from twilio.twiml.messaging_response import Message, MessagingResponse
wikipedia.set_lang("en")

def get_apk(app_name):
    site = "https://apkpure.com"
    url = "https://apkpure.com/search?q=%s" % (app_name)
    html = requests.get(url)
    parse = BeautifulSoup(html.text)
    for i in parse.find_all("p",class_="search-title"):
        try:
            a_url = i.find("a")["href"]
            app_url = site + a_url + "/download?from=details"
            html2 = requests.get(app_url)
            parse2 = BeautifulSoup(html2.text)
            link=parse2.find("a", id="download_link")
            return link["href"]
        except:
            pass

def trad(m, l):
    translator = Translator()
    return translator.translate(m, src='auto', dest=l).text
