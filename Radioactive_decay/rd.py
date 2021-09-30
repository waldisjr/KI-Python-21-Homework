import math

weight = float(input("Enter weight of Strontium-90: "))
[print(f"After {years} years it will be {weight * math.e ** (-(0.693 / 28.79) * years)} mg of Strontium-90")
    for years in [1, 25, 100, 500]]
