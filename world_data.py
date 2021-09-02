import pygame


# giving screen dimentions
screen_width=975
screen_height=750



# world-data tiles
worldData = [(
    [9,9,9,9,9,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,2,3,3],
    [15,15,16,0,0,0,0,14,16,0,12,9,9],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,14,15,15,16,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [3,3,3,4,0,0,0,0,0,0,2,4,0],
    [5,5,5,6,0,0,0,0,2,3,8,10,3],
    [5,5,5,6,0,2,3,7,8,5,5,5,5])
    
    ,
    
   ([0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,14,16,0,0,0,0,0,0,0,0,0],
    [6,0,0,0,0,0,0,1,0,0,0,14,16],
    [6,0,0,0,0,2,3,8,0,0,0,0,0],
    [10,3,0,0,0,12,0,0,0,14,15,15,16],
    [0,0,0,14,16,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,14,16,0,0,0,0,0],
    [0,0,14,16,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [3,3,3,3,3,0,2,4,0,0,0,0,0])
]

# objects data
objectData=[

    #  world 1
    ([0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,4],
    [2,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,11,13],
    [0,0,0,0,0,0,0,10,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [6,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,11,0,0,0,0,0,0,9,0,0,1],
    [0,0,0,0,0,0,0,5,0,0,0,0,0],
    [14,0,0,0,0,0,13,0,0,0,0,0,0])
    
    # world 2
    ,

    ([0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,15])
]

def drawGrid(screen):
    tile_size=75
    
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))




#  World cration #
class world():
    objType=[pygame.image.load(f'assets\Tiles_and_objects\Objects\ob{x}.png') for x in range(1,16)]
    tilType=[pygame.image.load(f'assets\Tiles_and_objects\Tiles\s{i}.png') for i in range(1,17)]
    
    def __init__(self):
        self.tile_list=[]
        self.objList=[]
        self.level=0
        self.tileSize=75
        self.rowCount=0 
       
        # Storing data in a list so that we can draw only those on screen 
        # and also we can have the obstruction with the player logic
         
        "worldatat tiles"
        for row in worldData[self.level]:
            self.colCount=0
            for tile in row:
                if tile!=0:
                    img11=self.tilType[tile-1]
                    img=pygame.transform.scale(img11,(self.tileSize,self.tileSize))
                    img_rect = img.get_rect()
                    img_rect.x = self.colCount * self.tileSize
                    img_rect.y = self.rowCount * self.tileSize
                    tile= (img, img_rect)
                    self.tile_list.append(tile)
                self.colCount+=1
            self.rowCount+=1

        "worlddata Objects"
        self.rowCount=0
        for row in objectData[self.level]:
            self.colCount=0
            for tile in row:
                if tile!=0:
                    img11=self.objType[tile-1]
                    img=pygame.transform.scale(img11,(self.tileSize,self.tileSize))
                    img_rect = img.get_rect()
                    img_rect.x = self.colCount * self.tileSize
                    img_rect.y = self.rowCount * self.tileSize
                    tile= (img, img_rect)
                    self.objList.append(tile)
                self.colCount+=1
            self.rowCount+=1





    def updateScreenTiling(self,level):
        """updates the tiling and layout while on nextcreen"""

        self.tile_list=[]
        self.objList=[]
        self.level=level

        self.rowCount=0
        
        for row in worldData[self.level]:
            self.colCount=0
            for tile in row:
                if tile!=0:
                    img11=self.tilType[tile-1]
                    img=pygame.transform.scale(img11,(self.tileSize,self.tileSize))
                    img_rect = img.get_rect()
                    img_rect.x = self.colCount * self.tileSize
                    img_rect.y = self.rowCount * self.tileSize
                    tile= (img, img_rect)
                    self.tile_list.append(tile)
                self.colCount+=1
            self.rowCount+=1
        
        self.rowCount=0
        for row in objectData[self.level]:
            self.colCount=0
            for tile in row:
                if tile!=0:
                    img11=self.objType[tile-1]
                    img=pygame.transform.scale(img11,(self.tileSize,self.tileSize))
                    img_rect = img.get_rect()
                    img_rect.x = self.colCount * self.tileSize
                    img_rect.y = self.rowCount * self.tileSize
                    tile= (img, img_rect)
                    self.objList.append(tile)
                self.colCount+=1
            self.rowCount+=1


    def draw(self,screen):
        """draws the tiling and objects on screen"""
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])

        for tile in self.objList:
            screen.blit(tile[0],tile[1])

            # rectangle print for tiles
            # pygame.draw.rect(screen,(255,255,255),tile[1],2)
            