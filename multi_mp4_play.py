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
        global file_count
        
        global sizerate
        sizerate =self.txt4.get()
        sizerate =int(sizerate)
        
        
        file_count=0  
        for name in self.filenames:
          video[file_count]=name
          file_count=file_count+1
        root_main.destroy()

 



root_main= tkinter.Tk()  
c=image_gui(root_main)  
root_main.title("rootです")  
root_main.geometry("300x100") 





root_main.mainloop()




import cv2
import threading

for i in range(file_count):
    cap[i] = cv2.VideoCapture(video[i])
    if (cap[i].isOpened()== False):  
        print("mp4 open error") 


def play(no):
    no=int(no)
    while(cap[no].isOpened()):

        ret, frame = cap[no].read()
        width = frame.shape[1]
        height = frame.shape[0]
        width=int(width/sizerate)
        height=int(height/sizerate)
        if ret == True:
            frame = cv2.resize(frame, (width, height))
            cv2.imshow("Video_"+str(no), frame)
        
            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break
    
        else:
            break
    cap[no].release()
    cv2.destroyAllWindows()
  
  
thread=[0]*100

for i in range(file_count):
      
    thread[i] = threading.Thread(target=play, args=(i,))
    thread[i].start()


  