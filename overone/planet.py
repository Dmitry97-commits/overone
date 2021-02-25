class Planeta:
    def __init__(self,size,name,color,race):
        self.size = size
        self.name = name
        self.color = color
        self.race = race
    def __str__(self):
        return f"Имя - {self.name}, Размер - {self.size}, Цвет - {self.color}, Раса - {self.race}"
    def new_race(self,new_race):
        self.race = new_race
    def crush(self,name_pl):
        if self.name == name_pl:
            del(self)
            print("плнета ууничтожена")


planeta1=Planeta(123,"dirol","blue",'da')
print(pl