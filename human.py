class Human:
    def __init__(self,color_of_eye,color_of_hair,race,name):
        self.color_of_eye = color_of_eye
        self.color_of_hair = color_of_hair
        self.race = race
        self.name = name

    def __str__(self):
        return f"Имя - {self.name}, Цвет волос -{self.color_of_hair} , Цвет глаз -{self.color_of_eye} , " \
               f"Раса -{self.race} "

    def rodina(self):
        if self.race == "Asian":
            return f"Asia"
        if self.race == "European":
            return f"Europe"
        if self.race == "Negroid":
            return f"Africa"
        else:
            return f"from Australia or not from Earth"


h1 = Human("blue",'black',"ttyy","Leon")
print(h1)
print(h1.rodina())