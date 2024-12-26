#Hier en daar zijn er nog tests of debugging lijnen te vinden die nu niets meer doen.
#Er wordt vaak print("\n") gebruikt, dit om alineas te vormen.
print("Vergeet zeker niet om uw geluid aan te zetten, op die manier kunt u de muziek horen.")
print("Die start binnen enkele seconden.")
#print("voor import")
import asyncio as a;from threading import Thread
from tkinter import Tk,Label
import nltk; from nltk.corpus import stopwords
from time import sleep, time;from numpy import subtract;from random import randint
from turtle import *
import sys
import nltk
from nltk.corpus import stopwords
import pygame
pygame.mixer.init()

from music import start_speel_muziek_normaal, speel_muziek_opstarten, speel_muziek_verloren, speel_muziek_gewonnen, stop_muziek_opstarten
from utils import print_tekst
from instructies import *
from tekenen import *

antwoorden_nee = frozenset(["neen","neen.","nee.","nee"])
antwoorden_ja = frozenset(["ja","ja.","zeker","zeker.","natuurlijk"])

eerste_run = True
print_woord = False #testen
print("Wil je dat de woorden geprint worden?")
invoer_print_woord = input("druk op enter voor nee of typ {ja} of {nee}    ")
match invoer_print_woord.strip().lower():
	case "ja":
		print_woord = True
		print("De woorden zullen geprint worden.")
	case _:
		print_woord = False
		print("De woorden zullen niet geprint worden.")
	
eerste_print = True
set_spaties = frozenset([1, 2, 3, 4, 5])
klaar_s_w = False
klaar_w = False
eerste_start = True
volledige_lijst_woorden = {}
gewonnen = False
spaties = ['']
spatie = ''
bestaat = False
bezig_andere_muziek = False
gemiddelde_tijd_opstarten = 3
verboden_karakters = ["^",'|', '<', '>',"&",",","#","_",";",*[str(i) for i in range(10)]]

def download_w():
	global nederlandse_woorden, klaar_w
	from list_words import nederlandse_woorden
	klaar_w = True

def download_s_w():
	global nederlandse_stopwoorden, klaar_s_w
	nltk.download('stopwords',quiet=True)
	nederlandse_stopwoorden = frozenset(stopwords.words('dutch'))     
	klaar_s_w = True

Thread(target = speel_muziek_opstarten,daemon=True).start()

klaar = False
		 
def kies_woord():
	global woord, volledige_lijst_woorden, maxlengte, spatie_toegelaten, verboden_karakters, print_woord
	woord = ''
	
	while not woord:
		if klaar:
			woord = volledige_lijst_woorden.pop().lower()
			while len(woord)>maxlengte or any(c in verboden_karakters for c in woord): #controleer op lengte en op verboden karakters, verander van woord indien nodig
				woord = volledige_lijst_woorden.pop().lower()
			
	if print_woord:
		print(woord)
	for i in range(4):
		print("\n")
	if eerste_print:
		print("eerste spel:")
	else:
		print("volgende spel:")
	print("\nHet woord dat je moet raden is",len(woord),"karakters lang.\n")

def importeer():
	global volledige_lijst_woorden, klaar, klaar_s_w, klaar_w, nederlandse_woorden, aantal_verloren,nederlandse_stopwoorden
	Thread(target = download_s_w, daemon=True).start()
	Thread(target = download_w, daemon=True).start()
	
	aantal_verloren=0

	while not volledige_lijst_woorden:
		if klaar_s_w and klaar_w:
			
			volledige_lijst_woorden = set(nederlandse_stopwoorden|nederlandse_woorden)
			
			klaar=True

Thread(target=importeer, daemon=True).start()

