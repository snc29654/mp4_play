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
import cv2
import threading

        


#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        self.cap=[0]*100
        self.video=[0]*100
        self.camera=0
        self.index_before = 0
        self.sizerate=2
        self.n_old=[]
        self.angle=0
        self.filenames =[]
        self.file_count=0  
        
        button3= Button(root_main, text=u'MP4選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=50, y=10) 


        button4= Button(root_main, text=u'カメラ', command=self.button4_clicked)  
        button4.grid(row=0, column=1)  
        button4.place(x=210, y=10) 

        button6= Button(root_main, text=u'終了', command=self.button6_clicked)  
        button6.grid(row=0, column=1)  
        button6.place(x=250, y=10) 


        self.txt3 = tkinter.Entry(width=6)
        self.txt3.place(x=100, y=40)
        self.txt3.insert(tkinter.END,"0.00")


        self.txt4 = tkinter.Entry(width=5)
        self.txt4.place(x=100, y=65)
        self.txt4.insert(tkinter.END,"2")

        self.txt6 = tkinter.Entry(width=5)
        self.txt6.place(x=100, y=90)
        self.txt6.insert(tkinter.END,"0")



        self.txt5 = tkinter.Entry(width=45)
        self.txt5.place(x=10, y=115)
        self.txt5.insert(tkinter.END,"")



        label3 = tkinter.Label(text="コマ間隔(秒)")
        label3.pack(side="top")
        label3.place(x=20, y=40) 


        label4 = tkinter.Label(text="サイズ倍率 = 1/")
        label4.pack(side="top")
        label4.place(x=20, y=65) 


        label5 = tkinter.Label(text="間引き数")
        label5.pack(side="top")
        label5.place(x=20, y=90) 


    def button3_clicked(self):  
       


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Video file", ".mp4") ], initialdir=iDir)
        print(self.filenames)
        button5= Button(root_main, text=u'再生', command=self.button5_clicked)  
        button5.grid(row=0, column=1)  
        button5.place(x=150, y=10) 


    def button4_clicked(self):  
       

        self.camera=1
        self.quit()
    def button5_clicked(self):  
       

        self.quit()


    def button6_clicked(self):  
       

        self.quit()
        root_main.destroy()




    def quit(self):
        global video


        for i in range(self.file_count):
            self.cap[i] = cv2.VideoCapture(self.video[i])
            if (self.cap[i].isOpened()== False):  
                print("mp4 open error") 


        self.sizerate =self.txt4.get()
        self.sizerate =int(self.sizerate)

        self.mabiki =self.txt6.get()
        self.mabiki =int(self.mabiki)

        self.interval =self.txt3.get()
        self.interval =float(self.interval)

        

        if(len(self.filenames)>100):  
            self.txt5.insert(tkinter.END,"ファイル数100超えました")

        else:
            
            self.file_count=0  
            for name in self.filenames:
                self.video[self.file_count]=name
                self.file_count=self.file_count+1
            if(self.camera==1):    
                self.video[0]=0
                self.file_count=1  
            #root_main.destroy()

            self.play_thread()
     
    def play(self,no):

        frame_count=0
        qflag=0
        no=int(no)
        self.cap[no] = cv2.VideoCapture(self.video[no])
        while(self.cap[no].isOpened()):
            try:
                ret, frame = self.cap[no].read()
                width = frame.shape[1]
                height = frame.shape[0]
                width=int(width/self.sizerate)
                height=int(height/self.sizerate)
                time.sleep(self.interval)
                if ret == True:
                    frame = cv2.resize(frame, (width, height))
                    if(frame_count%(self.mabiki+1)==0):
                        cv2.imshow("Video_"+str(no), frame)
        
                    if cv2.waitKey(25) & 0xFF == ord('q'): 
                        qflag=1
                        break
    
                else:
                    break
                frame_count=frame_count + 1
            except:
                break
        self.cap[no].release()
        if(qflag==0):
            self.play(no)
        cv2.destroyAllWindows()

    def play_thread(self):
        thread=[0]*100

        for i in range(self.file_count):
      
            thread[i] = threading.Thread(target=self.play, args=(i,))
            thread[i].start()





root_main= tkinter.Tk()  
c=image_gui(root_main)  
root_main.title("rootです")  
root_main.geometry("300x150") 


root_main.mainloop()








  


  