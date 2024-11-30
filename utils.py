import time
def print_tekst(alinea:list|tuple|set,wachttijd_tussen_regels,wachttijd_tussen_karakters):
	for regel in alinea:
		for karakter in regel:
			print(karakter,end="")
			time.sleep(wachttijd_tussen_karakters)
		print("\n")
		time.sleep(wachttijd_tussen_regels)