initial_bacterias = int(input("Enter the initial bacteria count: "))
formula = lambda time_in_ours: int(initial_bacterias * (2 ** (time_in_ours / 6)))
print(f"After one day: {formula(24)}\n"
      f"After two days: {formula(48)}\n"
      f"After week: {formula(168)}\n"
      f"After month (30 days): {formula(720)}")
