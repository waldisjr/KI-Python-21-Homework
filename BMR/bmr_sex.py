[weight, height, age], sex = [float(input(f"Enter your {rq}: ")) for rq in
                              ["weight (kg)", "height (cm)", "age (years)"]], input("Enter your sex (male|female): ")
print(f"Your BMR: {88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)}\n") if sex == "male" \
    else print(f"Your BMR: {447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)}") if sex == "female" \
    else print(f"Incorrect sex !")
