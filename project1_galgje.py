
#Hier en daar zijn er nog tests of debugging lijnen te vinden die nu niets meer doen.
#Er wordt vaak print("\n") gebruikt, dit om alineas te vormen.
print("Vergeet zeker niet om uw geluid aan te zetten, op die manier kunt u de muziek horen.")
print("Die start binnen enkele seconden.")
#print("voor import")
import asyncio as a;from threading import Thread
from tkinter import Tk
import nltk; from nltk.corpus import stopwords
from time import sleep, time;from numpy import subtract;from random import randint
from turtle import*
#print("na import")
antwoorden_nee=frozenset(["neen","Neen.","Nee.","Neen","nee","Nee"])
antwoorden_ja=frozenset(["Ja","ja","Ja.","zeker","Zeker","Zeker."])

eerste_run=True
print_woord=False #testen
print("Wil je dat de woorden geprint worden?")
invoer_print_woord=input("druk op enter voor nee of typ {ja} of {nee}    ").lower()
if invoer_print_woord==''or invoer_print_woord.strip().lower()=="nee":
    print_woord:bool=False
    print("De woorden zullen niet geprint worden.")
elif invoer_print_woord.strip().lower=="ja":
    print_woord=True
    print("De woorden zullen geprint worden.")
    
eerste_print=True
set_spaties=frozenset([1, 2, 3, 4, 5])
klaar_s_w=False
klaar_w=False
eerste_start=True
volledige_lijst_woorden={}
gewonnen=False
spaties=['']
spatie=''
bestaat=False
bezig_andere_muziek=False

#alles voor pygame: door de supplementaire code komen er geen nutteloze woorden in de uitvoer. 
#Er zou pygame ce geprint worden.
import os
import sys

    
stderr = sys.stderr
stdout = sys.stdout

sys.stderr = open(os.devnull, 'w')
sys.stdout = open(os.devnull, 'w')

    
import pygame

sys.stderr = stderr
sys.stdout = stdout
    
pygame.mixer.init()


for i in range(20):
    spatie+=' '
    spaties.append(spatie)

verboden_karakters = ["^",'|', '<', '>',"&",",","#","_",";"]

def speel_muziek_opstarten():
    global geluid_opstarten
    pad_muziek_opstarten=r".\muziek voor galgje\opstarten_muziek.mp3"
    geluid_opstarten = pygame.mixer.Sound(pad_muziek_opstarten)
    geluid_opstarten.play(-1,fade_ms=2000)#fade in=2s
thread_muziek_opstarten=Thread(target=speel_muziek_opstarten,daemon=True)
thread_muziek_opstarten.start()

def laden_stopwoorden():
    global nederlandse_stopwoorden, klaar_s_w
    nederlandse_stopwoorden = frozenset(stopwords.words('dutch'))     
    klaar_s_w=True
    
def laden_woorden():
    global nederlandse_woorden, klaar_w
    from list_words import nederlandse_woorden
    klaar_w=True

thread_stopwoorden=Thread(target=laden_stopwoorden, daemon=True)
thread_woorden=Thread(target=laden_woorden, daemon=True)

def download_w():
    global thread_woorden
    
    thread_woorden.start()

def download_s_w():
    global thread_stopwoorden
    nltk.download('stopwords',quiet=True)
    thread_stopwoorden.start()
    
thread_download_stopwoorden=Thread(target=download_s_w, daemon=True)
thread_download_woorden=Thread(target=download_w, daemon=True)
    
klaar=False
#sleep(4)
def aftellen():
    global root_opstarten, aftellen_label, tijd, tijdverschil
    tijd_wachten=0.5
    while not klaar_s_w or not klaar_w:
        try:
            tijdverschil=subtract(time(),tijd)
            tijd_tot_opgestart=round(subtract(6,tijdverschil))
            
            if tijd_tot_opgestart<0:
                aftellen_label.config(text="Het gaat niet helemaal zoals gepland, een onverwachte vertraging deed zich voor, het opstarten kan nog iets langer duren.")
                aftellen_label.config(fg="red")
                sleep(2)
                if klaar_w and klaar_s_w:#e
                    break
                sleep(2)
                if klaar_w and klaar_s_w:#e
                    break
                aftellen_label.config(text="bijna klaar.")
                sleep(tijd_wachten)
                aftellen_label.config(text="bijna klaar..")
                sleep(tijd_wachten)
                aftellen_label.config(text="bijna klaar...")
                sleep(tijd_wachten)
                if klaar_w and klaar_s_w:#e
                    break
                aftellen_label.config(text="bijna klaar....")
                sleep(tijd_wachten)
                aftellen_label.config(text="bijna klaar.....")
                sleep(tijd_wachten)
                aftellen_label.config(text="bijna klaar......")
            elif tijd_tot_opgestart<2:
                aftellen_label.config(fg="green")
            else:
                aftellen_label.config(fg="white")
                
            if tijd_tot_opgestart>0:
                aftellen_label.config(text="nog "+str(tijd_tot_opgestart)+" seconden wachten a.u.b.")
                if klaar_w and klaar_s_w:#e
                    break
                
        except:
            
              print("Er liep iets mis, mogelijk leidt dit tot problemen.")
              print("Meestal vormt dit echter geen probleem.")
              
    else:
         try:
            root_opstarten.attributes("-fullscreen",False)#Mag maar een keer worden uitgevoerd
            root_opstarten.destroy()#Dit mag meerdere keren worden uitgevoerd.
         except:
            print("De GUI werd gesloten, dit is normaal. Indien er problemen waren, zijn ze nu opgelost.")
