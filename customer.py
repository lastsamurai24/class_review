"""
#c-1
class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()
print(ken.full_name())
tom = Customer(first_name="Tom", family_name="Ford")
tom.full_name()
print(tom.full_name())
"""

"""
#c-2
class Customer:
    def __init__(self, first_name, family_name,age):
        self.age= age
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        return f"{self.first_name} {self.family_name}"
    
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.full_name
ken.age  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.full_name
tom.age # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.full_name
ieyasu.age # 73 という値を返す
print(ken.full_name(),ken.age)
print(tom.full_name(),tom.age)
print(ieyasu.full_name(),ieyasu.age)
"""
"""
#c-3
class Customer: 

    def __init__(self, first_name, family_name,age):
        self.age= age
        self.first_name = first_name
        self.family_name = family_name
        self.name = first_name + " " + family_name

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self,):
        if self.age < 20 :
            return 1000
        elif 20 <= self.age < 65 :
            return 1500
        elif 65 < self.age :
            return 1200
"""
"""        
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.full_name()
ken.age
ken.entry_fee()  # 1000 という値を返す
print(ken.full_name(),ken.age, ken.entry_fee())
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.full_name()
tom.age
tom.entry_fee() # 1500 という値を返す
print(tom.full_name(),tom.age, tom.entry_fee())
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.full_name()
ieyasu.age
ieyasu.entry_fee() # 1200 という値を返す
print(ieyasu.full_name(),ieyasu.age, ieyasu.entry_fee())
"""
"""
#c-4
class Customer:
    def __init__(self, first_name, family_name, age=None):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
        self.name = first_name + " " + family_name

    def entry_fee(self):
        if self.age is None:
            return None
        if self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 65 <= self.age:
            return 1200

    def info_csv(self):
        fee = self.entry_fee()
        fee_str = str(fee)
        
        return f"{self.name},{self.age},{fee_str}"
    
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())
"""