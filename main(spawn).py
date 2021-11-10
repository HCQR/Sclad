
from Obj import obj
from Draw import *
from settings import *


class let():
    def __init__(self, x, y, lenght):
        self.x=x
        self.y=y
        self.lenght=lenght
        self.High=40



    def draw(self,x,y):
        pygame.draw(screen,GREEN, (self.x, self.y), self.lenght, self.High)


Table1= obj(45,35,100,300,BLUE)
Table2= obj(45,35,200,200,GREEN)
Table3= obj(45,35,250,300,WHITE)
Table4= obj(45,35,130,220,YELLOW)


running = True
while running:
    clock.tick(60) # 60 fps


    drawWindow()

    Table1.draw()
    Table2.draw()
    Table3.draw()
    Table4.draw()


    surf = pygame.Surface((850, 650))
    surf.blit(screen, (0, 0))

    pygame.display.flip()
    #pygame.display.update()  # обновление окна

pygame.quit()