def label_aanpassen():
    global opstarten_label, klaar_s_w,klaar_w, aftellen_label, tijd, tijdverschil, vooruitgang_label
    tijd_tussen_veranderen=0.4
    thread_aftellen=Thread(target=aftellen,daemon=True)
    thread_aftellen.start()
    getoond_klaar_s_w=False
    getoond_klaar_w=False
    sleep(1)
    while not klaar_s_w or not klaar_w:
        if klaar_s_w==True and getoond_klaar_s_w!=True:
            vooruitgang_label.config(text="Alle veelgebruikte Nederlandse woorden zijn geladen.")
        if klaar_w==True and getoond_klaar_w!=True:
            vooruitgang_label.config(text="Alle Nederlandse woorden zijn geladen.(Ook de minder gebruikte woorden.)")
        
            
        try:
            opstarten_label.config(text="opstarten.    ")
            sleep(tijd_tussen_veranderen)
            sleep(tijd_tussen_veranderen)
            
            opstarten_label.config(text="opstarten..   ")
            sleep(tijd_tussen_veranderen)
            opstarten_label.config(text="opstarten...  ")
            sleep(tijd_tussen_veranderen)
           
            opstarten_label.config(text="opstarten.... ")
            sleep(tijd_tussen_veranderen)
            opstarten_label.config(text="opstarten.....")
            sleep(tijd_tussen_veranderen)
            
            opstarten_label.config(text="opstarten......")
            sleep(tijd_tussen_veranderen)
        except:
            break
        
         
    else:
        try:
            root_opstarten.attributes("-fullscreen",False)
            root_opstarten.destroy()
        except:
            print("De GUI werd gesloten, dit is normaal.")
        


thread_labels=Thread(target=label_aanpassen, daemon=True)
def even_geduld():
    global win,vooruitgang_label, opstarten_label, root_opstarten, lettertype, klaar_s_w, klaar_w, tijd, aftellen_label,hoek,hoek_start,cirkels,cirkels_hoeken, root_opstarten, straal_cirkel,canvas
    tijd=time()
    lettertype=("new times roman",20)
    
    print("even geduld alstublieft...")
    from tkinter import Label, Tk
    print("Het programma is aan het opstarten...")
    print("Je woorden worden bijeen geraapt...")
    root_opstarten=Tk()
    root_opstarten.attributes("-fullscreen",True)
    root_opstarten.configure(bg="dark blue")
    opstarten_label=Label(root_opstarten,text="opstarten...  (Normaal duurt dit ongeveer 6 seconden)",bg="dark blue", font=lettertype,fg="white",wraplength=500)
    opstarten_label.place(relx=0.3,rely=0.5)
    tijd_tot_opgestart=0
    aftellen_label=Label(root_opstarten,text="nog ongeveer "+str(tijd_tot_opgestart)+" wachten",bg="dark blue", font=lettertype,fg="white",wraplength=500)
    aftellen_label.place(relx=0.2,rely=0.6)
    vooruitgang_label=Label(root_opstarten,text="vooruitgang: de Nederlandse woorden zijn aan het laden", font=("new times roman",13),fg="white",bg="dark blue",wraplength=300)
    vooruitgang_label.place(relx=0.7,rely=0.8)
    
    
    thread_labels.start()
    
    root_opstarten.mainloop()
         
    
thread_geduld=Thread(target=even_geduld, daemon=True)
def kies_woord():
    global woord, volledige_lijst_woorden, maxlengte, spatie_toegelaten, verboden_karakters, print_woord
    woord=''
    
    while woord=="":
        if klaar==True:
            woord=volledige_lijst_woorden.pop().lower()
            while len(woord)>maxlengte:
                woord=volledige_lijst_woorden.pop().lower()
                
            for b in woord:
                item=b
                if item in verboden_karakters:
                    woord=volledige_lijst_woorden.pop().lower()
            if spatie_toegelaten==False:
                if b in spaties:
                    woord=volledige_lijst_woorden.pop().lower()
    if print_woord:
        print(woord)
    for i in range(4):
        print("")
    if eerste_print:
        print("eerste spel:")
    else:
        print("volgende spel:")
    print("\n")
    print("Het woord dat je moet raden is",len(woord),"karakters lang.")
    print("\n")

