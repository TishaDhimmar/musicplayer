import time
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog, messagebox
import pygame
from mutagen.mp3 import MP3
from PIL import Image, ImageTk

home = Tk()
home.title("Tunify Media Player - Home")
home.geometry("1200x675+110+50")
home.resizable(False, False)
home.iconbitmap("D:/Python/Music Player/favicon.ico")
home.configure(bg="#ff8e71")

def Login_Page():
    root = Toplevel()
    root.title("Tunify Media Player - Login")
    root.geometry("1200x675+110+50")
    root.resizable(False, False)
    root.iconbitmap("D:/Python/Music Player/favicon.ico")

    def login_credentials():

        if txt_password.get() == "" or txt_username.get() == "":
            messagebox.showerror("Error", "Please enter your Credentials!", parent=root)

        elif txt_password.get() == "Greek_God_Hercules" and txt_username.get() == "Vishu":
            messagebox.showinfo("Welcome", "Hello Mr. Vishesh!", parent=root)
            print("Vishesh has logged in.")

        elif txt_password.get() == "Neha" and txt_username.get() == "Neha":
            messagebox.showinfo("Welcome", "Hello Neha Ma'am!", parent=root)
            print("Neha has logged in.")

        elif txt_password.get() == "khushi" and txt_username.get() == "Khushi":
            messagebox.showinfo("Welcome!", "Hello Khushi Ma'am", parent=root)
            print("Khushi has logged in.")

        elif txt_password.get() == "aayush" and txt_username.get() == "Aayush":
            messagebox.showinfo("Welcome!", "Hello Soni Bhai", parent=root)
            print("Aayush has logged in.")

        elif txt_password.get() == "tisha" and txt_username.get() == "Tisha":
            messagebox.showinfo("Welcome!", "Hello Tisha Ma'am!", parent=root)
            print("Tisha has logged in!")

        elif txt_password.get() == "aakashsir" and txt_username.get() == "Aakash Gupta":
            messagebox.showinfo("Welcome!", "Hello Mentor! You're Most Welcome!", parent=root)
            print("Your Mentor, Mr. Akash Gupta has logged in!")

        else:
            messagebox.showerror(
                "Error", "Please check your details", parent=root)

    global bg
    bg = ImageTk.PhotoImage(Image.open("D:/Python/Music Player/login2.jpg"))
    bg_image = Label(root, image=bg)
    bg_image.place(x=0, y=0, relheight=1, relwidth=1)

    root_menu = Menu(root)
    root.config(menu=root_menu)

    goto_menu = Menu(root_menu)
    root_menu.add_cascade(label="Go-To", menu=goto_menu)
    goto_menu.add_command(label="Tunify", command=Music_Player)
    goto_menu.add_separator()
    goto_menu.add_command(label="Contact-Us", command=contact_us)

    Frame_main = Frame(root, bg="whitesmoke")
    Frame_main.place(x=150, y=125, height=350, width=510)

    # >>Main<<
    head = Label(Frame_main, text="Login Here!", font=(
        "Audiowide", 30, "bold"), fg="#0f3057", bg="whitesmoke")
    head.place(x=130, y=30)

    lbl_username = Label(Frame_main, text="Username:", fg="#00587a",
                         bg="whitesmoke", font=("Titillium Web ExtraLight", 15, "bold"))
    lbl_username.place(x=60, y=110)
    txt_username = Entry(Frame_main, font=(
        "Titillium Web ExtraLight", 15, "bold"), bg="lightgrey")
    txt_username.place(x=90, y=150, width=350, height=30)

    lbl_password = Label(Frame_main, text="Password:", fg="#00587a",
                         bg="whitesmoke", font=("Titillium Web ExtraLight", 15, "bold"))
    lbl_password.place(x=60, y=180)
    txt_password = Entry(Frame_main, font=(
        "Titillium Web ExtraLight", 15, "bold"), bg="lightgrey")
    txt_password.place(x=90, y=220, width=350, height=30)

    forget_button = Button(Frame_main, text="Forgot Password?", cursor="hand2",
                           bg="whitesmoke", bd=0, fg="#0f3057", font=("Titillium Web", 12, "bold"))
    forget_button.place(x=310, y=270)

    login_button = Button(root, text="Login", bg="darkslategrey", fg="white", font=(
        "Audiowide", 15), cursor="hand2", command=login_credentials)
    login_button.place(x=330, y=455, width=150, height=40)
    
    root.mainloop()

