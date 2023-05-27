import random

import pygame


class Field:
    def __init__(self, screen, conf, clock):
        self.conf = conf
        self.screen = screen
        self.clock = clock
        self.fields = [[{"type": "none"} for _ in range(int(self.conf["fields"]))]
                       for _ in range(int(self.conf["fields"]))]

        # self.fields = [[1,1],[1,2],[1,3],
        #                [2,1],[2,2],[2,3]]

        for crate in range(int(self.conf["crates"])):

            new_x = random.randint(0, int(self.conf["fields"]) - 1)
            new_y = random.randint(0, int(self.conf["fields"]) - 1)

            while True:
                if self.fields[new_x][new_y]["type"] != "none":
                    new_x = random.randint(0, int(self.conf["fields"]) - 1)
                    new_y = random.randint(0, int(self.conf["fields"]) - 1)
                else:
                    break

            self.fields[new_x][new_y] = {
                "rect": pygame.Rect(new_x * self.conf["field_size"], new_y * self.conf["field_size"],
                                                    self.conf["field_size"], self.conf["field_size"]),
                "type": "crate"}


    def draw(self):

        for field_x in self.fields:
            for field in field_x:
                if field["type"] == "crate":
                    pygame.draw.rect(self.screen, pygame.Color("orange"), field["rect"], 0)








