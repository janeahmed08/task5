pizza={
    "crust":"thin"
    ,"topping":"pepproni"
    ,"price":"15"}

pizza.update(({"sauce":"ranch"}))
print(pizza)

del pizza["price"]
print(pizza)

print(pizza["crust"])
