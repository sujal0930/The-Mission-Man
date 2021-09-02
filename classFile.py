import pygame
import Intro
pygame.font.init()


font = pygame.font.SysFont('serif', 40, bold=True, italic=False)
    


class player(object):
    "Player class the hero"
    # image loading
    walkRight = [pygame.image.load(f'player/w{i}.png') for i in range(1, 16)]
    deadImages = [pygame.image.load(f'player/dead{i}.png') for i in range(1, 16)]
    jump = pygame.image.load('player/j8.png')
    ideal = pygame.image.load('player/i2.png')

    def __init__(self, x, y, h, w):
        self.resetP(x, y, h, w)

    def resetP(self, x, y, h, w):
        """reset fuction -> reintialise all player attributes"""
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.vel = 3
        self.vel_y = 0
        self.isJump = False
        self.moveLeft = False
        self.moveRight = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x, self.y, 50, 90)
        self.health = 50
        self.dead = False
        self.j=0

    def drawPlayer(self, screen):
        """Draws player on main screen"""
        if self.health > 0:
            if self.walkCount+1 > 45:
                self.walkCount = 0
            elif self.isJump:
                if self.moveLeft:
                    # Rotating the image to left by 1st tranforming ,
                    # , then rotating by 180 as direct flip gae the mirror image
                    image = pygame.transform.scale(self.jump, (100, 100))
                    image = pygame.transform.flip(image, False, True)
                    rotated_image = pygame.transform.rotate(image, -180)
                    new_rect = rotated_image.get_rect(center=image.get_rect(center=(self.x, self.y)).center)
                    screen.blit(rotated_image, (self.x-self.width, self.y))
                    self.walkCount += 1
                else:
                    image = pygame.transform.scale(self.jump, (100, 100))
                    screen.blit(image, (self.x, self.y))
                    self.walkCount += 1

            elif self.moveRight:
                image = pygame.transform.scale(
                self.walkRight[self.walkCount//3], (100, 100))
                screen.blit(image, (self.x, self.y))
                self.walkCount += 1

            elif self.moveLeft:
                image = pygame.transform.scale(self.walkRight[self.walkCount//3], (100, 100))
                image = pygame.transform.flip(image, False, True)
                rotated_image = pygame.transform.rotate(image, -180)
                new_rect = rotated_image.get_rect(center=image.get_rect(center=(self.x, self.y)).center)
                screen.blit(rotated_image, (self.x-self.width, self.y))
                self.walkCount += 1

            elif self.standing:
                ideaImage = pygame.transform.scale(self.ideal, (100, 100))
                screen.blit(ideaImage, (self.x, self.y))

            if self.moveLeft and not self.standing:
                self.hitbox = (self.x-self.width//3, self.y, 50, 90)
            else:
                self.hitbox = (self.x, self.y, 50, 90)

            # "the hitbox lining"
            # pygame.draw.rect(screen, (10,10,10), self.hitbox,1 )

            # the health bar and its logic
            pygame.draw.rect(screen, (0, 255, 0), (self.hitbox[0]+5, self.hitbox[1]-self.hitbox[3]+69, 60 - (6*(10-self.health/5)), 10))
        else:
            self.walkCount += 1
            # if self.walkCount+1 > 45:
            #     self.walkCount=0
            if self.walkCount >= 45:
                self.dead = True
            else:
                image = pygame.transform.scale(self.deadImages[self.walkCount//3], (100, 100))
                screen.blit(image, (self.x, self.y))

    def movePlayer(self, list):
        """This function takes care of all movements of player"""
        dy = 0
        dx = 0
        # LEFT AND RIGHT MOVEMENT
        keys = pygame.key.get_pressed()
        # moveleft
        if keys[pygame.K_LEFT]:
            dx -= 5
            self.moveLeft = True
            self.moveRight = False
            self.standing = False
        # moveright    
        elif keys[pygame.K_RIGHT]:
            dx += 5
            self.moveLeft = False
            self.moveRight = True
            self.standing = False
        else:
            self.standing = True
            self.moveLeft = False
            self.moveRight = False

        # jUMPING LOGIC
        if keys[pygame.K_SPACE] and not self.isJump:
            self.vel_y = -25
            self.isJump = True
            self.moveLeft = False
            self.moveRight = False
            self.walkCount = 0
        if keys[pygame.K_SPACE] == False:
            self.isJump = False

        # shoot bullet 
        if keys[pygame.K_TAB] and bullet.shootLoop == 0:
            # bullet.play()

            if self.moveLeft:
                face = -1
            else:
                face = 1

            # Adding bullets whenever triggered 
            if len(bullet.bulletList) < 100:
                bullet.bulletList.append(
                    bullet(round(self.x+self.width//2), round(self.y+self.height//2), face))
            bullet.shootLoop = 1

        # adding gravity
        dy += self.vel_y
        self.vel_y += 2
        if self.vel_y > 20:
            self.vel_y = 20

        # Checking collision
        for tile in list:

            if tile[1].colliderect(self.hitbox[0] + dx, self.hitbox[1], 50, 95):
                dx = 0
            if tile[1].colliderect(self.hitbox[0], self.hitbox[1]+dy, 50, 95):
                if self.vel_y < 0:
                    dy = self.hitbox[1] - tile[1].bottom
                    self.vel_y = 0
                    dy = 0
                elif self.vel_y >= 0:
                    dy = self.hitbox[1]+95 - tile[1].top
                    self.vel_y = 0
                    dy = 0

        self.x += dx
        self.y += dy


        # screen_hieght avoid exiting the screen
        if self.y > 660:
            self.y = 660
            self.vel_y = 0
            dy = 0

    def hitEnemies(self, zom):
        """Checking coliison with enemies by comparing their hitboxes"""
        for i in zom:
            if i.visible:
                if self.hitbox[1] + self.hitbox[3] > i.hitbox[1] and self.hitbox[1] < i.hitbox[1]+i.hitbox[3]:
                    if self.hitbox[0] + self.hitbox[2] > i.hitbox[0] and self.hitbox[0] < i.hitbox[0]+i.hitbox[2]:
                        # print("Hit"+ str(self.j))
                        self.j += 1
                        self.health -= 1


class zombie():
    """ Zombie Class->
    (init , reset , draw , move , hit)
    """
    walk = [pygame.image.load(f'zombi/w{i}.png') for i in range(1, 11)]

    def __init__(self, x, y, width, height, end):
        self.resetZ(x, y, width, height, end)

    def resetZ(self, x, y, width, height, end):
        """Reseting the zombies back to wherever they were"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = 1
        self.walkCount = 0
        self.path = [self.x, self.end]
        self.hitbox = (self.x+10, self.y, self.width-20, self.height)
        self.health = 10
        self.visible = True

    def draw(self, screen):
        """Drawing the zombies on screen"""
        if self.visible:
            self.move()
            if self.walkCount+1 > 27:
                self.walkCount = 0
            if self.vel > 0:
                image = pygame.transform.scale(self.walk[self.walkCount//3], (80, 80))
                screen.blit(image, (self.x, self.y))
                self.walkCount += 1
            elif self.vel < 0:
                image = self.walk[self.walkCount//3]
                image = pygame.transform.scale(self.walk[self.walkCount//3], (80, 80))
                image = pygame.transform.flip(image, True, False)
                screen.blit(image, (self.x, self.y))
                self.walkCount += 1

            self.hitbox = (self.x+10, self.y, self.width-20, self.height)

            # pygame.draw.rect(screen, (255,0,0),(self.hitbox),1)

            # the health bar and its logic
            pygame.draw.rect(screen, (255, 0, 0), (self.hitbox[0]+5, self.hitbox[1]-self.hitbox[3]+69, 50 - (5*(10-self.health)), 10))

    def move(self):
        """moving logic of zombie"""
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        """health decrement when bullet hits zombie"""

        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


class bullet(object):
    """ Bullet class -> init , hitbullet , draw """

    # image and bulletlist where bullet is appended
    bullImg = pygame.image.load('assets\star_ammo\pro2.png')
    bulletList = []
    shootLoop = 0

    def __init__(self, x, y, bulletFace):
        self.x = x
        self.y = y
        self.bulletFace = bulletFace
        self.vel = 10 * bulletFace

    
    def hitBullet(zom, score):
        """checking hit with bullet"""

        # TO avaoid multiple bullets at once
        if bullet.shootLoop > 0 and bullet.shootLoop < 5:
            bullet.shootLoop += 1
        else:
            bullet.shootLoop = 0

        # hitting bullet logic
        for z1 in zom:
            i = 0
            while i < len(bullet.bulletList):
                if bullet.bulletList[i].y < z1.hitbox[1] + z1.hitbox[3] and bullet.bulletList[i].y > z1.hitbox[1]:
                    if bullet.bulletList[i].x > z1.hitbox[0] and bullet.bulletList[i].x < z1.hitbox[0]+z1.hitbox[2]:
                        # add sound
                        # hitSound.play()
                        if z1.visible:
                            z1.hit()
                            score += 1
                            bullet.bulletList.pop(i)
                            continue
                        else:
                            bullet.bulletList[i].x += (
                                bullet.bulletList[i].vel)

                # firing and moving logic of bullets

                if bullet.bulletList[i].x < 975 and bullet.bulletList[i].x > 0:
                    bullet.bulletList[i].x += (bullet.bulletList[i].vel)
                else:
                    bullet.bulletList.pop(i)
                    continue
                i += 1
        return score

    def draw(self, screen):
        """Draws the bullets on screen"""
        image = pygame.transform.scale(self.bullImg, (25, 25))
        image = pygame.transform.rotate(image, -90)
        if self.bulletFace == 1:
            screen.blit(image, (self.x, self.y))
        else:
            screen.blit(image, (self.x-20, self.y))


class star(object):
    """ Star class -> init, draw, resetS, grabstar """
    starList = []

    def __init__(self, x, y):
        self.resetS(x, y)

    def resetS(self, x, y):
        """resets the star at deafult declared locations"""
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets\star_ammo\star.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rotateFactor = 1
        self.visible = True

    def draw(self, screen):
        """draw the stars"""
        if self.visible:
            image = pygame.transform.scale(self.image, (40, 40))

            # rotation logic of star 
            rotated_image = pygame.transform.rotate(self.image, -90*self.rotateFactor//20)
            new_rect = rotated_image.get_rect(center=image.get_rect(center=(self.x, self.y)).center)
            screen.blit(rotated_image, new_rect)
            self.rotateFactor = (self.rotateFactor+1) % 80

    def grabStar(self, score, man):
        """ Logic for grabbing the star by player"""
        if self.visible:
            if self.rect.colliderect(man.hitbox):
                man.health += 10
                score = (score+5) % 50
                self.visible = False
        return score
