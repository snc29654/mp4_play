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

        

video=[0]*100
cap=[0]*100
sizerate=2
file_count=0
interval=0

#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        self.camera=0
        self.index_before = 0
        self.sizerate=2
        self.n_old=[]
        self.angle=0
        self.filenames =[]
        
        button3= Button(root_main, text=u'MP4選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=100, y=10) 

        button4= Button(root_main, text=u'カメラ', command=self.button4_clicked)  
        button4.grid(row=0, column=1)  
        button4.place(x=200, y=10) 



        self.txt3 = tkinter.Entry(width=10)
        self.txt3.place(x=100, y=40)
        self.txt3.insert(tkinter.END,"0.00")


        self.txt4 = tkinter.Entry(width=10)
        self.txt4.place(x=100, y=65)
        self.txt4.insert(tkinter.END,"2")

        self.txt5 = tkinter.Entry(width=45)
        self.txt5.place(x=10, y=90)
        self.txt5.insert(tkinter.END,"")


        label3 = tkinter.Label(text="コマ間隔(秒)")
        label3.pack(side="top")
        label3.place(x=20, y=40) 


        label4 = tkinter.Label(text="サイズ倍率 = 1/")
        label4.pack(side="top")
        label4.place(x=20, y=65) 



    def button3_clicked(self):  
       


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Video file", ".mp4") ], initialdir=iDir)
        print(self.filenames)
        self.quit()

    def button4_clicked(self):  
       

        self.camera=1
        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Video file", ".mp4") ], initialdir=iDir)
        print(self.filenames)
        self.quit()



    def quit(self):
        global video
        global file_count
        global interval
        global sizerate
        sizerate =self.txt4.get()
        sizerate =int(sizerate)

        interval =self.txt3.get()
        interval =float(interval)

        

        if(len(self.filenames)>100):  
            self.txt5.insert(tkinter.END,"ファイル数100超えました")

        else:
            
            file_count=0  
            for name in self.filenames:
                video[file_count]=name
                file_count=file_count+1
            if(self.camera==1):    
                video[0]=0
            root_main.destroy()

 



root_main= tkinter.Tk()  
c=image_gui(root_main)  
root_main.title("rootです")  
root_main.geometry("300x150") 





root_main.mainloop()




import cv2
import threading

for i in range(file_count):
    cap[i] = cv2.VideoCapture(video[i])
    if (cap[i].isOpened()== False):  
        print("mp4 open error") 



def play(no):
    qflag=0
    no=int(no)
    cap[no] = cv2.VideoCapture(video[no])
    while(cap[no].isOpened()):
        try:
            ret, frame = cap[no].read()
            width = frame.shape[1]
            height = frame.shape[0]
            width=int(width/sizerate)
            height=int(height/sizerate)
            time.sleep(interval)
            if ret == True:
                frame = cv2.resize(frame, (width, height))
                cv2.imshow("Video_"+str(no), frame)
        
                if cv2.waitKey(25) & 0xFF == ord('q'): 
                    qflag=1
                    break
    
            else:
                break
        except:
            break
    cap[no].release()
    if(qflag==0):
        play(no)
    cv2.destroyAllWindows()
  
thread=[0]*100

for i in range(file_count):
      
    thread[i] = threading.Thread(target=play, args=(i,))
    thread[i].start()


  