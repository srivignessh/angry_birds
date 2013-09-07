import serial
import time
import win32api
import math
import win32con
import win32com.client
def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
def click_and_drag(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
win32api.Sleep(100)
ser=serial.Serial(port='\\.\COM2', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
#ser.open()
ser.isOpen()
outx=''
outy=''
time.sleep(5)
while(1):
	if(ser.inWaiting()>0):
		c=ser.read(1)
		if(c=='a'):
			outx=ser.read(4)
		elif (c=='s'):
			outy=ser.read(4)
		elif(c=='b'):
			print 'begin'
			click_and_drag(375,400)
			click_and_drag(375,400)
			click_and_drag(375,400)
		elif(c=='e'):
			print 'end'
			click(x,y)
			#ser.close()
			#exit()
	if(outx != '' and outy != ''):		
		d1=int(outx)
		d2=int(outy)
		#print d1,d2
		#click(d2+200,d2+200)
		theta=((math.pi/600)*d1)+3*math.pi+math.pi/6
		r=(0.64)*d2-70
		x = int(371+r*math.sin(theta))
		y = int(411+r*math.cos(theta))
		click_and_drag(x,y)
		print r,theta
		outx=''
		outy=''
