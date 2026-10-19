
# Travel Recommendation System using Best-First Search

places = {
    "Goa": {"cost": 5000, "rating": 9},
    "Manali": {"cost": 7000, "rating": 10},
    "Jaipur": {"cost": 3000, "rating": 9.9},
    "Dwarka": {"cost": 2000, "rating": 9.5},
    "Mount Abu": {"cost": 2500, "rating": 8.9},
    "Agra":{"cost": 2000, "rating": 7.8}
}

print("=== AI Travel Recommendation System ===")

budget = int(input("Enter your travel budget: "))

# Find suitable destinations
suitable_places = []

for place, details in places.items():
    if details["cost"] <= budget:
        suitable_places.append(
            (place, details["cost"], details["rating"])
        )

# Best-First Search: prioritize the highest-rated destination
suitable_places.sort(key=lambda x: x[2], reverse=True)

if suitable_places:
    print("\nRecommended Travel Destinations:")

    for place, cost, rating in suitable_places:
        print("Place:", place)
        print("Estimated Cost: Rs.", cost)
        print("Rating:", rating, "/10")
        print()

    best = suitable_places[0]
    print("Best Recommendation:", best[0])

else:
    print("No destination found within your budget.")

