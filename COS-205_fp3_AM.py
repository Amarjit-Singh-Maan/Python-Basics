# Amarjit Maan
# COS 205, Python Programming
# Problem # 3

def LeapYearChk(mm,dd,yyyy):
    if yyyy%100==0:
        if yyyy%400==0:
            return("LeapYear")
        else:
            return ("NoLeapYear")
    else:
            return("LeapYear")

def DayCalc(check,mm,dd):
    dayNum = 31*(mm-1) + dd
    if mm > 2:
        dayNum -= int((4*mm + 23 )/10)
    if check == "LeapYear" and mm > 2:
        dayNum += 1
    return(dayNum)

#First check at least date is entered in asked format
Month30Days = [4,6,9,11]
Month31Days = [1,3,5,7,8,10,12]
dayNum=0
EnteredDate = input("Enter the date: ")
if len(EnteredDate)==10:
    mm=int(EnteredDate.split("/")[0])
    dd=int(EnteredDate.split("/")[1])
    yyyy=int(EnteredDate.split("/")[2])
    if(yyyy>999):
        if mm>0 and mm<=12:
            if yyyy%4==0:
                FlagVal=(LeapYearChk(mm,dd,yyyy))
                if FlagVal=="IncorrectDate":
                    print("Not a valid date")
                else:
                    print(DayCalc(FlagVal,mm,dd))
            else:
                if mm in Month30Days:
                    if dd>0 and dd<=30:
                        print(DayCalc("CorrectDate",mm,dd))
                    else:
                        print("Not a valid date")
                elif mm in Month31Days:
                    if dd>0 and dd<=31:
                        print(DayCalc("CorrectDate",mm,dd))
                    else:
                        print("Not a valid date")
                elif(mm==2):
                    if dd>0 and dd<=28:
                        print("Correct Date")
                        print(DayCalc("CorrectDate",mm,dd))
        else:
            print("Not a valid date")
else:
    print("Not a valid date")
