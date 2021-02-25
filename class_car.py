class Car:
    def __init__(self,color,wheel,door,owner):
        self.color = color
        self.wheel = wheel
        self.door = door
        self.owner = owner

    def __str__(self):
        return (f"Ваша машина имеет : Цвет - {self.color},Количество колес - {self.wheel}" 
               f", Количество дверей - {self.door}, Владелец - {self.owner}")

    def Color(self,new_color):
        self.color = new_color
        return print(f"Ваша машина изменила свой цвет с {self.color} на {new_color}")

