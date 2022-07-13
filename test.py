from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Tunify Media Player - Login")
        self.root.geometry("1200x675+110+50")
        self.root.resizable(False, False)
        
        #>>Background Image<< 
        self.bg = ImageTk.PhotoImage(Image.open("D:/Python/Music Player/login2.jpg"))
        self.bg_image = Label(root, image=self.bg)
        self.bg_image.place(x=0, y=0, relheight=1, relwidth=1)
        
        #>>Frame<<
        Frame_main = Frame(self.root, bg="whitesmoke")
        Frame_main.place(x=150, y=125, height=350, width=510)

        #>>Main<<
        head = Label(Frame_main, text = "Login Here!", font = ("Audiowide", 30, "bold"), fg="#0f3057", bg="whitesmoke")
        head.place(x=130, y=30)

        lbl_username = Label(Frame_main, text="Username:", fg="#00587a", bg="whitesmoke", font=("Titillium Web ExtraLight", 15, "bold"))
        lbl_username.place(x=60, y=110)
        self.txt_username = Entry(Frame_main, font=("Titillium Web ExtraLight", 15, "bold"), bg="lightgrey")
        self.txt_username.place(x=90, y=150, width=350, height=30)

        lbl_password = Label(Frame_main, text="Password:", fg="#00587a", bg="whitesmoke", font=("Titillium Web ExtraLight", 15, "bold"))
        lbl_password.place(x=60, y=180)
        self.txt_password = Entry(Frame_main, font=("Titillium Web ExtraLight", 15, "bold"), bg="lightgrey")
        self.txt_password.place(x=90, y=220, width=350, height=30)
        
        forget_button = Button(Frame_main, text = "Forgot Password?",cursor="hand2", bg="whitesmoke",bd=0, fg="#0f3057", font=("Titillium Web", 12, "bold"))
        forget_button.place(x=310, y=270)

        login_button = Button(self.root, text = "Login", bg="darkslategrey", fg="white", font=("Audiowide", 15), cursor="hand2",command=self.login_credentials)
        login_button.place(x=330, y=455, width=150, height=40)

    def login_credentials(self):
        if self.txt_password.get() == " " or self.txt_username.get() == " ":
            messagebox.showerror("Error","Please enter your Credentials!", parent=self.root)


        elif self.txt_password.get() == "god13" and self.txt_username.get() == "Vishu":
            messagebox.showinfo("Welcome", "Hello Mr. Vishesh!", parent=self.root)


        elif self.txt_password.get() == "chhapanbhog" and self.txt_username.get() == "Neha":
            messagebox.showinfo("Welcome", "Hello Neha Ma'am!", parent=self.root)


        elif self.txt_password.get() == "donkey" and self.txt_username.get() =="Khushi":
            messagebox.showinfo("Welcome!", "Hello Khushi Ma'am You're a Donkey!", parent=self.root)


        elif self.txt_password.get() == "chaman" and self.txt_username.get() == "Aayush":
            messagebox.showinfo("Welcome!", "Hello Soni Bhai", parent=self.root)

        elif self.txt_password.get() == "hindustanibhau" and self.txt_username.get() == "Tisha":
            messagebox.showinfo("Welcome!", "Hello Tisha Ma'am!", parent=self.root)

        else:
            messagebox.showerror("Error","Please check your details", parent=self.root)

      
root = Tk()
obj = Login(root)
root.mainloop()