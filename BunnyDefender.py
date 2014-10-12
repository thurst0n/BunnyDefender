#@author David Levy


#1 - Import librarys and Modules
import os.path, math, random, pygame
from pygame.locals import *
##from pygame.compat import geterror
import resources.menu

if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

#2 Game Constants
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption('Bunny Defender')
SCREENRECT = pygame.Rect((0,0), (640, 480))
healthvalue=194

main_dir = os.path.split(os.path.abspath('file'))[0]
data_dir = os.path.join(main_dir, 'data')

#3 Methods to load images and sounds
def load_image(name, colorkey=None):
    fullname = os.path.join('data',name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

def load_sound(name):
    class NoneSound:
        def play(self): passs
    if not pygame.mixer or not pygame.mixer.get_init():
        return None(sound)
    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load Sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound
    

"""
PROJECTILE CLASSES
LOOK AT IMPORTING A GENERIC PROJECTILE CLASS w/ UPDATE METHOD LIKE:
class Projectiles(pygame.sprite.Sprite):
    def update(self):
            self.position[0]+=math.cos(self.position[0])*self.speed #velx
            self.position[1]+=math.sin(self.position[0])*self.speed #vely
            self.image = pygame.transform.rotate(self.image, 360-self.angle*57.2957795131)
            if self.position[0]<-64 or self.position[0]>width or self.position[1]<-64 or self.position[1]>height:
                self.kill()
                
 ORIGINGAL IF LOGIC:
if projtype==0: ## Carrot
    self.angle = math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26))
    self.position = [playerpos1[0]+32,playerpos1[1]+32]
    self.speed = 10
    self.image = self.images[0]
elif projtype==1: ##Nuke
    self.position = [playerpos1[0]+32,playerpos1[1]+32]
    self.angle = math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26))
    self.speed = 10
    self.image = self.images[1]
    
elif projtype==2: ##Arrows
    self.position=[width,random.randint(25,height-25)]
    self.angle=math.atan2(playerpos1[1]-self.position[1],playerpos1[0]-self.position[0])
    self.speed = 10
    self.image= self.images[2]
    
elif projtype==3: ##Bullet
    self.position=[width,random.randint(25,height-25)]
    self.angle=math.atan2(playerpos1[1]-self.position[1],playerpos1[0]-self.position[0])
    self.speed = 10
    self.image = self.images[3]
self.rect=self.image.get_rect(center=self.position)
        

"""


class Player(pygame.sprite.Sprite):
    speed = 5
    images = [] 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.position = [100,240]
        self.mouse_pos = pygame.mouse.get_pos()

        
        self.angle = math.atan2(self.mouse_pos[1]-(272),self.mouse_pos[0]-(123))
        self.image = pygame.transform.rotate(self.images[0], 360-self.angle*57.2957795131)
        self.playerpos1 = (self.position[0]-self.image.get_rect().width/2, self.position[1]-self.image.get_rect().height/2)
        self.rect=pygame.Rect(self.image.get_rect())
        self.rect.top=self.playerpos1[0]
        self.rect.left=self.playerpos1[1]
        
    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.angle = math.atan2(self.mouse_pos[1]-(self.playerpos1[1]+32),self.mouse_pos[0]-(self.playerpos1[0]+26))
        self.image = pygame.transform.rotate(self.images[0], 360-self.angle*57.2957795131)
        self.playerpos1 = (self.position[0]-self.image.get_rect().width/2, self.position[1]-self.image.get_rect().height/2)
        self.rect=pygame.Rect(self.image.get_rect())
        self.rect.left=self.playerpos1[0]
        self.rect.top=self.playerpos1[1]
        #self.rect.inflate(-self.rect.width/3, -self.rect.height/3)#does nothing?
        #self.rect = self.rect.clamp(SCREENRECT)

    def move(self, x, y):
        self.rect.move_ip(x*self.speed,y*self.speed)
        self.position[0]+=x*self.speed
        self.position[1]+=y*self.speed
        self.update()
        
class Carrot(pygame.sprite.Sprite):
    images = []
    def __init__(self, mouse, playerpos1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.angle = math.atan2(mouse[1]-(playerpos1.top +32),mouse[0]-(playerpos1.left + 26 ))
        self.speed = 10
        self.image = pygame.transform.rotate(self.images[0], 360-self.angle*57.2957795131)
        self.rect= pygame.Rect(self.image.get_rect())
        self.rect.center = playerpos1.center
    def update(self):
        self.rect.left+=(math.cos(self.angle)*self.speed) #velx
        self.rect.top+=(math.sin(self.angle)*self.speed) #vely
        
        if self.rect.left<-64 or self.rect.right>width+64 or self.rect.top<-64 or self.rect.bottom>height+64:
            self.kill()

class Nuke(pygame.sprite.Sprite):
    images = []
    def __init__(self, mouse, playerpos1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.angle = math.atan2(mouse[1]-(playerpos1.centery+32),mouse[0]-(playerpos1.centerx+26))
        self.speed = 8
        self.image = pygame.transform.rotate(self.images[0], 360-self.angle*57.2957795131)
        self.rect= pygame.Rect(self.image.get_rect())
        self.rect.center = playerpos1.center
    def update(self):
        self.rect.left+=(math.cos(self.angle)*self.speed) #velx
        self.rect.top+=(math.sin(self.angle)*self.speed) #vely
        
        if self.rect.left<-64 or self.rect.right>width+64 or self.rect.top<-64 or self.rect.bottom>height+64:
            self.kill()

class Arrow(pygame.sprite.Sprite):
    images = []
    def __init__(self, playerpos1, speed = 8):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        randarrow=[width,random.randint(25,height-25)]
        self.angle = math.atan2((playerpos1.top+32)-randarrow[1],(playerpos1.left)-randarrow[0])
        self.speed = speed
        self.image = pygame.transform.rotate(self.images[0], 360-self.angle*57.2957795131)
        self.rect= pygame.Rect(self.image.get_rect())
        self.rect.left = randarrow[0]
        self.rect.top = randarrow[1]
    def update(self):
        self.rect.left+=(math.cos(self.angle)*self.speed) #velx
        self.rect.top+=(math.sin(self.angle)*self.speed) #vely
        
        if self.rect.left<-16 or self.rect.right>width+60 or self.rect.top<-64 or self.rect.bottom>height:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    images = []
    imgcnt = 0
    legs = False
    def __init__(self, speed = -2):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.speed=speed
        self.position= [width,random.randint(50, height-50)]
        self.rect= self.image.get_rect(center=self.position)

    def update(self):
        self.legs = not self.legs
        if self.legs == True:
            self.imgcnt+=1
        self.image = self.images[self.imgcnt]
        
        if self.imgcnt ==3:
            self.imgcnt=0
        self.rect.move_ip(self.speed, 0)
        if self.rect.right<0:
            global healthvalue
            healthvalue -=25
            self.kill()

class Evil(pygame.sprite.Sprite):
    images = []
    imgcnt =0
    def __init__(self, speed = -4):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.speed=speed
        self.position= [width,random.randint(50, height-50)]
        self.rect= self.image.get_rect(center=self.position)

    def update(self):
        self.imgcnt+=1
        self.image = self.images[self.imgcnt]
        if self.imgcnt ==3:
            self.imgcnt=0
        self.rect.move_ip(self.speed, 0)
        if self.rect.right<0:
            global healthvalue
            healthvalue-=50
            self.kill()
                    
class NukeUp(pygame.sprite.Sprite):
    images = []
    uptype = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.speed=-3
        self.position= [width,random.randint(50, height-50)]
        self.rect= self.images[0].get_rect(center=self.position)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right<0:
            self.kill()

class HeartUp(pygame.sprite.Sprite):
    images = []
    uptype =1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.speed=-3
        self.position= [width,random.randint(50, height-50)]
        self.rect= self.images[0].get_rect(center=self.position)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right<0:
            self.kill()
#def main():
#initialize pygame
#Set Display Mode/Screen Size
#Load images, assign them to sprite classes
#Decorate Game window (icon, caption, visible mouse etc)
#Create and tile the background image
#Load sounds
#initialize groups for our game objects
#assign containers for each sprite class
#Initialize starting values for scores and such
#Initialize our sprites
#MAIN WHILE LOOP


##--Menu Module
def main():
   # Initialize Pygame
   pygame.init()

   # Create a window of 800x600 pixels
   # Set the window caption


   #Create Menu Object
   menus = resources.menu.cMenu(width/2, 100, 20, 5, 'vertical', 5, screen,
               [('Start Game', 1, None),
                ('Exit',       2, None)])

   # Center the menu on the draw_surface (the entire screen here)
   menus.set_center(True, False)

   # Center the menu on the draw_surface (the entire screen here)
   menus.set_alignment('center', 'center')

   # Create the state variables (make them different so that the user event is
   # triggered at the start of the "while 1" loop so that the initial display
   # does not wait for user input)
   state = 0
   prev_state = 1

   # Ignore mouse motion (greatly reduces resources when not needed)
   pygame.event.set_blocked(pygame.MOUSEMOTION)

   # The main while loop
   while 1:
      # Check if the state has changed, if it has, then post a user event to
      # the queue to force the menu to be shown at least once
      if prev_state != state:
         pygame.event.post(pygame.event.Event(resources.menu.EVENT_CHANGE_STATE, key = 0))
         prev_state = state

      # Get the next event
      e = pygame.event.wait()

      # Update the menu, based on which "state" we are in - When using the menu
      # in a more complex program, definitely make the states global variables
      # so that you can refer to them by a name
      if e.type == pygame.KEYDOWN or e.type == resources.menu.EVENT_CHANGE_STATE:
         if e.key == K_ESCAPE:
              state = 3
         if state == 0:
            rect_list, state = menus.update(e, state)
         elif state == 1:
            #print 'Start Game!'
            state = 0
            pygame.event.set_allowed(pygame.MOUSEMOTION)
            f = open("resources/config.cfg")
            gamerun(int(f.readline()), int(f.readline()), int(f.readline()))
         else:
            #print 'Exit!'
            pygame.quit()
            exit(0)

      # Quit if the user presses the exit button
      if e.type == pygame.QUIT:
         pygame.quit()
         exit(0)

      # Update the screen
      pygame.display.update(rect_list)    

##--Game Run Module
def gamerun(g_time, g_nuke, g_hearts):
    global healthvalue
    healthvalue =194
    pygame.init()
    pygame.event.set_grab(True)
    
    #pygame.mouse.set_visible(0)
    time_a=g_time
    clock=pygame.time.Clock()
    pygame.time.set_timer(USEREVENT, 1000)##Clock tick every second
    
    #Load Object Images
    playerimg = pygame.image.load("resources/images/dude.png")
    Player.images = [playerimg,pygame.transform.flip(playerimg, 1, 0)]
    arrow = [pygame.image.load("resources/images/bullet.png")]
    carrot = [pygame.image.load("resources/images/carrot.png")]
    nukecarrot=[pygame.image.load("resources/images/nukecarrot.png")]
    heart = [pygame.image.load("resources/images/heart.png")]
    upnuke = [pygame.image.load("resources/images/upnuke.png")]
    badguyimg=[pygame.image.load("resources/images/badguy.png"), pygame.image.load("resources/images/badguy2.png"), pygame.image.load("resources/images/badguy3.png"), pygame.image.load("resources/images/badguy4.png")]
    evilguyimg =[pygame.image.load("resources/images/evilguy.png") ,pygame.image.load("resources/images/evilguy2.png"), pygame.image.load("resources/images/evilguy3.png"), pygame.image.load("resources/images/evilguy4.png")]

    Enemy.images=badguyimg
    Evil.images=evilguyimg
    Carrot.images  = carrot
    Nuke.images = nukecarrot
    Arrow.images = arrow
    NukeUp.images = upnuke
    HeartUp.images = heart

    ## need to add upgrades
    upgrades = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()
    nmeprojectiles = pygame.sprite.Group()
    carrots = pygame.sprite.Group()
    nukes = pygame.sprite.Group()
    arrows = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    evils = pygame.sprite.Group()
    playergroup = pygame.sprite.Group()
    nukegroup = pygame.sprite.Group()
    heartgroup = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    Player.containers = all, playergroup
    Carrot.containers = all, carrots, projectiles
    Nuke.containers = all, nukes, projectiles
    Arrow.containers = all, arrows, nmeprojectiles
    Enemy.containers = all, enemies, nmeprojectiles
    Evil.containers = all, evils, nmeprojectiles
    NukeUp.containers = all, upgrades, nukegroup
    HeartUp.containers = all, upgrades, heartgroup
    
    playersprite= Player()
    

    #Initialize Variables for Gamerun
    running=1 #Mainloop Flag
    exitcode = 0 #Win/Loss Flag
    keys = [False, False, False, False, False] #Keypress array
    
    acc=[0,0] #Initial accuracy [shots, hits]

    badtimer=100 #Initial bad timer
    badtimer1=0 #2nd bad timer variable allows for enemy spawn acceleration

    
    nukenumber=g_nuke # initial nuke number variable
    hearts=g_hearts #initial hearts
    if nukenumber >99:
        nukenumber = 99
    if hearts >12:
        hearts=12
    upnukeflag=False #nuke upgrade flag
    uphealthflag=False #health upgrade flag
    

    thisarrow=False #enemy projectile flag
    #initial base health value (194 to match provided health bar)
    pygame.mixer.init()    #initialize mixer to allow for audio
    


    # 3 - Load images
    grass = pygame.image.load("resources/images/grass.png")
    castle = pygame.image.load("resources/images/castle.png")

    healthbar = pygame.image.load("resources/images/healthbar.png")
    health = pygame.image.load("resources/images/health.png")
    
    gameover = pygame.image.load("resources/images/gameover.png")
    youwin = pygame.image.load("resources/images/youwin.png")
    
    #hitback = pygame.image.load("resources/images/hitred.png")
    #hitdude = pygame.image.load("resources/images/hitdude.png")
    
    # 3.1 - Load audio
    hit = pygame.mixer.Sound("resources/audio/explode.wav")
    enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
    shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
    missle = pygame.mixer.Sound("resources/audio/missle2.wav")
    equip = pygame.mixer.Sound("resources/audio/equip2.wav")
    
    hit.set_volume(0.05)
    enemy.set_volume(0.05)
    shoot.set_volume(0.05)
    equip.set_volume(0.5)
    missle.set_volume(0.5)
    pygame.mixer.music.load('resources/audio/moonlight.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.20)
    evil=3

    while running:
        clock.tick(40)
        #pygame.event.set_blocked(pygame.MOUSEMOTION)    
        badtimer-=1
        # 5 - clear the screen before drawing it again
        #screen.fill(0)
        
        # 6 - draw the screen elements
        for x in range(width/grass.get_width()+1):
            for y in range(height/grass.get_height()+1):
                screen.blit(grass,(x*100,y*100))
        screen.blit(castle,(-30,30))
        screen.blit(castle,(-30,135))
        screen.blit(castle,(-30,240))
        screen.blit(castle,(-30,345 ))
                           
        # 6.2 - Create Enemies
        if badtimer==0 and time_a >0:
            if evil==5:
                evil=0
                Evil()
            else:
                evil+=1
                Enemy()
            badtimer=120-(badtimer1*2)
            if badtimer1>=50:
                badtimer1=35
            else:
                badtimer1+=2
        index=0
        #6.3 - Create Pickups
        if time_a%15==0: #Nukes
            if upnukeflag==False:
                NukeUp()
                upnukeflag=True 
        if time_a%45==0: #Hearts
            if uphealthflag==False:
                HeartUp()
                uphealthflag=True
        #6.4 - Create Arrows
        if time_a%5==0:
            if thisarrow==False:
                Arrow(playersprite.rect)
            thisarrow=True

            
####################################
        #Move Objects
####################################
        all.update()


        
##################################
        #collision check.
###################################
        for bullet in pygame.sprite.groupcollide(playergroup, nmeprojectiles, 0, 1):  
            hearts-=1
            hit.play()
        for bullet in pygame.sprite.groupcollide(enemies, nukes, 1, 0):
            acc[0]+=1
            enemy.play()
        for bullet in pygame.sprite.groupcollide(enemies, carrots, 1, 1):
            acc[0]+=1
            enemy.play()
        for bullet in pygame.sprite.groupcollide(evils, nukes, 1, 1):
            acc[0]+=1
            enemy.play()
        for upgrade in pygame.sprite.groupcollide(playergroup,nukegroup, 0, 1):
            if nukenumber<99:
                equip.play()
                nukenumber+=3
            if nukenumber >99:
                nukenumber = 99
        for upgrade in pygame.sprite.groupcollide(playergroup,heartgroup, 0, 1):
            hearts+=1  
        for badguy in pygame.sprite.groupcollide(playergroup, nmeprojectiles, 0, 1):
            hearts-=1
            hit.play()          
                      
        # 6.4 - Draw clock
        font = pygame.font.SysFont("Arial", 18)
        time_a_str = "%d:%02d" % (int(time_a/60),int(time_a%60))
        survivedtext = font.render(time_a_str, True, (0,0,0))
        textRect = survivedtext.get_rect()
        textRect.topright=[635,8]
        screen.blit(survivedtext, textRect)
        
        # 6.5 - Draw health bar
        screen.blit(healthbar, (5,5))
        for health1 in range(healthvalue):
            screen.blit(health, (health1+8,8))
        for heart1 in range(hearts):
            heart1*=25
            screen.blit(heart[0], (565-heart1,5))
        if nukenumber>0:
            nukenumber_txt = font.render(str(nukenumber), True, (0,0,0))
            nukenumber_textRect = nukenumber_txt.get_rect()
            nukenumber_textRect.topright=[268,8]
            screen.blit(nukenumber_txt,nukenumber_textRect)
            screen.blit(upnuke[0],(230,5))

        
        # 8 - loop through the events
        for event in pygame.event.get():
            # check if the event is the X button 
            if event.type==pygame.QUIT:
                # if it is quit the game
                pygame.quit() 
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key==K_w or event.key==K_UP:
                    keys[0]=True
                elif event.key==K_a or event.key==K_LEFT:
                    keys[1]=True
                elif event.key==K_s or event.key==K_DOWN:
                    keys[2]=True
                elif event.key==K_d or event.key==K_RIGHT:
                    keys[3]=True
                elif event.key==pygame.K_F6:
                    pygame.event.set_grab(not pygame.event.get_grab()) 
                if nukenumber>0:
                    if event.key==K_SPACE or event.key ==K_KP0:
                        nukenumber-=1
                        acc[1]+=1
                        Nuke(pygame.mouse.get_pos(), playersprite.rect)
                        missle.play()
                        Arrow(playersprite.rect, 12)


                        
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w or event.key==K_UP:
                    keys[0]=False
                elif event.key==pygame.K_a or event.key==K_LEFT:
                    keys[1]=False
                elif event.key==pygame.K_s or event.key==K_DOWN:
                    keys[2]=False
                elif event.key==pygame.K_d or event.key==K_RIGHT:
                    keys[3]=False
                if event.key == pygame.K_ESCAPE:
                    running=0
                    exitcode=0
            if event.type==pygame.MOUSEBUTTONDOWN and len(projectiles)<20:
                shoot.play()
                acc[1]+=1
                Carrot(pygame.mouse.get_pos(),playersprite.rect)
            if event.type == USEREVENT:
                if time_a > 0:
                    time_a -= 1
                    thisarrow=False
                    upnukeflag=False;
                    upheartflag=False;
                else:
                    pygame.time.set_timer(USEREVENT, 0)
        
        # 9 - Move players
        if keys[0] and playersprite.rect.top>=-32:## move up
            playersprite.move(0,-1)
        elif keys[2]and playersprite.rect.bottom<=height+32 : ## move down
            playersprite.move(0,1)            
        if keys[1]and playersprite.rect.left>=-32: ## move left
            playersprite.move(-1,0)            
        elif keys[3]and playersprite.rect.right<=width+32:## move right
            playersprite.move(1,0)

        #10 - Win/Lose check
        if time_a<1 and len(nmeprojectiles)==0:
            running=0
            exitcode=1
        if healthvalue<=0 or hearts<=0:
            running=0
            exitcode=0
        if acc[1]!=0:
            accuracy=acc[0]*1.0/acc[1]*100
        else:
            accuracy=0
        # 7 - update the screen
        dirty = all.draw(screen)
        pygame.display.update()
        ####--END MAIN WHILE LOOP

            
    # 11 - Win/lose display
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 22)
    acctext = font.render("Accuracy: " +str(int(accuracy))+"% | "+ str(acc[0]) + "/" + str(acc[1]), True, (0,0,0))
    score=int((acc[0]*20)+(acc[1]*(accuracy))+(math.pow(hearts,2)*100)+(healthvalue*200/194)+(100*nukenumber))
    healthtext = font.render("Base Health: " +str(int(healthvalue*100.0/194))+"%" , True, (0,0,0))
    hearttext = font.render("Hearts: " +str(hearts) ,True,(0,0,0))
    nuketext = font.render("Nukes: " +str(nukenumber),True,(0,0,0))
    scoretext = font.render("Score: " +str(score), True,(0,0,0))

    statslist=[acctext, healthtext, hearttext, scoretext]

    index=1
    textRect = acctext.get_rect() #set them all to the same rect so they are all aligned.
    for texto in statslist:
       
       textRect.centerx=screen.get_rect().centerx
       textRect.centery=screen.get_rect().centery+index*25
       index+=1
       screen.blit(texto, textRect)
    if exitcode==0:
        screen.blit(gameover, (0,0))
    else:
        screen.blit(youwin, (0,0))
        pygame.font.init()
    
    pygame.display.update()
    #pygame.time.wait(5000)
    pygame.event.set_grab(False)
    main()
    ####--END GAME RUN
        
main()

if __name__ == '__main__': main()
