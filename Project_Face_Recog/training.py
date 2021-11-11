from tkinter import *
import tkinter
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
import cv2
import os
import numpy as np

class Trainng:
    def __init__(self,window):
        # window
        self.window=window
        self.window.geometry("1280x720-0+0")
        self.window.state('zoomed')
        self.window.title("Train Data")

        # Bg image
        bg=Image.open("Images/Training/bg.jpg")
        bg=bg.resize((1280,720),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)
        bglbl=Label(self.window,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)
        # heading
        heading=Label(self.window,text="Training Data",font=("times new roman",40,"bold"),bg="black",fg="darkgreen").place(x=0,y=20,relwidth=1)
        # training btn
        btn_img1=Image.open("Images/Training/img.png")
        btn_img1=btn_img1.resize((300,300),Image.ANTIALIAS)
        self.btn_img1=ImageTk.PhotoImage(btn_img1)
        b1=Button(self.window,image=self.btn_img1,command=self.training,cursor="hand2").place(x=490,y=150,width=300,height=200)
        b1_1=Button(self.window,text="Click Here To Train",command=self.training,cursor="hand2",font=("times new roman",15,"bold"),fg="red").place(x=490,y=350,width=300,height=40)

        # back btn
        bckimg=Image.open("Images/back.jpg")
        bckimg=bckimg.resize((50,50),Image.ANTIALIAS)
        self.bckimg=ImageTk.PhotoImage(bckimg)
        bck=Button(self.window,image=self.bckimg,cursor="hand2",command=self.windexit).place(x=20,y=30,width=50,height=50)

        # bottom img
        img=Image.open("Images/Training/img1.png")
        img=img.resize((1280,200),Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(img)
        imglbl=Label(self.window,image=self.img).place(x=0,y=450,relwidth=1,height=200)

    def training(self):
        data_folder=('PhotosSample')
        path=[ os.path.join(data_folder,file) for file in os.listdir(data_folder)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') # converting into grayscale image
            imgnp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imgnp)
            ids.append(id)
            cv2.imshow("Training",imgnp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # training the classifier
        classifr=cv2.face.LBPHFaceRecognizer_create()
        classifr.train(faces,ids)
        classifr.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Successful!!!",parent=self.window)

    # to exit
    def windexit(self):
        self.windexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit ? ",parent=self.window)
        if self.windexit>0:
            self.window.destroy()
        else:
            return

if __name__=="__main__":
    window=Tk()
    ob=Trainng(window)
    window.mainloop()