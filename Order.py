class Order:
  def __init__(self, cost, products, customer, type, driver) -> None:
      self.cost = cost
      self.products = products
      self.customer = customer
      self.type = type
      if (type == "Delivery"):
        self.driver = driver