def declareer_muziek_normaal():
    global  sound, sound2,sound3,sound4,sound5
    
    
    pad_muziek_normaal=r".\muziek voor galgje\normale_muziek.mp3"
    sound = pygame.mixer.Sound(pad_muziek_normaal)
    pad_muziek_normaal2=r".\muziek voor galgje\normale_muziek2.mp3"
    sound2 = pygame.mixer.Sound(pad_muziek_normaal2)
    pad_muziek_normaal3=r".\muziek voor galgje\normale_muziek3.mp3"
    sound3 = pygame.mixer.Sound(pad_muziek_normaal3)
    pad_muziek_normaal4=r".\muziek voor galgje\normale_muziek4.mp3"
    sound4 = pygame.mixer.Sound(pad_muziek_normaal4)
    pad_muziek_normaal5=r".\muziek voor galgje\normale_muziek5.mp3"
    sound5 = pygame.mixer.Sound(pad_muziek_normaal5)
    

def start_speel_muziek_normaal():
    a.run(speel_muziek_normaal())
    print("start muziek_normaal")
    
async def speel_muziek_normaal():
    global sound, sound2,sound3,sound4,sound5
    
    #deze functie staat in feite in een while-lus.
    while True:
        
        willekeurig_getal=randint(1,5)
        if not bezig_andere_muziek:
            try:
                if willekeurig_getal==1:
            
                    sound.play(1,fade_ms=2000)#1 wilt zeggen 1 keer afspelen
                    await a.sleep(68) 
                    sound.stop()
       
                if willekeurig_getal==2:
                    sound2.play(1,fade_ms=2000)
                    await a.sleep(100)
                    sound2.stop()
                    
                if willekeurig_getal==3:
                    sound3.play(1,fade_ms=2000)
                    await a.sleep(84)
                    sound3.stop()    
            
                if willekeurig_getal==4:
                    sound4.play(1,fade_ms=2000)
            
                    await a.sleep(62)
                    sound4.stop()
                    
                if willekeurig_getal==5:
                    sound5.play(1,fade_ms=2000)
                    await a.sleep(154)
                    sound5.stop()
                    
                if not bezig_andere_muziek:
                    continue
                else:
                    await a.sleep(10)
                    continue
                    
            except Exception as e:
                print("in except",e)
                declareer_muziek_normaal()#voornamelijk voor de eerste keer bedoeld.
                await a.sleep(4)
                continue
        else:
            await a.sleep(10)
            
            
        
def importeer():
    global win,volledige_lijst_woorden, klaar, thread_geduld, klaar_s_w, klaar_w, thread_download_stopwoorden, thread_download_woorden, nederlandse_woorden, aantal_verloren
    thread_geduld.start()
    declareer_muziek_normaal()
    thread_download_stopwoorden.start()
    thread_download_woorden.start()
    
    
    
    tijd_voor_laden=time()
    aantal_verloren=0
    
    


    while  volledige_lijst_woorden=={}:
        
        if klaar_s_w and klaar_w:
            
            volledige_lijst_woorden = set(nederlandse_stopwoorden|nederlandse_woorden)
            
            klaar=True
            
    tijd_na_laden=subtract(time(),tijd_voor_laden)
    #print(tijd_na_laden)

thread_import=Thread(target=importeer, daemon=True)

thread_import.start()
maxlengte=0
while maxlengte==0:#De keer waarin de maximumlengte en de rest worden ingesteld is de laatste run van de loop.
    if klaar==True:
            from time import sleep
            print("bijna klaar...")
            print("\n")
            tekst_maximumlengte="Waarschuwing: De langste woorden bevatten MEER DAN 30 karakters."
            tekst2_maximumlengte="Herhaling: de langste woorden bevatten MEER DAN 30 karakters, dit zijn bijgevolg ook moeilijke woorden."
            maxlengte_tuple=tekst_maximumlengte,tekst2_maximumlengte,"  "
            if eerste_print:
                for i in maxlengte_tuple:
                    for c in i:
                        print(c,end="")
                        sleep(0.01)
                    print("\n")
                    sleep(0.15)
            else:
                
                for i in maxlengte_tuple:
                    for c in i:
                        print(c,end="")
                        sleep(0.005)
                    print("\n")
                    sleep(0.07)
            maxlengte=0
            while maxlengte==0:#zolang niet gedefinieerd
                print("Druk op enter om de limiet in te stellen op 50 karakters.")
                maxlengte=input("Geef de maximum lengte van de woorden of woordgroepen die je wilt raden in.    ")
                if maxlengte=="":
                    maxlengte=50
                    print("Limiet ingesteld op 50.")
                    break
                elif maxlengte==0:
                    print("De limiet moet groter zijn dan 0.")
                try:
                    maxlengte=int(maxlengte)
                    break #versnel een beetje
                except:
                    maxlengte=0
                    print("string of float ingegeven, geef een integer")
            print("\n")#nieuwe lijn
            
            lijn1_term="Het aantal kansen dat je krijgt bepaalt de moeilijkheidsgraad."
            lijn2_term="Kies uit alle veelvouden van 2: 2,4,6,8,..."
            if eerste_print:
                for f in lijn1_term,lijn2_term:
                    for d in f:
                        print(d,end="")
                        sleep(0.005)
                    print("\n")
                    sleep(0.1)
            else:
                for f in lijn1_term,lijn2_term:
                    for d in f:
                        print(d,end="")
                        sleep(0.01)
                    print("\n")
                    sleep(0.3)
                    
            aantal_kansen="1"
            while aantal_kansen=="1":#zolang niet ingesteld
                try:
                    print("Als je op enter drukt(zonder iets in te geven) , blijft het 8 en heb je dus acht kansen, dat is de standaard.")
                    aantal_kansen=input("Geef de moeilijkheidsgraad in de vorm van het aantal kansen dat je wenst in.     ").strip()#mag hier nog niet crashen, anders werkt de if in except niet.
                    if str(aantal_kansen)=="":
                        aantal_kansen=8
                        print("De standaard waarde werd ingesteld(8)")
                        break# sla de volgende lijn over.
                    aantal_kansen=int(aantal_kansen)
                    
                    
                    if aantal_kansen%2==0:
                        print("De waarde werd ingesteld op:",str(aantal_kansen))
                    else:
                        aantal_kansen="1"
                        continue
                except:
                    aantal_kansen="1"
                    if aantal_kansen=="":
                        aantal_kansen=8
                        print("De standaard waarde werd ingesteld(8)")
                        break# sla de volgende lijn over.
                    print("Geef een veelvoud van 2 in.")
            term_stadium_vermeerderen=8/aantal_kansen
            print("\n")
        
           
