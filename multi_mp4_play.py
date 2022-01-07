### インポート
import tkinter
import glob
from tkinter import *
from PIL import ImageTk, Image
import os
import sys
import time
import tkinter
from PIL import Image, ImageTk
import threading
import time
import glob
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import shutil
import os
import glob
from tkinter import filedialog as tkFileDialog
import tkinter as tk
from tkinter import font

        

video=[0]*4
cap=[0]*4
sizerate=2


#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        self.index_before = 0
        self.sizerate=2
        self.n_old=[]
        self.angle=0
        self.filenames =[]
        
        button3= Button(root_main, text=u'MP4選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=100, y=10) 

        self.txt4 = tkinter.Entry(width=10)
        self.txt4.place(x=100, y=40)
        self.txt4.insert(tkinter.END,"2")

        label4 = tkinter.Label(text="サイズ倍率 = 1/")
        label4.pack(side="top")
        label4.place(x=20, y=40) 



    def button3_clicked(self):  
       


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Video file", ".mp4") ], initialdir=iDir)
        print(self.filenames)
        self.quit()


    def quit(self):
        global video
        
        global sizerate
        sizerate =self.txt4.get()
        sizerate =int(sizerate)
        
        
        i=0  
        for name in self.filenames:
          video[i]=name
          i=i+1
        root_main.destroy()

 



root_main= tkinter.Tk()  
c=image_gui(root_main)  
root_main.title("rootです")  
root_main.geometry("300x100") 





root_main.mainloop()




import cv2
import threading


cap[0] = cv2.VideoCapture(video[0])
cap[1] = cv2.VideoCapture(video[1])
cap[2] = cv2.VideoCapture(video[2])
cap[3] = cv2.VideoCapture(video[3])


if (cap[0].isOpened()== False):  
    print("mp4 open error") 
if (cap[1].isOpened()== False):  
    print("mp4 open error") 
if (cap[2].isOpened()== False):  
    print("mp4 open error") 
if (cap[3].isOpened()== False):  
    print("mp4 open error") 


def play1():
    while(cap[0].isOpened()):

        ret, frame = cap[0].read()
        width = frame.shape[1]
        height = frame.shape[0]
        width=int(width/sizerate)
        height=int(height/sizerate)
        if ret == True:
            frame = cv2.resize(frame, (width, height))
            cv2.imshow("Video_1", frame)
        
            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break
    
        else:
            break
    cap[0].release()
    cv2.destroyAllWindows()
  
  
def play2():
    while(cap[1].isOpened()):
    
    
        ret, frame = cap[1].read()
        width = frame.shape[1]
        height = frame.shape[0]
        width=int(width/sizerate)
        height=int(height/sizerate)
        if ret == True:
            frame = cv2.resize(frame, (width, height))
            cv2.imshow("Video_2", frame)
        
            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break
    
        else:
            break


    cap[1].release()
    cv2.destroyAllWindows()
  


def play3():
    while(cap[2].isOpened()):
    
    
        ret, frame = cap[2].read()
        width = frame.shape[1]
        height = frame.shape[0]
        width=int(width/sizerate)
        height=int(height/sizerate)
        if ret == True:
            frame = cv2.resize(frame, (width, height))
            cv2.imshow("Video_3", frame)
        
            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break
    
        else:
            break


    cap[2].release()
    cv2.destroyAllWindows()


def play4():
    while(cap[3].isOpened()):
    
    
        ret, frame = cap[3].read()
        width = frame.shape[1]
        height = frame.shape[0]
        width=int(width/sizerate)
        height=int(height/sizerate)
        if ret == True:
            frame = cv2.resize(frame, (width, height))
            cv2.imshow("Video_4", frame)
        
            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break
    
        else:
            break


    cap[3].release()
    cv2.destroyAllWindows()


  
thread1 = threading.Thread(target=play1)
thread1.start()

#jpgの変更処理
thread2 = threading.Thread(target=play2)
thread2.start()

thread3 = threading.Thread(target=play3)
thread3.start()

thread4 = threading.Thread(target=play4)
thread4.start()

  