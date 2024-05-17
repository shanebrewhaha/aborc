import pygame

width = 600
height = 400 


pygame.init()
screen = pygame.display.set_mode((width, height))

text_font = pygame.font.SysFont("ComicSans", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    

while True:
    screen.fill((255,255,255))
    
    draw_text("Hello", text_font, (0,0,0), 220, 150)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        input("Helo?")
    
    pygame.display.flip()
    
