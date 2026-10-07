homework=int(input("how much time does it take you to complete your homework in minutes:"))
if homework > 60:
    plan = "start immeadiately"
    print("that is way too much")
else:
    plan = "finish it and take your time"
    print("no need to rush you have a quick homework session ")
free_time = input("are you free after your homework(yes or no)")
if free_time == "yes":
    print("do what ever you want,you have earned it")
print("daily plan")
print("homework minutes:", homework)
print("plan:", plan)
print("free time:", free_time)
