total_slices = party_pizza_mini + large + medium
print("The total amount of pizza is {total_slices}")

total_people = people + 1
shared = slices / total_people
leftovers = slices / people
print("total_slices / total_people")
print("total_people / total_slices)

total_people = people + 3 #Eric and Brandon are coming too.
shared = slices / total_people
leftovers = slices / people
print("total_slices / total people")
print("total_people / total_slices")

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

total_slices = party_pizza_mini + party_pizza_mini + large + medium
shared = total_people / total_slices
leftovers = total_slices / total_people
print("total_slices / total_people")
print("total_people / total_slices")
print("...for Mr. Hollow Leg")