spatie_toegelaten="niet toegelaten"
print("Woordgroepen komen zelden voor")
print("druk op enter voor standaard: {geen woordgroepen}")
sleep(0.3)
while spatie_toegelaten=='niet toegelaten':#zolang de variabele nog niet gedefinieerd is.
    if klaar==True:
        antwoord=input("Mag het een woordgroep zijn?   ")
        
        if antwoord.strip().lower() in antwoorden_ja:
            spatie_toegelaten=True
        elif antwoord.strip().lower() in antwoorden_nee or antwoord=="":
            spatie_toegelaten=False
            
        else:
            print("Wat bedoel je? Antwoord met ja of nee.")
if not spatie_toegelaten:
    verboden_karakters.append(' ')
print("Dit zijn dan de verboden_karakters:",verboden_karakters)
print("Deze karakters komen dus niet voor in de woorden of woordgroepen, het heeft dan ook geen zin om deze in te geven.")
print("\n")

def maxlengte_wijzigen():
    global maxlengte
    from time import sleep
    print("\n")
    tekst_maximumlengte="Waarschuwing: De langste woorden bevatten MEER DAN 30 karakters."
    tekst2_maximumlengte="Herhaling: de langste woorden bevatten MEER DAN 30 karakters, dit zijn bijgevolg ook moeilijke woorden."
   
    
                
    for i in tekst_maximumlengte,tekst2_maximumlengte:
        for c in i:
            print(c,end="")
            sleep(0.005)
        print("\n")
        sleep(0.02)
    
    maxlengte=0
    while maxlengte==0:#zolang niet gedefinieerd
        print("Druk op enter om de limiet in te stellen op 50 karakters.")
        maxlengte=input("Geef de maximum lengte van de woorden of woordgroepen die je wilt raden in.    ")
        if maxlengte=="":
            maxlengte=50
            print("Limiet ingesteld op 50.")
            break
        elif maxlengte==0:
            print("De limiet moet groter zijn dan 0.")
        try:
            maxlengte=int(maxlengte)
            break #versnel een beetje
        except:
            maxlengte=0
            print("string of float ingegeven, geef een integer")
    print("De maximumlengte werd ingesteld op",maxlengte)
    print("\n")#nieuwe lijn
