import pygame.mixer
pygame.mixer.init()
from pygame.mixer import Sound

sound = Sound(".//muziek voor galgje//normale_muziek.mp3")
sound2 = Sound(".//muziek voor galgje//normale_muziek2.mp3")
sound3 = Sound(".//muziek voor galgje//normale_muziek3.mp3")
sound4 = Sound(".//muziek voor galgje//normale_muziek4.mp3")
sound5 = Sound(".//muziek voor galgje//normale_muziek5.mp3")

pad_muziek_opstarten = r".\muziek voor galgje\opstarten_muziek.mp3"


def speel_muziek_opstarten():
	geluid_opstarten = pygame.mixer.Sound(pad_muziek_opstarten)
	geluid_opstarten.play(-1,fade_ms=2000)#fade in=2s

