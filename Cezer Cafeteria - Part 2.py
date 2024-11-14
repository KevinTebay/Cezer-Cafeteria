# Define the initial menu array (1D array)
menu = ["Spaghetti Carbonara", "Nasi Lemak", "Bibimbap", "Quinoa Salad"]

# Define the nutrition array (2D array) with each row as [calories, protein, carbs, fats]
nutrition = [
    [700, 20, 85, 30],  # Spaghetti Carbonara: calories, protein, carbs, fats
    [650, 15, 80, 25],  # Nasi Lemak: calories, protein, carbs, fats
    [500, 12, 70, 10],  # Bibimbap: calories, protein, carbs, fats
    [400, 10, 60, 15]   # Quinoa Salad: calories, protein, carbs, fats
]

# Display the initial menu options
print("Welcome to Cezar Cafeteria! Here is today's menu:")
for i in range(len(menu)):
    print(i + 1, ". ", menu[i])

# Task 1: Allow the user to add 3 additional dishes
print("\nLet's add three additional dishes to the menu.")
for _ in range(3):
    dish_name = input("Enter the name of the new dish: ")
    calories = int(input("Enter calories for " + dish_name + ": "))
    protein = int(input("Enter protein (g) for " + dish_name + ": "))
    carbs = int(input("Enter carbohydrates (g) for " + dish_name + ": "))
    fats = int(input("Enter fats (g) for " + dish_name + ": "))

    # Append the new dish and its nutrition to the arrays
    menu.append(dish_name)
    nutrition.append([calories, protein, carbs, fats])

# Task 2: Display the updated menu with added dishes
print("\nUpdated menu:")
for i in range(len(menu)):
    print(i + 1, ". ", menu[i])

# Task 3: Sort the menu in ascending order using bubble sort and reorder nutrition accordingly
print("\nSorting dishes in ascending order by name...")
n = len(menu)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        # Compare adjacent items and swap if they are in the wrong order
        if menu[j] > menu[j + 1]:
            # Swap menu items
            menu[j], menu[j + 1] = menu[j + 1], menu[j]
            # Swap corresponding nutrition information
            nutrition[j], nutrition[j + 1] = nutrition[j + 1], nutrition[j]

# Display the sorted menu
print("\nSorted menu:")
for i in range(len(menu)):
    print(i + 1, ". ", menu[i])

# Display the sorted menu with nutritional information option
show_info = input("\nWould you like to view the nutritional information for each dish? (yes/no): ")
if show_info.lower() == "yes":
    for i in range(len(menu)):
        print("\nDish:", menu[i])
        print("  Calories:", nutrition[i][0], "kcal")
        print("  Protein:", nutrition[i][1], "g")
        print("  Carbohydrates:", nutrition[i][2], "g")
        print("  Fats:", nutrition[i][3], "g")
