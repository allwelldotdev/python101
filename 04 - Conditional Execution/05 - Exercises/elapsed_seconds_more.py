seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_day = 24 * seconds_in_hour
seconds_in_week = 7 * seconds_in_day

elapsed = 604_800 + (seconds_in_day * 3) + 1 # time in seconds

if elapsed < seconds_in_minute: # less than 1 minute - 60 seconds in 1 minute
  magnitude = f"{elapsed} {'second' if elapsed == 1 else 'seconds'}"
elif elapsed < seconds_in_hour: # less than 1 hour - 3600 seconds in 1 hour
  magnitude = f"{elapsed // seconds_in_minute} {'minute' if elapsed // seconds_in_minute == 1 else 'minutes'}, {elapsed % seconds_in_minute} {'second' if elapsed % seconds_in_minute == 1 else 'seconds'}"
elif elapsed < seconds_in_day: # less than 1 day - 86_400 seconds in 1 day
  magnitude = f"{elapsed // seconds_in_hour} {'hour' if elapsed // seconds_in_hour == 1 else 'hours'}, {(elapsed % seconds_in_hour) // seconds_in_minute} {'minute' if (elapsed % seconds_in_hour) // seconds_in_minute == 1 else 'minutes'}, {(elapsed % seconds_in_hour) % seconds_in_minute} {'second' if (elapsed % seconds_in_hour) % seconds_in_minute == 1 else 'seconds'}"
elif elapsed < seconds_in_week: # less than 1 week - 604_800 seconds in 1 week
  magnitude = f"{elapsed // seconds_in_day} {'day' if elapsed // seconds_in_day == 1 else 'days'}, {(elapsed % seconds_in_day) // seconds_in_hour} {'hour' if (elapsed % seconds_in_day) // seconds_in_hour == 1 else 'hours'}, {((elapsed % seconds_in_day) % seconds_in_hour) // seconds_in_minute} {'minute' if ((elapsed % seconds_in_day) % seconds_in_hour) // seconds_in_minute == 1 else 'minutes'}, {((elapsed % seconds_in_day) % seconds_in_hour) % seconds_in_minute} {'second' if ((elapsed % seconds_in_day) % seconds_in_hour) % seconds_in_minute == 1 else 'seconds'}"
else: # more than 1 week
  magnitude = f"{elapsed // seconds_in_week} {'week' if elapsed // seconds_in_week == 1 else 'weeks'}, {(elapsed % seconds_in_week) // seconds_in_day} {'day' if (elapsed % seconds_in_week) // seconds_in_day ==1 else 'days'}, {((elapsed % seconds_in_week) % seconds_in_day) // seconds_in_hour} {'hour' if ((elapsed % seconds_in_week) % seconds_in_day) // seconds_in_hour == 1 else 'hours'}, {(((elapsed % seconds_in_week) % seconds_in_day) % seconds_in_hour) // seconds_in_minute} {'minute' if (((elapsed % seconds_in_week) % seconds_in_day) % seconds_in_hour) // seconds_in_minute == 1 else 'minutes'}, {(((elapsed % seconds_in_week) % seconds_in_day) % seconds_in_hour) % seconds_in_minute} {'second' if (((elapsed % seconds_in_week) % seconds_in_day) % seconds_in_hour) % seconds_in_minute == 1 else 'seconds'}"

print(magnitude)
