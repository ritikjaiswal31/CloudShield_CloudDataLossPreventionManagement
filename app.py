from tkinter import *
from tkinter import messagebox
import base64
import os
from fpdf import FPDF
import pikepdf

root = Tk()
root.title('Cloud Data Loss Prevention Management ---> Encryption Decryption Application')
root.geometry('925x500+300+200')
root.configure(bg='black')
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    if username =='admin' and password =='12345':
        screen = Toplevel(root)
        screen.title("Encryption Decryption Application")
        screen.geometry('925x500+300+200')
        screen.config(bg='black')

        Label(screen, text = 'Welcome to Cloud Data Loss Prevention Management', bg='#fff', font = ('Calibri(Body)', 22, 'bold')).pack(expand = True)

        screen.mainloop()

    elif username!= 'admin' and password!='12345':
        messagebox.showerror("Invalid", "Invalid username and password")
    
    elif password!="12345":
        messagebox.showerror('Invalid', "Invalid Password")

    elif username!="admin":
        messagebox.showerror("Invalid", "Invalid Username")

img = PhotoImage(file = 'login.png')
Label(root, image = img, bg = 'white').place(x=50, y=100)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text = 'Login', fg = 'black', bg = 'white', font = ('Calibri',22, 'bold'))
heading.place(x=130, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == ' ':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg = 'black', border = 0, bg = 'white', font = ('Calibri',11))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == ' ':
        code.insert(0, 'Password')

code = Entry(frame, width=25,  fg = 'black', border = 0, bg = 'white', font = ('Calibri',11))
code.place(x=30, y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Login', bg='black', fg='white', border=0, command = signin).place(x=35, y=204)
label = Label(frame,text="Cloud Data Loss Prevention Management", fg = 'black', bg = 'white', font = ('Calibri',9))
label.place(x=55, y=270)

root.mainloop()

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.message = ''

    def set_title(self, title):
        self.title = title

    def set_message(self, message):
        self.message = message

    def header(self):
        # Set up the title
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, self.title, 0, 1, 'C')

    def footer(self):
        # Add a page number
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def body(self):
        # Add the message
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, self.message)

screen = Tk()
screen.geometry("925x500+300+200")
screen.title("Encryption Decryption Application")
screen.configure(bg="black")
image_icon=PhotoImage(file="keys.png")
screen.iconphoto(False,image_icon)

#Encryption Function

def encrypt():
    password=code.get()

    if password == "12345":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("500x500")
        screen1.configure(bg="red")

        message = text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1, text="Encrypted Code", font="arial 12 bold", fg="white", bg="red").place(x=10, y=0) 
        text2=Text (screen1, font="arial 12 bold", bg="white", wrap=WORD, bd=0) 
        text2.place(x=10, y=40,width=380,height=150)
        text2.insert (END, encrypt)
        
    elif password=="": 
        messagebox.showerror ("Error", "Please Enter the Password")
    elif password !="12345":
        messagebox.showerror("Oops!", "Invalid Password")

    pdf = PDF()
    pdf.set_title("Encrypted Message")
    pdf.set_message(encrypt)
    pdf.add_page()
    pdf.body()
    filename = "encrypted_message.pdf"
    pdf.output(filename, 'F')
    messagebox.showinfo("Success", "The encrypted message has been saved as a PDF.")

    old_pdf = pikepdf.Pdf.open("encrypted_message.pdf")
    no_extr = pikepdf.Permissions(extract = False)
    old_pdf.save("passwordprotected_encryption.pdf", encryption = pikepdf.Encryption(user = "12345", owner = "ritik", allow = no_extr))
    

#Decryption Function

def decrypt():
    password = code.get()

    if password == '12345':
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("500x500")
        screen2.configure(bg = "green")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="Decrypted Code", font="arial 12 bold", fg="white", bg="green").place(x=10, y=0) 
        text2=Text (screen2, font="arial 12 bold", bg="white", wrap=WORD, bd=0) 
        text2.place(x=10, y=40,width=380,height=150)
        text2.insert (END, decrypt)
        
    elif password=="": 
        messagebox.showerror ("Error", "Please Enter the Password")
    elif password !="12345":
        messagebox.showerror("Oops!", "Invalid Password")

    pdf = PDF()
    pdf.set_title("Decrypted Message")
    pdf.set_message(decrypt)
    pdf.add_page()
    pdf.body()
    filename = "decrypted_message.pdf"
    pdf.output(filename, 'F')
    messagebox.showinfo("Success", "The decrypted message has been saved as a PDF.")

    old_pdf = pikepdf.Pdf.open("decrypted_message.pdf")
    no_extr = pikepdf.Permissions(extract = False)
    old_pdf.save("passwordprotected_decryption.pdf", encryption = pikepdf.Encryption(user = "12345", owner = "ritik", allow = no_extr))

#Reset Function

def reset():
  text1.delete(1.0, END)
  code.set("")

#Label

Label(screen, text = "Cloud Data Loss Prevention Management", font = "impack 15 bold").place (x=275, y=6)

#Text

text1 = Text(screen, font = "20")
text1.place(x=270, y=45, width = 410, height = 120)

#Label

Label(screen, text = "Enter Secret Key", font = "impack 13 bold").place(x=410, y=185)

#Entry
code = StringVar()

Entry(textvariable= code, bd = 4, font = "20", show = "*").place(x=365, y=220)

#Button

Button(screen, text = "ENCRYPT", font = "arial 15 bold", bg = "red", fg = "white", command = encrypt).place(x=230, y=280, width = 200)
Button(screen, text = "DECRYPT", font = "arial 15 bold", bg = "green", fg = "white", command = decrypt).place(x=530, y=280, width = 200)
Button(screen, text = "RESET", font = "arial 15 bold", bg = "blue", fg = "white", command = reset).place(x=360, y=350, width = 300)

screen.mainloop()