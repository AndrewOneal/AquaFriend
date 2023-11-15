class Pet:
    state = "happy"

    def set_state(self, state):
        self.state = state

    def display_dog(self, state):
        if self.state == "happy":
            print(r"""       
               /^-^\
              / o o \
             /   Y   \
             V \ V / V
               / - \
              /    |
        (    /     |
         ===/___) ||""")
        elif self.state == "mid":
            print(r"""       
                       /^-^\
                      / o o \
                     /   Y   \
                     V \ _ / V
                       / - \
                      /    |
                    /     |
                ====/___) ||""")
        elif self.state == "sad":
            print(r"""       
                       /^-^\
                      / o o \
                     /   Y   \
                     V \ ^ / V
                       / - \
                      /    |
                    /     |
                ====/___) ||""")
        elif self.state == "dead":
            print(r"""       
                       /^-^\
                      / X X \
                     /   Y   \
                     V \ ^ / V
                       / - \
                      /    |
                     /     |
                ====/___) ||""")

class WaterIntake:
    totalOzWater = 0

class UserProfile:
    name = ""
    _weight = ""
    lifestyle = ""
    _lifestyleFactor = ""
    _daily_intake = ""

    def __init__(self, name, lifestyle):
        self.name = name
        self.lifestyle = lifestyle
        self.set_weight_from_input()
        self.set_lifestyle_factor(lifestyle)
        self.calc_daily_intake()

    def set_weight_from_input(self):
        try:
            self._weight = int(input("Please enter your weight in pounds: "))
        except ValueError:
            print("Error: Please enter a number")
            self.get_weight_from_input()


    def set_lifestyle_factor(self, lifestyle):
        if lifestyle == "a":
            factor = 1
        elif lifestyle == "s":
            factor = 0.75
        else:
            factor = 0.5
        self._lifestyleFactor = factor

    def calc_daily_intake(self):
        return self._weight * self._lifestyleFactor

    def print_user_profile(self):
        print("____User Profile____")
        print(f"Name: {self.name}")
        print(f"Weight: {self._weight} pounds")
        if self.lifestyle == "a":
            print("Lifestyle: active")
        elif self.lifestyle == "m":
            print("Lifestyle: moderately active")
        else:
            print("Lifestyle: sedentary")
        print(f"Recommended Daily Water Intake: {self._daily_intake}")

if __name__ == '__main__':

    print("Welcome to AquaFriend!")
    print("Please set up your user profile below")
    name = input("Please enter your name: ")
    lifestyle = ""
    while lifestyle not in ['a', 'm', 's']:
        lifestyle = input("Please select your lifestyle: (a)ctive, (m)oderately active, or (s)edentary:\n")
    userProf = UserProfile(name, lifestyle)
    print(userProf.calc_daily_intake())
    userProf.print_user_profile()