"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    def __init__(self, species, qty, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = tax

    def get_total(self):
        """Calculate price."""

        base_price = 5

        if self.species == "Christmas":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""
        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""


    def __init__(self, species, qty, tax):
        super(DomesticMelonOrder, self).__init__(species, qty, tax)
        self.order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, tax, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, tax)
        """Initialize melon order attributes"""

        self.country_code = country_code
        self.order_type = "international"
    
    def get_total(self):
        return super(InternationalMelonOrder, self).get_total() + 3 * (self.qty < 10)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
