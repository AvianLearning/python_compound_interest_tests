class CompoundInterest:
    def __init__(self, principle, years, interest):
        self.p = principle
        self.y = years
        self.i = interest
        self.n = 12
    
    def amount_returned(self):
        calculation = self.p * ((1 + (self.i / self.n)) ** (self.n * self.y))
        return round(calculation, 2)