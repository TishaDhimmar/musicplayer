from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
main = Tk()
main.title("Tunify - Mp3 Player")
main.geometry("1200x675+110+50")
main.resizable(False, False)
main.iconbitmap("C:/Python/Music Player/favicon.ico")
main.configure(bg="#ff8e71")

pygame.mixer.init()

def song_time():
    if stopped:
        return
    curr_time = pygame.mixer.music.get_pos() / 1000
    converted_curr_time = time.strftime("%H:%M:%S", time.gmtime(curr_time))
    
    status_bar.after(1000, song_time)
    song = playlist.get(ACTIVE)
    song = f"C:/Users/91963/Music/{song}.mp3"
    
    
    song_mutagen = MP3(song)

    global song_length
    song_length = song_mutagen.info.length
    convert_song_length = time.strftime("%H:%M:%S", time.gmtime(song_length))
    if curr_time >= 1:
        status_bar.config(text=f'Time Passed: {converted_curr_time} of {convert_song_length}')

    song_slider.config(to=song_length)
    if paused == True:
        song_slider.config(value=curr_time)
    else:
        next_time = int(song_slider.get()) + 1 
        song_slider.config(value=next_time)
   
def add_song():
    global browseSong
    browseSong = filedialog.askopenfilename(initialdir="C:/Users/91963/Music", title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"), ))
    browseSong = browseSong.replace("C:/Users/91963/Music/", "")
    browseSong = browseSong.replace(".mp3", "")
    playlist.insert(END, browseSong)

def add_many_songs():
    global Songs
    Songs = filedialog.askopenfilenames(initialdir="C:/Users/91963/Music", title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"), ))
    for Song in Songs:
        Song = Song.replace("C:/Users/91963/Music/", "")
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
    song = f"C:/Users/91963/Music/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_time()

global paused
paused = False
def pauseSong(is_paused):
    global paused
    paused = is_paused

    if paused:
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
    #reset slider and status bar
    status_bar.config(text="")
    song_slider.config(value=0)

    next_song = playlist.curselection()
    next_song = next_song[0] + 1
    song = playlist.get(next_song)
    song = f"C:/Users/91963/Music/{song}.mp3"
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
    song = f"C:/Users/91963/Music/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    playlist.selection_clear(0, END)
    playlist.activate(pre_song)
    playlist.selection_set(pre_song, last=None)

def adjust_vol_slider(x):
    pygame.mixer.music.set_volume(vol_slider.get())

def adjust_song_slider(x):
    pass

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
play_button_image = PhotoImage(file='C:/Python/Music Player/Images/play50.png')
pause_button_image = PhotoImage(file='C:/Python/Music Player/Images/pause50.png')
back_button_image = PhotoImage(file='C:/Python/Music Player/Images/back50.png')
forward_button_image = PhotoImage(file='C:/Python/Music Player/Images/forward50.png')
stop_button_image = PhotoImage(file='C:/Python/Music Player/Images/stop50.png')

# buttons
play_button = Button(frame, image=play_button_image, bd=0, bg="#ff8e71", command=playSong)
play_button.grid(row=0, column=2, padx=15)
    
back_button = Button(frame, image=back_button_image, bd=0, bg="#ff8e71", command=previousSong)
back_button.grid(row=0, column=0, padx=15)

forward_button = Button(frame, image=forward_button_image, bd=0, bg="#ff8e71", command=nextSong)
forward_button.grid(row=0, column=1, padx=15)

pause_button = Button(frame, image=pause_button_image, bd=0, bg="#ff8e71", command=lambda: pauseSong(paused))
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