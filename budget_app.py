# Create a Budget class that can instantiate objects based on different budget categories like food,
# clothing, and entertainment. These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories

class Budget:
    
    def __init__(self, food_budget, clothing_budget, entertainment_budget):
        self.food = food_budget
        self.clothing = clothing_budget
        self.entertainment = entertainment_budget
        
    def deposit(self, amount):
        print("1.FOOD")
        print("2.CLOTHING")
        print("3.ENERTAINMENT")
        deposit = int(input("Select the category you want to make a deposit in: "))
        if deposit == 1:
            self.food += amount
            print(f"Food budget balance is {self.food}")
        elif deposit == 2:
            self.clothing += amount
            print(f"Cloth budget balance is {self.clothing}")
        elif deposit == 3:
            self.entertainment += amount
            print(f"Entertainment budget balance is {self.entertainment}")
        else:
            print("Invalid category!")
            
    def withdraw(self, amount):
        print("1.FOOD")
        print("2.CLOTHING")
        print("3.ENERTAINMENT")
        withdrawal = int(input("Select the category you want to make a withdrawal on: "))
        if withdrawal == 1:
            if amount > self.food:
                print("Insufficient balance, Enter lesser amount")
            else:
                self.food -= amount
                print(f"Food budget balance is {self.food}")
        elif withdrawal == 2:
            if amount > self.clothing:
                print("Insufficient balance, Enter lesser amount")
            else:
                self.clothing -= amount
                print(f"Cloth budget balance is {self.clothing}")
        elif withdrawal == 3:
            if amount > self.entertainment:
                print("Insufficient balance, Enter lesser amount")
            else:
                self.entertainment -= amount
                print(f"Entertainment budget balance is {self.entertainment}")
        else:
            print("Invalid category!")
    
    
    def balance(self):
        print("1.FOOD")
        print("2.CLOTHING")
        print("3.ENERTAINMENT")
        balance = int(input("Select the category in which you want to check the balance: "))
        if balance == 1:
            print(f"Your food budget balance is #{self.food}")
        elif balance == 2:
            print(f"Your clothing budget balance is #{self.clothing}")
        elif balance == 3:
            print(f"Your entertainment budget balance is #{self.entertainment}")
        else:
            print("Invalid category!")  
            
               
    def transfer(self):    
        print("1.FOOD")
        print("2.CLOTHING")
        print("3.ENERTAINMENT")
        transfer_to = int(input("Which of the category do you want to transfer to? "))
        transfer_from = int(input("Which of the category do you want to transfer from?"))
        if transfer_to == 1 and transfer_from == 2:
            self.food += self.clothing
            self.clothing -= self.clothing
            print(f"Your food budget balance is #{self.food}")
            print(f"Your clothing budget balance is #{self.clothing}")
        elif transfer_to == 1 and transfer_from == 3:
            self.food += self.entertainment
            self.entertainment -= self.entertainment
            print(f"Your food budget balance is #{self.food}")
            print(f"Your entertainment budget balance is #{self.entertainment}")
        elif transfer_to == 2 and transfer_from == 1:
            self.clothing += self.food
            self.food -= self.food
            print(f"Your clothing budget balance is #{self.clothing}")
            print(f"Your food budget balance is #{self.food}")
        elif transfer_to == 2 and transfer_from == 3:
            self.clothing += self.entertainment
            self.entertainment -= self.entertainment
            print(f"Your clothing budget balance is #{self.clothing}")
            print(f"Your entertainment budget balance is #{self.entertainment}")
        elif transfer_to == 3 and transfer_from == 1:
            self.entertainment += self.food
            self.food -= self.food
            print(f"Your food budget balance is #{self.food}")
            print(f"Your entertainment budget balance is #{self.entertainment}")
        else:
            self.entertainment += self.clothing
            self.clothing -= self.clothing
            print(f"Your clothing budget balance is #{self.clothing}")
            print(f"Your entertainment budget balance is #{self.entertainment}")
        
            
budget_1 = Budget(10000, 20000, 30000)

# print(budget_1.deposit(50000))
# print(budget_1.food)
# print(budget_1.balance())
print(budget_1.transfer())