#ROI PROJECT
#Define classes
#Define class variables
#Create a constructor
#Implement methods
#Calculate_ROI
#Calculate_net_profits
#Calculate_total_investments
#display_results
#Input functions
#Create an instance of the class
#Rental Calculater

class RentalPropertyCalculator:
    def __init__(self, purchase_price, rental_income, expenses):
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.expenses = expenses

    def calculate_roi(self):
        net_profit = self.calculate_net_profit()
        total_investment = self.calculate_total_investment()
        roi = (net_profit / total_investment) * 100
        return roi

    def calculate_net_profit(self):
        return self.rental_income - self.expenses

    def calculate_total_investment(self):
        return self.purchase_price + self.expenses

    def display_results(self, roi):
        print("Return on Investment (ROI): {:.2f}%".format(roi))


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Gather property information from the user
purchase_price = get_float_input("Enter the purchase price of the property: ")
rental_income = get_float_input("Enter the monthly rental income: ")
expenses = get_float_input("Enter the monthly expenses: ")

#Step 11 create an instance
calculator = RentalPropertyCalculator(purchase_price, rental_income, expenses)

# Calculate ROI and display the results
roi = calculator.calculate_roi()
calculator.display_results(roi)

