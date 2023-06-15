import time
timestamp = time.strftime('%H:%M:%S')
print("time:",timestamp)
hour = int(time.strftime('%H'))
print(hour)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)


if (hour<12):
  print("good morning")
elif (hour<18 and timestamp>12):
  print("good afternoon")
elif (hour>18):
  print("Night Night")
