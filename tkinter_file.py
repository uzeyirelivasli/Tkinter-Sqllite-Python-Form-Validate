# from tkinter import *
# import sqlite3 as db
# #connect server and create table
# conn = db.connect('tkinter_sign.db')
# cur  = conn.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS USER(
#       Fname TEXT,
#       Username TEXT,
#       Password TEXT
#      )''')
# cur.close()
# conn.commit()
# conn.close()
#
#
# def turn_to_sign(newWindow):
#     newWindow.destroy()
#     main_func()
#
# def sign_up_now(name,username,password):
#     name = name.get()
#     username = username.get()
#     password = password.get()
#     conn = db.connect('tkinter_sign.db')
#     conn.execute("insert into USER values(?, ?, ?)", (name, username, password))
#     conn.commit()
#     conn.close()
#
#
# def sign_up_window():
#      global newWindow
#      newWindow = Toplevel()
#      newWindow.title("New Window")
#      newWindow.geometry("300x300")
#
#      sign_up_status = Label(newWindow, text='sign up now :)')
#      sign_up_status.grid(row = 0 , column = 0)
#
#      Label(newWindow, text ="Name: ").grid(row = 1, column = 0)
#      Label(newWindow,  text ="Username ").grid(row = 2, column = 0)
#      Label(newWindow,  text ="Password: ").grid(row = 3, column = 0)
#
#      sign_up_name = Entry(newWindow)
#      sign_up_name.grid(row = 1, column = 1)
#
#      sign_up_username = Entry(newWindow)
#      sign_up_username.grid(row = 2, column = 1)
#
#      sign_up_password = Entry(newWindow)
#      sign_up_password.grid(row = 3, column = 1)
#
#      actual_sign_up_button = Button(newWindow, text = 'sign up now', command =lambda: sign_up_now(sign_up_name,sign_up_username,sign_up_password))
#      actual_sign_up_button.grid(row = 4, column = 2)
#
#      actual_sign_in_button = Button(newWindow , text = 'back to sign in', command =lambda : turn_to_sign(newWindow))
#      actual_sign_in_button.grid(row = 5, column = 2 )
#
#      master.withdraw()
#
#
# def select_et(username,password):
#     conn = db.connect('tkinter_sign.db')
#     data=conn.execute("select * from USER where Username=? and Password=?", (username, password))
#     data=data.fetchall()
#     conn.commit()
#     conn.close()
#     return data
#
#
# def sign_in_func(Username,Password):
#     UsernameValue = Username.get()
#     PasswordValue = Password.get()
#     data = select_et(UsernameValue, PasswordValue)
#     global status
#     if data==[]:
#         status.set('Daxil edilen melumatlar yanlisdir')
#         print('yanlis')
#
#     else:
#         status.set('Xos geldiniz')
#         print('dogru')
#
#
# def main_func():
#  #CREATE WINDOW
#     global master
#     master = Tk()
#     master.geometry('500x300')
#
#     global status
#     status = StringVar()
#  #LABELS
#     Label(master, text='Username: ').grid(row = 0, column = 0)
#     Label(master, text='Password: ').grid(row = 1, column = 0 )
#     status_label = Label(master, textvariable = status)
#     status_label.grid(row = 2, column = 2)
#
#  #ENTRY
#     Username = Entry(master)
#     Username.grid(row = 0, column = 1)
#     Password = Entry(master)
#     Password.grid(row = 1, column = 1)
#
#  #button
#     sign_up_btn = Button(master,text = 'sign up', command = sign_up_window)
#     sign_up_btn.grid(row = 4, column = 2)
#     sign_in_btn = Button(master,text = 'sign in', command = lambda: sign_in_func(Username,Password))
#     sign_in_btn.grid(row = 4, column = 3)
#
#     master.mainloop()
#
# main_func()


