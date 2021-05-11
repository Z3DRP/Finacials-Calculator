#!/user/bin/env python3
#Finacials... - Zach Palmer 3/25/21
#main file

import locale
from Annuity import Annuity as annuity
from Loan import Loan as loan
from FV import FutureValue as Fval


def getChoice():
    goodVal = False
    while not goodVal:
        try:
            choice = int(input("Select Operation: 1-Annuity, 2-Loan, 3-Future Value, 0-Quit : "))
            if choice not in range(0,4):
                print("Unknown Operation: Valid operations are 1,2,3 or 0")
            else:
                goodVal = True
        except ValueError:
            print("Illegal Input: valid ops are 0,1,2 and 3")
            goodVal = False
    return choice


def getValue(prompt,val_type):
    #valtype: 'i' = int, 'f' = float
    goodVal = False
    while not goodVal:
        try:
            if val_type.lower() == "i":
                value = int(input(prompt))
            else:
                value = float(input(prompt))
            goodVal = True
        except ValueError as ex:
            print(f"Illegal Value: {ex}")
            goodVal = False
    return value

def doAnnuity():
    amount = getValue("Monthly Deposit : ",'i')
    rate = getValue("Annual Interest Rate (6.5% = 6.5) : ",'f')
    term = getValue("Term in months : ", 'i')
    Annuity = annuity(amount,rate,term)
    if Annuity.isValid():
        print(f"A monthly depost of : %s" % locale.currency(Annuity.getAmount(),grouping=True)
              + " earning " + "{:.2%}".format(Annuity.getRate()/100)
              + f" annually after {Annuity.getTerm()} months "
              + "will have a final value of : %s" %locale.currency(Annuity.getFVA(),grouping=True))
        print("That includes interest earned of : %s" %locale.currency(Annuity.getFVATotInt(),grouping=True))
        sched = input("Full Schedule (Y/N) ? : ")
        if len(sched) > 0 and sched[0].upper() == "Y":
            print("Month    Begin Bal.  Deposit    Interest Earned    End Bal.")
            for i in range(1,Annuity.getTerm()+1):
                print("{:4}".format(i)
                      + "{:12,.2f} {:12,.2f} {:12,.2f} {:15,.2f}".format(Annuity.getFVABbal(i),Annuity.getAmount(),Annuity.getFVAInt(i),Annuity.getFVAEBal(i)))
    else:
        print("Annuity Error : " + Annuity.getError())
    
    

def doLoan():
    amount = getValue("Loan Amount : ",'i')
    rate = getValue("Annual Interest Rate (6%=6) : ",'f')
    term = getValue("Term (in months) : ",'i')
    Loan = loan(amount,rate,term)
    if Loan.isValid():
        print(f"A Loan of : %s" %locale.currency(Loan.getAmount(),grouping=True)
            + " charging " + "{:.2%}".format(Loan.getRate()/100) + " annually "
            + f" with a term of {Loan.getTerm()} months will require "
            + "a monthly payment of : %s" %locale.currency(Loan.getMonthlyPayment(),grouping=True))
        print("That includes interest charges of : %s" %locale.currency(Loan.getInterest(),grouping=True))
        sched = input("Full Schedule (Y/N) ? : ")
        if len(sched) > 0 and sched[0].upper() == "Y":
            print("Month    Begin Bal.      Payment    Interest Charged    End Bal.")
            for i in range(1,Loan.getTerm()+1):
                print("{:4}".format(i)
                      + "{:13,.2f} {:13,.2f} {:13,.2f} {:18,.2f}".format(Loan.getBeginBalance(i),Loan.getMonthlyPayment(),Loan.getInterestCharged(i),Loan.getEndBalance(i)))
    else:
        print("Loan Error : " + Loan.getError())
        
def doFutureValue():
    deposit = getValue("Initial Deposit : ", "f")
    rate = getValue("Annual Interest Rate (6%=6) : ","f")
    term = getValue("Term (in months) : ","i")
    fv = Fval(deposit,rate,term)
    if fv.isValid():
        print("A Deposit of : %s" %locale.currency(fv.getDeposit(),grouping=True)
              +" earning " + "{:.2%}".format(fv.getRate()/100) + f"annualy after {fv.getTerm()} months"
              +" will have a Future Value of : %s" %locale.currency(fv.getFutureValue(),grouping=True))
        print("Earning a Total Interest of : %s" %locale.currency(fv.getInterestEarned(),grouping=True))
        sched = input("Full Schedule (Y/N) ? : ")
        if len(sched) > 0 and sched[0].upper() == "Y":
            print("Month    Begin Bal.     Interest Earned    End Bal.")
            for i in range(1,fv.getTerm()+1):
                print("{:4}".format(i)
                      + "{:13,.2f} {:13,.2f} {:18,.2f}".format(fv.getBeginBalance(i),fv.getInterest(i),fv.getEndBalance(i)))
    else:
        print("Future Value Error: " + fv.getError())

def main():
    result = locale.setlocale(locale.LC_ALL,'')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL,'en_US')

    print("Welcome to The Financials Calculator")
    choice = getChoice()
    while choice != 0:
        try:
            if choice == 1:
                doAnnuity()
            elif choice == 2:
                doLoan()
            elif choice == 3:
                doFutureValue()
            else:
                print("Operation Unknown or not Implemented")
        except ValueError as DataErrMsg:
            print(f"Data ErrorL {DataErrMsg}")
        except Exception as GenErrMsg:
            print(f"General Error: {GenErrMsg}")
            
        choice = getChoice()
        print()
        
    print("Thanks for using The Financials Calculator")

if __name__ == "__main__":
    main()
            
            
    
                           
                         
