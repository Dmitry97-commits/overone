class Bank:
    def __init__(self,name,last_name,vklad,valuta,credit):
        self.__name = name
        self.__last_name = last_name
        self.__vklad = vklad
        self.__valuta = valuta
        self.__credit = credit

    def __str__(self):
        return f"Имя - {self.__name},Фамилия - {self.__last_name},Размер вклада - {self.__vklad},Валюта - {self.__valuta}," \
               f"Размер кредита - {self.__credit}"
    @property
    def name(self):
        return self.__name
    @property
    def last_name(self):
        return self.__last_name

    @property
    def vklad(self):
        return self.__vklad
    @vklad.setter
    def vklad(self,new_vklad):
        if new_vklad.isdigit():
            self.__vklad = new_vklad
        else:
            print("error")



    @property
    def valuta(self):
        return self.__valuta
    @valuta.setter
    def valuta(self,new_valuta):
        if new_valuta == "dollar" or "euro" or "ruble":
            self.__valuta = new_valuta



    @property
    def credit(self):
        return self.__credit
    @credit.setter
    def credit(self,new_credit):
        if new_credit.isdigit():
            self.__credit = new_credit
        else:
            print("error")




h = Bank("Ivan",'Petrov',"2000",'$',"50000")
print(h)
h.vklad = "400"
print(h.vklad)
print(h)
h.valuta="euro"
print(h)
h.credit = "70000000000000000"
print(h)