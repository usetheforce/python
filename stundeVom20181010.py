### Python-Kurs

# Datentypen:
# 	Zahlen --> Ziffern
#	Text --> "..." 
#	Listen --> [1,"Text",[1,2]]
#	Wahrheitswert --> True oder False
if False:
	print (5) # Zahl
	print ("Sepp") # Text
	print ([1,"Text",[1,2]]) # Liste

# Operatoren fuer Zahlen
#	+, -, * (mal), / (geteilt), (...) (Klammern)
if False:
	print ( (5+5-2)*4/2 )

# Operatoren fuer Text
#	+ (Aneinanderhaengen)
#	*<Zahl> (Text vervielfachen)
#	[<Zahl>] (Text ausschneiden)
#	<Text> in <Text> (Test, ob enthalten)
if False:
	print ( "Ein Text"+" und noch ein Text")
	print ( "Ein Text "*10 )
	print ( "Ein Text "[4] )
	print ( "Ein Text "[4:7] ) # vom 5. bis zum 7. Buchstaben
	print ( "Ein Testtext"[4:-1] ) # -1: bis zum vorletzten
	print ( "Ein Testtext"[4:] ) # bis zum Ende
	print ( "Text" in "Ein Text " )
	print ( "@" in "josefmeier@mail.de" )
	print ( "@" in "josefmeier(AT)mail.de" )

# Operatoren fuer Listen
#	[<Zahl>] (Inhalt ausschneiden)
#	<Inhalt> in <Liste> (Test, ob enthalten)
if True:
	print ( [1,"Text",2,"Noch ein Text"][-1] )
	print ( [1,"Text",2,"Noch ein Text"][1:3] )
	print ( "Text" in [1,"Text",2,"Noch ein Text"] ) # True
	print ( 5 in [1,"Text",2,"Noch ein Text"] ) # False
	print ( "Noch" in [1,"Text",2,"Noch ein Text"] ) # False

for x in ["Meier","Mueller","Huber","Schmidt"]:
	print x
	# Aufgabe: bei Meier "Gruess Gott Herr " vor den Namen schreiben

#for x in [1,2,3,4,5]: # Schleife
#	print ( x+100 )
#	if x==3: # Verzweigung
#		print ( "Das war eine " )