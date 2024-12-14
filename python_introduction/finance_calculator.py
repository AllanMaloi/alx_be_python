monthly_income = float(input("Enter your mothly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))
monthly_savings = monthly_expenses - monthly_income
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)
print(f"\nYour monthly savings: {monthly_savings:.2f}")
print(f"Projected annual savings after 5% interest: {projected_annual_savings:.2f}")
