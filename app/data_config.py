#!/usr/bin/python
import os

basedir = os.getcwd() + '/db/'
DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'lahman.db')

if __name__ == "__main__":
	print (DATABASE_URI)
