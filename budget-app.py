#[1] creating our class
class Category:
    #[2] intializing our class
    def __init__(self, name):
        self.name = name
        self.ledger = []

    #[3] creating our deposit function
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    #[4] creating our withdraw function
    def withdraw(self, amount, description=''):
        #[8] checking if withdrawing is possible
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    #[5] creating our get_balance function
    def get_balance(self):
        total_balance = 0
        for transaction in self.ledger:
            total_balance += transaction['amount']
        return total_balance

    #[6] creating our transfer function
    def transfer(self, amount, destination):
        #[9] checking if withdrawing is possible
        if self.check_funds(amount):
            self.withdraw(amount, description=f'Transfer to {destination.name}')
            destination.deposit(amount, description=f'Transfer from {self.name}')
            return True
        else:
            return False

    #[7] creating our check_funds function
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    #[10] creating our category printing function
    def __str__(self):
        menu = self.name.center(30, '*') + '\n'
        for transaction in self.ledger:
            desc = transaction['description'][:23]
            amt = transaction['amount']
            menu += f'{desc:<23}{amt:>7.2f}\n'
        menu += f'Total: {self.get_balance()}'
        return menu

#[12] creating our create spend chart function
def create_spend_chart(categories):
    #[13] calculating the percentage
    total_spent = 0
    withdraws = []
    percentages = []
    
    for index, categorie in enumerate(categories):
        spent = 0
        for transaction in categorie.ledger:
            if transaction['amount'] < 0:
                total_spent += abs(transaction['amount'])
                spent += abs(transaction['amount'])
        withdraws.append(spent)
        
    for index, withdraw in enumerate(withdraws):
        percentage = int((withdraw / total_spent) * 10) * 10
        percentages.append(percentage)

    #[14] printing the chart
    chart = 'Percentage spent by category\n'
    line = len(categories) * '---' + '-'   
    for i in range(100, -10, -10):
        chart += f'{i:>3}| '
        for percentage in percentages:
            if percentage >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
        
    chart += f'    {line}\n'

    #[15] printing the names at the bottom of the chart
    max_length = 0
    for categorie in categories:
        if len(categorie.name) > max_length:
            max_length = len(categorie.name)
    for j in range(max_length):
        chart += '     '  
        for categorie in categories:
            if len(categorie.name) - 1 >= j:
                chart += f'{categorie.name[j]}  ' 
            else: 
                chart += '   '
        if j != max_length - 1:
            chart += '\n'
    return chart

#[11] our testing data
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
clothing.deposit(1000, "initial deposit")
auto.deposit(1000, "initial deposit")

food.withdraw(60, "groceries")
clothing.withdraw(20, "shoes")
auto.withdraw(10, "gas")

#[16] calling our data
print(food, '\n')
print(clothing, '\n')
print(auto, '\n')
print(create_spend_chart([food, clothing, auto]))