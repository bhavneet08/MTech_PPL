# Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

print("Original Dictionary:", student)

# Access
print("Name:", student["name"])

# Update
student["age"] = 21
student["city"] = "Delhi"
print("Updated Dictionary:", student)

# Delete
del student["course"]
print("After Deleting:", student)