import csv
class printer:
	def __init__(self, model, typ, ile):
		self.model = model
		self.typ = typ
		self.ile = ile
	def info(self):
		x = "Model: " + self.model + "; \t\t\tTyp: " + self.typ + "; \t\t\tIlosc: " + str(self.ile)
		return x
	def wiecej(self):
		self.ile += 1
#	def ile():
line_counter = 0
drukarki = []
model=""
historia=[]
d=1
f=0

print('POWTARZAJACE SIE DRUKARKI\n\n')
with open('Pulpit/glpi.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=';')
	for row in readCSV:
		model=row[5]
		if model not in historia:
			if (line_counter == 0):
				line_counter += 1
			else:
				drukarki.append(printer(row[5],row[4], d))
				historia.append(row[5])
				d=1
				line_counter += 1
		else:
			line_counter += 1
			x = line_counter - 2
			m = row[5]
			print('\t\t' + str(x) + '\t' + row[5] + '\t' + str(historia.index(row[5])))
			drukarki[historia.index(row[5])].ile += 1





print('\n\n\nDRUKARKI I ILE ICH JEST\n')


#print(drukarki[0].info())
c = 0
for i in drukarki:
	print(drukarki[c].info())
	c+=1
#nazwa = ""
#nazwa += model
#model = row[5]
#typ = row[4]
#nazwa = printer(model, typ)
#modtyp[row[5]]=row[4]
#modele.append(row[5])
#line_counter += 1





#Nazwa objektu - Model - row[5]
#	Atrybuty obiektu
#		Typ
#			row[4]
#		Potrzebne kolory
#			jesli typ taki taki lub taki tyle kolorow
#			jesli inny to tyle
#		Ile razy sie powtarza
#			func()
#	Metody
#		Na powtarzanie sie
#
