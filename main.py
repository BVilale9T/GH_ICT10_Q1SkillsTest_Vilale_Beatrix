from pyscript import display, document

def details(e):
    name = document.getElementById('name').value
    hometown = document.getElementById('town').value
    phonenumber = document.getElementById('number').value

    carbonara = document.getElementById('carbonara').value
    garlicbread = document.getElementById('garlic bread').value
    caesarsalad = document.getElementById('caesarsalad').value
    icedtea = document.getElementById('icedtea').value
    sparklingwater = document.getElementById('sparklingwater').value

items = {
    "Carbonara": "carbonara",
    "Garlic Bread": "garlicbread",
    "Caesar Salad": "caesarsalad",
    "Iced Tea": "icedtea",
    "Sparkling Water": "sparklingwater"
}

order = {}
for item, item_id in items.items():
    value = document.getElementById(item_id).value
    if value.isdigit() and int(value) > 0:
        order[item] = int(value)

        
