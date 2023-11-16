import time

class Pet:
    state = "sad"

    def set_state(self, state):
        self.state = state

    def display_dog(self):
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
    _goal_intake = ""
    _total_intake = 0

    def __init__(self, name, lifestyle):
        self.name = name
        self.lifestyle = lifestyle
        self.set_weight_from_input()
        self.set_lifestyle_factor(lifestyle)
        self.set_goal_intake()

    def set_weight_from_input(self):
        try:
            self._weight = int(input("Please enter your weight in pounds: "))
        except ValueError:
            print("Error: Please enter a number")
            self.get_weight_from_input()


    def set_lifestyle_factor(self, lifestyle):
        if lifestyle == "a":
            factor = 0.9
        elif lifestyle == "s":
            factor = 0.65
        else:
            factor = 0.4
        self._lifestyleFactor = factor

    def set_goal_intake(self):
        self._goal_intake = self._weight * self._lifestyleFactor

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
        print(f"Recommended Daily Water Intake: {self._goal_intake}")

    def add_intake(self, intake):
        print("Intake Recorded!")
        self._total_intake += intake

if __name__ == '__main__':
    dog = Pet()

    print("Welcome to AquaFriend!")
    print("Please set up your user profile below")
    name = input("Please enter your name: ")
    lifestyle = ""
    while lifestyle not in ['a', 'm', 's']:
        lifestyle = input("Please select your lifestyle: (a)ctive, (m)oderately active, or (s)edentary:\n")
    userProf = UserProfile(name, lifestyle)
    userProf.set_goal_intake()
    userProf.print_user_profile()

    while True:
        intake = int(input("Please input your water intake for the hour in fluid ounces: "))
        userProf.add_intake(intake)
        if userProf._total_intake < (0.25 * userProf._goal_intake):
            dog.set_state("dead")
            print("Keep drinking! Your pet is sick :-(")
        elif userProf._total_intake < (0.5 * userProf._goal_intake):
            dog.set_state("sad")
            print("Good progress! Your pet is still sad however")
        elif userProf._total_intake < (0.99 * userProf._goal_intake):
            dog.set_state("mid")
            print("Almost there, your pet is content")
        elif userProf._total_intake >= userProf._goal_intake:
            dog.set_state("happy")
            print("Your reached your goal! Your pet is happy! :-)")

        dog.display_dog()
        
        time.sleep(10)