class Category:
  
  def __init__(self, name):
    self.ledger = []
    self.name = name
  
  def __str__(self):
    lines = []
    name = "*"*int((30-len(self.name))/2) + self.name + "*"*int((30-len(self.name))/2) +"\n"
    lines.append(name)

    for t in self.ledger:
      description = t["description"]
      
      if len(description)>23:
        description = description[:23]

      amount = "{:.2f}".format(t["amount"])

      aux = description + " "*(23-len(description))+ " "*(7-len(amount)) + amount + "\n"
      lines.append(aux)
    
    lines.append("Total: {}".format(self.get_balance()))

    return ''.join(str(line) for line in lines)

  def get_balance(self):
    balance = 0.0
    for t in self.ledger:
      balance += float(t["amount"])
    return balance

  def deposit(self ,amount ,description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self ,amount ,description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def transfer(self,amount,category):
    if self.withdraw(amount,"Transfer to {}".format(category.name)):
      category.deposit(amount,"Transfer from {}".format(self.name))
      return True
    return False
  def check_funds(self,amount):
    return self.get_balance() - amount >=0
  
  def calculate_spent(self):
    spent = 0.0
    for t in self.ledger:
      if t["amount"]<0:
        spent += abs(t["amount"])

    return spent

def create_spend_chart(categories):
  lines = []
  lines.append("Percentage spent by category\n")
  total = sum(category.calculate_spent() for category in categories)
  
  percentages = []
  for category in categories:
    percentages.append((category.calculate_spent()/total)*100)
  
  for i in range(11):
    
    rowIndicator =" "*(3-len(str((10-i)*10)))+ str((10-i)*10)
    row = (10-i)*10
    lines.append("{}| {}  {}  {}  ".format(rowIndicator,getChar(percentages[0], row),getChar(percentages[1], row),getChar(percentages[2], row))+"\n")
  
  lines.append( "    "+"-"*10 + "\n")
  maxLength = max(len(category.name) for category in categories) 

  for i in range(maxLength):
    aux = ""
    if i<len(categories[0].name):
        aux += "     {}".format(categories[0].name[i]) 
    else:
      aux += "      " 

    if i<len(categories[1].name):
        aux += "  {}".format(categories[1].name[i])
    else:
      aux += "   "
    
    if i<maxLength-1:
      if i<len(categories[2].name):
        aux += "  {}  ".format(categories[2].name[i]) + "\n"
      else:
        aux += "     "+ "\n"
    elif i == maxLength-1:
      if i<len(categories[2].name):
        aux += "  {}  ".format(categories[2].name[i])
      else:
        aux += "     "
    
    lines.append(aux)

  return ''.join(str(line) for line in lines)

def getChar(percentage,row):
  if percentage >=row:
    return "o"
  return " "



 



