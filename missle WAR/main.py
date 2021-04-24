import pygame
import pygame_sdl2

import random

from pygame.locals import *



#Colornumber=1

pygame.init()

SCREEN_WIDTH = 800#500
SCREEN_HEIGHT = 480#400

screen = pygame .display .set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], RESIZABLE)
screenrect=screen.get_rect()

Buttongap=25 

score =0

touched =False
Color =['red', 'green', 'blue', 'yellow', 'white', 'orange']
#global 
Colornumber=0

# Create a custom event for adding a new enemy
ADDENEMY = pygame .USEREVENT + 1
pygame . time.set_timer(ADDENEMY,600 )

ADDCLOUD = pygame .USEREVENT + 2
pygame . time.set_timer(ADDCLOUD, 1000 )

ADDBULLET = pygame .USEREVENT + 3
pygame . time.set_timer(ADDBULLET, 12000 )

ADDFLAME = pygame .USEREVENT + 4
pygame . time.set_timer(ADDFLAME, 400 )
 
class Player(pygame .sprite .Sprite):
	def __init__ (self):
		super(Player, self). __init__ () 
		#self. surf =pygame . Surface((75 , 25))
		#self. surf.fill(( 255 , 255, 255))
		self. surf = pygame . image .load( "jet.png" ).convert()
		self. surf.set_colorkey(( 0, 0 , 0), RLEACCEL)
		self. rect =self .surf.get_rect(center=(100,40)) 
		
	#Move the sprite based on user keypresses
	def update( self , pressed_keys):
		if pressed_keys[K_UP]:
			self. rect .move_ip( 0 ,-5 )
		if pressed_keys[K_DOWN]:
			self. rect .move_ip( 0 , 5)
		if pressed_keys[K_LEFT]:
			self. rect .move_ip( - 5, 0 )
		if pressed_keys[K_RIGHT]:
			self. rect .move_ip( 5 , 0)
		
player = Player() 

class Addbutton(pygame .sprite .Sprite):
	def __init__ (self):
		super(Addbutton, self). __init__ () 
		#self.x, self.y=
		self. surf = pygame . Surface((210, 120))
		self. surf.fill(( 255 ,5, 5))
		self. rect = 100,50#self .surf.get_rect()
		self.rect2 = pygame.Rect((0, 0), (210, 120))
		self.surf.set_alpha(40) 

################
# Define the enemy object by xtending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame .sprite. Sprite):
	def __init__ (self):
		super(Enemy, self). __init__ ()
		#self. surf = pygame . Surface((20 , 20))
		#self. surf.fill(( 255 , 255, 255), self. surf.get_rect().inflate(-1,-1)) 
		self. surf = pygame . image .load( "missile.png" ).convert()
		self. surf.set_colorkey(( 0, 0 , 0), RLEACCEL)
		self. rect = self .surf.get_rect(center =(random. randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),random. randint(0, SCREEN_HEIGHT),))
		self. speed = random.randint( 2,3)
		
		# Move the sprite based on speed
		# Remove the sprite when it passes the left edge of the screen
	def update( self ):
	   	self. rect .move_ip(-self .speed, 0)
	   	if self.rect .right < 0:
	   		self .kill() 

    #Define the cloud object by extending pygame.sprite.Sprite
    # Use an image for a better-looking sprite
class Cloud(pygame . sprite.Sprite):
	def __init__ (self ):
		super(Cloud, self ).__init__ ()
		self .surf = pygame .image .load( "cloud.png" ). convert()
		self .surf.set_colorkey(( 0, 0, 0), RLEACCEL)
		# The starting position is randomly generated
		self .rect = self .surf. get_rect(center=(random .randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),random .randint(0, SCREEN_HEIGHT),))
		
	# Move the cloud based on a constant speed
	# Remove the cloud when it passes the left edge of the screen
	def update( self ):
		self. rect .move_ip( -1, 0)
		if self. rect .right < 0:
			self .kill()



class Bullet(pygame . sprite.Sprite):
	def __init__ (self ):
		super(Bullet, self ).__init__ ()
		self .surf = pygame .image .load( "bullet.png" ). convert()
		self .surf.set_colorkey(( 0, 0, 0), RLEACCEL)
		# The starting position is randomly generated
		
		self . center_x = player.rect [0]+player.rect [2]
		self.center_y=player.rect[1]+player.rect[3]/2
		self . angle = - 90
		#self . top = player.bottom 
		
		#self .rect = self .surf. get_rect(center=(random .randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),random .randint(0, SCREEN_HEIGHT),))
		self .rect = self .surf. get_rect(center=(self.center_x,self.center_y))
		
	# Move the cloud based on a constant speed
	# Remove the cloud when it passes the left edge of the screen
	def update( self ):
		self. rect .move_ip( 8, 0)
		if self. rect .right < 0:
			self .kill() 



