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
        self.filenames =[]
        self.file_count=0  
        
        
       
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
       

        self.quit()
    def button5_clicked(self):  
       

        self.quit()


    def button6_clicked(self):  
       

        self.quit()

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

        root_main.destroy()





root_main= tkinter.Tk()  
root_main.title("webで動画再生")  
root_main.geometry("300x200") 

var = tk.StringVar(master=root_main)
l = tk.Label(textvariable=var,font=48)
l.place(x=0,y=0)
c=image_gui(master=root_main,var=var)  


root_main.mainloop()
