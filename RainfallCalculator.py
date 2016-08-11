# Declare initial variables to hold the entered and calculated rainfalls
totalRainfall = 0.00
monthRainfall = 0.00
averageWeekRainfall = 0.00
averageDayRainfall = 0.00
weeks = 0
totalDays = 0

#define list of strings with name of weekdays to iterate through
WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

#ask user to input number of weeks to calculate rainfall
#input validation - require number of weeks to be an integer greater than 0
while True:
	try:
		weeks = int(input('Enter the number of weeks which rainfall should be calculated: '))
		if weeks > 0:
			break
		else:
			print ('Number of weeks must be at least 1')
	except (ValueError):
		print ('Number of weeks must be an integer')

#first for loop iterates through number of weeks input by user	
for week in range(weeks):
#second for loop iterates through the 7 days of the week, asking the user to input rainfall for the day
#input validation - requires the rainfall amount to be a non-negative integer
	for day in range(7):
		while True:
			try:
				dayRainfall = int(input( \
				'Enter the amount of rain (in mm) for %s of week %s: ' %(WEEKDAYS[day], week+1)))
				if dayRainfall >= 0:
					break
				else:
					print ('Amount of rain must be non-negative')
			except (ValueError):
				print ('Amount of rain must be an integer')

#count the total number of days and rainfall				
		totalDays +=1
		totalRainfall += dayRainfall
		
#calculate the average daily and weekly rainfall from the data input by the user		
averageWeekRainfall = totalRainfall / weeks
averageDayRainfall = totalRainfall / totalDays

#print the values to the user, limiting averages to 2 decimal places
print ("\n")
print ('Total rainfall: ', int(totalRainfall), 'mm')
print ('Average rainfall per week: ', format(averageWeekRainfall, '.2f'), 'mm')
print ('Average rainfall per day: ', format(averageDayRainfall, '.2f'), 'mm')