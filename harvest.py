############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""
        #Initializing each attribute to instance
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        #adding each pair to the pairings list
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    #Creating an empty list of melons
    all_melon_types = []

    #Instanciating(sp?) each melon
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')

    casaba = MelonType('cas', 2003, 'orange', False, False, "Casaba")
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')

    crenshaw = MelonType('cren', 1996, 'green', False, False, "Crenshaw")
    crenshaw.add_pairing('proscuitto')

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing('ice cream')

    #adding all melons to list all_melon_types
    all_melon_types.extend([musk, casaba, crenshaw, yellow_watermelon])

    #returning a list of all the melons
    return all_melon_types

#storing the output of make_melon_types to all_melons
all_melons = make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    #looping over each melon in our list of melons
    for melon in melon_types:
        #printing the name of each melon and 'pairs with'
        print melon.name + "pairs with"
        #looping over each pair and printing
        for pair in melon.pairings:
            print "- " + str(pair)
        print


def make_melon_type_lookup(all_melons):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    #Setting up a dictionary with codes as keys, melon instances as values
    melons_dict = {}
    #Looping over each melon in the list and adding the code and melon instances
    for melon in all_melons:
        melons_dict[melon.code] = melon

    return melons_dict
    # Fill in the rest

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initialize a melon."""
        #Initializing each attribute to instance
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        if self.shape_rating >= 5 and self.color_rating >= 5 and self.field != 3:
            return True
        else:
            return False

#FIXME: need to accept a list of melons as input
def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_dict = make_melon_type_lookup(melon_types)
    #Creating an empty list of melon objects
    melon_objects = []

    #Instanciating(sp?) each melon
    melon_1 = Melon(melon_dict['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melon_dict['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melon_dict['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melon_dict['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melon_dict['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melon_dict['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melon_dict['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melon_dict['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melon_dict['yw'], 7, 10, 3, 'Sheila')

    #adding all melons objects to list melon_objects
    melon_objects.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6,
                          melon_7, melon_8, melon_9])

    #returning a list of melon objects
    return melon_objects


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.is_sellable():
            print melon.harvester



