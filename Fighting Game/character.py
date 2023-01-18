import pygame

class Samurai():
    def __init__(self,player,x,y,flip,playerdata,sprite_sheet,animationsteps):
        self.player = player
        self.scale1 = playerdata[1]
        self.size = playerdata[0]
        self.offset = playerdata[2]
        self.rect = pygame.Rect((x,y,80,180))
        self.velocity_y = 0
        self.jump = False
        self.attacktype = 0
        self.attacking = False
        self.health = 11
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animationsteps)
        self.frame_index = 0
        self.action = 1  #0 is hurt ,1 is idle, 2 is attack 1, 3 is attack 2 , 4 is running, 5 is dead, 6 is jump,
        self.update_time = pygame.time.get_ticks()
        self.running = False
        self.image = self.animation_list[self.action][self.frame_index]
        self.atkcd = 0
        self.hit = False
        self.alive = True
    
    def load_images(self,sprite_sheet,animationsteps):
        #get images 
        animationlist=[]
        for y, animation in enumerate(animationsteps):            
            tempimagelist=[]
            for x in range(animation):
                tempimage = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                tempimagelist.append(pygame.transform.scale(tempimage, (self.size * self.scale1  , self.size * self.scale1)))
            animationlist.append(tempimagelist)
        return animationlist
        

    def move(self, s_width, s_height, surface, enemy, roundover):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.running = False
        self.attacktype = 0
    
    #get keypresses
        key = pygame.key.get_pressed()
    #only can do moves if not attacking 
        if self.attacking == False and self.alive == True and roundover==False:
            #check player 1 controls
            if self.player ==1:
            #movement keys 
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx=SPEED
                    self.running = True
                #jump
                if key[pygame.K_w] and self.jump == False:
                    self.velocity_y = -30
                    self.jump = True
                #Attack Buttons
                if key[pygame.K_f] or key[pygame.K_g]:
                    self.attack(enemy)
                    #determine what Attack
                    if key[pygame.K_f]:
                        self.attacktype=1
                    if key[pygame.K_g]:
                        self.attacktype=2

            if self.player ==2:
            #movement keys 
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx=SPEED
                    self.running = True
                #jump
                if key[pygame.K_UP] and self.jump == False:
                    self.velocity_y = -30
                    self.jump = True
                #Attack Buttons
                if key[pygame.K_n] or key[pygame.K_m]:
                    self.attack(enemy)
                    #determine what Attack
                    if key[pygame.K_n]:
                        self.attacktype=1
                    if key[pygame.K_m]:
                        self.attacktype=2



            #gravity do the funnying
            self.velocity_y += GRAVITY
            dy += self.velocity_y 

            #make sure player stays on screen
            if self.rect.left +dx <0:
                dx = 0 - self.rect.left
            if self.rect.right + dx > s_width:
                dx = s_width - self.rect.right
            if self.rect.bottom + dy > s_height - 50:
                self.velocity_y = 0
                self.jump = False
                dy = s_height - 50 - self.rect.bottom


            #make sure players are looking at eachother
            if enemy.rect.centerx > self.rect.centerx:
                self.flip = False
            else:
                self.flip = True
            
            #attack cooldown
            if self.atkcd>0 :
                self.atkcd -= 1
        


        #update player posiiton
        self.rect.x += dx
        self.rect.y += dy
    
    #animation updating
    def update(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.updateaction(5)
        elif self.hit == True:
            self.updateaction(0)
        #check what action is happening
        elif self.attacking == True:
            if self.attacktype == 1:
                self.updateaction(2)
            elif self.attacktype ==2:
                self.updateaction(3)
        elif self.jump == True:
            self.updateaction(6)
        elif self.running == True:
            self.updateaction(4)
        else:
            self.updateaction(1)
        animationcd = 100
        self.image = self.animation_list[self.action][self.frame_index]
        #check if time had passed
        if pygame.time.get_ticks() - self.update_time > animationcd:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        #check if animtiaon is done
        if self.frame_index >= len(self.animation_list[self.action]):
            #player dead end animation
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                #check if attack was done
                if self.action == 2 or self.action == 3:
                    self.attacking = False
                    self.atkcd = 30
                #check for damage
                if self.action == 0:
                    self.hit= False
                    #if player was in animation, then the animaiton is stopped (attack)
                    self.attacking = False
                    self.atkcd = 30


    def attack(self, enemy):
        if self.atkcd == 0:
            self.attacking = True
            hitbox = pygame.Rect(self.rect.centerx - (2*self.rect.width*self.flip),self.rect.y, 1.5 * self.rect.width,self.rect.height)
            if hitbox.colliderect(enemy.rect):
                enemy.health -= 5
                enemy.hit = True
                
    def updateaction(self,newaction):
        #check if new action is different to the old one
        if newaction != self.action:
            self.action = newaction
        #update settings for animation
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self,surface):
        imag = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(imag, (self.rect.x -(self.offset[0] * self.scale1) ,self.rect.y-(self.offset[1]*self.scale1)))