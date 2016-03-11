#!/bin/python
import csv

with open('blt_1_2_yr_olds.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	rows = list(reader)
	for row in rows:
	#for row in reader:
		row[4] = row[4].replace(',','')
with open('blt_out_1_2_yr_olds.csv', 'wb') as csvfile:
	  writer = csv.writer(csvfile)
	  writer.writerows(rows)
