class MobilePhone:
    def __init__(self,screen_type,network_type,dual_sim,front_camera,rear_camera,ram,storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, number):
        print(f"Receiving call from {number}...")

    def take_picture(self):
        print(f"Taking picture with {self.rear_camera} rear camera...")


class Apple(MobilePhone):
    def __init__(self, model, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def show_details(self):
        print(f"Apple Model   : {self.model}")
        print(f"Network       : {self.network_type}")
        print(f"Dual SIM      : {self.dual_sim}")
        print(f"Front Camera  : {self.front_camera}")
        print(f"Rear Camera   : {self.rear_camera}")
        print(f"RAM           : {self.ram}")
        print(f"Storage       : {self.storage}")
        print("-" * 40)


class Samsung(MobilePhone):
    def __init__(self, model, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def show_details(self):
        print(f"Samsung Model : {self.model}")
        print(f"Network       : {self.network_type}")
        print(f"Dual SIM      : {self.dual_sim}")
        print(f"Front Camera  : {self.front_camera}")
        print(f"Rear Camera   : {self.rear_camera}")
        print(f"RAM           : {self.ram}")
        print(f"Storage       : {self.storage}")
        print("-" * 40)


# Creating Apple Mobile Objects
apple1 = Apple("iPhone SE", "4G", False, "8MP", "12MP", "3GB", "64GB")
apple2 = Apple("iPhone 12", "5G", False, "12MP", "12MP", "4GB", "128GB")

# Creating Samsung Mobile Objects
samsung1 = Samsung("Galaxy A30", "4G", True, "12MP", "32MP", "4GB", "64GB")
samsung2 = Samsung("Galaxy S21", "5G", True, "16MP", "48MP", "8GB", "128GB")

# Showing details of each phone
apple1.show_details()
apple2.show_details()
samsung1.show_details()
samsung2.show_details()

# Testing functionalities
apple1.make_call("9876543210")
apple2.take_picture()
samsung1.receive_call("9988776655")
        