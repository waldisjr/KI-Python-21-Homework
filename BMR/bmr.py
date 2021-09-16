weight, height, age = [float(input(f"Enter your {rq}: ")) for rq in ["weight (kg)", "height (cm)", "age (years)"]]
print(f"If you`re male, your BMR: {88.36+(13.4*weight)+(4.8*height)-(5.7*age)}\n"
      f"If you`re female, your BMR: {447.6+(9.2*weight)+(3.1*height)-(4.3*age)}")
