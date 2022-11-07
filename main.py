import pygame

pygame.init()
time_font = pygame.font.Font("assets/GlacialIndifference-Regular.otf", 90)
talks_font = pygame.font.Font("assets/GlacialIndifference-Regular.otf", 66)

date = input("Date of the event >").upper()
time = input("Time of the event >").upper()
talk_names = input("Talk names >")
output = input("Output file name >")

base_image = pygame.image.load("assets/Smartmonday brain.png")
size = base_image.get_size()
base_surface = pygame.Surface(size)
window = pygame.display.set_mode(size)

date = f"{date} • {time}"
date_text = time_font.render(date, True, (0, 0, 0))
talk_text = talks_font.render(talk_names, True, (0, 0, 0))

base_image.blit(base_image, (0, 0))
base_image.blit(date_text, (size[0] // 2 - date_text.get_size()[0] // 2, 1600))
base_image.blit(talk_text, (size[0] // 2 - talk_text.get_size()[0] // 2, 1750))

pygame.image.save(base_image, output)

# while True:
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             break
