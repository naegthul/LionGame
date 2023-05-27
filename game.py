# Example file showing a basic pygame "game loop"
import pygame
from field import Field

def game():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    conf = start_menu(screen)
    conf["field_size"] = 10

    screen = pygame.display.set_mode((int(conf["fields"]) * conf["field_size"],
                                      (int(conf["fields"]) * conf["field_size"])))

    field = Field(screen, conf, clock)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        field.draw()




        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(30)  # limits FPS to 60

    pygame.quit()


def start_menu(screen: pygame.display) -> dict|None:

    font = pygame.font.Font(None, 28)
    return_dict = {
        "fields": "",
        "crates": ""
    }

    input_num_fields = pygame.Rect(200, 10, 400, 40)
    label_num_fields = font.render("Number of fields: ", True, pygame.Color('white'))
    input_num_crates = pygame.Rect(200, 60, 400, 40)
    label_num_crates = font.render("Number of crates: ", True, pygame.Color('white'))
    button_ok = pygame.Rect(50, 150, 80, 40)

    color_active = pygame.Color("white")
    color_inactive = pygame.Color("blue")
    active = [None, None]

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_num_fields.collidepoint(event.pos):
                    active = [input_num_fields, return_dict["fields"]]
                elif input_num_crates.collidepoint(event.pos):
                    active = [input_num_crates, return_dict["crates"]]
                elif button_ok.collidepoint(event.pos):
                    if return_dict["fields"].isnumeric() and return_dict["crates"].isnumeric():
                        return return_dict
                    else:
                        print("Enter a positive number")


                else:
                    active = [None, None]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if active[0] == input_num_fields:
                        return_dict['fields'] = return_dict['fields'][:-1]
                    elif active[0] == input_num_crates:
                        return_dict['crates'] = return_dict['crates'][:-1]
                else:
                    try:
                        if active[0] == input_num_fields:
                            return_dict['fields'] += event.unicode
                        elif active[0] == input_num_crates:
                            return_dict['crates'] += event.unicode

                    except ValueError:
                        print("Please enter a positive number.")

        pygame.draw.rect(screen, color_active if active[0] == input_num_fields else color_inactive, input_num_fields, 2)
        pygame.draw.rect(screen, color_active if active[0] == input_num_crates else color_inactive, input_num_crates, 2)
        pygame.draw.rect(screen, color_inactive, button_ok, 2)

        screen.blit(label_num_fields, (10, 10))
        screen.blit(label_num_crates, (10, 60))
        txt_surface_fields = font.render(str(return_dict["fields"]), True, pygame.Color('white'))
        screen.blit(txt_surface_fields, (input_num_fields.x + 5, input_num_fields.y + 5))

        txt_surface_crates = font.render(str(return_dict["crates"]), True, pygame.Color('white'))
        screen.blit(txt_surface_crates, (input_num_crates.x + 5, input_num_crates.y + 5))

        txt_surface_crates = font.render("OK", True, pygame.Color('white'))
        screen.blit(txt_surface_crates, (button_ok.x + 5, button_ok.y + 5))

        pygame.display.flip()

4
if __name__ == "__main__":
    game()
