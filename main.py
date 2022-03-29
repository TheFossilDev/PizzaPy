import User


class Ref:
  def __init__(self, name, age, balance) -> None:
    # Reminder about arrow syntax: It is purely documentation to indicate return type
      self.name = name
      self.age = age
      self.balance = balance

  def send(self):
    print(f"Name: {self.name}. Age: {self.age}. Balance: {self.balance}.")


Adam = Ref("Adam", 15, 0)
Adam.send()

John = User.User("John")
print(John.name)