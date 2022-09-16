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
import threading
import webbrowser
import os


        


#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, var,master=None):  
        self.cap=[0]*100
        self.video=[0]*100
        self.camera=0
        self.index_before = 0
        self.sizerate=2
        self.n_old=[]
        self.angle=0
        self.filenames =[]
        self.file_count=0  
        
        self.gridx=300
        self.gridy=400
        
       
        button3= Button(root_main, text=u'MP4選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=10, y=10) 

        button7= Button(root_main, text=u'MP4追加', command=self.button7_clicked)  
        button7.grid(row=0, column=1)  
        button7.place(x=80, y=10) 


        button6= Button(root_main, text=u'終了', command=self.button6_clicked)  
        button6.grid(row=0, column=1)  
        button6.place(x=250, y=10) 

        button8= Button(root_main, text=u'web表示', command=self.button8_clicked)  
        button8.grid(row=0, column=1)  
        button8.place(x=10, y=170) 



        
        self.var = var                      



    def button3_clicked(self):  

        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        self.filenames = tkFileDialog.askopenfilenames(filetypes= [("Video file", ".mp4") ], initialdir=iDir)
        print(self.filenames)


    def button7_clicked(self):  

        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        filenames = tkFileDialog.askopenfilenames(filetypes= [("Video file", ".mp4") ], initialdir=iDir)
        self.filenames=self.filenames + filenames
        print(self.filenames)



    def button4_clicked(self):  
       

        self.camera=1
        self.quit()
    def button5_clicked(self):  
       
        self.camera=0

        self.quit()


    def button6_clicked(self):  
       

        self.quit()
        root_main.destroy()

    def button8_clicked(self):  
        SAMPLE_DIR = "C:\\html_link"
 
        if not os.path.exists(SAMPLE_DIR):
        # ディレクトリが存在しない場合、ディレクトリを作成する
            os.makedirs(SAMPLE_DIR)       

        f = open("C:\\html_link\\web.html", 'w')


        datalist = []
        datalist.append('<!DOCTYPE html>\n')
        datalist.append('<html>\n')
        datalist.append('<head>\n')
        datalist.append('<title> 画像表示 </title>\n')  
        for file in self.filenames:
            datalist.append('<video controls width=300 src =  ')
            datalist.append(file)  
            datalist.append('  ></video>\n')  
            datalist.append('<a href =')
            datalist.append(file)
            datalist.append(' target = \"_blank\">▼</a>\n')
            
        datalist.append('</head>\n')
        datalist.append('<body>\n')
   
        
        
        datalist.append('</body>\n')
        f.writelines(datalist)

        f.close()



        webbrowser.open('C:/html_link/web.html')




    def quit(self):
        global video




        self.sizerate =self.txt4.get()
        self.sizerate =float(self.sizerate)

        self.mabiki =self.txt6.get()
        self.mabiki =int(self.mabiki)

        self.interval =self.txt3.get()
        self.interval =float(self.interval)


        self.gridx =self.txt7.get()
        self.gridx =int(self.gridx)

        self.gridy =self.txt8.get()
        self.gridy =int(self.gridy)


        self.x_count =self.txt10.get()
        self.x_count =int(self.x_count)

        self.exec_count =self.txt11.get()
        self.exec_count =int(self.exec_count)
        

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
        divide_param=0
        canny=0
        mono=0
        schetch=0
        schcolor=0
        sizerate=float(self.sizerate)
        mabiki=self.mabiki
        interval=self.interval
        for j in range(self.exec_count):
            frame_count=0
            qflag=0
            no=int(no)

    def play_thread(self):
        thread=[0]*100

        for i in range(self.file_count):
      
            thread[i] = threading.Thread(target=self.play, args=(i,))
            thread[i].start()





root_main= tkinter.Tk()  
root_main.title("webで動画再生")  
root_main.geometry("300x200") 

var = tk.StringVar(master=root_main)
l = tk.Label(textvariable=var,font=48)
l.place(x=0,y=0)
c=image_gui(master=root_main,var=var)  


root_main.mainloop()
