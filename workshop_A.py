quantity = 60
cost_price = 200
sell_price = 250
team_members = 5
income = quantity * sell_price
base_cost = quantity * cost_price
profit = income - base_cost
boss_share = profit / 20
crew_pay = (profit - boss_share) / team_members
print (income, base_cost, profit, boss_share, crew_pay)