def herstart():
    global geluid_opstarten,eerste_run,woord,huidig_deel, stadium, invoer,einde, gemeenschappelijke_karakters, gem_lijst, lijst, geraden_deel, lijst, eerste_start, verder, gewonnen, eerste_print, lijst_al_getekend
    
    from time import sleep
    
    

    
    #turtle blijft op dezelfde plaats, voor het tekenen gaat hij steeds naar het midden (-100,0)
    if eerste_start==True:
        pensize(3)
        pencolor("green")
        eerste_start=False
    else:
        clear()#verwijder de tekening van de galg. turtle.reset is het in feite, aleen wordt de plaats en oriëntatie niet veranderd
        
        if gewonnen==False:
            print("Dit was het woord dat je moest raden:",woord)
            
        for i in range(5):
            print(" ")#laat 5 lijnen open voor nieuw spel
    if eerste_run:
        
        thread_muziek_normaal=Thread(target=start_speel_muziek_normaal,daemon=True)
        thread_muziek_normaal.start()#start met normale muziek te spelen!!
        sleep(0.7)#overgang
        geluid_opstarten.stop()
        eerste_run=False
        
    woord=''
    geraden_deel=''
    kies_woord()
    stadium=0
    invoer=""
    huidig_deel=""
    einde=False
    verder=True
    gewonnen=False
    gemeenschappelijke_karakters=0

    gem_lijst=[]
    lijst=[]
    lijst_al_getekend=[]
    
    lijn1="eindig programma door stop op eender welk moment te typen."
    lijn2="herstart door herstart te typen, dan krijg je het woord dat je moest raden ook te zien."
    extra_tussen_lijn1_lijn2="verander de maximumlengte van de woorden die je wilt raden door {maxlengte} te typen"
    lijn3="Je mag hoofdletters gebruiken, maar die hebben geen effect."
    lijn4="Wanneer je een gok wilt doen naar het woord, dan begin je met : en schrijf je daarachter het woord dat je denkt dat het is."
    lijn5="Bijvoorbeeld: Als je schoen wilt raden, dan typ je {:schoen}."
    lijn6="De plaatsen van alle overeenkomende karakters worden geprint."
    lijn7="Iedere underscore betekent een karakter of spatie die nog niet geraden is."
    lijn8="De woorden zijn zowel afkomstig uit het alledaagse leven als uit het ICT domein."
    lijn9="Andere specifieke domeinen komen niet aan bod."
    lijn10="De woorden kunnen zowel makkelijk als moeilijk zijn."
    lijn11="Alle woorden die trema's of accenten bevatten zijn inbegrepen."
    lijn12="Houd er rekening mee dat die geraden moeten worden zonder de accenten."
    lijn13="Opmerking: Hoe snel de tekst wordt geprint is omgekeerd evenredig met hoe aandachtig je de tekst zou moeten lezen. "
    lijn14="Dit werd echter enkel in de mate van het mogelijke gerealiseerd."
    lijn15="m.a.w. De tekst die aandachtig gelezen moet worden verschijnd trager dan de tekst waar er diagonaal door gelezen mag worden."
    lijn16="Zowel bij winst als bij verlies wordt er een liedje afgespeeld."
    lijn17="Sommige woorden zijn overigens afkomstig uit Nederland of worden hoofdzakelijk gebruikt in Nederland."
    lijn18="De woorden kunnen vervoegingen van werkwoorden bevatten."
    algemene_info_verzameling=lijn1,lijn2,"  ",lijn3,lijn4,lijn5,"  ",lijn6,lijn7,"  ", lijn8,lijn9, lijn10, lijn11, lijn12,"  ", lijn13, lijn14,lijn15, lijn16,"  ", lijn17, lijn18
    if eerste_print:
        from time import sleep #Normaal wordt er aan het begin geimporteerd, maar dit spaart tijd.
        for i in algemene_info_verzameling:
            for b in i:
                print(b,end="")
                sleep(0.025)
            sleep(0.15)
        eerste_print=False
    else:#print sneller als de instructies al gelezen konden worden bij de start van het programma.
        for i in algemene_info_verzameling:
            for b in i:
                print(b,end="")
                sleep(0.001)
            sleep(0.01)
    
    print("\n\n")#laat lijn open
    print(":", end="")
    for i in range(len(woord)):
        print("_",end="")
    print("\n")
def bepaal_gemeenschappelijk():
    global huidig_deel,gemeenschappelijke_karakters, woord, gem_lijst, geraden_deel, gewonnen, lijst
    gem_lijst=[]
    gemeenschappelijke_karakters=0
    geraden_deel=':'
    for c in huidig_deel:
        for b in woord:
            if c==b and c not in gem_lijst:
                aantal=woord.count(c)#hoeveel keer komt de waarde van c voor in woord
                gem_lijst.append(c)
                gemeenschappelijke_karakters+=aantal
                
    if gemeenschappelijke_karakters>0:          
        print("Je hebt ondertussen al",gemeenschappelijke_karakters,"karakter(s) geraden.")
    elif gemeenschappelijke_karakters==0:
        print("Je hebt helaas nog geen enkel karakter geraden. Een tandje bijsteken wordt sterk aangeraden.")
    try:
        if gemeenschappelijke_karakters>len(woord)/2 and invoer in woord:
            print("Je bent goed bezig, meer dan halfweg met het raden, doe zo verder!")
    except:
        pass
        
    for h in woord:# bereken de tekst om te tonen, inclusief underscores
        if h in gem_lijst:
        
            geraden_deel+=h
        else:
            geraden_deel+="_" 
                
    if  gemeenschappelijke_karakters==len(woord):
        gewonnen=True
    for i in range(2):
        print("\n")
    print(geraden_deel)
    
def stel_penkleur_in(penkleur:str):
    global win
    pencolor(penkleur)
    
def verander_penkleur(penkleur):
    global stadium
    stel_penkleur_in(penkleur)
def pauzeer_normale_muziek(duurtijd:int):
    
    global sound,sound2, sound3, sound4, sound5, bezig_andere_muziek
    
    sound.stop()
    sound2.stop()
    sound3.stop()
    sound4.stop()
    sound5.stop()
    
    bezig_andere_muziek=True
    sleep(duurtijd)
    bezig_andere_muziek=False
    
def speel_muziek_verloren():
    global sound, sound2,sound3,sound4,sound5
    from playsound import playsound
    pad=r".\muziek voor galgje\verloren_muziek.mp3"
    duurtijd=60+43
    thread_pauzeer_muziek=Thread(target=pauzeer_normale_muziek,args=(duurtijd,))
    thread_pauzeer_muziek.start()    
    playsound(pad,)
    
