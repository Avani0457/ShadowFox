# Initial List
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)
# 1. Number of members
count_members = len(justice_league)
print("\n1. Number of members:", count_members)
# 2. Batman recruits Batgirl & Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2. After adding Batgirl & Nightwing:", justice_league)
# 3. Wonder Woman becomes leader (move to start)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. Wonder Woman becomes leader:", justice_league)
# 4. Separate Aquaman & Flash by inserting Superman OR Green Lantern
# Let's choose Superman
justice_league.remove("Superman")
index_aquaman = justice_league.index("Aquaman")
justice_league.insert(index_aquaman, "Superman")
print("\n4. After separating Aquaman & Flash:", justice_league)
# 5. Replace with a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n5. New Justice League team assembled by Superman:", justice_league)
# 6. Sort alphabetically and select new leader
justice_league.sort()
print("\n6. Sorted Justice League:", justice_league)
print("New Leader (index 0):", justice_league[0])
