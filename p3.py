import csv
def getData(str):
	data = []
	with open(str) as CSV_:
		d = csv.reader(CSV_, delimiter=',')
		for row in d:
			data.append(row)
#	print(data)
	return data

def Transpose(data):

        TOT = len(data[0])
        RES = []
        temp = []
        for x in range(TOT):
                temp.clear()
                for index, line in enumerate(data):
                        try:
                                temp.append(float(line[x]))
                        except:
                                temp.append(line[x])
                RES.append(temp.copy())
        return RES

def CheckComplete(inp):
	if(inp == "FALSE"):
		return 0
	else:
		return 1
def main():
	data = getData("TechSurvey-Survey.csv");
	data = Transpose(data)
	unanswered = 0
	NaPrio = 0
	NaPC = 0
	LPrio = 0
	LPC = 0
	MPrio = 0
	MPC = 0
	HPrio = 0
	HPC = 0
	#data[54] is my value
	for index, d in enumerate(data[54]):
		if(d == ''):
			#unansered, therefore automatically incomlete
			unanswered+=1
		if(d == 'Not a Priority'):
			NaPC+=CheckComplete(data[1][index])
			NaPrio+=1
		if(d == 'Low Priority'):
			LPC+=CheckComplete(data[1][index])
			LPrio+=1
		if(d == 'Medium Priority'):
			MPC+=CheckComplete(data[1][index])
			MPrio+=1
		if(d == 'High Priority'):
			HPC+=CheckComplete(data[1][index])
			HPrio+=1

	print("length of data: %5d" %(len(data[54])-1))
	print("unanswered: %9d" %(unanswered))
	print("Not a Priority: %5d" %(NaPrio))
	print("Low Priority: %7d" %(LPrio))
	print("Medium Priority: %4d" %(MPrio))
	print("High Priority: %6d" %(HPrio))
	print('---------------------')
	print('%'+"empty: %13.4f" %(unanswered/(len(data[54])-1)))
	print('%'+"Not a Priority that completed: %8.4f" %(NaPC/NaPrio))
	print('%'+"low Priority that completed: %10.4f" %(LPC/LPrio))
	print('%'+"medium Priority that completed: %7.4f" %(MPC/MPrio))
	print('%'+"high Priority that completed: %9.4f" %(HPC/HPrio))
main()
