#!C:/Python27/ArcGIS10.2/python.exe
#-*- coding:utf-8 -*-
"""
#============================================
#
# Project: ResultHandout
# Name: The file name is mockdata
# Purpose: 
# Auther: lantucx
# Tel: 17372796660
#
#============================================
#
"""
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ResultHandout.settings")
import django

django.setup()

from results.models import Result
from faker import Faker

def mockdata():
    f = Faker(locale='zh_CN')
    for i in range(10000):
        x =f.file_path(13)
        Result.objects.create(path=x,pathdeep=13,pathlength=39)
    return True


if __name__ == "__main__":
    mockdata()