def Music_Player():
    home.destroy()
    main = Tk()
    main.title("Tunify - Mp3 Player")
    main.geometry("1200x675+110+50")
    main.resizable(False, False)
    main.iconbitmap("D:/Python/Music Player/favicon.ico")
    main.configure(bg="#ff8e71")

    pygame.mixer.init()
    
    def song_time():
        if stopped:
            return

        curr_time = pygame.mixer.music.get_pos() / 1000 
        converted_curr_time = time.strftime("%H:%M:%S", time.gmtime(curr_time))
        
        status_bar.after(1000, song_time) #Status bar after every 1 second
        song = playlist.get(ACTIVE)
        song = f"C:/Users/JANAK/Music/{song}.mp3"
        song_mutagen = MP3(song)

        global song_length
        song_length = song_mutagen.info.length
        convert_song_length = time.strftime("%H:%M:%S", time.gmtime(song_length))
        if int(song_slider.get()) == int(song_length):
            nextSong()
            status_bar.config(text=f'Time Passed: -- of --')

        elif paused == True:
            pass
            # song_slider.config(value=curr_time)
        else:
            next_time = int(song_slider.get()) + 1 
            song_slider.config(to=song_length, value=next_time)
            converted_curr_time = time.strftime("%H:%M:%S", time.gmtime(int(song_slider.get())))
            status_bar.config(text=f'Time Passed: {converted_curr_time} of {convert_song_length}')
            
        if curr_time >= 1:
            status_bar.config(text=f'Time Passed: {converted_curr_time} of {convert_song_length}')

    def add_song():
        global browseSong
        browseSong = filedialog.askopenfilename(initialdir="C:/Users/JANAK/Music", title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"), ))
        browseSong = browseSong.replace("C:/Users/JANAK/Music/", "")
        browseSong = browseSong.replace(".mp3", "")
        playlist.insert(END, browseSong)

    def add_many_songs():
        global Songs
        Songs = filedialog.askopenfilenames(initialdir="C:/Users/JANAK/Music", title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"), ))
        for Song in Songs:
            Song = Song.replace("C:/Users/JANAK/Music/", "")
            Song = Song.replace(".mp3", "")
            playlist.insert(END, Song)

    def delete_songs():
        playlist.delete(ANCHOR)
    
    def delete_songs_all():
        playlist.delete(0, END)
    
    def playSong():
        global stopped
        stopped = False
        song = playlist.get(ACTIVE)
        song = f"C:/Users/JANAK/Music/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)

        song_time()

    global paused
    paused = False
    def pauseSong(is_paused):
        global paused
        paused = is_paused

        if paused: #if paused == True:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.pause()
            paused = True

    global stopped
    stopped = False
    def stopSong():
        pygame.mixer.music.stop()
        playlist.selection_clear(ACTIVE)

        status_bar.config(text=f'Time Passed: -- of --')
        song_slider.config(value=0)
        global stopped
        stopped = True  

    def nextSong():
        status_bar.config(text="")
        song_slider.config(value=0)
        next_song = playlist.curselection()
        next_song = next_song[0] + 1
        song = playlist.get(next_song)
        song = f"C:/Users/JANAK/Music/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        playlist.selection_clear(0, END)
        playlist.activate(next_song)
        playlist.selection_set(next_song, last=None)
        print(next_song)
    
    def previousSong():
        status_bar.config(text="")
        song_slider.config(value=0)
        pre_song = playlist.curselection()
        pre_song = pre_song[0] - 1
        song = playlist.get(pre_song)
        song = f"C:/Users/JANAK/Music/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        playlist.selection_clear(0, END)
        playlist.activate(pre_song)
        playlist.selection_set(pre_song, last=None)

    def adjust_vol_slider(x):
        pygame.mixer.music.set_volume(vol_slider.get())

    def adjust_song_slider(x):
        song = playlist.get(ACTIVE)
        song = f"C:/Users/JANAK/Music/{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0, start=song_slider.get())

    playlist = Listbox(main, bg="#00587a", fg="whitesmoke", width=60, selectbackground="#ff8e71", selectforeground="#00587a")
    playlist.place(x=50, y=30, width=1100, height=300)

    vol_frame = LabelFrame(main, text="Volume", bg="#ff8e71")
    vol_frame.place(x=850, y=350)

    song_frame = LabelFrame(main, text="Current Track", bg="#ff8e71")
    song_frame.place(x=450, y=480)

    vol_slider = ttk.Scale(vol_frame, from_=1, to=0, orient=VERTICAL, value=1, command=adjust_vol_slider)
    vol_slider.pack(pady=10, padx=10)

    song_slider = ttk.Scale(song_frame, from_=0, to=100, orient=HORIZONTAL, value=0, length=320, command=adjust_song_slider)
    song_slider.pack(padx=15, pady=15)

    # frame
    frame = Frame(main, bg="#ff8e71")
    frame.place(x=400, y=400)
    #Button Images
    global play_button_image
    global pause_button_image
    global back_button_image
    global forward_button_image
    global stop_button_image
    play_button_image = PhotoImage(file='D:/Python/Music Player/Images/play50.png')
    pause_button_image = PhotoImage(file='D:/Python/Music Player/Images/pause50.png')
    back_button_image = PhotoImage(file='D:/Python/Music Player/Images/back50.png')
    forward_button_image = PhotoImage(file='D:/Python/Music Player/Images/forward50.png')
    stop_button_image = PhotoImage(file='D:/Python/Music Player/Images/stop50.png')

    # buttons
    play_button = Button(frame, image=play_button_image, bd=0, bg="#ff8e71", command=playSong)
    play_button.grid(row=0, column=2, padx=15)
    

    back_button = Button(frame, image=back_button_image, bd=0, bg="#ff8e71", command=previousSong)
    back_button.grid(row=0, column=0, padx=15)

    forward_button = Button(frame, image=forward_button_image, bd=0, bg="#ff8e71", command=nextSong)
    forward_button.grid(row=0, column=1, padx=15)

    pause_button = Button(frame, image=pause_button_image, bd=0, bg="#ff8e71", command= lambda: pauseSong(paused))
    pause_button.grid(row=0, column=3, padx=15)

    stop_button = Button(frame, image=stop_button_image, bd=0, bg="#ff8e71", command=stopSong)
    stop_button.grid(row=0, column=4, padx=15)

    main_menu = Menu(main)
    main.config(menu=main_menu)

    songAdd_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Add Songs", menu=songAdd_menu)
    songAdd_menu.add_command(label="Add a Track", command=add_song)
    songAdd_menu.add_command(label="Browse for Multiple", command=add_many_songs)

    remove_song_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Delete Songs", menu=remove_song_menu)
    remove_song_menu.add_command(label="Delete a Track", command=delete_songs)
    remove_song_menu.add_command(label="Delete All", command=delete_songs_all)

    #Status bar
    status_bar = Label(main, text="", bd=1, relief=GROOVE, anchor=N, fg="#ff8e71", bg="#00587a", font=("Centaur", 13))
    status_bar.pack(fill=X, side=BOTTOM, ipady=2)
    main.mainloop()

def contact_us():
    op = Toplevel()
    op.resizable(False, False)
    op.geometry("1200x1050")
    op.iconbitmap("D:/Python/Music Player/favicon.ico")
    op.configure(bg="#4d375d")
    op.title("Contact US!")

    op_menu = Menu(op)
    op.config(menu=op_menu)

    goto_menu = Menu(op_menu)
    op_menu.add_cascade(label="Go-to", menu=goto_menu)
    goto_menu.add_command(label="Tunify", command=Music_Player)
    goto_menu.add_separator()
    goto_menu.add_command(label="Login-Page", command=Login_Page)
    goto_menu.add_separator()
    goto_menu.add_command(label="Exit", command=op.quit)

    #Assigning Globals
    global Vishu
    global Neha
    global Khushi
    global Aayush
    global Tisha
    #Assigning Path
    Vishu = ImageTk.PhotoImage(Image.open("D:\\Python\\Music Player\\Images\\Vishu.jpg"))
    Neha = ImageTk.PhotoImage(Image.open("D:\\Python\\Music Player\\Images\\Neha.png"))
    Khushi = ImageTk.PhotoImage(Image.open("D:/Python/Music Player/Images/Khushi.png"))
    Aayush = ImageTk.PhotoImage(Image.open("D:/Python/Music Player/Images/Aayush.png"))
    Tisha = ImageTk.PhotoImage(Image.open("D:/Python/Music Player/Images/Tisha.png"))
    #Creating Labels for each
    Vishu_label = Label(op, image=Vishu, bg="#4d375d")
    Neha_label = Label(op, image=Neha, bg="#4d375d")
    Khushi_label = Label(op, image=Khushi, bg="#4d375d")
    Aayush_label = Label(op, image=Aayush, bg="#4d375d")
    Tisha_label = Label(op, image=Tisha, bg="#4d375d")
    #Placing Labels in op
    Vishu_label.place(x=0, y=0)
    Neha_label.place(x=995, y=200)
    Khushi_label.place(x=0, y=400)
    Aayush_label.place(x=995, y=600)
    Tisha_label.place(x=0, y=800)
    #Head
    Head = Label(op, text='Team Tunify!', font=("Shadows Into Light", 55), bg="#4d375d")
    Head.place(x=700, y=20)
    #Details Vishesh
    Vishu_label_details = Label(op, text="Yo peeps!, I'm Vishesh Mistry", font=("Righteous", 17), bg="#4d375d")
    Vishu_label_details.place(x=250, y=30)
    Vishu_label_details_pt2 = Label (op, text="Mail me on: 20102028.nuv.ac.in", font=("Righteous", 17), bg="#4d375d") 
    Vishu_label_details_pt2.place(x=250, y=60)
    Vishu_label_details_pt3 = Label(op, text="I am from FY-BCA", font=("Righteous", 17), bg="#4d375d")
    Vishu_label_details_pt3.place(x=250, y=90)
    Vishu_label_details_pt4 = Label(op, text="Stay Tunifyied! 😎", font=("Righteous", 17), bg="#4d375d")
    Vishu_label_details_pt4.place(x=250, y=120)
    #Details Neha
    Neha_label_details = Label(op, text="Helluuu! This is Neha Pandya", font=("Righteous", 17), bg="#4d375d")
    Neha_label_details.place(x=600, y=230)
    Neha_label_details_pt2 = Label(op, text="Mail me on: 20102051@nuv.ac.in", font=("Righteous", 17), bg="#4d375d")
    Neha_label_details_pt2.place(x=600, y=260)
    Neha_label_details_pt3 = Label(op, text="I am from FY-BCA!", font=("Righteous", 17), bg="#4d375d")
    Neha_label_details_pt3.place(x=600, y=290)
    Neha_label_details_pt4 = Label(op, text="Rock on! 🎸", font=("Righteous", 17), bg="#4d375d")
    Neha_label_details_pt4.place(x=600, y=320)
    #Details Khushi
    Khushi_label_details = Label(op, text="Hey! Hey People! This is Khushi Bhatt!", font=("Righteous", 17), bg="#4d375d")
    Khushi_label_details.place(x=250, y=430)
    Khushi_label_details_pt2 = Label(op, text="You can Mail me on: 20102012@nuv.ac.in", font=("Righteous", 17), bg="#4d375d")
    Khushi_label_details_pt2.place(x=250, y=460)
    Khushi_label_details_pt3 = Label(op, text="FY-BCA OP in the Chat!", font=("Righteous", 17), bg="#4d375d")
    Khushi_label_details_pt3.place(x=250, y=490)
    Khushi_label_details_pt4 = Label(op, text="Eat, Sleep, Music, Repeat! 🎧", font=("Righteous", 17), bg="#4d375d")
    Khushi_label_details_pt4.place(x=250, y=520)
    #Details Aayush
    Aayush_label_details = Label(op, text="Hola! Aayush Soni here.", font=("Righteous", 17), bg="#4d375d")
    Aayush_label_details.place(x=600, y=630)
    Aayush_label_details_pt2 = Label(op, text="My mail: 20102001@nuv.ac.in", font=("Righteous", 17), bg="#4d375d")
    Aayush_label_details_pt2.place(x=600, y=660)
    Aayush_label_details_pt3 = Label(op, text="FY-BCA Jai Ho!!", font=("Righteous", 17), bg="#4d375d")
    Aayush_label_details_pt3.place(x=600, y=690)
    Aayush_label_details_pt4 = Label(op, text="Tune it on! 🎶", font=("Righteous", 17), bg="#4d375d")
    Aayush_label_details_pt4.place(x=600, y=720)
    #Details Tisha
    Tisha_label_details = Label(op, text="Hola píos! This is Tisha Dhimmar from FY-BCA!!", font=("Righteous", 17), bg="#4d375d")
    Tisha_label_details.place(x=250, y=830)
    Tisha_label_details_pt2 = Label(op, text="Wanna contact me? Here's my mail: 20102053@nuv.ac.in", font=("Righteous", 17), bg="#4d375d")
    Tisha_label_details_pt2.place(x=250, y=860)
    Tisha_label_details_pt3 = Label(op, text="Headphones ON! 🎧", font=("Righteous", 17), bg="#4d375d")
    Tisha_label_details_pt3.place(x=250, y=920)
    Tisha_label_details_pt4 = Label(op, text="FY-BCA rockss!!", font=("Righteous", 17), bg="#4d375d")
    Tisha_label_details_pt4.place(x=250, y=890)

home_menu = Menu(home)
home.config(menu=home_menu)

option_menu = Menu(home_menu)
home_menu.add_cascade(label="File", menu=option_menu)
option_menu.add_command(label="Tunify", command=Music_Player)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=home.quit)

help_menu = Menu(home_menu)
home_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Contact Us", command=contact_us)

login_menu = Menu(home_menu)
home_menu.add_cascade(label="Login", menu=login_menu)
login_menu.add_command(label="Login", command=Login_Page)
login_menu.add_separator()
login_menu.add_command(label="Exit", command=home.quit)

head_label = Button(home, text="Tunify", bg="#ff8e71", fg="#00587a", font=("Popstick-Demo", 120, "bold"), bd=0, command=Music_Player, cursor="hand2")
head_label.place(x=350, y=50)

description_label = Label(home, text="Let the Music Speak.", bg="#ff8e71", fg="#00587a", font=("Centaur", 17, "italic bold"))
description_label.place(x=470, y=360)

Login_button = Button(home, text="Login", command=Login_Page, font=("Centaur", 15, "bold"),bd=0, bg="#ff8e71", fg="#00587a")
Login_button.place(x=1100, y=10, width=90, height=35)

information_label = Label(home, text="Click on 'Tunify' to continue..", bg="#ff8e71", fg="#00587a", font=("Centaur", 13))
information_label.place(x=475, y=620)

home.mainloop()
