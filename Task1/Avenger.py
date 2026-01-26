class Avenger:
    def __init__(self,name,age,gender,superpower,weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.superpower = superpower
        self.weapon = weapon
    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Super Power: {self.superpower}")
        print(f"Weapons: {self.weapon}")
        print("-" * 40)
    def is_leader(self):
        if self.name == "Captain America":
            print(f"{self.name} is the leader of the Avengers.")
        else:
            print(f"{self.name} is not the leader.")
avenger1 = Avenger("Captain America", 105, "Male", "Super strength", "Shield")
avenger2 = Avenger("Iron Man", 48, "Male", "Technology", "Armor")
avenger3 = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
avenger4 = Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon")
avenger5 = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
avenger6 = Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")
super_heroes = [avenger1, avenger2, avenger3, avenger4, avenger5, avenger6]
for hero in super_heroes:
    hero.get_info()
    hero.is_leader()
    print()

        
        
        