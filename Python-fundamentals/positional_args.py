#arguments example args
def user_info(name,age,city):
    """This prints all the user info"""
    print("{} is {} years old, from {}".format(name,age,city))

user_info("Janet",59,"Oklahoma Ciy")

#this will error out
#user_info(34,"New York")

#this is example of kwargs

def user_info_new(name,age=0,city="London"):
    print("{} is {} years old, from {}".format(name,age,city))

user_info_new("Russell",56,"Chicago")

#this will not error out
user_info_new("Micah")
user_info_new(age=24,name="Nadeem")

def new_applicaton(fname,lname,email,company,*args,**kwargs):
    print("{} {} works at {}. Her email is {}".format(fname,lname,company,email))

new_applicaton("Jess","Ingress","test@test.com","Mckinsey",60000,hire_date="Dec 2019")