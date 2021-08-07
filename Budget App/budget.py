class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        pass
    
    def __str__(self):
        result = ""
        result += self.name.center(30,'*') + "\n"
        cash = 0
        for items in self.ledger:
            result += f"{items['description'][:23]:23}" + "{:.2f}".format(items["amount"]).rjust(7) + "\n"
            cash += items["amount"]
        result += f"Total: {cash:.2f}"
        return result
        pass

    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})
        pass
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
        pass

    def get_balance(self):
        total_money = 0
        for objects in self.ledger:
            total_money += objects["amount"]
        return total_money
        pass
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
        pass

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, description =  "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False
        pass

def round_down(num):
        temp = num % 10
        return num - temp

def create_spend_chart(categories):
    spent_list = []
    total_spent = 0
    for category in categories:
        temp_spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                temp_spent += item['amount']
                total_spent += -item['amount']
        spent_list.append(-temp_spent)
    
    for i in range(len(spent_list)):
        spent_list[i] = round_down((spent_list[i] / total_spent)*100)

    final_str = "Percentage spent by category\n"

    for i in range(100, -10, -10):
        final_str += (str(i)).rjust(3) + "| "
        for j in range(len(spent_list)):
            if spent_list[j] >= i:
                final_str += 'o  '
            else:
                final_str += '   '
        final_str += '\n'

    final_str += '    ' + ('-') * (len(spent_list)*3+1) + '\n'

    max_len = 0
    
    for category in categories:
        if len(category.name) > max_len:
            max_len = len(category.name)

    extended_categories = []
    
    for category in categories:
        category.name += ' '*(max_len - len(category.name))
        extended_categories.append(category.name)
        
    for index in range(max_len):
        final_str += ' '*5
        
        for category in extended_categories:
            final_str += category[index] + '  '
        
        final_str += '\n'

    return final_str[:-1]

    pass