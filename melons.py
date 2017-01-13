from random import randint
from datetime import datetime
# datetime.now() gives current local date and time, datetime.weekday() gives day of the week
# as an integer, where Monday is 0 and Sunday is 6

order_time = raw_input("Would you like to place your order now or later?: ")

if order_time == "now":
    order_time = datetime.now()

# Add else order later, add code to determine later date/time and surge

print order_time


"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        # self.order_type = None
        # self.tax = 0
    #    self.base_price = base_price

    def get_base_price(self):
        #self.base_price = randint(5, 9)
        return randint(5, 9)
        


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price = base_price * 1.5

        
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""
        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    passed_inspection = False
    order_type = "government"

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty)

    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)
        # self.order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)
        """Initialize melon order attributes"""
        
        self.country_code = country_code
        
    
    def get_total(self):
        return super(InternationalMelonOrder, self).get_total() + 3 * (self.qty < 10)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
