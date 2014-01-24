import csv
import datetime


########### Simulation Control Variables ###########

present = "PR"
absent = "AB"
first_half = "FH"
second_half = "SH"
half_day = "H"
half_day_time = 13
min_req_hours = 7
read_filename = "log_raw.csv"
write_filename = "log_processed.csv"

####################################################




### READ

ifile  = open(read_filename, "rb")
reader = csv.reader(ifile)


### WRITE

c = csv.writer(open(write_filename, "wb"))
c.writerow(["Date","ID","Swipes","Log In","Log Out","Difference","Total Swipes","Even","Status"])

rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        
        date = row[0]
        emp_id = row[1]
        swipes = row[2]
        split_swipes = swipes.split(",")
        total_swipes = len(split_swipes)
        status = ''
        even = 1 if (total_swipes % 2 == 0) else 0
        log_in = str(split_swipes[0])
        log_out = str(split_swipes[len(split_swipes)-1])
        

        if (total_swipes == 1 and split_swipes[0] == ''):
            #Absent
            status = absent
            log_in = log_out = diff = ''
            total_swipes = 0

        elif (total_swipes == 1 and split_swipes[0] is not ''):
            #One swipe only
            status = absent
            log_out = ''
            diff = ''

        else:
            diff = round(((( datetime.datetime.strptime(log_out, '%H:%M') - datetime.datetime.strptime(log_in, '%H:%M') ).total_seconds() / 60) / 60),2)
            if (diff >= min_req_hours):
                status = present
            elif (diff < min_req_hours and int(log_out.split(":")[0]) < half_day_time):
                status = first_half
            elif (diff < min_req_hours and int(log_in.split(":")[0]) > half_day_time):
                status = second_half
            elif (diff >= min_req_hours/2 and diff < min_req_hours):
                status = half_day


        ### Writing into CSV file
        c.writerow([date,emp_id,swipes,log_in,log_out,diff,total_swipes,even,status])

    rownum += 1

ifile.close()