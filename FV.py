#!/user/bin/env python3
#FV class ... by - Zach Palmer
#Supporting File for Finacials

class FutureValue: #fv = deposit*(1+rate)^term // rate = rate/12.0/100.0
    """Future Value Logic for Finacial Calculator"""
    
    def __init__(self,deposit=0.0,rate=0.0,term=0.0):
        self.setDeposit(deposit)
        self.setRate(rate)
        self.setTerm(term)
        self._FutureValue = 0
        self._Error = ""
        if self.isValid():
            self.buildFV()
    def setDeposit(self,deposit):
        self._Deposit = deposit
    def getDeposit(self):
        return self._Deposit

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
        if self._Deposit < 0:
            #self._Error = "Deposit Amount Must Be Positive"
            raise Exception("Deposit Amount Must Be Positive")
            valid = False
        elif self._Rate < 1 or self._Rate > 26:
            #self._Error = "Rate Is Out Of Bounts: Must Be Between 1-25"
            raise Exception("Rate Is Out Of Bounds: Must Be Between 1-25%")
            valid = False
        elif self._Term < 0:
            #self._Error = "Term Must Be Positive"
            raise Exception("Term Must Be Positive")
            valid = False
        return valid
    def getError(self):
        return self._Error

    def buildFV(self):
        self._BeginBalance = [0] * self._Term
        self._InterestEarned = [0] * self._Term
        self._EndBalance = [0] * self._Term

        self._BeginBalance[0] = self._Deposit
        monthlyRate = self._Rate/12/100
        self._FutureValue = self._Deposit * (1 + monthlyRate)**self._Term

        for month in range(0,self._Term):
            if month == 0:
                self._InterestEarned[month] = self._BeginBalance[month] * monthlyRate
                self._EndBalance[month] = self._BeginBalance[month] + self._InterestEarned[month]
            else:
                self._BeginBalance[month] = self._EndBalance[month-1]
                self._InterestEarned[month] = self._BeginBalance[month] * monthlyRate
                self._EndBalance[month] = self._BeginBalance[month] + self._InterestEarned[month]

    def getFutureValue(self):
        return self._FutureValue

    def getInterest(self,mo):
        if mo < 0:
            raise Exception("Month Must Be A Non-Negative Number")
        else:
            return self._InterestEarned[mo-1]
    
    def getInterestEarned(self):
        totalInterest = 0
        for months in range(0,self._Term):
            totalInterest += self._InterestEarned[months]
        return totalInterest

    def getBeginBalance(self,mo):
        if mo < 0:
            raise Exception("Month Must Be A Non-Negative Number")
        else:
            return self._BeginBalance[mo-1]

    def getEndBalance(self,mo):
        if mo < 0:
            raise Exception("Month Must Be A Non-Negative Number")
        else:
            return self._EndBalance[mo-1]

        

































    
