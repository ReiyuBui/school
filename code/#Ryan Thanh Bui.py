#Ryan Thanh Bui
#November 16th 2022
#Alsomost HEardle
#ICS- SOmthing
#Teacher: Ms.Townshend
import tkinter as tk
from tkinter import ttk
import time
from tkinter import *
import pygame
from pygame import mixer
import random  #import libraries

window = tk.Tk()  #initaliaziting the programs and some modules
window.configure(background="#000080")
pygame.mixer.init()

losemessage = "AMONNNNGGG USSSS" #end message

green = '#00FF00'  #hex for colors
red = '#FF0000'
#first is the song ,lists songs for buttons and their color's when clicked, how long
songz = [
  ['AttackOntitanOP.wav','Attack on Titan','Vinland Saga','Naruto','Chainsaw man', green, red,red,red,7],
  ['DeathParadeOP.wav','Death Parade','Deadman Wonderland','Death Note','Fairy Tail', green, red, red, red, 7],
  ['DemonSlayerOP.wav','Demon Slayer','Attack on Titan', 'Sword Art Online','Your Name', green, red, red, red, 7],
  ['DomesticGirlfriendOP.wav','Domestic Girlfriend','Rent-A-Girlfriend','Blend-S','Love is War', green, red, red, red,7],
  ['HaikyuOP.wav','Haikyu','Blue Lock','Naruto','Assasination Classroom',green,red,red,red,7],
  ['JujitsuKaisenOP.wav','Jujitsu Kaisen','Naruto','Death Note','Parasyte',green,red,red,red,7],
  ['MobPsycho100OP.wav','Mob Psycho 100','One Punch Man','Monster','Full Metal Alchemist',green,red,red,red,7],
  ['NGEOP.wav','Neon Genesis Evangelion','Cowboy Bebop','Darling in the FRANXX','Tokyo Ghoul:Re',green,red,red,red,7],
  ['OnePieceOP.wav','One Piece','Bleach','Dragon Ball','Dragon Ball Z',green,red,red,red,7],
  ['TokyoGhoulOP.wav','Tokyo Ghoul', 'Tokyo Ghoul:RE','Re:ZERO','Konosuba',green,red,red,red,7],
]
points = StringVar(value=0) #Points is a changable variable
songorder = random.sample(range(len(songz)),len(songz)) 
buttonorder = random.sample(range(1, 5),4)  #makes  song and button random order

songs = songorder[0] #makes songs in array

def finish():
    ProgressBar.destroy()
    PlayButton.destroy()
    A1.destroy() #deletes all the buttons and resets the screeen
    A2.destroy()
    A3.destroy()
    A4.destroy()
    losetext = tk.Label(window, text = losemessage, font = ('New Times',25),bg="#000052",fg="White") #adds label with message
    losetext.pack(pady=20)
    finalscoreloss = tk.Label(window,text = "Score" + str(points.get()) + "/10", font = ('New Times', 25),bg="#000052",fg="White")
    finalscoreloss.pack(pady=20)  #calculates score out of 10

def progress(song, audiolength):  #progressbar movement
    global songs
    ProgressBar['value'] = 0 #value is 0
    playthis = mixer.Sound(song)
    mixer.Sound.play(playthis)  #play song
    timeplayed = 100 / audiolength
    for i in range(audiolength):
        ProgressBar['value'] += timeplayed
        window.update_idletasks() #follows the song length and fills progress bar
        time.sleep(1)
    ProgressBar['value'] = 0

def answers(buttonpressed):
  global songs
  global buttonorder
  global points
  if songz[songs][4+buttonorder[buttonpressed-1]] == green: points.set(int(points.get())+1) #adds points if the button is green on click
  if len(songorder) > 1:
    del(songorder[0]) #deltes one of the questions
    songs = songorder[0]
    buttonorder = random.sample(range(1, 5),4)
    A1.config(text = songz[songs][buttonorder[0]],activebackground = songz[songs][buttonorder[0] + 4]) #resets options with new options and answers
    A2.config(text = songz[songs][buttonorder[1]],activebackground = songz[songs][buttonorder[1] + 4])
    A3.config(text = songz[songs][buttonorder[2]],activebackground = songz[songs][buttonorder[2] + 4])
    A4.config(text = songz[songs][buttonorder[3]],activebackground = songz[songs][buttonorder[3] + 4])
  else:
    finish()

Title = tk.Label(window, #makes title
                 height=2,
                 width=50,
                 text="GUESS THE ANIME OPENINIGS QUIZ",
                 background="#000080",
                 font=('New Times', 10),
                 fg="white")
Title.pack(pady=20)

ProgressBar = ttk.Progressbar( #makes progress bar
    window,
    orient="horizontal",
    length=500,
    mode='determinate',
)
ProgressBar.pack(pady=20)

PlayButton = tk.Button(window, #makes play button
                       height=1,
                       width=10,
                       bg="lime",
                       fg="black",
                       text="▶",
                       font=('New Times', 10),
                       command=lambda: progress(songz[songs][0],songz[songs][9]))
PlayButton.pack(pady=20)

A1 = tk.Button(window, #makes answer buttons
               height=1,
               width=50,
               bg="#000052",
               fg="white",
               text=songz[songs][buttonorder[0]],
               font=('New Times', 10),
              activebackground = songz[songs][4+buttonorder[0]],
              command = lambda: answers(1) )
A1.pack(pady=20)

A2 = tk.Button(window,
               height=1,
               width=50,
               bg="#000052",
               fg="white",
               text=songz[songs][buttonorder[1]],
               font=('New Times', 10),
              activebackground = songz[songs][4+buttonorder[1]],
              command = lambda: answers(2))
A2.pack(pady=20)

A3 = tk.Button(window,
               height=1,
               width=50,
               bg="#000052",
               fg="white",
               text=songz[songs][buttonorder[2]],
               font=('New Times', 10),
              activebackground = songz[songs][4+buttonorder[2]],
              command = lambda: answers(3))
A3.pack(pady=20)

A4 = tk.Button(window,
               height=1,
               width=50,
               bg="#000052",
               fg="white",
               text=songz[songs][buttonorder[3]],
               font=('New Times', 10),
              activebackground = songz[songs][4+buttonorder[3]],
              command = lambda: answers(4))
A4.pack(pady=20)

window.mainloop() #loops code.
