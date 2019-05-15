import square
import pygame
import random
import math


class Map:
    def __init__(self, width, height, seeds):

        random.seed()
        self.seeds = seeds
        self.height = height
        self.width = width
        self.map = []

        for i in range(self.width):
            self.map.append([])
            for j in range(self.height):
                self.map[i].append("vesi")

        for n in range (seeds):

            x = random.randint(1,self.width-2)
            y = random.randint(1,self.height-2)
            self.map[x][y] = "maa"
            self.map[x+1][y+1] = "maa"
            self.map[x+1][y] = "maa"
            self.map[x+1][y-1] = "maa"
            self.map[x][y+1] = "maa"
            self.map[x][y] = "maa"
            self.map[x][y-1] = "maa"
            self.map[x-1][y+1] = "maa"
            self.map[x-1][y] = "maa"
            self.map[x-1][y-1] = "maa"

            koko = 25
            puol = 13

            for i in range (koko):
                for j in range (koko):
                    if (x+i-puol > self.width-1 or y+j-puol > self.height-1 or x+i-puol < 0 or y+j-puol < 0):
                        continue
                    if (i-puol==0 and j-puol==0):
                        continue
                    if math.sqrt((math.pow(i-puol,2))+(math.pow(j-puol,2)))/koko < math.pow(random.random(),2):
                        self.map[x+i-puol][y+j-puol] = "maa"



    def get_map():
        return map

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_pos(self, x, y):
        return self.map[x][y]

    def clean(self):
        for i in range(1,self.width-1):
            for j in range(1,self.height-1):
                erot = 0

                if self.map[i][j] == "vesi":
                    if self.map[i+1][j-1] == "maa":
                        erot += 1
                    if self.map[i+1][j+1] == "maa":
                        erot += 1
                    if self.map[i-1][j-1] == "maa":
                        erot += 1
                    if self.map[i-1][j+1] == "maa":
                        erot += 1
                    if self.map[i+1][j] == "maa":
                        erot += 1
                    if self.map[i][j+1] == "maa":
                        erot += 1
                    if self.map[i-1][j] == "maa":
                        erot += 1
                    if self.map[i][j-1] == "maa":
                        erot += 1
                    if erot > 5:
                        self.map[i][j] = "maa"
                elif self.map[i][j] == "maa":
                    if self.map[i+1][j-1] == "vesi":
                        erot += 1
                    if self.map[i+1][j+1] == "vesi":
                        erot += 1
                    if self.map[i-1][j-1] == "vesi":
                        erot += 1
                    if self.map[i-1][j+1] == "vesi":
                        erot += 1
                    if self.map[i+1][j] == "vesi":
                        erot += 1
                    if self.map[i][j+1] == "vesi":
                        erot += 1
                    if self.map[i-1][j] == "vesi":
                        erot += 1
                    if self.map[i][j-1] == "vesi":
                        erot += 1
                    if erot > 8:
                        self.map[i][j] = "vesi"

