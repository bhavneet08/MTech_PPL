# Create a set
fruits = {"Apple", "Banana", "Mango"}
print("Original Set:", fruits)

# Access an element
print("Elements in the set:")
for fruit in fruits:
    print(fruit)

# Update the set
fruits.add("Orange")
print("Updated Set:", fruits)

# Delete an element
fruits.remove("Banana")
print("After Deleting Banana:", fruits)

# Delete the complete set
del fruits
print("Set deleted successfully")