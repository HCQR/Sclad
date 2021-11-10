from settings import *
from Draw import *
import random


class obj():
    def __init__(self,beer_hight,beer_width,beer_x_pos,beer_y_pos,color):
        self.beer_hight = beer_hight  # размеры пива
        self.beer_width = beer_width
        self.beer_x_pos =beer_x_pos
        self.beer_y_pos = beer_y_pos
        self.beer = pygame.Surface((self.beer_hight, self.beer_width), pygame.SRCALPHA)  # создание поверхности пива
        self.beer.fill(color)  # заливка цветом
        self.beer_rect = self.beer.get_rect(center=(self.beer_x_pos, self.beer_y_pos))
        self.transparency = 255 # прозрачность


    def draw(self): # рисуем пиво
        self.beer.set_alpha(self.transparency)
        screen.blit(self.beer, (self.beer_x_pos, self.beer_y_pos))

    def getBeerPos(self):
        return self.beer_rect.center # возвращаем позицию пива
        #print(self.beer_rect.center)

    def beerTaken(self): # если пиво взяли, то уменьшаем прозрачность до нуля

        for i in range (0, 255):
            self.transparency -= 5

    def setBeerPos(self, pos):
        self.beer_x_pos = pos[0] # меняем координаты пива
        self.beer_y_pos = pos[1]
        self.beer_rect = self.beer.get_rect(center=pos)
        self.transparency = 255
