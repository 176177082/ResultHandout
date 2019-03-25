#!C:/Python27/ArcGIS10.2/python.exe
#-*- coding:utf-8 -*-
"""
#============================================
#
# Project: pyarcgis
# Name: The file name is mysqlite
# Purpose: 
# Auther: lantucx
# Tel: 17372796660
#
#============================================
#
"""
import sqlite3
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def mysqlite(dir,dbname):
	conn = sqlite3.connect(dbname)
	cursor = conn.cursor()
	cursor.execute('create table result (filepath varchar(5000), flag varchar(10))')
	for root, dirs, files in os.walk(dir, True):
		for name in files:
			path=os.path.join(root,name)
			row=(path,0)
			cursor.execute("insert into result values (?,?)",row)
		for name in dirs:
			path = os.path.join(root, name)
			row = (path, 0)
			cursor.execute("insert into result  values (?, ?)",row)
	cursor.close()
	conn.commit()
	conn.close()
	print dbname,u"扫描完成"
	return True


if __name__ == "__main__":
	mysqlite(u'E:\\arcgis10.2\\Arcgis Desktop 10.2.2',u"E:/sqlitedb/中国1.db")