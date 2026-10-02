print("grocery list comparasion tool")
rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4
basket_cost_per_person = (rice_price + milk_price + fruit_price) * number_of_baskets / family_members
print("\npart 1- this weeks shop")
print("cost per person:", basket_cost_per_person)
print("\npart 2 - sharing the items")
total_items = int(input("enter the total number of grocery items: "))
people = int(input("enter the number of people sharing them: "))
if people == 0:
    print("You cannot share items between 0 people.")
else:
    if total_items % people == 0:
        print(total_items, "items divide equally among", people, "people -", total_items // people, "each.")
    else:
        print(total_items, "items do not divide equally among", people, "people -", total_items % people, "left over.")
print("\npart 3 - Fixing the weekly average")
recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80
recorded_total = recorded_average * total_weeks
corrected_total = recorded_total - wrong_week_cost + correct_week_cost
corrected_average = corrected_total / total_weeks
print("recorded total was:", recorded_total)
print("corrected total is:", corrected_total)
print("corrected weekly average:", corrected_average)
print("\npart 4 - comparing the stores")
store_a_average = 70
store_b_average = 75
store_c_average = 80
print("store a:", store_a_average, "| store b:", store_b_average, "| store c:", store_c_average)
if corrected_average < store_a_average and corrected_average < store_b_average and corrected_average < store_c_average:
    verdict = "cheaper than all three stores"
elif corrected_average > store_a_average and corrected_average > store_b_average and corrected_average > store_c_average:
    verdict = "more expensive than all three stores"
else:
    verdict = "somewhere in between the three stores"
print("Your average is", verdict)
print("\nsummary")
print("cost per person this week:", basket_cost_per_person)
print("corrected weekly average:", corrected_average)
print("verdict:", verdict)