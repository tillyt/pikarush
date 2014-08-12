import csv
import sys

'''
Run this python script in Terminal: "python csv2edn.py Fall2014RushEvents.csv"
(change to whatever the actual rush events csv file is)
Be sure the csv file is in the format:
Name,Location,Description,Date Time
name 1,location 1,description 1,date 1,starttime 1, endtime 1
name 2,location 2,description 2,date 2,starttime 2, endtime 2
name 3,location 3,description 3,date 3,starttime 3, endtime 3
'''


def main():
	readfile = sys.argv[1]
	writefile = sys.argv[1][:-4]+'.edn'

	with open(readfile, 'rb') as f:
		reader = csv.reader(f)
		header = reader.next()
		rows = [tuple(row) for row in reader]

	infos = []
	for row in rows:
		info = "{:name \"%s\" \n :location \"%s\" \n :description \"%s\" \n :date \"0%s\" \n :time  [\"%s\",\"%s\"]} \n \n" % row
		infos.append(info)

	ff = open(writefile, 'w')
	ff.write("[")
	for info in infos:
		ff.write(info)
	ff.write("]")
	ff.close()


if __name__ =='__main__':
	main()
