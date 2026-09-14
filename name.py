name = input("enter your real name,club member: ")
club = input("enter your school club name: ")
member_number = 8
points_earned = 9.5
event_count = 6
meeting_hours = 1.5
is_active = True
print("name:", name, "-> type:", type(name))
print("club:", club, "-> type:", type(club))
print("member number:", member_number, "-> type:", type(member_number))
print("points earned:", points_earned, "-> type:", type(points_earned))
print("event count:", event_count, "-> type:", type(event_count))
print("meeting hours:", meeting_hours, "-> type:", type(meeting_hours))
print("is active:", is_active, "-> type:", type(is_active))
member_number_text = str(member_number)
event_count_text = str(event_count)
points_text = str(points_earned)
status_text = str(is_active)
print("member number as text:", member_number_text, "-> type:", type(member_number_text))
print("event count as text:", event_count_text, "-> type:", type(event_count_text))
print("points as text:", points_text, "-> type:", type(points_text))
print("status as text:", status_text, "-> type:", type(status_text))
first_three = name[0:3]
last_letter = name[-1:]
badge_code = first_three + last_letter
print("first 3 letters of name:", first_three)
print("last letter of name:", last_letter)
print("badge Code:", badge_code)
reversed_club = club[::-1]
print("reversed club name:", reversed_club)
badge_line_1 = "club member" + badge_code.upper()
badge_line_2 = "id: " + member_number_text + " | EVENTS: " + event_count_text
badge_line_3 = "points: " + points_text + " | ACTIVE: " + status_text
badge_line_4 = "secret club code: " + reversed_club.upper()
print("")
print("school member badge")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("")