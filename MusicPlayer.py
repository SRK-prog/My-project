from tkinter import *
import pygame
from tkinter import filedialog
import glob,os

root = Tk()
root.title('Music Player')
root.geometry('260x265')
icon = PhotoImage(file='C:/Users/Windows/PycharmProjects/musicplayer.png')
root.iconphoto(False, icon)


scroll = Scrollbar(root, orient=VERTICAL)
scroll.pack(side=RIGHT, fill=Y)

list = Listbox(root,yscrollcommand=scroll.set, height=10, width=33)
list.pack(pady=10)

frame = Frame(root)
frame.pack()

pygame.mixer.init()

def add_song_path(): 
    def add_btn():
        new = display.get()
        new = new.replace("\`", "/`")
        os.chdir(new)
        os.listdir() 
        for file in glob.glob('*.mp3'): 
            list.insert(END, file)   
    new_win = Toplevel(root)
    new_win.title('Enter path')
    new_win.geometry('300x50')
    display = Entry(new_win, width=50)
    display.grid(row=0, column=0, columnspan=2)
    new_win.iconphoto(False, icon)
    button = Button(new_win, text='Ok', width=7, command=lambda: [add_btn(), new_win.destroy()])
    button.grid(row=1, column=0)
    button1 = Button(new_win, text='Cancel', width=7, command=new_win.destroy)
    button1.grid(row=1, column=1)

  
def add_songs():
    songs = filedialog.askopenfilenames(initialdir='/', title='select one or more songs', filetypes=(('mp3 Files', '*.mp3'), ))
    for song in songs:
        list.insert(END, song)

def play():
    song = list.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

global paused
paused = False
def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def stop():
    pygame.mixer.music.stop()
    list.select_clear(ACTIVE)
def forward():
    for_song = list.curselection()
    for_song = for_song[0]+1
    song = list.get(for_song)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    list.select_clear(0, END)
    list.activate(for_song)
    list.selection_set(for_song, last=None)
def back():
    for_song = list.curselection()
    for_song = for_song[0] - 1
    song = list.get(for_song)
   # song = f'C:/Users/Windows/PycharmProjects/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    list.select_clear(0, END)
    list.activate(for_song)
    list.selection_set(for_song, last=None)

image_btn = PhotoImage(file='C:/Users/Windows/PycharmProjects/play.png')
image_btn1 = image_btn.subsample(4, 4)
for_btn = PhotoImage(file='C:/Users/Windows/PycharmProjects/for_btn.png')
for_btn1 = for_btn.subsample(8, 9)
back_btn = PhotoImage(file='C:/Users/Windows/PycharmProjects/back_btn.png')
back_btn1 = back_btn.subsample(8, 9)
pause_btn = PhotoImage(file='C:/Users/Windows/PycharmProjects/pause_btn.png')
pause_btn1 = pause_btn.subsample(8, 9)
stop_btn = PhotoImage(file='C:/Users/Windows/PycharmProjects/stop_btn.png')
stop_btn1 = stop_btn.subsample(8, 9)

button_back = Button(frame,image=back_btn1,command=back, borderwidth=0)
button_back.grid(row=0, column=0, pady=10)
button_forward = Button(frame, image=for_btn1, command=forward, borderwidth=0)
button_forward.grid(row=0, column=1)
button_play = Button(frame, image=image_btn1, command=play, borderwidth=0)
button_play.grid(row=0, column=2)
button_pause = Button(frame, image=pause_btn1,command=lambda: pause(paused), borderwidth=0)
button_pause.grid(row=0, column=4)
button_stop = Button(frame, image=stop_btn1, command=stop, borderwidth=0)
button_stop.grid(row=0, column=5)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song = Menu(my_menu)
my_menu.add_cascade(label="➕", menu=add_song)
add_song.add_command(label="Add song", command=add_songs)

add_song.add_command(label="Add song path", command=add_song_path)

add_song.add_command(label="Exit", command=root.quit)

mainloop()