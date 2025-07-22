Funds=2500

budgets={}

expenses={}

def AddBudget (Name, Ammount):
    global Funds
    budgets[Name]=Ammount
    Funds-=Ammount
