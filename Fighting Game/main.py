import pygame
from pygame import mixer
mixer.init()
pygame.init()
pygame.mixer.init()
from character import Samurai


#opens the game
S_WIDTH = 1000
S_HEIGHT = 600
#game vairables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0,0] #player scores [P1,P2]
roundover = False
ROUND_OVERCD = 2000

#define variables for characters 
Asamuraisize = 102
Asamuraiscale = 2.5
AsamuraiOffset = [36,26]
Asamuraidata = [Asamuraisize,Asamuraiscale,AsamuraiOffset]
samurai2size = 102
samurai2data =[samurai2size,Asamuraiscale,AsamuraiOffset]
#displays screen with the variables of screen width and height
window = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
pygame.display.set_caption("Samurai")

#set fps
time = pygame.time.Clock()
FPS = 60

#load music and sounds
pygame.mixer.music.load("Assets/images/New folder/yas.wav")
pygame.mixer.music.set_volume(0.07)
pygame.mixer.music.play(-1,0.0,5000)

swordsound = pygame.mixer.Sound("Assets/images/New folder/sowrd affect.wav")
swordsound.set_volume(0.1)

#get background image
bgimage = pygame.image.load("Assets/images/Background/frame_1_delay-0.15s.jpg").convert_alpha()
#win image
winimg = pygame.image.load("Assets/images/New folder/winner.png").convert_alpha()
scaledwin=pygame.transform.scale(winimg,(500,500))
#define fonts
count_font = pygame.font.Font("Assets\Fonts\Turok.ttf",80)
score_font = pygame.font.Font("Assets\Fonts\Turok.ttf",30)

#draw the text
def draw_text(text,font,text_col,x,y):
    fontimg = font.render(text,True,text_col)
    window.blit(fontimg,(x,y))
#get sprite sheets
Asamuraisheet = pygame.image.load("Assets\images\Asamurai\Asamuraosprite.png").convert_alpha()
samurai2sheet = pygame.image.load("Assets\images\Asamurai\Asamuraospriteplayer2.png").convert_alpha()

#define number of steps in each animation
Asamuraisteps = [1,1,6,6,8,3,6]
samurai2steps = [1,1,6,6,8,3,6]

#cr3eate funciton to make background
def draw_bg():
    scaledbg=pygame.transform.scale(bgimage,(S_WIDTH,S_HEIGHT))
    window.blit(scaledbg,(0,0))

#make health bars
def draw_health_bar(health,x,y):
    ratio = health / 100 
    pygame.draw.rect(window, (255,0,0),( x, y, 400,30))
    pygame.draw.rect(window, (0,255,0), ( x, y, 400 * ratio,30))


#create two object/characters
samurai1= Samurai(1,200,370,False, Asamuraidata,Asamuraisheet,Asamuraisteps, swordsound)
samurai2= Samurai(2,700,370,True, samurai2data,samurai2sheet,samurai2steps, swordsound)
samurai1.load_images(Asamuraisheet,Asamuraisteps)


#runs game forever
#make it a variable so you are able to leave the loop when game end
LOOP = True
while LOOP:
    #set fps in game
    time.tick(FPS)
    #draw the background
    draw_bg()
    #show stats
    draw_health_bar(samurai1.health, 20,20)
    draw_health_bar(samurai2.health, 580,20)
    draw_text("P1:"+str(score[1]),score_font, (0,0,255),20,60)
    draw_text("P2:"+str(score[0]),score_font, (0,0,255),580,60)
    print(intro_count)

    #move the characters
    if intro_count <=0:
        samurai1.move(S_WIDTH,S_HEIGHT, window, samurai2, roundover)
        samurai2.move(S_WIDTH,S_HEIGHT, window, samurai1,roundover)
    else:
        #dipslay timer
        draw_text(str(intro_count), count_font, (255,0,0), S_WIDTH/2, S_HEIGHT/3)
        #update counter
        if(pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count-=1
            last_count_update = pygame.time.get_ticks()
            print(intro_count)
    #update the characters
    samurai1.update()
    samurai2.update()
    #Draw the characters
    samurai1.draw(window)
    samurai2.draw(window)

    #check for win loss
    if roundover == False:
        if samurai1.alive == False:
            score[0]+=1
            roundover = True
            round_over_time = pygame.time.get_ticks()
        elif samurai2.alive == False:
            score[1]+=1
            roundover = True
            round_over_time = pygame.time.get_ticks()
            
    else:
        #show vitory image
        window.blit(scaledwin,(250,50))
        if pygame.time.get_ticks()-round_over_time > ROUND_OVERCD:
            roundover = False
            intro_count=3
            samurai1= Samurai(1,200,370,False, Asamuraidata,Asamuraisheet,Asamuraisteps, swordsound)
            samurai2= Samurai(2,700,370,True, samurai2data,samurai2sheet,samurai2steps, swordsound)


    #event handler that will end the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when click exit
            LOOP = False
    #update the display
    pygame.display.update()
#End program
pygame.quit()