class Human:
    default_name = "aaaaa"
    default_age = 18
    default_money = 500
    default_house = False
    def __init__(self,name = default_name, age = default_age, money = default_money,house = default_house):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house
    def __str__(self):
        return f"{self.name},{self.age},{self.__money},{self.__house}"

    @staticmethod
    def default_info():
        print( f"{Human.default_name},{Human.default_age}")

    def __make_deal(self,house,price):
        if self.__money >= price:
            self.__money - int(price)
            return f"Ваш дом - {house}"

    def earn_money(self,money):
        self.__money=self.__money + money
        return self.__money

    def buy_house(self,price,size_of_discount):
        price_with_disc = price - (price * size_of_discount)
        if self.__money < price_with_disc:
            print("Недостаточно денег")
        else:
            self.__money = self.__money - price_with_disc
            self.__house = True
            print("Дом куплен")


class House:
    def __init__(self,_area,_price):
        self.area = _area
        self.price = _price
    def final_price(self,sise_of_discount):
        return self.price-(self.price * sise_of_discount)

class SmallHouse(House):
    __area = 40
    def __init__(self,_price):
        super().__init__(SmallHouse.__area, _price)

human = Human()
print(human)
house = SmallHouse(501)
human.buy_house(house.price,0.25)
print(human)
human.earn_money(500)
print(human)
