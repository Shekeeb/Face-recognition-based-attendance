
import numpy as np
import cv2
from  src.encode_faces import enf
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import time
from src.dbconnection import *
from tkinter import *
from tkinter import messagebox
cap = cv2.VideoCapture(0)
WORD = re.compile(r'\w+')

from collections import Counter
import math
#-----------------------------
#face expression recognizer initialization
import pymysql
# con=pymysql.connect(host='localhost', port=3306,user='root',password='Root_root1',db='mask_violation')
# cmd=con.cursor()
fn=''
qry="SELECT DISTINCT `date` FROM `attendance` WHERE `date`!=CURDATE()"
res=selectall(qry)
for r in res:
	qryy="SELECT `login_id` FROM `student` WHERE `login_id` NOT IN(SELECT `stud_id` FROM `attendance` WHERE `date`=%s)"
	val=(str(r[0]),)
	print(val)
	reee=selectallnew(qryy,val)
	for rr in reee:
		qry="INSERT INTO `attendance` VALUES(NULL,%s,%s,'0')"
		val=(str(rr[0]),r[0])
		iud(qry,val)
while(True):
	try:
		ret, img = cap.read()
		# img=cv2.imread(fn)
		print(ret)

		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		emolist = []
		cv2.imshow("Frame", img)
		if len(faces) > 0:
			cv2.imwrite("samp.jpg",img)
			enf("samp.jpg")


		if cv2.waitKey(1) & 0xFF == 27:

			break
	except Exception as e:
		print(e)
		pass

