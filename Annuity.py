#!/user/bin/env python3
#Annuity class ... by - Zach Palmer
#Supporting File for Finacials


class Annuity:
    """Annuity Logic for Financial Calculator"""
# this is a consstructor dont have to send all 3values has default values
    def __init__(self,amount=0.0,rate=0.0,term=0):
        #create "private" variables for class values
        self.setAmount(amount)
        self.setRate(rate)
        self.setTerm(term)
        self._Error = ""
        if self.isValid():
            self.buildAnnuity()

#get and set methods encaspulate data values
        
    def setAmount(self,amnt):
    #self._variableName makes the variable a private or hidden member variable
        self._Amount = amnt
    def getAmount(self):
    #member method(function) to get the private member variable
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
            #self._Error = "Deposit Amount Must Be Positive"
            raise Exception("Amount Must Be Positive")
            valid = False
        elif self._Rate < 1 or self._Rate >= 26:
            #self._Error = "Rate Is Out Of Bounds: Must Be Between 1-25"
            raise Exception("Rate Is Out Of Bounds: Must Be Between 1-25%")
            valid = False
        elif self._Term <= 0:
            #self._Error = "Term Must Be Positive"
            raise Exception("Term Must Be Positive")
            valid = False
        return valid

    def getError(self):
        return self._Error

    def buildAnnuity(self):
        #create all values needed for annuityy schedule
        #3 lists to store column values
        #creates member var list [] * says give me as many elements in
        #list as there is in terms
        self._BeginBalance = [0] * self._Term
        self._InterestEarned = [0] * self._Term
        self._EndBalance = [0] * self._Term

        self._BeginBalance[0] = 0
        monthlyRate = self._Rate / 12 / 100 #monthRate is fraction
        for i in range(0,self._Term):
            if i > 0:
                self._BeginBalance[i] = self._EndBalance[i-1]
                
            self._InterestEarned[i] = (self._BeginBalance[i] + self._Amount)* monthlyRate
            
            self._EndBalance[i] = self._BeginBalance[i] + self._Amount + self._InterestEarned[i]
   
    def getFVA(self):
        #return end balance from the last element of list
        return self._EndBalance[self._Term-1]

    def getFVATotInt(self):
        return self._EndBalance[self._Term-1] - (self._Amount * self._Term)

    def getFVABbal(self,month):
        #additonl extra credit: buble up exception validate month and
        #raise exception if month is out of bounds (handle exceptiion)
        #in main program
        if month < 0:
            raise Exception("Month Must Be A Non-Negative Number")
        else:
            return self._BeginBalance[month-1]

    def getFVAInt(self,mo):
        if mo < 0:
            raise Exception("Month Must Be A Non-Negative Number")
        else:
            return self._InterestEarned[mo-1]

    def getFVAEBal(self,mo):
        if mo < 0:
            raise Exception("Month Must Be A Non-Negative Number")
        else:
            return self._EndBalance[mo-1]
        
        
        
        
