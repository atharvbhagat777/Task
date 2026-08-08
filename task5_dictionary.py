# 1. Friends' names

friends = ["Aditya", "Rahul", "Rohan", "Priya", "Sneha"]

friends_tuples = []

for name in friends:
    friends_tuples.append((name, len(name)))

print("Friends:", friends_tuples)


# 2. Expenses

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate totals
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total:", your_total)
print("Partner's total:", partner_total)

# Who spent more?
if your_total > partner_total:
    print("You spent more")
elif partner_total > your_total:
    print("Your partner spent more")
else:
    print("Both spent the same amount")

# Find biggest difference
max_difference = 0
category_name = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])

    if difference > max_difference:
        max_difference = difference
        category_name = category

print("Biggest difference:", category_name)
print("Difference:", max_difference)