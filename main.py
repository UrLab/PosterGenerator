import pygame
from sys import argv

pygame.init()
times_font = pygame.font.Font("assets/LEMONMILK-Medium.otf", 60)
talks_font = pygame.font.Font("assets/GlacialIndifference-Bold.otf", 60)

if len(argv) > 1:
    output = argv[1]
else:
    output = "a"

text1 = "Des conférences sur la technologie et"
text2 = "l'informatique tous les premiers"
text21 = "lundis du mois à 18h30"
text3 = "Plus d'infos sur : https://urlab.be/sm"
text4 = "Nous contacter ? contact@urlab.be"

base_image = pygame.image.load("assets/Smartmonday brain.png")
size = base_image.get_size()

urlab = pygame.image.load("assets/urlabLogo.png")
qrCode = pygame.image.load("assets/QRSM.png")
ci = pygame.image.load("assets/cerkinfoLogo.png")

urlab = pygame.transform.scale(urlab, (urlab.get_size()[0] * 0.5, urlab.get_size()[1] * 0.5))
qrCode = pygame.transform.scale(qrCode, (256, 256))
ci = pygame.transform.scale(ci, (ci.get_size()[0] * 0.1, ci.get_size()[1] * 0.1))

date_text = times_font.render(text1, True, (0, 0, 0))
text2_text = times_font.render(text2, True, (0, 0, 0))
text21_text = times_font.render(text21, True, (0, 0, 0))
text3_text = talks_font.render(text3, True, (0, 0, 0))
text4_text = talks_font.render(text4, True, (0, 0, 0))

base_image.blit(base_image, (0, 0))

#base_image.blit(urlab, (size[0] // 2 - urlab.get_size()[0] // 2, 1800))
#base_image.blit(qrCode, (size[0] // 2 - qrCode.get_size()[0] // 2, 0))
#base_image.blit(ci, (size[0] // 2 - ci.get_size()[0] // 2, 0))

base_image.blit(date_text, (size[0] // 2 - date_text.get_size()[0] // 2, 1600))
base_image.blit(text2_text, (size[0] // 2 - text2_text.get_size()[0] // 2, 1680))
base_image.blit(text21_text, (size[0] // 2 - text21_text.get_size()[0] // 2, 1760))
base_image.blit(text3_text, (size[0] // 2 - text3_text.get_size()[0] // 2, 2050))
base_image.blit(text4_text, (size[0] // 2 - text4_text.get_size()[0] // 2, 2120))

pygame.image.save(base_image, output)

