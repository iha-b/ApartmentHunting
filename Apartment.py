class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition
    def getRent(self):
        return self.rent
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    def getCondition(self):
        return self.condition
    def getApartmentDetails(self):
        return("(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(self.rent,self.metersFromUCSB,self.condition))
    def __gt__(self, other):
        if self.rent == other.rent:
            if self.metersFromUCSB == other.metersFromUCSB:
                if self.condition == other.condition:
                    return False
                elif self.condition == "bad":
                    return True
                elif other.condition == "bad":
                    return False
                elif self.condition == "average":
                    return True
                else:
                    return False
            return self.metersFromUCSB > other.metersFromUCSB
        return self.rent >  other.rent
    def __eq__(self,rhs):
        return self.rent == rhs.rent and self.metersFromUCSB == rhs.metersFromUCSB and self.condition == rhs.condition
    def __lt__(self,rhs):
        if rhs > self and not rhs == self:
            return True
        
