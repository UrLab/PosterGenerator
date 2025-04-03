import pygame

pygame.init()
times_font = pygame.font.Font("assets/LEMONMILK-Medium.otf", 60)
talks_font = pygame.font.Font("assets/GlacialIndifference-Bold.otf", 60)

output = 'a'

text1 = "Des conférences sur la technologie et"
text2 = "l'informatique tous les premiers"
text21 = "lundis du mois à 18h30"
text3 = "Plus d'infos sur : https://urlab.be/sm"
text4 = "Nous contacter ? contact@urlab.be"

base_image = pygame.image.load("assets/Smartmonday brain.png")
size = base_image.get_size()
base_surface = pygame.Surface(size)
window = pygame.display.set_mode(size)

date = f"{text1}"
date_text = times_font.render(date, True, (0, 0, 0))
text2_text = times_font.render(text2, True, (0, 0, 0))
text21_text = times_font.render(text21, True, (0, 0, 0))
text3_text = talks_font.render(text3, True, (0, 0, 0))
text4_text = talks_font.render(text4, True, (0, 0, 0))

base_image.blit(base_image, (0, 0))
base_image.blit(date_text, (size[0] // 2 - date_text.get_size()[0] // 2, 1600))
base_image.blit(text2_text, (size[0] // 2 - text2_text.get_size()[0] // 2, 1680))
base_image.blit(text21_text, (size[0] // 2 - text21_text.get_size()[0] // 2, 1760))
base_image.blit(text3_text, (size[0] // 2 - text3_text.get_size()[0] // 2, 1950))
base_image.blit(text4_text, (size[0] // 2 - text4_text.get_size()[0] // 2, 2020))

pygame.image.save(base_image, output)

# while True:
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             break

