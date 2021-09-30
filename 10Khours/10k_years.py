import datetime
import time

# 10000*60*60
seconds = 36000000

time_needed = seconds

end = datetime.datetime.fromtimestamp(round(time.time()+time_needed))

years_needed = end.timestamp() - datetime.datetime.now().timestamp()

print(f"End at (if you`ll start now): {end} about {} years")

