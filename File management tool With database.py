import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456789",database="Serverpath")


main_win = tkinter.Tk()
main_win.title("File Management Application")
message='Note :SELECT THE LOCAL SERVER BEFORE USING THE TOOL'
w = Label(main_win, text=message)
w.config(bg='lightgreen')
w.pack()
main_win.geometry("350x450")
mycursor =mydb.cursor()

def sql(sfile_path,dfile_path,commit_message):
    sql = "INSERT INTO details (sourcepath,despath, message) VALUES (%s, %s, %s)"
    val =(sfile_path,dfile_path,commit_message)
    mycursor.execute(sql, val)
    mydb.commit()
    print("record inserted.")

def chooseDir():
    main_win.sourcedir =  filedialog.askdirectory(parent=main_win, initialdir= "/", title='Please select a directory')
    x=input("Enter a folder name starting with \\\:")
    shutil.copytree(main_win.sourcedir,main_win.changeser+x)
    message = input("Commit message :")
    sql(main_win.sourcedir,main_win.changeser,message)


def chooseFile():
    main_win.sourcefile = filedialog.askopenfilename(parent=main_win, initialdir= "/", title='Please select a directory')
    shutil.copy2(main_win.sourcefile,main_win.changeser)
    message = input("Commit message :")
    sql(main_win.sourcefile, main_win.changeser, message)

def Server():
    os.startfile(main_win.changeser)

def changeser():
    main_win.changeser =  filedialog.askdirectory(parent=main_win, initialdir= "/", title='Select Server')
    message = input("Commit message :")
    sql("no source path", main_win.changeser, message)

def openfile():

    f = []
    f=os.listdir(main_win.changeser)
    print(f)
    n=int(input("Select the index of the file :"))
    filename=input("Enter the new file name for the duplication of the source file :")
    shutil.copy2(main_win.changeser+'/'+f[n],main_win.changeser+'/'+filename)
    text = open(main_win.changeser+'/'+filename, "r+")
    print(text.read())
    to_add=input("Write the file : ")
    text.write(to_add)
    text.close()
    message = input("Commit message :")
    sql("no source path", main_win.changeser, message)

b_changeser = tkinter.Button(main_win, text = "Select the Local server", width = 30, height = 3, command = changeser)
b_changeser.place(x = 65,y = 50)

b_chooseDir = tkinter.Button(main_win, text = "Upload Entire Folder", width = 30, height = 3, command = chooseDir)
b_chooseDir.place(x =65,y = 125)

b_chooseFile = tkinter.Button(main_win, text = "Upload File", width = 30, height = 3, command = chooseFile)
b_chooseFile.place(x = 65,y = 200)

b_Server = tkinter.Button(main_win, text = "Open Local Server", width = 30, height = 3, command = Server)
b_Server.place(x = 65,y = 275)

b_Server = tkinter.Button(main_win, text = "Open a File", width = 30, height = 3, command = openfile)
b_Server.place(x = 65,y = 350)

main_win.mainloop()
