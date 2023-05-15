#simple class 
class pokemon :
    #__init__ are the built in or magic function
    def __init__(self,name,age,weight):
        ##we have called 3 attributes name(pikachu,age,weight)
        self.name=name
        self.age=age
        self.weight= weight
    
    #defining the 3 mathodes (get_name,get_age,get_weight)
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_weigth(self):
        return self.weight
    
#defining object(my_pokemon) from class (pokemon)
my_pokemon= pokemon("Pikcachu",20,"5kg")

print(my_pokemon.get_name())
print(my_pokemon.get_age())
print(my_pokemon.get_weigth())   
