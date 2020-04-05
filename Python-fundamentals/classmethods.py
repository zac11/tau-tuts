import random


class Person:
    def __init__(self,firstname,lastname,health,status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def intrdocue(self):
        print("Hi I'm {} {}.".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion ==1:
            print("{} is happy today".format(self.firstname))


        elif emotion ==2:
            print("{} is not happy today".format(self.firstname))


    def statuschange(self):
        if self.health ==100:
            print("{} is perfectly fine".format(self.firstname))

        elif self.health >=76:
            print("{} is little tired today".format(self.firstname))

        elif self.health >=51:
            print("{} feels unwell".format(self.firstname))

        elif self.health >=40:
            print("{} is not well and needs to go to the doctor".format(self.firstname))

        else:
            print("{} is unconsious. Please call 911")
class Enemy(Person):
    def __init__(self,weapon,firstname, lastname,health,status):
        super().__init__(firstname,lastname,health,status)
        self.weapon = weapon


    def hurt(self,other):
        if self.weapon == "ak47":
            other.health = 0
            print("Person has died.")

        elif self.weapon == "rock":
            other.health -= 10

        elif self.weapon == "stick":
            other.health -= 5


        print(other.health)

    def insult(self,other):
        if other.health<=80:
            print("{}, you are tried and weak".format(other.firstname))

        if other.health >=81:
            print("{}, No need to show off".format(other.firstname))


    def steal(self,other):
        print("ha ha ha , {}, I have all of your stuff".format(other.firstname))

        if other.status == True:
            other.status = False

Maria = Person("Maria","Krimesky", 56 ,status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Carl = Person("Carl","Ray Jr.",90, status=True)
print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))
print("{} is my friend? {}".format(Carl.firstname, Carl.status))

print(Maria.intrdocue())
print(Rey.intrdocue())
print(Carl.intrdocue())

Alex = Enemy("ak47",'Bruce',"Wayne",75, status=True)

Alex.hurt(Maria)
Alex.insult(Rey)