import csv
final=[]
class printer:
	def __init__(self, type, model , quantity):
		self.type = type
		self.model = model
		self.quantity = quantity
		#USTALANIE BLACK/CMYK
		if(self.type == "Igłowa"):
			self.color = "Black"
		elif(self.type == "Urządzenie laserowe monochromatyczne"):
			self.color = "Black"
		elif(self.type == "Urządzenie wielofunkcyjne monochromatyczne"):
			self.color = "Black"
		elif(self.type == "Urządzenie wielofunkcyjne kolorowe"):
			self.color = "CMYK"
		elif(self.type == "Urządzenie wielofunkcyjne kolorowe atramentowe"):
			self.color = "CMYK"
		else:
			self.color = "Color"
		#JEZELI BLACK TO BLACK I DODAJE 4 ELEMENTY DO LISTY OBIEKTOW
		if(self.color == "Black"):
			final.append(self.type)
			final.append(self.model)
			final.append(self.quantity)
			final.append(self.color)
		#JEZELI CMYK TO ROZBIJA NA 4 KOLORY I DODAJE 4*4=16 ELEMENTOW DO LISTY
		else:
			for i in range (4):
				cmyk = ['Cyan', 'Magenta', 'Yellow', 'Black']
				final.append(self.type)
				final.append(self.model)
				final.append(self.quantity)
				final.append(cmyk[i])
		#FUNKCJA POKAZUJACA WSZYSTKIE ATRYBUTY
	def info(self):
		if(self.color=="Black"):
			x = "Type: " + self.type + "; \tModel: " + self.model + "; \tHow many: " + str(self.quantity) + "; \tColor: " + self.color
		else:
			x = "Type: " + self.type + "; \tModel: " + self.model + "; \tHow many: " + str(self.quantity) + "; \tColor: Cyan"
			x += "\nType: " + self.type + "; \tModel: " + self.model + "; \tHow many: " + str(self.quantity) + "; \tColor: Magenta"
			x += "\nType: " + self.type + "; \tModel: " + self.model + "; \tHow many: " + str(self.quantity) + "; \tColor: Yellow"
			x += "\nType: " + self.type + "; \tModel: " + self.model + "; \tHow many: " + str(self.quantity) + "; \tColor: Black"
		return x
	def more(self):
		self.quantity += 1

line_counter = 0
printers = []
model=""
history=[]
d=1
f=0

#print('Repeating printers\n\n')
with open('Pulpit/glpi.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=';')
	for row in readCSV:
		model=row[5]
		if model not in history:
			if (line_counter == 0):
				line_counter += 1
			else:
				printers.append(printer(row[4],row[5], d))
				history.append(row[5])
				d=1
				line_counter += 1
		else:
			line_counter += 1
			x = line_counter - 2
			m = row[5]
			#print('\t\t' + str(x) + '\t' + row[5] + '\t' + str(history.index(row[5])))
			printers[history.index(row[5])].quantity += 1

print('\n\n\nDRUKARKI I ILE ICH JEST\n')
c = 0

for i in printers:
	print(str(printers[c].info()))
	c+=1
