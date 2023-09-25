"""class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        return f"{self.first_name} {self.family_name}"
    def entry_fee(self,):
        if self.age < 20 :
            return 1000
        elif 20 <= self.age < 65 :
            return 1500
        elif 65 < self.age :
            return 1200
    def info_csv(self):
"""


"""
c-1
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
c-2
class Customer:
    def __init__(self, first_name, family_name,age):
        self.age= age
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.age  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.age # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.age # 73 という値を返す
print(ken.age)
print(tom.age)
print(ieyasu.age)
"""

"""
c-3
class Customer: 
    def __init__(self, first_name, family_name,age):
        self.age= age
    def entry_fee(self,):
        if self.age < 20 :
            return 1000
        elif 20 <= self.age < 65 :
            return 1500
        elif 65 < self.age :
            return 1200
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す
print(f"kenは{ken.entry_fee()}円です")
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
tom.entry_fee() # 1500 という値を返す
print(f"tomは{tom.entry_fee()}円です")
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee() # 1200 という値を返す
print(f"ieyasuは{ieyasu.entry_fee()}円です")
"""