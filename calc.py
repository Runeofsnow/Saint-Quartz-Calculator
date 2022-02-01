#!bin/env/python3
import math
from datetime import date
import datetime
#Note predictions are based on the events projected for 2022 and 2023 and assume completion of events and login
#This also assumes a login over 300 to account for SQ from the 30 day bonus
#It does not account for download campaigns or movie bonuses as those are harder to predict placement
#There is some variability with the anniversary since the NA server's anniversary is on a different month
yweek=52

#find the current date
current_time = datetime.datetime.now()
#assign month, day and year to variables
year=current_time.year
month=current_time.month    
day= current_time.day

#calculate the week number
week=int(datetime.date(year, month, day).isocalendar()[1])

#Obtain the projected banner end date
tyr, tmon, tday = input("Enter the target year, month and day in numerical format and separated by commas ").split(",")
targetwk=int(datetime.date(int(tyr), int(tmon), int(tday)).isocalendar()[1])

#calculate the number of SQ at a projected period of time
initial=int(input("How many SQ do you have right now?\n"))
#print(initial)
#List the SQ per event 2022
if year==2022:
   Jan=95
   Feb=6
   Mar=23
   Apr=88
   May=19
   Jun=46
   Jul=369
   Aug=76
   Sept=2
   Oct=21
   Nov=17
   Dec=51
elif year==2023:
   Jan=43
   Feb=6
   Mar=20
   Apr=22
   May=28
   Jun=90
   Jul=520
   Aug=22
   Sept=18
   Oct=45
   Nov=34
   Dec=6

#prelim=initial
#if tyr==2022:
login=(initial+(targetwk-week)*5+30*((targetwk-week)/4))
#elif tyr==2023:
#    login=initial
#Add in the projected SQ from events that should occur during these months
#Does not include the month itself due to trying not to assume event completion
if month==1:
   prelim=login+Feb+Mar+Apr+May+Jun+Jul+Aug+Sept+Oct+Nov+Dec
elif month==2:
   prelim=login+Mar+Apr+May+Jun+Jul+Aug+Sept+Oct+Nov+Dec
elif month==3:
   prelim+Apr+May+Jun+Jul+Aug+Sept+Oct+Nov+Dec
elif month==4:
   prelim+May+Jun+Jul+Aug+Sept+Oct+Nov+Dec
elif month==5:
   prelim+Jun+Jul+Aug+Sept+Oct+Nov+Dec
elif month==6:
   prelim+Jul+Aug+Sept+Oct+Nov+Dec
elif month==7:
   prelim+Aug+Sept+Oct+Nov+Dec
elif month==8:
   prelim+Sept+Oct+Nov+Dec
elif month==9:
   prelim+Oct+Nov+Dec
elif month==10:
   prelim+Nov+Dec
elif month==11:
   prelim+Dec
elif month==12:
   prelim=login

#print(login)
#print(prelim)
#This asks for the completion of the month's event(s)
#Based on projections from the JP server
ans=input("Did you complete this month's event?(y/n)\n")
if ans=="n":
        if month=="1":
            total=prelim+Jan
        elif month=="2":
            total=prelim+Feb
        elif month=="3":
            total=prelim+Mar
        elif month=="4":
            total=prelim+Apr
        elif month=="5":
            total=prelim+May
        elif month=="6":
            total=prelim+Jun
        elif month=="7":
            total=prelim+Jul
        elif month=="8":
            total=prelim+Aug
        elif month=="9":
            total=prelim+Sept
        elif month=="10":
            total=prelim+Oct
        elif month=="11":
            total=prelim+Nov
        elif month=="12":
            total=prelim+Dec
elif ans=="y":
   total=prelim


print("You should have {} SQ by the target date" .format(total))