def speel_muziek_gewonnen():
    global sound, sound2, sound3, sound4,sound5
    from playsound import playsound
    pad=r".\muziek voor galgje\gewonnen_muziek.mp3"
    pad2=r".\muziek voor galgje\gewonnen_muziek2.mp3"
    # geeft geen error als het nog niet bezig is.  

    willekeurig_getal2=randint(1,2)
    if willekeurig_getal2==1:
        duurtijd=60+47
        thread_pauzeer_muziek=Thread(target=pauzeer_normale_muziek,args=(duurtijd,))
        thread_pauzeer_muziek.start()
        playsound(pad,)
        
    elif willekeurig_getal2==2:
        duurtijd=60+26
        thread_pauzeer_muziek=Thread(target=pauzeer_normale_muziek,args=(duurtijd,))
        thread_pauzeer_muziek.start()
        playsound(pad2,)
        
def root_verloren_verberg():
    global root_verloren, bestaat
    try:
        root_verloren.withdraw()
        print("na withdraw")
        bestaat=True
    except:
        print("excepted in root_verloren")
        bestaat=False

verloren = True  # Globale variabele om de staat van het venster bij te houden
from tkinter import Label, Tk, PhotoImage

def toon_scherm_verloren():
    global verloren, root_verloren, bestaat, thread_muziek_verloren
    
    thread_muziek_verloren=Thread(target=speel_muziek_verloren,daemon=True)#een thread stoppen is moeilijk.
    thread_muziek_verloren.start()
    lettertype_verloren = ("new times roman", 40)
    
    if verloren:
        if bestaat:
            root_verloren.deiconify()
        else:
            root_verloren = Tk()
            
            root_verloren.attributes("-fullscreen", True)
            root_verloren.config(bg="white")
            
            label_verloren = Label(root_verloren, fg="red", bg="white", font=lettertype_verloren, text="Je bent helaas verloren")
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
    

def teken():
    global stadium, einde, gewonnen, verder, aantal_verloren, verloren, aantal_resterende_pogingen,aantal_kansen, lijst_al_getekend
    #haakjes zijn vaak optioneel, maar staan er voor de duidelijkheid
    #Door de bewerkingen niet te vereenvoudigen blijft het ook duidelijker. (meerdere keer hetzelfde in plaats van schijnbaar verschillende bewerkingen)
    penup()
    speed(0)
    goto(-110,50)
    setheading(90)
    shape("turtle")
    stamp()
    shape("classic")
    
    goto(-100,0)
    setheading(0)#wijs naar rechts
    pendown()
    fillcolor("grey")
    if stadium*(aantal_kansen/8)>=aantal_kansen/8:
        stadium_te_tekenen=1
        verhoog_snelheid_bij_herhaling(lijst_al_getekend,stadium,aantal_kansen,stadium_te_tekenen)
        penkleur="green"
        verander_penkleur(penkleur)
        #voet
        forward(60)
        backward(100)
        forward(40)
        #paal
        left(90)
        forward(85)
        right(45)
        forward(pow((pow(15,2)+pow(15,2)),0.5))#stelling van pythagoras macht 0,5 is een vierkantswortel; hypothenusa
        left(90+45)
        forward(15)#rechthoekszijde
        left(90)
        forward(15)#rechthoekszijde
        right(180)
        forward(15)
        right(90)
        forward(40)
        right(90)
        forward(15)
    if stadium*(aantal_kansen/8)>=aantal_kansen/4:
        stadium_te_tekenen=2
        verhoog_snelheid_bij_herhaling(lijst_al_getekend,stadium,aantal_kansen,stadium_te_tekenen)
        penkleur="green"
        straal_cirkel=13
        verander_penkleur("green")
        penup()
        goto(-100+40-straal_cirkel,100-15-straal_cirkel)
        pendown()
        begin_fill()
        circle(straal_cirkel)
        end_fill()
    if stadium*(aantal_kansen/8)>=(aantal_kansen/8)*3:
        stadium_te_tekenen=3
        verhoog_snelheid_bij_herhaling(lijst_al_getekend,stadium,aantal_kansen,stadium_te_tekenen)
        penkleur="green"
        verander_penkleur("green")
        penup()
        circle(straal_cirkel,90)#een vierde van een cirkel om op de juiste plek te eindigen.
        setheading(270)#draai naar beneden.
        pendown()
        forward(30)
        setheading(90)#draai naar boven
        forward(20)
        setheading(270)
    if stadium*(aantal_kansen/8)>=(aantal_kansen/8)*4:
        stadium_te_tekenen=4
        verhoog_snelheid_bij_herhaling(lijst_al_getekend,stadium,aantal_kansen,stadium_te_tekenen)
        penkleur="yellow"
        verander_penkleur("yellow")
        binnenhoek_armen=70
        lengte_armen=22
        left(180-binnenhoek_armen)
        forward(lengte_armen)
        left(180)
        forward(lengte_armen)     
        
    if stadium*(aantal_kansen/8)>=(aantal_kansen/8)*5:
        stadium_te_tekenen=5
        verhoog_snelheid_bij_herhaling(lijst_al_getekend,stadium,aantal_kansen,stadium_te_tekenen)
        penkleur="yellow"
        verander_penkleur("yellow")
        setheading(binnenhoek_armen+90)#draai
        forward(lengte_armen)
        left(180)
        forward(lengte_armen)
        setheading(270)#draai naar beneden
        
    if stadium*(aantal_kansen/8)>=(aantal_kansen/8)*6:
        stadium_te_tekenen=6
        verhoog_snelheid_bij_herhaling(lijst_al_getekend,stadium,aantal_kansen,stadium_te_tekenen)
        penkleur="orange"
        verander_penkleur("orange")
        binnenhoek_benen=30
        forward(20)#afstand tussen armen en benen
        lengte_benen=20
        left(binnenhoek_benen)
        forward(lengte_benen)
        left(180)
        forward(lengte_benen)
        setheading(270)
        
    if stadium*(aantal_kansen/8)>=(aantal_kansen/8)*7:
        stadium_te_tekenen=7
        verhoog_snelheid_bij_herhaling(lijst_al_getekend,stadium,aantal_kansen,stadium_te_tekenen)
        penkleur="red"
        verander_penkleur("red")
        right(binnenhoek_benen)
        forward(lengte_benen)
        left(180)
        forward(lengte_benen)
        setheading(270)
        
    if stadium*(aantal_kansen/8)>=aantal_kansen:
        penkleur="red"
        verander_penkleur("red")
        penup()
        pensize(5)
        speed(0)
        goto(-20,-25)
        setheading(135)
        pendown()
        speed(3)
        forward(pow(pow(150,2)+pow(150,2),0.5))#stelling van pythagoras
        penup()
        setheading(270)
        forward(150)
        left(135)
        pendown()
        forward(pow(pow(150,2)+pow(150,2),0.5))#stelling van pythagoras
        penup()

        sleep(3)
        aantal_verloren+=1
        thread_verloren=Thread(target=toon_scherm_verloren,daemon=True)
        einde=True
        verder=False
        gewonnen=False # voeg toe op einde!!!
        verloren=True
        try:
            thread_verloren.start()
            sleep(9)
            thread_verloren.stop()
            #print("thread gestart")
            thread_verloren.join()
        except:
            print("Je bent verloren, je bent al",aantal_verloren,"keer verloren")
        finally:
            aantal_verloren+=1
    
