
print "Kofi Dwomoh-Ababio\nWelcome to birthpress"
Fname=  raw_input("Please enter your first name :")
Sname=  raw_input("Please enter your last name :")
print "Please enter your date of birth??"
month=int(raw_input("Month(eg. 02,01,12...):"));year=raw_input("Year(eg. 2012...):");day=int(raw_input("day(eg. 31,22...):"))
if(month==1 or month==2):
    Fakemonth=month+10
else:
    Fakemonth=month-2
if(Fakemonth==11 or Fakemonth==12):
    pyear=int(raw_input("Enter previous year: "));
else:
    pyear=int(year);
weekday=""
A=Fakemonth
B=day
C=(pyear%100)
"""if(Fakemonth==11 or Fakemonth==12):
    C=C-1;"""

D=int(pyear/100)
W = (13*A - 1) / 5
X=C/4
Y=D/4
Z = W + X + Y + B + C - 2*D
R = Z%7
if(R<0):R=R+7;
if(R==0):
    weekday="Sunday"
elif(R==1):
    weekday="Monday"
elif(R==2):
    weekday="Tuesday"
elif(R==3):
    weekday="Wednesday"
elif(R==4):
    weekday="Thursday"
elif(R==5):
    weekday="Friday"
elif(R==6):
    weekday="Saturday"

    

print Fname+" "+Sname+" was born on a "+weekday
