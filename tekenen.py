from turtle import *
straal_cirkel = 13
binnenhoek_armen = 70
lengte_armen = 22
binnenhoek_benen = 30
lengte_benen = 20

def initialiseer_turtle():
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

def teken_voet_en_paal():
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

def teken_hoofd():
	global straal_cirkel
	penup()
	goto(-100+40-straal_cirkel,100-15-straal_cirkel)
	pendown()
	begin_fill()
	circle(straal_cirkel)
	end_fill()

def teken_lichaam():
	global straal_cirkel
	penup()
	circle(straal_cirkel,90)#een vierde van een cirkel om op de juiste plek te eindigen.
	setheading(270)#draai naar beneden.
	pendown()
	forward(30)
	setheading(90)#draai naar boven
	forward(20)
	setheading(270)

def teken_eerste_arm():
	global binnenhoek_armen, lengte_armen
	left(180-binnenhoek_armen)
	forward(lengte_armen)
	left(180)
	forward(lengte_armen)

def teken_tweede_arm():
	setheading(binnenhoek_armen+90)#draai
	forward(lengte_armen)
	left(180)
	forward(lengte_armen)
	setheading(270)#draai naar beneden

def teken_been_bovenlichaam():
	forward(20)#afstand tussen armen en benen
	left(binnenhoek_benen)
	forward(lengte_benen)
	left(180)
	forward(lengte_benen)
	setheading(270)

def teken_tweede_been():
	right(binnenhoek_benen)
	forward(lengte_benen)
	left(180)
	forward(lengte_benen)
	setheading(270)

def teken_rood_kruis():
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