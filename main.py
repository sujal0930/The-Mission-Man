import pygame
import time
import classFile
import world_data
import Intro

pygame.display.init()
clock=pygame.time.Clock()

# background
bg = pygame.image.load('assets\BG.png')

#fix the game screen width
screen_width=975
screen_height=750
screen = pygame.display.set_mode((screen_width,screen_height))


"DECLARATION OF objects"

#check for next level display
nextScreen=False
score=0
gamewon = False

# to change background image on next level
Bgx=0

# Introscreen
introScreen =True

# object declarations

world = world_data.world()
man = classFile.player(100,400,75,75)
zom=[]
z1 = classFile.zombie(300,600,75,75,450)
z2 = classFile.zombie(130,150,75,75,160)
zom.append(z1)
zom.append(z2)
s1=classFile.star(700,100)


def reset():
    """ This function calls the reset function of each object class and re-initialise them """
    man.resetP(100,400,75,75)
    z1.resetZ(300,600,75,75,450)
    z2.resetZ(130,150,75,75,160)
    s1.resetS(700,100)
    nextScreen=False
    return 
    

def won(man):
    """This function check if won and calls the buffer screen with respective messages."""
    if Bgx<0 and man.x>900:
        Intro.run(screen,"YOU WON","play Again","Exit")
        bgX=reset()
        return True

def lost(man):
    """This function check if lost and calls the buffer screen with respective messages."""
    if man.dead:
        Intro.run(screen,"Oops! YOU LOST","Play Again","Exit")    
        bgX=reset()
        return True


def redrawWindow():
    """ Draws or blits all whole world """

    # redraw just the background to avoid mutiprint as in loop.
    screen.blit(bg,(Bgx,0))
    

    # draw World
    world.draw(screen)

    #draw zombie
    for z in zom:
       flag=z.draw(screen)


    # display bullets
    for i in range(len(classFile.bullet.bulletList)):
        classFile.bullet.bulletList[i].draw(screen)

    # draw player
    man.drawPlayer(screen)

    # star 
    s1.draw(screen)
    
    #update the screen 
    pygame.display.update()
    return True
    


# Main while loop
run=True

while run:
    """  MAIN LOOP  """
    clock.tick(60)
    if introScreen:
        Intro.button.intro=True
        Intro.run(screen,"THE MISSION MAN","START GAME")
        introScreen=False

            
    # Screen Scroll Logic
    if man.x>950 and not nextScreen:
        Bgx=-975
        screen.blit(bg,(Bgx,0))
        nextScreen=True
        man.x+=Bgx
        world.updateScreenTiling(1)

    # Events and player movememt
    man.movePlayer(world.tile_list)

    # bullet hitCheck
    score=classFile.bullet.hitBullet(zom,score) 

    # hit with Player and enemies
    man.hitEnemies(zom)

    # star grab
    score=s1.grabStar(score,man)

    # redraw the whole world
    run=redrawWindow()


    # checking whether won or lost ad updating screen accordingly
    if  won(man):
        Bgx=0
        screen.blit(bg,(Bgx,0))
        world.updateScreenTiling(0)
        nextScreen=False
    if lost(man):
        # if i=on next level it reinitialse it on 1st screen
        if nextScreen:
            Bgx=0
        screen.blit(bg,(Bgx,0))
        world.updateScreenTiling(0)
        nextScreen=False
        
    # Quit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.quit()