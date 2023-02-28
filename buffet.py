buffetItems = ("lemon chicken", "sweet and sour pork", "springrolls", "chicken fried rice", "mixed vegetables")
print("original tuple:")
[print(food) for food in buffetItems]


# got an error! buffetItems[2] = "sushi"


buffetItems = ("lemon chicken", "sweet and sour pork", "eggrolls", "chicken fried rice", "sushi")
print("New tuple:")
[print(food) for food in buffetItems]
