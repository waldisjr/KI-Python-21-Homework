initial_bacterias = int(input("Enter the initial bacteria count: "))
formula = lambda time_in_seconds: initial_bacterias * (2 ** (time_in_seconds // 588))
print(f"After one day: {formula(24*3600)}\n"
      f"After two days: {formula(48*3600)}\n"
      f"After week: {formula(168*3600)}\n"
      f"After month (30 days): {formula(720*3600)}")
