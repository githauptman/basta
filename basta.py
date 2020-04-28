class Menu():
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    def __repr__(self):
        return "The {} menu is available from {} to {}".format(self.name, self.start_time, self.end_time)
    def calculate_bill(self, purchased_items):
        calculated_bill = 0
        for item in purchased_items:
            calculated_bill +=  self.items[item]
        return calculated_bill

class Franchise():
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    def __repr__(self):
        return self.address
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time > menu.start_time and time < menu.end_time:
                available_menus.append(menu.name)
        return available_menus

class Business():
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
		
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_menu_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

arepas_menu_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

brunch_menu = Menu('Brunch', brunch_items, 11, 16)
early_bird_menu = Menu('Early-Bird', early_bird_items, 15, 18)
dinner_menu = Menu('Dinner', dinner_items, 17, 23)
kids_menu = Menu('Kids', kids_menu_items, 11, 21)
arepas_menu = Menu('Arepas', arepas_menu_items, 10, 20)

"""
#print calculate bill function
print(brunch_menu.calculate_bill(['pancakes', 'home fries','coffee']))
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
"""

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu, arepas_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Stree", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", menus)

#print(flagship_store.available_menus(14))

Business = Business("Take a' Arepa", arepas_place)


