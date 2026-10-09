pasta = ("pasta arabiata", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hot")
print = ("Recipe 1:", pasta)
print = ("name:", pasta[0])
print = ("cuisine", pasta[1])
print = ("Difficulty", pasta[-1])

# STEP 1 - Nested tuples and slicing
all_recipes = (pasta, biryani)
print ("\nfirst recipe name:", all_recipes[0][0])
print ("second recipe time:", all_recipes[1][2], "mins")
print ("pasta details(sliced):", pasta[1:3])

# STEP 2 - iterate through a tuple 
print("\nPasta Recipe Details:")
for detail in pasta:
    print(" -",detail)

# STEP 4 - Create sets for ingredients (no duplicates allowed)
pasta_ingrediets = {"tomato","garlic", "olive oil", "chili", "pasta", "garlic"}
biryani_ingridents = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
print("\nPasta ingredients:" pasta_ingredients)
print("Biryani ingredients:" biryani_ingridents)
print("Total pasta ingredients:", len(pasta_ingredients))