class Flame(pygame . sprite.Sprite):
	def __init__ (self ):
		super(Flame, self ).__init__ ()
		self .surf = pygame .image .load( "flame.png" ). convert()
		self .surf.set_colorkey(( 0, 0, 0), RLEACCEL)
		# The starting position is randomly generated
		
		self . center_x = player.rect [0]
		self.center_y=player.rect[1]+player.rect[3]/2
		self . angle = - 190
		#self . top = player.bottom 
		
		#self .rect = self .surf. get_rect(center=(random .randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),random .randint(0, SCREEN_HEIGHT),))
		self .rect = self .surf. get_rect(center=(self.center_x,self.center_y))
		
	# Move the cloud based on a constant speed
	# Remove the cloud when it passes the left edge of the screen
	def update( self ):
		self. rect .move_ip( -6, 0)
		if self. rect .right < 0:
			self .kill() 
 





#adding extra attributes to buttons
# I donknownow why hut the collusion rect have off set of (105,60)		
buttonup=Addbutton() 
buttonup.rect=(10,screenrect.h-280)
buttonup.rect2.center = (115,screenrect.h-220)#surfrect.w / 2, surfrect.h / 2)

buttondown=Addbutton() 
buttondown.rect=(10,buttonup.  rect[1]+ buttonup.surf. get_rect()[3]+Buttongap )
buttondown.rect2.center=(115,buttonup.  rect[1]+ buttonup.surf. get_rect()[3]+Buttongap+60 )

buttonshoot=Addbutton() 
buttonshoot.rect=(screenrect.w-240,screenrect.h-280)
buttonshoot.rect2.center = ((screenrect.w-240)+105 ,screenrect.h-220)#surfrect.w / 2, surfrect.h / 2)
 
buttonrestart=Addbutton() 
font = pygame.font.Font('freesansbold.ttf', 22) 
buttonrestart.text= font.render("Press Button to restart", False, (255, 255,255))
buttonrestart.rect=((screenrect.w/2)-(buttonrestart.rect2[2]/2),(screenrect.h/2)-buttonrestart.rect2[3]) 
buttonrestart.rect2.center = ((screenrect.w/2)-(buttonrestart.rect2[2]/2)+105 ,(screenrect.h/2)-buttonrestart.rect2[3]+ 60)#surfrect.w / 2, surfrect.h / 2)
  
Scorefont= pygame.font.Font('freesansbold.ttf', 162) 
Scorefonttext= font.render(str(score), False, (255, 255,255))

 
 
 
 
 
# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position update
# - all_sprites is used for rendering
enemies = pygame .sprite .Group()
flames = pygame .sprite .Group()
clouds = pygame .sprite .Group() 
bullets=pygame .sprite .Group()


all_sprites = pygame . sprite.Group()
all_sprites .add(player)
 
 
 
def airbrush():
    airbrush = True
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == True and buttonup.rect2.collidepoint(cur): # evaluate left button
        #pygame.draw.circle(gameDisplay, colorChosen, (cur[0] + random.ran
        player . rect .move_ip( 0 ,-5 )

    if click[0] == True and buttondown.rect2.collidepoint(cur): # evaluate left button
        #pygame.draw.circle(gameDisplay, colorChosen, (cur[0] + random.ran
        player . rect .move_ip( 0, 5 )
        
    if click[0] == True and buttonshoot.rect2.collidepoint(cur): # evaluate left button
        #pygame.draw.circle(gameDisplay, colorChosen, (cur[0] + random.ran
       pass#player . rect .move_ip( 0, 5 )
    #player. rect.clamp_ip(screen) 
# Keep player on the screen
    if player .rect .left < 0:
    	player. rect .left = 0
    if player .rect .right > SCREEN_WIDTH:
    	player. rect .right = SCREEN_WIDTH
    if player .rect .top <= 0:
    	player. rect .top = 0
    if player .rect .bottom >= SCREEN_HEIGHT:
    	player . rect .bottom = SCREEN_HEIGHT 



def Drawbuttons():
	screen.blit(buttonup.surf, buttonup.rect)
	screen.blit(buttondown.surf, buttondown.rect)
	screen.blit(buttonshoot.surf, buttonshoot.rect)
	
	if not player. alive ():
	    screen.blit(buttonrestart.surf, buttonrestart.rect)
	    screen.blit(buttonrestart.text, buttonrestart.rect) 
	
	Scorefonttext= font.render(str(score) , False, (255, 255,255))
	screen.blit(Scorefonttext,(SCREEN_WIDTH-60,20)) 
	     
    