def opnieuw_spelen():
    global gewonnen, ja_nee, antwoorden_ja,antwoorden_nee, thread_muziek_gewonnen
    
    if gewonnen==True:
        print("Op naar de volgende prijs!")
        thread_muziek_gewonnen=Thread(target=speel_muziek_gewonnen,daemon=True)#een thread stoppen is lastig
        thread_muziek_gewonnen.start()
        gewonnen=False
    elif gewonnen==False and einde!=True:
        print("Niet getreurd, je zal nog kansen krijgen.")
    
    ja_nee=""
    if True:
        while ja_nee=="" or ja_nee==None:
            #print("in loop")
            sleep(2)
            print("Druk op enter voor ja of geef {ja} of {nee} in.")
            ja_nee=input("Wil je opnieuw spelen?    ")
            
            if ja_nee.strip().lower() in antwoorden_ja or ja_nee=="":
                hoofdprogramma()
            elif ja_nee.strip().lower() in antwoorden_nee:
                print("Ik sta steeds paraat als je nog eens wilt spelen!")
                print("Tot een volgende keer!")
                break#voor de duidelijkheid
            else:
                print("?")
                ja_nee=""
    
def opnieuw_spelen_aangepast():
    global gewonnen, ja_nee, antwoorden_ja,antwoorden_nee, thread_muziek_gewonnen
    
    if gewonnen==True:
        print("Op naar de volgende prijs!")
        thread_muziek_gewonnen=Thread(target=speel_muziek_gewonnen,daemon=True)#een thread stoppen is lastig
        thread_muziek_gewonnen.start()
        gewonnen=False
    elif gewonnen==False and einde!=True:
        print("Niet getreurd, je zal nog kansen krijgen.")
    hoofdprogramma()