maxlengte = None
while maxlengte is None:#De keer waarin de maximumlengte en de rest worden ingesteld is de laatste run van de loop.
	if klaar:
			print("bijna klaar...")
			print("\n")
			
			if eerste_print:
				print_tekst(maxlengte_tuple,0.15,0.01)
			else:
				print_tekst(maxlengte_tuple,0.07,0.005)
				
			maxlengte = None
			while maxlengte is None:#zolang niet gedefinieerd
				print("Druk op enter om de limiet in te stellen op 50 karakters.")
				maxlengte = input("Geef de maximum lengte van de woorden of woordgroepen die je wilt raden in.    ")
				if not maxlengte:
					maxlengte = 50
					print("Limiet ingesteld op 50.")
					break
				elif maxlengte==0:
					print("De limiet moet groter zijn dan 0.")
				try:
					maxlengte = int(maxlengte)
					break #versnel een beetje
				except:
					print("string of float ingegeven, geef een integer")
			print("\n")#nieuwe lijn
			
			if eerste_print:
				print_tekst(tuple_moeilijkheidsgraad,0.1,0.005)
			else:
				print_tekst(tuple_moeilijkheidsgraad,0.3,0.01)
					
			aantal_kansen = None
			while aantal_kansen is None:#zolang niet ingesteld
				try:
					print("Als je op enter drukt(zonder iets in te geven) , blijft het 8 en heb je dus acht kansen, dat is de standaard.")
					aantal_kansen = input("Geef de moeilijkheidsgraad in de vorm van het aantal kansen dat je wenst in.     ").strip()#mag hier nog niet crashen, anders werkt de if in except niet.
					if not aantal_kansen:
						aantal_kansen=8
						print("De standaard waarde werd ingesteld(8)")
						break# sla de volgende lijn over.
					aantal_kansen = int(aantal_kansen)
					
					
					if aantal_kansen%2==0:
						print("De waarde werd ingesteld op:",str(aantal_kansen))
					else:
						aantal_kansen = None
						continue
				except:
					aantal_kansen="1"
					if not aantal_kansen:
						aantal_kansen=8
						print("De standaard waarde werd ingesteld(8)")
						break# sla de volgende lijn over.
					print("Geef een veelvoud van 2 in.")
			term_stadium_vermeerderen = 8/aantal_kansen
			print("\n")
		
		   
print("Dit zijn de verboden_karakters:",verboden_karakters)
print("Deze karakters komen dus niet voor in de woorden of woordgroepen, het heeft dan ook geen zin om deze in te geven.")
print("\n")

def maxlengte_wijzigen():
	global maxlengte
	print("\n")
	print_tekst(maxlengte_tuple,0.02,0.005)
	
	maxlengte = None
	while maxlengte is None:#zolang niet gedefinieerd
		print("Druk op enter om de limiet in te stellen op 50 karakters.")
		maxlengte = input("Geef de maximum lengte van de woorden of woordgroepen die je wilt raden in.    ")
		if not maxlengte:
			maxlengte = 50
			print("Limiet ingesteld op 50.")
			break
		elif maxlengte==0:
			print("De limiet moet groter zijn dan 0.")
		try:
			maxlengte = int(maxlengte)
			break
		except:
			print("string of float ingegeven, geef een integer")
	print("De maximumlengte werd ingesteld op",maxlengte)
	print("\n")#nieuwe lijn

def herstart():
	global geluid_opstarten,eerste_run,woord,huidig_deel, stadium,einde, gemeenschappelijke_karakters, gem_lijst, reeds_geprobeerde_karakters, geraden_deel, reeds_geprobeerde_karakters, eerste_start, gewonnen, eerste_print, lijst_al_getekend
	
	#turtle blijft op dezelfde plaats, voor het tekenen gaat hij steeds naar het midden (-100,0)
	if eerste_start:
		pensize(3)
		pencolor("green")
		eerste_start = False
	else:
		clear()#verwijder de tekening van de galg. turtle.reset is het in feite, aleen wordt de plaats en ori�ntatie niet veranderd
		
		if not gewonnen:
			print("Dit was het woord dat je moest raden:",woord)
			
		for i in range(3):
			print("\n")#laat 6 lijnen open voor nieuw spel
	
	if eerste_run:
		Thread(target=start_speel_muziek_normaal,daemon=True,args=(bezig_andere_muziek,)).start()
		sleep(0.7)#overgang
		stop_muziek_opstarten()
		eerste_run = False
		
	woord = ''
	geraden_deel = ''
	kies_woord()
	stadium = 0
	huidig_deel = ""
	einde = False
	gewonnen = False
	gemeenschappelijke_karakters = 0

	gem_lijst = []
	reeds_geprobeerde_karakters = []
	lijst_al_getekend = []
	
	if eerste_print:
		print_tekst(algemene_info_verzameling,0.15,0.025)
		eerste_print = False
	else:#print sneller als de instructies al gelezen konden worden bij de start van het programma.
		print_tekst(algemene_info_verzameling,0.01,0.001)

	print("\n\n:", end="")#laat lijn open
	for i in range(len(woord)):
		print("_",end="")
	print("\n")

