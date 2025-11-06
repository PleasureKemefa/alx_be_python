monthly_income = int(input("Enter your monthly income:"))
total_monthly_expenses = int(input("Enter your monthly expenses:"))

monthly_savings = monthly_income - total_monthly_expenses

simple_annual_interest = 0.05

projected_saving = monthly_savings * 12 + (monthly_savings * 12 * 0.05)


print(monthly_savings)
print("Your monthly saving are", monthly_savings)
print("Projected savings after one year, with interest, is:", projected_saving)
