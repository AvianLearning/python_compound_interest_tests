class CompoundInterest:
    def __init__(self, principle, years, interest):
        self.principle = principle
        self.years = years
        self.interest = interest
        self.number_times_compounded = 12
    
    def amount_returned(self):
        amount = self.principle * ((1 + (self.interest / self.number_times_compounded) ** (self.number_times_compounded * self.years)))
        return amount 