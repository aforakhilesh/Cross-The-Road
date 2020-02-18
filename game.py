import pygame as py
import random
import math
from config import *

import sys,time

py.init()
#clock = py.time.get_ticks()
screen = py.display.set_mode((1300,750))
bg=py.image.load('bgf.png')
running=True

py.display.set_caption(title)
my_icon = py.image.load('/home/akhilesh/Desktop/gamepad.png')
py.display.set_icon(my_icon)

player1X = 634
player1Y = 710

score1 = 0
score2 = 0


def player1():
	screen.blit(player1img, (player1X,player1Y))

def enemyf(x,y):
	screen.blit(enemy1img, (enemyfX,enemyfY))

def enemye(x,y):
	screen.blit(enemy1img, (enemyeX,enemyeY))

def enemyb(x,y):
	screen.blit(enemy2img, (enemybX,enemybY))

def enemyf1(x,y):
	screen.blit(enemy1img, (enemyf1X,enemyf1Y))

def enemye1(x,y):
	screen.blit(enemy2img, (enemye1X,enemye1Y))

def enemyb1(x,y):
	screen.blit(enemy2img, (enemyb1X,enemyb1Y))

def enemyf2(x,y):
	screen.blit(enemy1img, (enemyf2X,enemyf2Y))

def enemye2(x,y):
	screen.blit(enemy1img, (enemye2X,enemye2Y))

def enemyb2(x,y):
	screen.blit(enemy2img, (enemyb2X,enemyb2Y))

def obstacle11(x,y):
	screen.blit(obsimg1, (obstacle11X, obstacle11Y))

def obstacle12(x,y):
	screen.blit(obsimg1, (obstacle12X, obstacle12Y))

def obstacle13(x,y):
	screen.blit(obsimg1, (obstacle13X, obstacle13Y))

def obstacle21(x,y):
	screen.blit(obsimg1, (obstacle21X, obstacle21Y))

def obstacle22(x,y):
	screen.blit(obsimg1, (obstacle22X, obstacle22Y))

def obstacle23(x,y):
	screen.blit(obsimg1, (obstacle23X, obstacle23Y))

def obstacle31(x,y):
	screen.blit(obsimg1, (obstacle31X, obstacle31Y))

def obstacle32(x,y):
	screen.blit(obsimg1, (obstacle32X, obstacle32Y))

def obstacle33(x,y):
	screen.blit(obsimg1, (obstacle33X, obstacle33Y))

def obstacle41(x,y):
	screen.blit(obsimg1, (obstacle41X, obstacle41Y))

def obstacle42(x,y):
	screen.blit(obsimg1, (obstacle42X, obstacle42Y))

def iscollision(eX,eY,pX,pY):
	distance = math.sqrt(math.pow(eX-pX ,2) + math.pow(eY-pY,2))
	if distance < 25:
		return True
	else:
		return False

# def message_display(text):
# 	x=1000
# 	while x>0:
# 	    largeText = py.font.Font('freesansbold.ttf',50)
# 	    TextSurf, TextRect = text_objects(text, largeText)
# 	    TextRect.center = (0,0)
# 	    screen.blit(TextSurf, TextRect)
# 	    py.display.update()
# 	    x-=1

# def text_objects(text, font):
#     textSurface = font.render(text, True, black)
#     return textSurface, textSurface.get_rect()

font = py.font.Font('freesansbold.ttf', 50)
font1 = py.font.Font('freesansbold.ttf', 25)

text1 = font.render('You have crashed!', True, black)
text1Rect = text1.get_rect()
text1Rect.center = (650,375)



flag = 0
level = 1

player1img = py.image.load('pokemon1.png')
enemy1img = py.image.load('car1.png').convert_alpha()
enemy2img = py.image.load('car2.png').convert_alpha()
obsimg1 = py.image.load('stone.png').convert_alpha()