def bepaal_gemeenschappelijk(invoer):
	global huidig_deel,gemeenschappelijke_karakters, woord, gem_lijst, geraden_deel, gewonnen, reeds_geprobeerde_karakters
	gem_lijst = []
	gemeenschappelijke_karakters = 0
	geraden_deel = ':'
	huidig_deel += ''.join([i for i in invoer if i in woord])
	for c in huidig_deel:
		for b in woord:
			if c==b and c not in gem_lijst:
				aantal = woord.count(c)#hoeveel keer komt de waarde van c voor in woord
				gem_lijst.append(c)
				gemeenschappelijke_karakters += aantal
				
	if gemeenschappelijke_karakters>0:
		print("Je hebt ondertussen al",gemeenschappelijke_karakters,"karakter(s) geraden.")
	else:
		print("Je hebt helaas nog geen enkel karakter geraden. Een tandje bijsteken wordt sterk aangeraden.")
		
	for h in woord:# bereken de tekst om te tonen, inclusief underscores
		if h in gem_lijst:
			geraden_deel += h
		else:
			geraden_deel += "_"
	print(geraden_deel)
	if  gemeenschappelijke_karakters==len(woord):
		gewonnen = True

	for i in range(2): print("\n")
		
def root_verloren_verberg():
	global root_verloren, bestaat
	try:
		root_verloren.withdraw()
		print("na withdraw")
		bestaat = True
	except:
		print("excepted in root_verloren")
		bestaat = False

verloren = True  # Globale variabele om de staat van het venster bij te houden

def toon_scherm_verloren():
	global verloren, root_verloren, bestaat
	
	Thread(target=speel_muziek_verloren,daemon=True).start()

	lettertype_verloren = ("new times roman", 40)
	
	if verloren:
		if bestaat:
			root_verloren.deiconify()
		else:
			root_verloren = Tk()
			
			root_verloren.attributes("-fullscreen", True)
			root_verloren.config(bg="white")
			
			label_verloren = Label(root_verloren, fg="red", bg="white", font=lettertype_verloren, text="Je hebt helaas verloren")
			label_verloren.place(rely=0.5, relx=0.3)
			
			
			bestaat = True
			
		
		root_verloren.update()
		root_verloren.attributes("-fullscreen", True)
		sleep(7)
		root_verloren.attributes("-fullscreen", False)
		root_verloren.withdraw()
		bestaat = True
		verloren = False
	else:
		try:
			root_verloren.withdraw()
			bestaat = False
		except:
			pass

	if root_verloren is not None:
		try:
			root_verloren.mainloop()
		except:
			pass
		
		
def verhoog_snelheid_bij_herhaling(lijst_al_getekend:list,stadium:float,aantal_kansen:int,stadium_te_tekenen:float):
	if stadium_te_tekenen in lijst_al_getekend:
		speed(0)#hoogste snelheid, traagst: 1, snel:10, snelst: 0 of alle getallen groter dan 10
	else:
		speed(2)#traagst
		lijst_al_getekend.append(stadium_te_tekenen)#hierna is het wel getekend.
	
def stel_penkleur_in(penkleur:str):
	pencolor(penkleur)
	
def verander_penkleur(penkleur):
	stel_penkleur_in(penkleur)

