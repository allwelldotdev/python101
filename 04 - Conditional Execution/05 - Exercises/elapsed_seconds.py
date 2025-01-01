seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_day = 24 * seconds_in_hour
seconds_in_week = 7 * seconds_in_day

elapsed = seconds_in_day * 7 # time in seconds

if elapsed < seconds_in_minute: # less than 1 minute - 60 seconds in 1 minute
  magnitude = 'seconds'
elif elapsed < seconds_in_hour: # less than 1 hour - 3600 seconds in 1 hour
  magnitude = 'minutes'
elif elapsed < seconds_in_day: # less than 1 day - 86_400 seconds in 1 day
  magnitude = 'hours'
elif elapsed < seconds_in_week: # less than 1 week - 604_800 seconds in 1 week
  magnitude = 'days'
else: # more than 1 week
  magnitude = 'weeks'

print(magnitude)