from tkinter import *
import sqlite3 as db
#connect server and create table
conn = db.connect('tkinter_sign.db')
cur  = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS USER(
      Fname TEXT,
      Username TEXT,
      Password TEXT
     )''')
cur.close()
conn.commit()
conn.close()


#MELUMATI BAXIR KI SQL SERVER DE BU ISTIFADECI VAR YA YOX
def select_et(username,password):
    conn = db.connect('tkinter_sign.db')
    data=conn.execute("select * from USER where Username=? and Password=?", (username, password))
    data=data.fetchall()
    conn.commit()
    conn.close()
    return data


class Window:
    def __init__(self, root, geometry):
        self.root = root
        self.root.geometry(geometry)  

#ESAS EKRAN
class rootWindow(Window):
    def __init__(self, root,geometry):
        super().__init__(root, geometry)
        
        #SIGN UP WINDOWUNU AC
        def sign_up_window_func():
            self.root.withdraw()
            newWindow = Toplevel()
            newWindow = Sign_Up_Window(newWindow,'300x300')
            
        #SIGN IN => MELUMATI SQL'DEN YOXLASIN 
        def sign_in_func(Username,Password,status):
            UsernameValue = Username.get()
            PasswordValue = Password.get()
            #SELECT ET FUNKSIYASI YOXDU
            data = select_et(UsernameValue, PasswordValue)
            
            if UsernameValue == "" or PasswordValue=="":
                print('yanlis')
                status.set('Daxil edilen melumatlar yanlisdir')
            elif data==[]:
                status.set('Daxil edilen melumatlar yanlisdir')
                print('yanlis')
            else:
                status.set('Xos geldiniz')
                print('dogru')
           
        #LABELS
        status = StringVar()
        Label(self.root, text='Username: ').grid(row = 0, column = 0)
        Label(self.root, text='Password: ').grid(row = 1, column = 0 )
        Label(self.root, textvariable = status).grid(row = 2, column = 0)
        
        #ENTRY
        Username = Entry(self.root)
        Username.grid(row = 0, column = 1)
        Password = Entry(self.root)
        Password.grid(row = 1, column = 1)
        
        #BUTTON
        sign_up_btn = Button(self.root,text = 'sign up', command = sign_up_window_func)
        sign_up_btn.grid(row = 4, column = 2)
        sign_in_btn = Button(self.root,text = 'sign in', command = lambda: sign_in_func(Username,Password,status) )
        sign_in_btn.grid(row = 4, column = 3)
        
        self.root.mainloop()

    
#SIGN UP PENCERESINI YARAT 
class Sign_Up_Window(Window):
    def __init__(self, root,geometry):
        super().__init__(root, geometry)
        
        def turn_to_sign():
            self.root.withdraw()
            #root mainloop etmek lazimdi
            main_window_func()
            
        def sign_up_now(name,username,password):
            name = name.get()
            username = username.get()
            password = password.get()
            conn = db.connect('tkinter_sign.db')
            conn.execute("insert into USER values(?, ?, ?)", (name, username, password))
            conn.commit()
            conn.close() 
               
        sign_up_status = Label(self.root, text='sign up now :)')
        sign_up_status.grid(row = 0 , column = 0)

        Label(self.root, text ="Name: ").grid(row = 1, column = 0)
        Label(self.root,  text ="Username ").grid(row = 2, column = 0)
        Label(self.root,  text ="Password: ").grid(row = 3, column = 0)

        sign_up_name = Entry(self.root)
        sign_up_name.grid(row = 1, column = 1)

        sign_up_username = Entry(self.root)
        sign_up_username.grid(row = 2, column = 1)

        sign_up_password = Entry(self.root)
        sign_up_password.grid(row = 3, column = 1)

        actual_sign_up_button = Button(self.root, text = 'sign up now', command = lambda: sign_up_now(sign_up_name,sign_up_username,sign_up_password) )
        actual_sign_up_button.grid(row = 4, column = 2)
 
        actual_sign_in_button = Button(self.root , text = 'back to sign in', command = turn_to_sign )
        actual_sign_in_button.grid(row = 5, column = 2 )

        self.root.mainloop()   

def main_window_func():
  #CREATE WINDOW
     main_screen = Tk()
     main_screen = rootWindow(main_screen,'500x300')
main_window_func()



    
































