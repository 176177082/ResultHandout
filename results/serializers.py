#!C:/Python27/ArcGIS10.2/python.exe
#-*- coding:utf-8 -*-
"""
#============================================
#
# Project: ResultHandout
# Name: The file name is serializers
# Purpose: 
# Auther: lantucx
# Tel: 17372796660
#
#============================================
#
"""

from rest_framework import serializers
from results.models import Result


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'path', 'pathdeep', 'pathlength')