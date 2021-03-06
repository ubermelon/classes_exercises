"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price."""
        base_price = 5
        # Christmas melons will cost 1.5 times base price.
        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        # a flat fee of $3 will be added to all international orders with less than 10 melons.
        if self.order_type == "international" and self.qty < 10:
            total = total + 3.0
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize locally country_code attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    order_type = "international"
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A Government order that has no tax which includes inspection."""

    def __init__(self, species, qty):
        """Initialize locally country_code attributes"""
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_inspection = False

    order_type = "government"
    tax = 0.0

    def inspect_melons(self, passed):
        """Set inspected to be true."""
        if passed == True:
            self.passed_inspection = True
        else:
            self.passed_inspection = False

