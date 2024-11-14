# Define the menu array (1D array)
menu = ["Spaghetti Carbonara", "Nasi Lemak", "Bibimbap", "Quinoa Salad"]

# Define the nutrition array (2D array) with each row as [calories, protein, carbs, fats]
nutrition = [
    [700, 20, 85, 30],  # Spaghetti Carbonara: calories, protein, carbs, fats
    [650, 15, 80, 25],  # Nasi Lemak: calories, protein, carbs, fats
    [500, 12, 70, 10],  # Bibimbap: calories, protein, carbs, fats
    [400, 10, 60, 15]   # Quinoa Salad: calories, protein, carbs, fats
]

# Display the menu options to the user, starting from 1
print("Welcome to Cezar Cafeteria! Here is today's menu:")
for i in range(len(menu)):
    print(i + 1, ". ", menu[i])

# Prompt the user to select a dish
try:
    choice = int(input("\nPlease enter the number of the dish you'd like to know more about: ")) - 1

    # Check if the choice is within the valid range
    if 0 <= choice < len(menu):
        # Display the selected dish and its nutritional information
        selected_dish = menu[choice]
        dish_nutrition = nutrition[choice]

        print("\nYou selected: ", selected_dish)
        print("Nutritional Information:")
        print("  Calories: ", dish_nutrition[0], " kcal")
        print("  Protein: ", dish_nutrition[1], " g")
        print("  Carbohydrates: ", dish_nutrition[2], " g")
        print("  Fats: ", dish_nutrition[3], " g")
    else:
        print("Invalid choice. Please select a valid dish number.")

except ValueError:
    print("Invalid input. Please enter a number.")
