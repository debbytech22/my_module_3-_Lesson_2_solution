class car:
    def __init__(self,colour,brand,model,engine_number,plate_number):
        self.colour=colour
        self.brand=brand
        self.model=model
        self.engine_number=engine_number
        self.plate_number=plate_number
    def reverse(self):
       return self.plate_number  +"," + "Pls use the side mirror to avoid accident" 
    def speed(self,km):
        print("stop")
    def wind_down(self,):
        return self.brand +" "+self.model+"," +" "+ "Children in car pls wind up"
    def Run(self,km):
        return "The car is running at" +" "+ str(km) +"km" + " " + "pls slow down"
    def Turn(self,direction):
        return "The" + " " + self.colour +  " " + "car is reversing in" +" " + direction +" "+ "direction"
Car_1=car("red","Toyota","SUV_2016",33443, 1234)
print(Car_1.Turn("right"))
Car_2=car("blue","Volks wagen",2019, 633, "IKD_675_LS")
print(Car_2.colour)
print(Car_2.Run(150))
print(Car_2.reverse())
print(Car_1.wind_down())