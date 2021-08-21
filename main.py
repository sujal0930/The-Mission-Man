import pygame
import time
import classFile
import world_data
import Intro

pygame.display.init()
clock=pygame.time.Clock()
# background
bg = pygame.image.load('assets\BG.png')


screen_width=975
screen_height=750
screen = pygame.display.set_mode((screen_width,screen_height))


#### DECLARATION OF objects
nextScreen=False
score=0
shootLoop=0
# gameOver =False
gamewon = False
Bgx=0
MenuVisible =True


world = world_data.world()
man = classFile.player(100,400,75,75)
zom=[]
z1 = classFile.zombie(300,600,75,75,450)
z2 = classFile.zombie(130,150,75,75,160)
zom.append(z1)
zom.append(z2)
s1=classFile.star(700,100)






def reset():
    man.resetP(100,400,75,75)
    z1.resetZ(300,600,75,75,450)
    z2.resetZ(130,150,75,75,160)
    s1.resetS(700,100)
    nextScreen=False
    return 
    

def won(man):
    if Bgx<0 and man.x>900:
        Intro.run(screen,"YOU WON","play Again","Exit")
        bgX=reset()
def lost(man):
    if man.dead:
        Intro.run(screen,"Oops! YOU LOST","Play Again","Exit")    
        bgX=reset()


def redrawWindow():
    """ Draws or blits all whole world """


    screen.blit(bg,(Bgx,0))
    # world_data.drawGrid(screen)
    

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
    
    
    pygame.display.update()
    return True
    

"""  MAIN LOOP  """

# Main while loop
run=True

while run:
    clock.tick(45)
    # print(Bgx)
    if MenuVisible:
        Intro.button.intro=True
        Intro.run(screen,"THE MISSION MAN","START GAME")
        MenuVisible=False

            
    # Screen Scroll Logic
    if man.x>950 and not man.nextScreen:
        Bgx=-975
        screen.blit(bg,(Bgx,0))
        man.nextScreen=True
        man.x+=Bgx
        world.updateScreenTiling()
   # QUit Window

    # Event and player movememt
    man.movePlayer(world.tile_list)

    #bullet hitCheck
    score=classFile.bullet.hitBullet(zom,score) 

    #hit with Player and enemies
    man.hitEnemies(zom)

    #star grab
    score=s1.grabStar(score,man)

    # redraw the whole world
    run=redrawWindow()

    if  won(man):
        Bgx+=975
        screen.blit(bg,(Bgx,0))
        world.updateScreenTiling()
    if lost(man):
        Bgx+=975

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.quit()