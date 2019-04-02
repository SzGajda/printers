import csv
class printer:
	def __init__(self, model, type , quantity):
		self.model = model
		self.type = type
		self.quantity = quantity
	def info(self):
		x = "Model: " + self.model + "; \t\t\tType: " + self.type + "; \t\t\tHow much: " + str(self.quantity)
		return x
	def more(self):
		self.quantity += 1

line_counter = 0
printers = []
model=""
history=[]
d=1
f=0

print('Repeating printers\n\n')
with open('Pulpit/glpi.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=';')
	for row in readCSV:
		model=row[5]
		if model not in history:
			if (line_counter == 0):
				line_counter += 1
			else:
				printers.append(printer(row[5],row[4], d))
				history.append(row[5])
				d=1
				line_counter += 1
		else:
			line_counter += 1
			x = line_counter - 2
			m = row[5]
			print('\t\t' + str(x) + '\t' + row[5] + '\t' + str(history.index(row[5])))
			printers[history.index(row[5])].ile += 1

print('\n\n\nDRUKARKI I ILE ICH JEST\n')
c = 0
for i in printers:
	print(printers[c].info())
	c+=1
