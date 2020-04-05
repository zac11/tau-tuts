stuff = {"food":15, "energy":100, "enenmies":3}
print(stuff.get("food"))
print(stuff.items())
print(stuff.keys())
print(stuff.popitem())
print(stuff)
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends",123))
print(stuff)

#update
new_items = {"rocks":3,"arrows":78}
stuff.update(new_items)
print(stuff)


#new update
new_items = {"rocks":6,"arrows":89}
stuff.update(new_items)
print(stuff)

#update again
up_new = {"food":4,"web":2}
stuff.update(up_new)
print(stuff)

#update again and again
stuff.update(food=450,cookies=7)
print(stuff)