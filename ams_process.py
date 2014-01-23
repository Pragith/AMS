'''
Date  |  ID  |  Log In  |  Log Out  |  Difference  |  Total Swipes  |  Even (1 for True)  |  Status  

Present	GT 8 hours	
Absent	0 hours	
FH	LT 8 hours	Time Out before 13:00
SH	LT 8 hours	Time In after 13:00

Date,ID,Swipes
2013-01-01,DU0001,"11:43,14:42,16:08,19:38"
2013-01-01,DU0002,"09:24,19:38"
2013-01-01,DU0005,10:57
2013-01-01,DU0013,

'''

import csv

read_filename = "log_raw.csv"
write_filename = "log_processed.csv"



### READ


ifile  = open(read_filename, "rb")
reader = csv.reader(ifile)

rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        date = row[0]
        emp_id = row[1]
        swipes = row[2]
        print date
        for value in row:        	
			heading = header[colnum]
			#print swipes
			#print '%-8s: %s' % (heading, value)
			colnum += 1
            
    rownum += 1

ifile.close()



### WRITE

c = csv.writer(open(write_filename, "wb"))

c.writerow(["Date","ID","Log In","Log Out","Difference","Total Swipes","Even","Status"])
c.writerow(["Name11","Address","Telephone","Fax","E-mail","Others"])