def teken():
	global stadium, einde, gewonnen, aantal_verloren, verloren, aantal_resterende_pogingen, aantal_kansen, lijst_al_getekend
	#haakjes zijn vaak optioneel, maar staan er voor de duidelijkheid
	#Door de bewerkingen niet te vereenvoudigen blijft het ook duidelijker. (meerdere keer hetzelfde in plaats van schijnbaar verschillende bewerkingen)
	initialiseer_turtle()

	STADIA_PER_DEEL = aantal_kansen / 8
	
	# Dictionary met tekenfuncties en hun eigenschappen
	teken_stadia = {
		1: {"functie": teken_voet_en_paal, "kleur": "green", "grens": STADIA_PER_DEEL},
		2: {"functie": teken_hoofd, "kleur": "green", "grens": 2 * STADIA_PER_DEEL},
		3: {"functie": teken_lichaam, "kleur": "green", "grens": 3 * STADIA_PER_DEEL},
		4: {"functie": teken_eerste_arm, "kleur": "yellow", "grens": 4 * STADIA_PER_DEEL},
		5: {"functie": teken_tweede_arm, "kleur": "yellow", "grens": 5 * STADIA_PER_DEEL},
		6: {"functie": teken_been_bovenlichaam, "kleur": "orange", "grens": 6 * STADIA_PER_DEEL},
		7: {"functie": teken_tweede_been, "kleur": "red", "grens": 7 * STADIA_PER_DEEL},
	}
	
	initialiseer_turtle()
	huidige_stadium_waarde = stadium * STADIA_PER_DEEL
	
	# Teken de delen van de hangman
	for stadium_nummer, eigenschappen in teken_stadia.items():
		if huidige_stadium_waarde >= eigenschappen["grens"]:
			verhoog_snelheid_bij_herhaling(lijst_al_getekend, stadium, aantal_kansen, stadium_nummer)
			verander_penkleur(eigenschappen["kleur"])
			eigenschappen["functie"]()
	if huidige_stadium_waarde >= aantal_kansen :
		verwerk_verloren_spel()

def verwerk_verloren_spel():
	global einde, gewonnen, verloren, aantal_verloren
	verander_penkleur("red")
	teken_rood_kruis()
	sleep(3)
	
	einde = True
	gewonnen = False
	verloren = True
	
	# Start thread voor verloren scherm
	thread_verloren = Thread(target=toon_scherm_verloren, daemon=True)
	try:
		thread_verloren.start()
		sleep(8)
		thread_verloren.stop()
		thread_verloren.join()
	except:
		print(f"Je hebt verloren, je hebt al {aantal_verloren} keer verloren")
	finally:
		aantal_verloren += 1
	
def opnieuw_spelen():
	global gewonnen, ja_nee, antwoorden_ja,antwoorden_nee
	
	if gewonnen:
		print("Op naar de volgende prijs!")
		Thread(target=speel_muziek_gewonnen,daemon=True).start()
		gewonnen = False
	elif gewonnen and not einde:
		print("Niet getreurd, je zal nog kansen krijgen.")
	
	while True:
		sleep(2)
		print("Druk op enter voor ja of geef {ja} of {nee} in.")
		ja_nee = input("Wil je opnieuw spelen?    ").strip().lower()
			
		if ja_nee in antwoorden_ja:
			hoofdprogramma()

		elif ja_nee in antwoorden_nee:
			print("Ik sta steeds paraat als je nog eens wilt spelen!")
			print("Tot een volgende keer!")
			break
		else:
			print("?")
			ja_nee = None
	
def opnieuw_spelen_aangepast():
	global gewonnen, ja_nee, antwoorden_ja,antwoorden_nee
	
	if gewonnen:
		print("Op naar de volgende prijs!")
		Thread(target=speel_muziek_gewonnen,daemon=True).start()
		gewonnen = False
	elif not gewonnen and not einde:
		print("Niet getreurd, je zal nog kansen krijgen.")
	hoofdprogramma()

def lees_karakter():
	global reeds_geprobeerde_karakters, einde, geprobeerd_woord, gemeenschappelijke_karakters, stadium, gewonnen

	if reeds_geprobeerde_karakters:#een lege lijst printen heeft geen zin!
		print("Deze letters heb je al geprobeerd:",reeds_geprobeerde_karakters)
	
	while True:
		invoer = input("geef een karakter in dat je wilt uitproberen   ").strip().lower()

		if invoer.startswith(":"):
			verwerk_woord_invoer(invoer)
			break

		if invoer in ["stop","herstart","maxlengte"]:
			verwerk_commando(invoer)
			if invoer == "herstart":
				continue
			break

		if not is_geldig_karakter(invoer):
			continue

		if invoer in reeds_geprobeerde_karakters:
			print("je hebt dit karakter al geprobeerd")
			print("Deze letters heb je al geprobeerd.",reeds_geprobeerde_karakters)
			continue
		else:
			reeds_geprobeerde_karakters.append(invoer)
			break
	return invoer

