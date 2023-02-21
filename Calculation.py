

class ROI_calculator:
    def __init__(self):
        self.property_value = 0
        self.down_payment = 0
        self.loan_amount = 0
        self.interest_rate = 0
        self.loan_term = 0
        self.rent_income = 0
        self.other_income = 0
        self.vacancy_rate = 0
        self.property_tax = 0
        self.insurance = 0
        self.repairs_maintenance = 0
        self.capital_expenditures = 0
        self.management_fees = 0
        self.utilities = 0
        self.hoa_fees = 0
        self.other_expenses = 0
        self.roi = 0



    def property_information(self):
        street = input("What is the property street address? ")
        if street:
            city = input("What is the name of the city where your property is located? ")
            if city:
                state = input("What state is your property located in? ")
                if state:
                    zipcode = input("What is the zipcode where your property is located? ")
                    if zipcode:
                        print(street, city, state, zipcode)
                    else:
                        print("Please enter the correct zipcode where your property is located.")
                else:
                    print("Please enter the correct state where your property is located.")
            else:
                print("Please enter the correct city where your property is located.")
        else:
            print("Please enter the correct street address for your property.")

    def loan_details(self):
        purchase_method = input("Are you purchasing this property with cash or a loan? ")
        if purchase_method.lower() == "cash":
            self.down_payment = eval(input("What is your down payment? "))
            self.property_value = eval(input("What is the property value? "))
        elif purchase_method.lower() == "loan":
            self.loan_amount = eval(input("What is your loan amount? "))
            at_closed = self.loan_amount * .03
            closing = input(f"Is this the amount you paid at closing? {at_closed} ")
            if closing.lower() == "yes":
                    self.down_payment = eval(input("What is your down payment? "))
                    self.interest_rate = float(input("What is your interest rate? "))
                    self.loan_term = int(input("What is the length of your loan in years? "))
                    if self.loan_term == self.loan_term:
                        self.rent_income = eval(input("What is the monthly rent income? "))
                        self.other_income = eval(input("What is the monthly income from other sources? "))
                        self.vacancy_rate = float(input("What is the vacancy rate as a decimal (e.g. 0.05)? "))
                        self.property_tax = eval(input("What is the monthly property tax? "))
                        self.insurance = eval(input("What is the monthly insurance cost? "))
                        self.repairs_maintenance = eval(input("What is the monthly cost of repairs and maintenance? "))
                        self.capital_expenditures = eval(input("What is the monthly cost of capital expenditures? "))
                        self.management_fees = eval(input("What is the monthly cost of property management fees? "))
                        if self.utilities ==self.utilities:
                            gross_income = self.rent_income + self.other_income
                            total_expenses = self.property_tax + self.insurance + (self.repairs_maintenance / 100) * self.property_value + \
                                             self.capital_expenditures + self.management_fees + self.utilities + self.hoa_fees + self.other_expenses
                            net_income = gross_income * (1 - self.vacancy_rate) - total_expenses
                            annual_cash_flow = net_income * 12
                            total_investment = self.down_payment + (self.loan_amount * (self.interest_rate / 12) * ((1 + (self.interest_rate / 12)) ** (self.loan_term * 12))) - self.loan_amount
                            self.roi = (annual_cash_flow / total_investment) * 100
            elif closing.lower() == "no":
                closing_costs = eval(input("What are your closing costs? "))
                if closing_costs:
                    self.down_payment = eval(input("What is your down payment? "))
                    self.interest_rate = float(input("What is your interest rate? "))
                    self.loan_term = int(input("What is the length of your loan in years? "))
                    if self.loan_term == self.loan_term:
                        self.rent_income = eval(input("What is the monthly rent income? "))
                        self.other_income = eval(input("What is the monthly income from other sources? "))
                        self.vacancy_rate = float(input("What is the vacancy rate as a decimal (e.g. 0.05)? "))
                        self.property_tax = eval(input("What is the monthly property tax? "))
                        self.insurance = eval(input("What is the monthly insurance cost? "))
                        self.repairs_maintenance = eval(input("What is the monthly cost of repairs and maintenance? "))
                        self.capital_expenditures = eval(input("What is the monthly cost of capital expenditures? "))
                        self.management_fees = eval(input("What is the monthly cost of property management fees? "))
                        self.utilities = eval(input("What is the monthly cost of utilities"))
                        if self.utilities ==self.utilities:
                            gross_income = self.rent_income + self.other_income
                            total_expenses = self.property_tax + self.insurance + (self.repairs_maintenance / 100) * self.property_value + \
                                             self.capital_expenditures + self.management_fees + self.utilities + self.hoa_fees + self.other_expenses
                            net_income = gross_income * (1 - self.vacancy_rate) - total_expenses
                            annual_cash_flow = net_income * 12
                            total_investment = self.down_payment + (self.loan_amount * (self.interest_rate / 12) * ((1 + (self.interest_rate / 12)) ** (self.loan_term * 12))) - self.loan_amount
                            self.roi = (annual_cash_flow / total_investment) * 100


                else:
                    print("Please enter a valid closing cost.")
            else:
                print("Please enter a valid amount paid at closing.")
        else:
            print("Please enter a valid purchase method.")


calcuter = ROI_calculator()
calcuter.property_information()
calcuter.loan_details()
calcuter.loan()
calcuter.calculate()