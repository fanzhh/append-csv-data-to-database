#! /usr/bin/python
#-*- coding:utf-8 -*-

import sys
import os.path
import psycopg2
import csv

DBNAME = 'your database name'
USER = 'your user name'
PASSWORD = 'your password'
PORT = 5432 # default posgresql post is 5432

def append_csv(table_name, csv_file):
	try:
	  # Connect to Database
		conn = psycopg2.connect(database=DBNAME,user=USER,password=PASSWORD,port=PORT)
		conn.autocommit =True
	except:
		print "Cannot connect to db."
		sys.exit(0)
	cur = conn.cursor()
	with open(csv_file) as f:
	  # Suppose the delimiter is ',' and the quote char is '"' in csv file.
		reader = csv.reader(f,delimiter=',',quotechar='"')
		i = -1
		for row in reader:
			if i == -1:
			  # The csv file first row should contain the field names to be import
				field_list = ','.join(row)
				i += 1
				continue
			# Quoted each value before insert 
			value_list = ["'%s'" % r for r in row]
			value_list = ','.join(value_list)
			try:
			   cur.execute("insert into %s (%s) values(%s)" % (table_name, field_list, value_list))
			   i += 1
			except:
				print "Cannot insert value: %s" % value_list
	return i

if __name__ == "__main__":
  # The args should be: ImportData.py TableName CSVFile.csv
	if len(sys.argv) <=2:
		print "Cannot find the table name and csv file parameter."
		sys.exit(1)
	table_name = sys.argv[1] # Argv 1 is table name
	csv_file = sys.argv[2]   # Argv 2 is the csv file contain data to be imported
	# Determin the csv file exist or not
	if not os.path.isfile(csv_file):
		print "Cannot file the file: %s" % csv_file
		sys.exit(1)
	result = append_csv(table_name, csv_file)
	print "%d records appended." % result
		