def verwerk_woord_invoer(invoer):
	global geprobeerd_woord, woord, einde, gewonnen, gemeenschappelijke_karakters
	geprobeerd_woord = invoer.split(":")[1].strip()
	print("Je woord is uitgetest.")
	if geprobeerd_woord==woord:
		print("Je hebt gewonnen! Het woord was", woord)
		print("Je hebt het volgende woord juist geraden:",woord)
		gemeenschappelijke_karakters = len(woord)
		einde = True
		gewonnen = True # initialisatie voor volgende poging
		opnieuw_spelen()
	else:
		print("Dit is niet het woord dat we zoeken")
		print("probeer opnieuw")
		verhoog_stadium()
		teken()

def verwerk_commando(invoer):
	global einde
	if invoer == "stop":
		verwerk_stop()
	elif invoer == "herstart":
		hoofdprogramma()
	elif invoer == "maxlengte":
		maxlengte_wijzigen()
		lees_karakter()

def verwerk_stop():
	global einde
	from inputimeout import inputimeout, TimeoutOccurred
	print("  ")
	try:
		inputimeout(prompt='Druk op een willekeurige toets binnen de 5 seconden als je toch wilt herstarten  ', timeout=5)
		opnieuw_spelen_aangepast()
	except TimeoutOccurred:
		print('Ik sluit af. Tot de volgende keer.')
		sys.exit()

def is_geldig_karakter(invoer):
	if len(invoer) > 1:
		print(f"De invoer is te lang: {len(invoer)} karakters.")
		return False

	if any(karakter in verboden_karakters for karakter in invoer):
		print("Verboden karakter ingevoerd.")
		return False

	return True

def verhoog_stadium():
	global stadium, term_stadium_vermeerderen
	stadium += term_stadium_vermeerderen

def print_aantal_resterende_pogingen():
	global aantal_kansen, term_stadium_vermeerderen, stadium,aantal_resterende_pogingen
	aantal_resterende_pogingen = round((8-stadium)*(aantal_kansen/8))
	if aantal_resterende_pogingen>0:
		print("Bijgevolg resten je nog",str(aantal_resterende_pogingen),"poging(en)")

def hoofdprogramma():
	global einde, huidig_deel, stadium, gewonnen, gemeenschappelijke_karakters, woord, stadium, term_stadium_vermeerderen, aantal_kansen, antwoorden_ja,antwoorden_nee
	herstart()# wordt een keer uitgevoerd
	while gemeenschappelijke_karakters < len(woord) and not gewonnen and not einde:
		invoer = lees_karakter()
	
		if einde:
			break

		if invoer in woord:
			print("Het woord bevat de gegeven letter("+str(invoer)+"); je bent goed bezig.")
			print("Je huidige stadium is onveranderd en dus :", round(stadium*aantal_kansen/8))
			print_aantal_resterende_pogingen()
		else:
			verhoog_stadium()
			teken()
			print("Het te zoeken woord bevat de letter ("+str(invoer) +") die je net hebt ingegeven helaas niet.")
			print("Je huidige stadium is veranderd en dus :", round(stadium*aantal_kansen/8))
			print_aantal_resterende_pogingen()
	
		bepaal_gemeenschappelijk(invoer)
	else:
		if gewonnen or gemeenschappelijke_karakters==len(woord):
			print("Je hebt gewonnen!!")
			print("Je hebt het volgende woord geraden:",woord)
			gewonnen = True# initialisatie voor volgende poging
			opnieuw_spelen()
		else:
			print("Je hebt helaas verloren.   ")
			print("het woord was:", woord)
			gewonnen = False
			opnieuw_spelen()
		
hoofdprogramma()