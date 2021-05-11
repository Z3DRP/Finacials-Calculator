#!/user/bin/env python3
#Loan class ... by - Zach Palmer
#Supporting File for Finacials

class Loan:
    """Loan Logic for Finacial Calculator"""

    def __init__(self,amount=0,rate=0,term=0):
        #complete constructor to store
        #starting values in global "private" variables
        #and check validity, build if ok
        self.setAmount(amount)
        self.setRate(rate)
        self.setTerm(term)
        self._MonthlyPayment = 0
        self._Error = ""
        if self.isValid():
            self.buildLoan()

    def setAmount(self,amount):
        self._Amount = amount
    def getAmount(self):
        return self._Amount

    def setRate(self,rate):
        self._Rate = rate
    def getRate(self):
        return self._Rate

    def setTerm(self,term):
        self._Term = term
    def getTerm(self):
        return self._Term

    def isValid(self):
        valid = True
        if self._Amount <= 0:
            #self.Error = "Deposit Amount Must Be Positive"
            raise Exception("Loan Amount Must Be Positive")
            valid = False
        elif self._Rate < 1 or self._Rate >= 26:
            #self._Error = "Rate Is Out Of Bounds: Must Be Between 1-25"
            raise Exception("Rate out of Bounds: Mus Be Between 1-25%")
            valid = False
        elif self._Term <= 0:
            #self._Error = "Term Must Be Positive"
            raise Exception("Term Must Be Positive")
            valid = False
        return valid

    def getError(self):
        return self._Error

    def buildLoan(self):
        #monthly payment calculation
        self._BeginBalance = [0] * self._Term
        self._InterestCharge = [0] * self._Term
        self._EndBalance = [0] * self._Term

        self._BeginBalance[0] = self._Amount
        monthlyRate = self._Rate / 12 / 100#rate per month
        mopayDenom = ((1 + monthlyRate)**self._Term) -1
        #mopayDenom -= 1
        self._MonthlyPayment = (monthlyRate + monthlyRate / mopayDenom)* self._Amount
        #then calc denominator:((1+monthlyRate) ** term) -1
        #then calculate monthly Payment using denominator
        #mpayment : monthlyRate + monthlyRate/denominator * loanAmnt (principal)
        for month in range(0,self._Term):
            if month == 0:
                self._InterestCharge[month] = self._BeginBalance[month] * monthlyRate
                self._EndBalance[month] = self._BeginBalance[month] + self._InterestCharge[month] - self._MonthlyPayment
            else:
                self._BeginBalance[month] = self._EndBalance[month-1]
                self._InterestCharge[month] = self._BeginBalance[month] * monthlyRate
                self._EndBalance[month] = self._BeginBalance[month] + self._InterestCharge[month] - self._MonthlyPayment
            
    def getMonthlyPayment(self):
        return self._MonthlyPayment

    def getInterest(self):
        totalInterest = 0
        for months in range(0,self._Term):
            totalInterest += self._InterestCharge[months]
        return totalInterest

    def getBeginBalance(self,mo):
        if mo < 0:
            raise Exception("Month Must Be A Non-Negative Number")
        else:
            return self._BeginBalance[mo-1]

    def getInterestCharged(self,mo):
        if mo < 0:
            raise Exception("Month Must Be A Non-Negative Number")
        else:
            return self._InterestCharge[mo-1]

    def getEndBalance(self,mo):
        if mo < 0:
            raise Exception("Month Must Be A Non-Negative Number")
        else:
            return self._EndBalance[mo-1]
