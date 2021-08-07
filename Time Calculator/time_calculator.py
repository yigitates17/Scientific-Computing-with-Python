def add_time(start, duration, given_day=None):

  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  day_count = 0
  temp_time = []
  duration = duration.split(":")
  start = start.split(' ')
  starting_time = start[0].split(":")
  day_time = start[1]

  if day_time == "PM":
      starting_time[0] = str(int(starting_time[0]) + 12)

  temp_time.append(int(duration[0]) + int(starting_time[0]))
  temp_time.append(int(duration[1]) + int(starting_time[1]))

  while temp_time[0] >= 24 or temp_time[1] > 60:
      if temp_time[1] > 60:
          temp_time[1] -= 60
          temp_time[0] += 1
      if temp_time[0] >= 24:
          day_count += 1
          temp_time[0] -= 24
          
  if temp_time[1] >= 0 and temp_time[1] < 10:
      temp_time[1] = str(temp_time[1]).zfill(2)

  if temp_time[0] > 12 and temp_time[0] <= 23:
      temp_time[0] -= 12
      new_time = str(temp_time[0])+ ':' + str(temp_time[1])
      if given_day != None:
        new_time += ' PM,'
      else:
        new_time += ' PM'

  elif temp_time[0] == 12:
      new_time = str(temp_time[0])+ ':' + str(temp_time[1])
      if given_day != None:
        new_time += ' PM,'
      else:
        new_time += ' PM'

  else:
      if temp_time[0] == 0:
        temp_time[0] += 12
      new_time = str(temp_time[0])+ ':' + str(temp_time[1])
      if given_day != None:
        new_time += ' AM,'
      else:
        new_time += ' AM'
      

  if given_day != None:

    for i, day in enumerate(days):
      if given_day.lower() == day.lower():
        index_no = i

    new_index = (index_no + day_count) % 7

    new_day = days[new_index]    

    if new_index > 6:
      temp = new_index//6
      new_index = new_index - 6*temp - 1

    new_day = days[new_index]

    new_time += ' ' + new_day 

  if day_count == 1:
      new_time += " (next day)"

  elif day_count > 1:
      new_time += ' (' + str(day_count) + ' days later' + ')'

  return new_time