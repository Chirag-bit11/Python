import sys
list01 = ["how many days in a week?", "how many wonders of the world?"]
print("\"Welcome to the game\"")
print("To display a question on the screen, press 1")
a = int(input())

if a == 1:
    print(list01[0])  # Accessing the element at index 0 of the list
    ans1 = int(input())
    if (ans1 == 7):
      print("you have been rewarded with 10 points\n press 2 for question 2")
      account = 10
    else:
      print("youve failed to answer")
      sys.exit()
    b = int(input())
    if b == 2:
      print(list01[1])
      ans2 = int(input())
      if ans2 == 7:
        print("congrats")
        account = account +10
else:
  print("nikal")

    

print("Total amount won is: " , account)