def Updatebutton ():
        global Colornumber
        global player, touched
        if Colornumber>4:
        	Colornumber=0
        for ev in pygame.event.get():
            if ev.type == QUIT:
            	pygame.quit()
            	
            # Add a new enemy?
            elif ev .type == ADDENEMY:
            	# Create the new enemy and add it to sprite groups
            	new_enemy = Enemy()
            	enemies. add(new_enemy)
            	all_sprites .add(new_enemy)
            	
            # Add a new cloud?
            elif ev .type == ADDCLOUD:
            	#Create the new cloud and add it to sprite groups
            	new_cloud = Cloud()
            	clouds . add(new_cloud)
            	#all_sprites .add(new_cloud)
            	
            elif ev .type == ADDFLAME:
            	#Create the new cloud and add it to sprite groups
            	new_flame =Flame()
            	flames . add(new_flame)
            	#all_sprites .add(new_cloud)

            elif ev.type == pygame.MOUSEBUTTONDOWN:
                #if rect.collidepoint(ev.pos):
                if buttonup.rect2.collidepoint(ev.pos):
                    touched = True
                    Colornumber+=1
                    buttonup. surf.fill((Color[Colornumber]))
                    #player.update (K_UP)
                    #player. rect .move_ip( 0 ,-5 )
                    # This is the starting point
                    pygame.mouse.get_rel()   
                if buttondown.rect2.collidepoint(ev.pos):
                    touched = True
                    Colornumber+=1
                    buttondown. surf.fill((Color[Colornumber]))
                    # This is the starting point
                    #player. rect .move_ip( 0 , 5) 
                    pygame.mouse.get_rel()
                if buttonshoot.rect2.collidepoint(ev.pos):
                    touched = True
                    Colornumber+=1
                    buttonshoot. surf.fill((Color[Colornumber]))
                    
                    new_bullet =Bullet()
                    
                    bullets.add(new_bullet)
                    # This is the starting point
                    #player. rect .move_ip( 0 , 5)
                if buttonrestart.rect2.collidepoint(ev.pos)and not player.alive():
                    touched = True
                    Colornumber+=1
                    buttonrestart. surf.fill((Color[Colornumber]))
                     
                    restart()
                    pygame.mouse.get_rel() 
                    
            elif ev.type == pygame.MOUSEBUTTONUP:
                touched = False
                #pass



#print('hellooooooooo')



def GameDraw():
	#Draw the player on the screen
	#screen .blit(player .surf, player.rect) 
	# Draw all sprites
	for entity in clouds:
		screen .blit(entity .surf, entity.rect)
	
	if player.alive ():
		for entity in flames:
			screen .blit(entity .surf, entity.rect)
  
	for entity in all_sprites:
		screen.blit(entity .surf, entity.rect)
	
	if player.alive():
		for entity in bullets:
			screen .blit(entity .surf, entity.rect)
	
	Drawbuttons() 	 
		 
		 
def GameUpdate():
	global score
	# Check if any enemies have collided with the player
	if pygame . sprite.spritecollideany(player, enemies) and player.alive():
		pygame . sprite.spritecollideany(player, enemies).kill()
		# If so, then remove the player and stop the loop
		player. kill()
		running = False
	
	#shooting things
	for entity in bullets:
		if pygame . sprite.spritecollideany(entity, enemies) and player.alive():
			score +=1
			pygame . sprite.spritecollideany(entity, enemies).kill()
			# If so, then remove the player and stop the loop
			entity. kill()
			#running = False
	 
	#Update enemy position
	enemies.update()
	clouds . update()
	 
	#update these if player i s alive 
	if player.alive ():
		bullets. update()
		flames. update()   
		
	pressed_keys = pygame . key .get_pressed()
	Updatebutton()
		
def restart():
	global score 
	del score #=0
	all_sprites.empty()
	enemies.empty()
	flames.empty()
	#clouds.empty()
	#bullets.empty ()
	all_sprites .add(player) 
	score=0
def main():
	while True:
		screen .fill(('skyblue')) 
		#pygame. draw . circle(screen, (0, 0, 255 ), (250 , 250), 75)
		#pygame_sdl2.touch.get_finger(1, 0) 
		# Get all the keys currently pressed
		#Update the player sprite based on user keypresses
		#player.update(pressed_keys) 
		airbrush()
		GameDraw()
		GameUpdate() 
		
		#screen.fill((55, 255, 255), buttonup.rect2)
		#screen.fill((55, 255, 255), buttondown.rect2)
		#screen.fill((55, 255, 255), buttonshoot.rect2)
		#screen.fill((55, 255, 255), buttonrestart.rect2)
		 
		pygame .display . flip()
		#pygame . quit() 
#while True:
main()


