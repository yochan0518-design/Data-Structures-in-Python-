# STEP 1 - Create tuples for recipe details (Fixed - cannot be changed )
pasta = ("pasta arabiata", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hot")
print = ("Recipe 1:", pasta)
print = ("name:", pasta[0])
print = ("cuisine", pasta[1])
print = ("Difficulty", pasta[-1])

# STEP 2 - Nested tuples and slicing
all_recipes = (pasta, biryani)
print ("\nfirst recipe name:", all_recipes[0][0])
print ("second recipe time:", all_recipes[1][2], "mins")
print ("pasta details(sliced):", pasta[1:3])

# STEP 3 - iterate through a tuple 
print("\nPasta Recipe Details:")
for detail in pasta:
    print(" -",detail)

# STEP 4 - Create sets for ingredients (no duplicates allowed)
pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
print("\nPasta ingredients:", pasta_ingredients)
print("Biryani ingredients:", biryani_ingredients)
print("Total pasta ingredients:", len(pasta_ingredients))

# STEP 5 - Modify the set
pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print("\nUpdated pasta ingredients:", pasta_ingredients)

# STEP 6 - Set operations
all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll ingredients (union):", all_ingredients)
print("Common ingredients (intersection):", common)
print("Only in Pasta (difference):", only_pasta)
print("Not shared (sym. difference):", unique_to_each)
