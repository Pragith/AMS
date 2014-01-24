import random
import datetime
import csv


########### Simulation Control Variables ###########

hours_range = [9,21]
minutes_range = [0,60]
swipes_range = [0,15]
emp_ids_range = [1,1001]
start = datetime.date(2012,01,01) ### Format - YYYY,MM,DD
end = datetime.date(2013,12,31)
filename = "log_raw.csv"

####################################################








############### Calculating difference in dates ###############

def date_range(start, end):
    r = (end+datetime.timedelta(days=1)-start).days
    return [start+datetime.timedelta(days=i) for i in range(r)]
 

dateList = date_range(start, end)
dates = []

for date in dateList:
	if (date.isoweekday() != 6 and date.isoweekday() != 7):
		dates.append(date)


###############################################################



############### Generating Entries For Every Day ###############

#fo = open(filename, "w")

f = csv.writer(open(filename, "wb"))
f.writerow(["Date","ID","Swipes"])

for day in range(0,len(dates)):

	########### Generating Entries For Every Employee ###########

	log = []
		
	for emp_id in range(emp_ids_range[0],emp_ids_range[1]):
		emp_id = str(emp_id).zfill(4)

		### Generating Random Swipes
		swipes = []
		swipe_count = random.choice(range(swipes_range[0],swipes_range[1]))

		for n in range(0,swipe_count):
			time = str(random.choice(range(hours_range[0],hours_range[1]))).zfill(2) + ':' + str(random.choice(range(minutes_range[0],minutes_range[1]))).zfill(2)			
			swipes.append(time)

		swipes = sorted(swipes)
		swipes = ','.join(swipes)

		###

		#log = '"'+str(dates[day])+'","DU'+emp_id+'","'+swipes+'"'
		f.writerow([dates[day],"DU"+emp_id,swipes])

		#fo.write(log)
		#fo.write("\n")

	####################################################

#fo.close()

##################################################################
