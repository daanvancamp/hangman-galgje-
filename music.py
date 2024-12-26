import pygame.mixer
pygame.mixer.init()
from pygame.mixer import Sound
import asyncio as a
from random import randint
from playsound import playsound
from time import sleep
from threading import Thread


sound = Sound(".//muziek voor galgje//normale_muziek.mp3")
sound2 = Sound(".//muziek voor galgje//normale_muziek2.mp3")
sound3 = Sound(".//muziek voor galgje//normale_muziek3.mp3")
sound4 = Sound(".//muziek voor galgje//normale_muziek4.mp3")
sound5 = Sound(".//muziek voor galgje//normale_muziek5.mp3")

sounds = [sound,sound2,sound3,sound4,sound5]
length_sounds = [68,100,84,62,154]

pad_muziek_opstarten = r".\muziek voor galgje\opstarten_muziek.mp3"


def speel_muziek_opstarten():
	global geluid_opstarten
	geluid_opstarten = pygame.mixer.Sound(pad_muziek_opstarten)
	geluid_opstarten.play(-1,fade_ms=2000)#fade in=2s

def stop_muziek_opstarten():
	global geluid_opstarten
	geluid_opstarten.stop()

def start_speel_muziek_normaal(bezig_andere_muziek):
	a.run(speel_muziek_normaal(bezig_andere_muziek))
	print("start muziek_normaal")
	
async def speel_muziek_normaal(bezig_andere_muziek):
	global sound, sound2,sound3,sound4,sound5
	while True:
		if not bezig_andere_muziek:
			try:
				random_index = randint(0,4)
				sound_to_play = sounds[random_index]
				duration_of_sound = length_sounds[random_index]
				
				sound_to_play.play(1,fade_ms=2000)#1 wilt zeggen 1 keer afspelen
				await a.sleep(duration_of_sound)
				sound.stop()
					
				if not bezig_andere_muziek:
					continue
				else:
					await a.sleep(10)
					continue
					
			except Exception as e:
				print("in except",e)
				await a.sleep(4)
				continue
		else:
			await a.sleep(10)

def pauzeer_normale_muziek(duurtijd:int):
	
	global sound,sound2, sound3, sound4, sound5, bezig_andere_muziek
	
	sound.stop()
	sound2.stop()
	sound3.stop()
	sound4.stop()
	sound5.stop()
	
	bezig_andere_muziek = True
	sleep(duurtijd)
	bezig_andere_muziek = False
	
def speel_muziek_verloren():
	global sound, sound2,sound3,sound4,sound5

	pad = r".\muziek voor galgje\verloren_muziek.mp3"
	duurtijd = 60+43
	Thread(target=pauzeer_normale_muziek,args=(duurtijd,)).start()
	playsound(pad,)
	
def speel_muziek_gewonnen():
	global sound, sound2, sound3, sound4,sound5

	pad = r".\muziek voor galgje\gewonnen_muziek.mp3"
	pad2 = r".\muziek voor galgje\gewonnen_muziek2.mp3"
	bestandspaden = [pad,pad2]
	duurtijden = [60+47,60+26]

	idx = randint(0,1)
	willekeurig_pad = bestandspaden[idx]
	duurtijd = duurtijden[idx]
	Thread(target=pauzeer_normale_muziek,args=(duurtijd,)).start()
	playsound(willekeurig_pad,)