def lees_karakter():
    global lijst, invoer, einde, geprobeerd_woord, gemeenschappelijke_karakters, stadium, gewonnen
    if lijst:#een lege lijst printen heeft geen zin!
        print("Deze letters heb je al geprobeerd:",lijst)
    
    verder=False
    invoer=""
    while len(str(invoer))!=1 or verder==True:
        try:
            invoer=input("geef een karakter in dat je wilt uitproberen   ").strip()
        except:
            invoer=""
            pass
        if not invoer.startswith(":"):
            
            if invoer.strip().lower()=="stop":
                 einde=True
                 
                 from inputimeout import inputimeout, TimeoutOccurred
                 print("  ")
                 try:
                    invoer_afsluiten = inputimeout(prompt='Druk op een willekeurige toets binnen de 5 seconden als je toch wilt herstarten  ', timeout=5)
                    opnieuw_spelen_aangepast()
                 except TimeoutOccurred:
                    print('Ik sluit af, je gaf niets in.')
                 print("Ik sta steeds paraat als je nog eens wilt spelen!")
                 print("Tot een volgende keer!")
                 sys.exit()#sluit af
            elif invoer.strip().lower()=="herstart":
                 hoofdprogramma()
                 continue#normaal kom je hier nooit.
            elif invoer.strip().lower()=="maxlengte":
                print("Je verzoek werd aangenomen.")
                maxlengte_wijzigen()
                lees_karakter()
                
            try:
            
                invoer=float(invoer)
                invoer=int(invoer)
                print("type float,int")
                lees_karakter()
                verder=True
            except:
            
                if len(invoer.strip())>1 and not invoer.startswith(":"):
                    if len(invoer)>10:
                        print("De ingevoerde string is veel te lang, die is namelijk",len(invoer),"karakters lang")
                    else:
                        print("De ingevoerde string is te lang, die is namelijk",len(invoer),"karakters lang")
                    
                    tekst_te_lang="Ben je zeker dat je niet {:"+invoer+"} bedoeld?"
                    tekst2_te_lang="Mischien wil je een woord raden."
                    for y in tekst_te_lang,tekst2_te_lang:
                        for x in y:
                            print(x,end="")
                            sleep(0.01)
                        sleep(0.15)
                        print("\n")#ga naar volgende lijn
                elif invoer in spaties and spatie_toegelaten==False:
                    if invoer!="":
                        print("Geef invoer.")
                    elif invoer=="":
                        print("Geef iets in!")
                    else:
                        print("Een spatie is niet toegestaan")
                else:
                    for f in invoer:
                        for c in verboden_karakters:
                            if f==c:
                                print("Dit karakter behoort tot de verboden karakters en kan dus niet voorkomen in het woord")
                invoer=invoer.strip().lower()
            if invoer in lijst:
                print("je hebt dit karakter al geprobeerd")
                print("Deze letters heb je al geprobeerd.",lijst)
                verder=True
                continue
            else:
                verder=False
            
        else:
            geprobeerd_woord=invoer.split(":")[1].strip()
            print("Je woord is uitgetest.")
            if geprobeerd_woord==woord:
                print("Je bent gewonnen!!")
                print("Je hebt het volgende woord juist geraden:",woord)
                gemeenschappelijke_karakters=len(woord)
                einde=True
                gewonnen=True# initialisatie voor volgende poging
                opnieuw_spelen()
                break
            else:
                print("Dit is niet het te zoeken woord")
                print("probeer opnieuw")
                stadium+=term_stadium_vermeerderen
                teken()
        if  len(str(invoer))==1 and invoer!="herstart" and invoer!="stop":
            try:
                float(invoer)# alternatieve manier om datatype te controleren
                int(invoer)
            except:
             lijst.append(invoer.strip().lower())#enkel wanneer er een string wordt ingegeven, wordt dit uitgevoerd.         
    
        
def print_aantal_resterende_pogingen():
    global aantal_kansen, term_stadium_vermeerderen, stadium,aantal_resterende_pogingen
    aantal_resterende_pogingen=round((8-stadium)*(aantal_kansen/8))
    if aantal_resterende_pogingen>0:
        print("Bijgevolg resten je nog",str(aantal_resterende_pogingen),"poging(en)")
        

def hoofdprogramma():
    global einde, huidig_deel, stadium, gewonnen, gemeenschappelijke_karakters, woord, invoer, stadium, term_stadium_vermeerderen, aantal_kansen, antwoorden_ja,antwoorden_nee
    herstart()# wordt een keer uitgevoerd
    while gemeenschappelijke_karakters<len(woord) and gewonnen!=True and einde!=True:
        lees_karakter()
    
        if einde==True:
            break
        try:
            for i in invoer:
                if i in woord:
                    huidig_deel+=i
        except:
            print("fout datatype, geef string!!")
        if huidig_deel!="":
            print("De letters die je al hebt ingegeven en in het woord voorkomen:",huidig_deel)
        try:
            if str(invoer) in str(woord):
                    print("Het woord bevat de gegeven letter("+str(invoer)+"); je bent goed bezig.")
                    print("Je huidige stadium is onveranderd en dus :", round(stadium*aantal_kansen/8))
                    print_aantal_resterende_pogingen()
            else:
                    stadium+=term_stadium_vermeerderen
                    teken()
                    print("Het te zoeken woord bevat de letter ("+str(invoer) +") die je net hebt ingegeven helaas niet.")
                    print("Je huidige stadium is veranderd en dus :", round(stadium*aantal_kansen/8))
                    print_aantal_resterende_pogingen()
        except:
            print("Geef een karakter of een woord.")

                
            
        bepaal_gemeenschappelijk()
    else:
        if gewonnen==True or gemeenschappelijke_karakters==len(woord):
            print("Je bent gewonnen!!")
            print("Je hebt het volgende woord geraden:",woord)
            gewonnen=True# initialisatie voor volgende poging
            opnieuw_spelen()
        else:
            print("Je bent helaas verloren.   ")
            print("het woord was:", woord)
            gewonnen=False
            opnieuw_spelen()
        
            
hoofdprogramma()