enemyfX = random.randint(0,650)
enemyfY = 107
enemybX = random.randint(650,1300)
enemybY = 70
enemyeX = random.randint(0,650)
enemyeY = 144
enemyfX_change = 2*level
enemybX_change = -1.5*level
enemyeX_change = 1*level

enemyf1X = random.randint(0,650)
enemyf1Y = 285
enemyb1X = random.randint(650,1300)
enemyb1Y = 325
enemye1X = random.randint(0,650)
enemye1Y = 365
enemyf1X_change = 3*level
enemyb1X_change = -1*level
enemye1X_change = -2.5*level

enemyf2X = random.randint(0,650)
enemyf2Y = 522
enemyb2X = random.randint(650,1300)
enemyb2Y = 560
enemye2X = random.randint(0,650)
enemye2Y = 600
enemyf2X_change = 2*level
enemyb2X_change = -4*level
enemye2X_change = 1.5*level

obstacle11X = random.randint(0,1300)
obstacle11Y = random.randint(0,30)
obstacle12X = random.randint(0,1300)
obstacle12Y = random.randint(0,30)
obstacle13X = random.randint(0,1300)
obstacle13Y = random.randint(0,30)

obstacle21X = random.randint(0,1300)
obstacle21Y = random.randint(175, 250)
obstacle22X = random.randint(0,1300)
obstacle22Y = random.randint(175, 250)
obstacle23X = random.randint(0,1300)
obstacle23Y = random.randint(175, 250)

obstacle31X = random.randint(0,1300)
obstacle31Y = random.randint(400, 500)
obstacle32X = random.randint(0,1300)
obstacle32Y = random.randint(400, 500)
obstacle33X = random.randint(0,1300)
obstacle33Y = random.randint(400, 500)

obstacle41X = random.randint(0,600)
obstacle41Y = random.randint(650,700)
obstacle42X = random.randint(800,1300)
obstacle42Y = random.randint(650,700)

player1X_change = 0
player1Y_change = 0
eX=0
eY=0
pX=0
pY=0
flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
flag6 = False



