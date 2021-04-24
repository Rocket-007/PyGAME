import pygame
import math
import random 
pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Squarey")
x = 100
y = 100
baddyX = 300
baddyY = 300
vel = 16
baddyVel = 6
run = True 
touched = False


mousepos=[0,0]
mousepos[0] =0
mousepos[1]=0

def CheckCollision(x1,y1,w1,h1, x2,y2,w2,h2):
	return x1 < x2+w2 and x2 < x1+w1 and y1 < y2+h2 and y2 < y1+h1


class Enemy(pygame . sprite.Sprite):
	def __init__ (self ):
		super(Enemy, self ).__init__ ()
		#self .surf = pygame .iage .load( "bullet.png" ). convert()
		#self .surf.set_colorkey(( 0, 0, 0), RLEACCEL)
		# The starting posiion is randomly generated
		self.w=40
		self.h=40
		self . x =random.randint(170,250)
		self.y=random.randint(30,270)
		self.vel=random.randint(1,7)
		#self . top = player.bottom 

		#self .rect = self .surf. get_rect(center=(random .randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),random .randint(0, SCREEN_HEIGHT),))
		#self .rect = self .surf. get_rect(center=(self.center_x,self.center_y))
		
	# Move the cloud based on a constant speed
	# Remove the cloud when it passes the left edge of the screen
	def update( self ):
		'''
		self. rect .move_ip( 8, 0)
		if self. rect .right < 0:
			self .kill() '''
		if self.x  < x - 10:
		    	self. x += self.vel
		    	#drawGame() 
		if self. x > x + 10:
		    #drawGame()
		    self.x-=self.vel
		if self.y < y - 10:
		    self.y +=self.vel  
		elif self.y> y + 10:
		    self.y -= self.vel
		else:
			global run 
			if CheckCollision(self.x,self. y,self. w,self. h, x,y,20,20):
				run = False
 
Enemieslist=[1,2,3]
Enemieslist [0]=Enemy()
Enemieslist[1]=Enemy()
Enemieslist[2]=Enemy()
 
def updateKeys(event):
	 if event.type == pygame.QUIT:
	     run = False
	 keys = pygame.key.get_pressed()
	 if keys[pygame.K_LEFT]:
	    x -= vel
	 if keys[pygame.K_RIGHT]:
	    x += vel
	 if keys[pygame.K_UP]:
	    y -= vel
	 if keys[pygame.K_DOWN]:
	           y += vel
            
def moveplayer():
	global x, y, touched
	if mousepos[0] != x and mousepos[1]!=y and touched :
		ang=math.atan2(mousepos[1], mousepos[0])
	#x=mousepos[0]
	#y=mousepos[1]
	#if touched:
		#x+=vel* math.cos(ang)
		#y += vel* math.sin(ang)
		
		# Vector from me to cursor
		dx = mousepos[0] - x
		dy = mousepos[1] -y
		
		# Unit vector in the same direction
		distance = math.sqrt(dx*dx + dy*dy)
		dx /= distance
		dy /= distance 
		if distance >2:
			#global touched 
		    #touched =True
		 x +=vel* dx
		y+=vel* dy

def drawGame():
          win.fill((0, 0, 0))
          for i in Enemieslist:
          	pygame.draw.rect(win,  (255,0,0), (i.x, i.y,40,40))
          	
          pygame.draw.rect(win, (0, 0, 255), (x, y, 20, 20))
          pygame.draw.rect(win, (255, 0, 0), (baddyX, baddyY,40, 40))
          pygame.display.update()
while run:
      pygame.time.delay(100)
      for i in Enemieslist:
          	i.update()
          	
      if baddyX < x - 10:
      	baddyX = baddyX + baddyVel
      	#drawGame() 
      elif baddyX > x + 10:
          #drawGame()
          baddyX = baddyX - baddyVel
      elif baddyY < y - 10:
      	baddyY = baddyY + baddyVel 
      elif baddyY > y + 10:
          baddyY = baddyY - baddyVel
      else:
          run = False
      for ev in pygame.event.get():
           if ev.type == pygame.MOUSEMOTION:
           #if rect.collidepoint(ev.pos):
                #Global 
                #mousepos=[0,0]
                mousepos[0] =ev.pos[0]
                mousepos[1]=ev.pos[1]
                
                #moveplayer(ev.pos)
                touched = True
                # This is the starting point
                pygame.mouse.get_rel()
           elif ev.type == pygame.MOUSEBUTTONUP:
            touched = False
      moveplayer()
       
      drawGame()
pygame.quit()