import pygame
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
WHITE   = (255, 255, 255)
BLACK =   (0, 0, 0)
def main():
    pygame.init()
    while True:
        window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('Hello World')
        BasicFont = pygame.font.Font('freesansbold.ttf', 20)
        text = BasicFont.render("Hello world", True, BLACK)
        textCoord = text.get_rect()
        window.fill(WHITE)
        window.blit(text, textCoord)
        pygame.display.flip()
 
if __name__ == "__main__":
    main()
