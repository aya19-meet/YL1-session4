##class Animal(object):
##    def __init__(self,sound,name,age,fav_color):
##        self.sound = sound
##        self.name = name
##        self.age = age
##        self.fav_color = fav_color
##    def eat(self,food):
##        print('Yummy!! ' + self.name + ' is eating ' + food)
##    def description(self):
##        print(self.name + ' is ' + self.age + " years old and loves the color " + self.fav_color)
##    def make_sound(self,times):
##        print(self.name + " : " + self.sound*times)
##Bruno = Animal("bark","Bruno",'2',"pink")
##
##Bruno.eat("apples")
##
##Bruno.description()
##
##Bruno.make_sound(5)
##

##class person(object):
##    def __init__(self,name,age,city,gender,bf,sport):
##        self.name = name
##        self.age = age
##        self.city = city
##        self.gender = gender
##        self.bf = bf
##        self.sport = sport
##    def eat(self):
##        print(self.name + " is eating " + self.bf)
##    def play_sport(self):
##        print(self.name + ' loves ' + self.sport)
##
##              
##Juan = person("Juan", 17 , "New Mexico" , "Male" , "pancakes", "swimming")
##            
##Juan.eat()
##Juan.play_sport()

class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing(self):
        print(self.lyrics)

panda = song('panda,panda,panda')

panda.sing()



