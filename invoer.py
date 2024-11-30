def IntInput(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Voer een getal in")

def StringInput(prompt):
	while True:
		invoer = input(prompt)
		try:
			int(invoer.strip())
			print("Voer een string in, geen getal.")
		except:
			return invoer
