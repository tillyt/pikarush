import csv
import sys

'''
Run this python script in Terminal: "python csv2edn.py Fall2014RushEvents.csv"
(change to whatever the actual rush events csv file is)
Be sure the csv file is in the format:
Name,Location,Description,row[3] Time
name 1,location 1,description 1,row[3] 1,starttime 1, endtime 1
name 2,location 2,description 2,row[3] 2,starttime 2, endtime 2
name 3,location 3,description 3,row[3] 3,starttime 3, endtime 3
In the spreadsheet, row[3]s need to be like 9/1 and times need to be like 13:00 (Go to Format --> Number in Google Drive)
'''


def main():
	readfile = sys.argv[1]
	writefile = sys.argv[1][:-4]+'.edn'

	with open(readfile, 'rb') as f:
		reader = csv.reader(f)
		header = reader.next()
		rows = [row for row in reader]

	infos = []
	for row in rows:
		# print row
		# google drive sux, dates like '9/1' need to be '09/01'
		#gonna put the leading month zero in later, this is just to fix the lack of leading day zero
		if len(row[3]) < 4:
			if len(row[3]) == 3:
				row[3] = row[3][0:2]+str(0)+row[3][2]


		info = "{:name \"%s\" \n :location \"%s\" \n :description \"%s\" \n :date \"0%s\" \n :time  [\"%s\",\"%s\"]} \n \n" % tuple(row)
		infos.append(info)

	ff = open(writefile, 'w')
	ff.write("[")
	for info in infos:
		ff.write(info)
	ff.write("]")
	ff.close()


if __name__ =='__main__':
	main()
