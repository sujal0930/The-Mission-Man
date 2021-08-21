import pygame
from pygame.locals import *

pygame.font.init()

font = pygame.font.SysFont('Constantia', 25)
font1 = pygame.font.SysFont('Constantia', 90)

imIdeal = pygame.image.load('player\i1.png')
imDead = pygame.image.load('player\dead1.png')
imIdeal = pygame.transform.scale(imIdeal,(200,200))
#define colours
bg = pygame.image.load('assets\BG.png')
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#define global variable
clicked = False
counter = 0

class button():
	intro=False
	won=False
	lost =False
	#colours for button and text
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = black
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self,screen,heading,but):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add text to button
		text_img = font1.render(heading, 1, (111,111,111))
		screen.blit(text_img, (100,200))
		text_img = font.render(self.text, 1, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action

def run(screen,heading,*but):
    	
	if len(but)==1:
		intro = button(370, 400,but[0])
	else:
		gameend1 = button(170, 400,but[0])
		gameend2 = button(170, 500,but[1])
		

	run = True
	while run:
		
		screen.blit(bg,(0,0))
		
		if len(but)==1:
			if intro.draw_button(screen,heading,but) :
				run=False
		else:
			screen.blit(imIdeal,(600,400))
			if gameend1.draw_button(screen,heading,but[0]):
				run=False
				
			if gameend2.draw_button(screen,heading,but[1]):
				run=False
				pygame.display.quit()
				
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False	


		pygame.display.update()