while running:
	screen.fill((102, 255, 153))
	screen.blit(bg,(0,0))
	for event in py.event.get():
		if event.type == py.QUIT:
			running=False

	text2 = font1.render('Player 1: ' + str(score1), True, black)
	text2Rect = text2.get_rect()
	text2Rect.center = (100,25)

	text3 = font1.render('Player 2: ' + str(score2), True, black)
	text3Rect = text3.get_rect()
	text3Rect.center = (100,725)

	text4 = font1.render('Player 1 has passed Level-1', True, black)
	text4Rect = text4.get_rect()
	text4Rect.center = (650,375)

	text5 = font1.render('Player 2 has passed Level-1', True, black)
	text5Rect = text5.get_rect()
	text5Rect.center = (650,375)

	screen.blit(text2, text2Rect)
	screen.blit(text3, text3Rect) 
	if flag == 0:
		keys = py.key.get_pressed()
		if keys[py.K_UP]:
			player1Y -= 2
		if keys[py.K_DOWN]:
			player1Y += 2
		if keys[py.K_LEFT]:
			player1X -= 2
		if keys[py.K_RIGHT]:
			player1X += 2
		# if event.type == py.KEYDOWN:
		# 	if event.key == py.K_LEFT:
		# 		player1X_change = -1.5
		# 	if event.key == py.K_RIGHT:
		# 		player1X_change = 1.5
		# 	if event.key == py.K_DOWN:
		# 		player1Y_change = 1.5
		# 	if event.key == py.K_UP:
		# 		player1Y_change = -1.5
		# if event.type == py.KEYUP:
		# 	if event.key == py.K_LEFT or event.key == py.K_RIGHT or event.key == py.K_UP or event.key == py.K_DOWN:
		# 		player1X_change = 0
		# 		player1Y_change = 0

	else:
		keys = py.key.get_pressed()
		if keys[py.K_w]:
			player1Y -= 2
		if keys[py.K_s]:
			player1Y += 2
		if keys[py.K_a]:
			player1X -= 2
		if keys[py.K_d]:
			player1X += 2
		# if event.type == py.KEYDOWN:
		# 	if event.key == py.K_a:
		# 		player1X_change = -1.5
		# 	if event.key == py.K_d:
		# 		player1X_change = 1.5
		# 	if event.key == py.K_s:
		# 		player1Y_change = 1.5
		# 	if event.key == py.K_w:
		# 		player1Y_change = -1.5
		# if event.type == py.KEYUP:
		# 	if event.key == py.K_a or event.key == py.K_d or event.key == py.K_w or event.key == py.K_s:
		# 		player1X_change = 0
		# 		player1Y_change = 0


	# player1X += player1X_change
	if player1X<0:
		player1X = 0
	if player1X>1268:
		player1X = 1268
	if player1Y<0:
		player1Y = 0
	if player1Y>718:
		player1Y = 718

	enemyfX += enemyfX_change
	if(enemyfX>=1300):
		enemyfX = -32 

	enemybX += enemybX_change
	if(enemybX<=-32):
		enemybX = 1332

	enemyeX += enemyeX_change
	if(enemyeX>=1300):
		enemyeX = -32 

	enemyf1X += enemyf1X_change
	if(enemyf1X>=1300):
		enemyf1X = -32 

	enemye1X += enemye1X_change
	if(enemye1X<=-32):
		enemye1X = 1332 

	enemyb1X += enemyb1X_change
	if(enemyb1X<=-32):
		enemyb1X = 1332 

	enemyf2X += enemyf2X_change
	if(enemyf2X>=1300):
		enemyf2X = -32 

	enemye2X += enemye2X_change
	if(enemye2X>=1332):
		enemye2X = -32

	enemyb2X += enemyb2X_change
	if(enemyb2X<=-32):
		enemyb2X = 1332 

	# player1Y += player1Y_change
	player1()
	enemyf(enemyfX,enemyfY)
	enemyb(enemybX,enemybY)
	enemye(enemyeX,enemyeY)
	enemyf1(enemyf1X,enemyf1Y)
	enemye1(enemye1X,enemye1Y)
	enemyb1(enemyb1X,enemyb1Y)
	enemyf2(enemyf2X,enemyf2Y)
	enemye2(enemye2X,enemye2Y)
	enemyb2(enemyf2X,enemyb2Y)
	obstacle11(obstacle11X,obstacle11Y)
	obstacle12(obstacle12X,obstacle12Y)
	obstacle13(obstacle13X,obstacle13Y)
	obstacle21(obstacle21X,obstacle21Y)
	obstacle22(obstacle22X,obstacle22Y)
	obstacle23(obstacle23X,obstacle23Y)
	obstacle31(obstacle31X,obstacle31Y)
	obstacle32(obstacle32X,obstacle32Y)
	obstacle33(obstacle33X,obstacle33Y)
	obstacle41(obstacle41X,obstacle41Y)
	obstacle42(obstacle42X,obstacle42Y)

	if flag == 0:
		if player1Y < 635 and player1Y > 484 and flag1==False:
			score1 += 10
			flag1 = True
		if player1Y < 484 and player1Y > 396 and flag2==False:
			score1 += 30
			flag2 = True
		if player1Y < 396 and player1Y > 242 and flag3==False:
			score1 += 15
			flag3 = True
		if player1Y < 242 and player1Y > 108 and flag4==False:
			score1 += 30
			flag4 = True
		if player1Y < 108 and player1Y > 30 and flag5==False:
			score1 += 15
			flag5 = True
		if player1Y < 30 and flag6==False:
			score1 += 15
			flag6 = True
	else:
		if player1Y > 635 and flag1==False:
			score2 += 10
			flag1=True
		if player1Y > 484 and player1Y < 635 and flag2==False:
			score2 += 30
			flag2=True
		if player1Y > 396 and player1Y < 484 and flag3==False:
			score2 += 15
			flag3=True
		if player1Y > 242 and player1Y < 396 and flag4==False:
			score2 += 30
			flag4=True
		if player1Y > 108 and player1Y < 242 and flag5==False:
			score2 += 15
			flag5=True
		if player1Y > 30 and player1Y < 108 and flag6==False:
			score2 += 15
			flag6=True

	collision = iscollision(enemyfX,enemyfY,player1X,player1Y)
	collision1 = iscollision(enemybX,enemybY,player1X,player1Y)
	collision2 = iscollision(enemyf1X,enemyf1Y,player1X,player1Y)
	collision3 = iscollision(enemyb1X,enemyb1Y,player1X,player1Y)
	collision4 = iscollision(enemyf2X,enemyf2Y,player1X,player1Y)
	collision5 = iscollision(enemyb2X,enemyb2Y,player1X,player1Y)
	collision6 = iscollision(enemyeX,enemyeY,player1X,player1Y)
	collision7 = iscollision(enemye1X,enemye1Y,player1X,player1Y)
	collision8 = iscollision(enemye2X,enemye2Y,player1X,player1Y)
	collision9 = iscollision(obstacle11X,obstacle11Y,player1X,player1Y)
	collision10 = iscollision(obstacle12X,obstacle12Y,player1X,player1Y)
	collision11 = iscollision(obstacle13X,obstacle13Y,player1X,player1Y)
	collision12 = iscollision(obstacle21X,obstacle21Y,player1X,player1Y)
	collision13 = iscollision(obstacle22X,obstacle22Y,player1X,player1Y)
	collision14 = iscollision(obstacle23X,obstacle23Y,player1X,player1Y)
	collision15 = iscollision(obstacle31X,obstacle31Y,player1X,player1Y)
	collision16 = iscollision(obstacle32X,obstacle22Y,player1X,player1Y)
	collision17 = iscollision(obstacle33X,obstacle33Y,player1X,player1Y)
	collision18 = iscollision(obstacle41X,obstacle41Y,player1X,player1Y)
	collision19 = iscollision(obstacle42X,obstacle42Y,player1X,player1Y)
	if collision or collision1 or collision2 or collision3 or collision4 or collision5 or collision6 or collision7 or collision8 or collision9 or collision10 or collision11 or collision12 or collision13 or collision14 or collision15 or collision16 or collision17 or collision18 or collision19 or player1X<=20:
		screen.blit(text1, text1Rect)
		if flag == 0:
			flag = 1
			flag1 = False
			flag2 = False
			flag3 = False
			flag4 = False
			flag5 = False
			flag6 = False
		else:
			flag = 0
			flag1 = False
			flag2 = False
			flag3 = False
			flag4 = False
			flag5 = False
			flag6 = False
		if flag == 0:	
			player1X = 634
			player1Y = 710
			score2 = 0
			flag1 = False
			flag2 = False
			flag3 = False
			flag4 = False
			flag5 = False
			flag6 = False
		else:
			player1X = 634
			player1Y = 8
			score1 = 0
			flag1 = False
			flag2 = False
			flag3 = False
			flag4 = False
			flag5 = False
			flag6 = False
		py.display.flip()
		time.sleep(1)

	if flag == 0 and player1Y < 5:
		flag = 1
		i=1000
		while i>0:	
			screen.blit(text4, text4Rect)
			py.display.flip()
			i -= 1
		flag1 = False
		flag2 = False
		flag3 = False
		flag4 = False
		flag5 = False
		flag6 = False
		player1X = 634
		player1Y = 10
		continue
	if flag == 1 and player1Y > 710:
		flag = 0
		i=1000
		while i>0:	
			screen.blit(text5, text5Rect)
			py.display.flip()
			i -= 1
		flag1 = False
		flag2 = False
		flag3 = False
		flag4 = False
		flag5 = False
		flag6 = False
		player1X = 634
		player1Y = 705
		continue


	py.display.flip()

	print(score1)


