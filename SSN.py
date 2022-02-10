def main():
    mySSN=input("Enter your SSN (###-##-####):- ")
    if len(mySSN) == numberDigits(mySSN) and isValidFormat(mySSN)==True:
        print("The SSN is VALID")
    else:
        print("The SSN is INVALID")

def numberDigits(str):
    count=2
    for n in range(0,len(str)):
        if str[n].isdigit():
            count=count + 1
    return count

def isValidFormat(str):
    if len(str)==11 and (str[3]=="-" and str[6]=="-"):
        valid=True
    else:
        valid=False
    return valid

main()
