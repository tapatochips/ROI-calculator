# #this apps purpose is to calculate return investment on rental properties.
# #income from property
# rental_income = float(input("How much is the tenent paying in rent a month? "))
# laundry_etc = float(input("How much is the tenent paying in laundry expenses etc if any? "))
# #expenses from property
# taxes = float(input("How much are your monthly taxes on the property? "))
# insurance = float(input("How much does the insurance cost on the property? "))
# #if the tenent pays for their own utilities then just say 0 for utilities, otherwise, input the cost of them
# utilities = float(input("How much do the utilities cost every month? "))
# hoa_lawn_snow = float(input("How much, if any, does the lawn and or HOA cost every month? "))
# vac_repair_CapEX = float(input("How much are you saving for vacancy, repairs, capital expenses? "))
# property_management = float(input("How much are you paying a property manager if you have one? "))
# mortgage = float(input("How much is the mortgage? "))

# income = rental_income + laundry_etc
# expenses = taxes + insurance + utilities + hoa_lawn_snow + vac_repair_CapEX + property_management + mortgage

# total_monthly_cash_flow = income - expenses

# down_payment = float(input("What was the amount of the downpayment if any? "))
# closing = float(input("How much did the closing costs cost? "))
# rehab_budget = float(input("How much did you pay to restore the property at th start? "))
# other = float(input("How much else if any, did you put in the property at the start? "))

# total_investment_start = down_payment + closing + rehab_budget + other

# yearly_cash_flow = total_monthly_cash_flow * 12

# return_of_investment = yearly_cash_flow / total_investment_start * 100
"""
above was my original idea for the program, and then i rememembered the instructions stated to do the project using OOP, so everything below is the same but OOP friendly.
"""


class RentalProperty:
    def __init__(self, rental_income, laundry_etc, taxes, insurance, utilities, hoa_lawn_snow, vac_repair_capex, property_management, mortgage, down_payment, closing_costs, rehab_budget, other):
        self.rental_income = rental_income
        self.laundry_etc = laundry_etc
        self.taxes = taxes
        self.insurance = insurance
        self.utilities = utilities
        self.hoa_lawn_snow = hoa_lawn_snow
        self.vac_repair_capex = vac_repair_capex
        self.property_management = property_management
        self.mortgage = mortgage
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.other = other

    def calculate_cash_flow(self):
        income = self.rental_income + self.laundry_etc
        expenses = self.taxes + self.insurance + self.utilities + self.hoa_lawn_snow + self.vac_repair_capex + self.property_management + self.mortgage
        total_monthly_cash_flow = income - expenses
        yearly_cash_flow = total_monthly_cash_flow * 12
        return yearly_cash_flow

    def calculate_return_on_investment(self):
        total_investment_start = self.down_payment + self.closing_costs + self.rehab_budget + self.other
        yearly_cash_flow = self.calculate_cash_flow()
        return_on_investment = yearly_cash_flow / total_investment_start * 100
        return return_on_investment

#gets info from the property owner/land-lord
rental_income = float(input("How much is the tenant paying in rent a month? "))
laundry_etc = float(input("How much is the tenant paying in laundry expenses etc if any? "))
taxes = float(input("How much are your monthly taxes on the property? "))
insurance = float(input("How much does the insurance cost on the property? "))
utilities = float(input("How much do the utilities cost every month? "))
hoa_lawn_snow = float(input("How much, if any, does the lawn and or HOA cost every month? "))
vac_repair_capex = float(input("How much are you saving for vacancy, repairs, capital expenses? "))
property_management = float(input("How much are you paying a property manager if you have one? "))
mortgage = float(input("How much is the mortgage? "))
down_payment = float(input("What was the amount of the down payment if any? "))
closing_costs = float(input("How much did the closing costs cost? "))
rehab_budget = float(input("How much did you pay to restore the property at the start? "))
other = float(input("How much else if any, did you put in the property at the start? "))

#creates the rental propery
property = RentalProperty(rental_income, laundry_etc, taxes, insurance, utilities, hoa_lawn_snow, vac_repair_capex, property_management, mortgage, down_payment, closing_costs, rehab_budget, other)

#calcs and returns the ROI
roi = property.calculate_return_on_investment()
print("The return on investment for the property is:", roi, "%")
