class phonecontacts():

    def __init__(self,s,p,l,r,h,e,i,f,ff):

        self.__simcontacts=s
        self.__phonecontacts=p
        self.__log=l
        self.__recent=r
        self.__history=h
        self.__exportcontacts=e
        self.__importcontacts=i
        self.__find=f
        self.favourites=ff

    def display(self):

        self.__picture="choose from gallery" or "take photo"
        print("insert photo")

        self.__contact="phone number"
        print("enter phone number")

        self.__email="email id"
        print("enter email id")

        self.__group="home" or "education" or "office"
        print("create group")

        self.__link="link number"
        print("link with email")

        self.__options="existing number" or "new number"
        print("create number")


owner= phonecontacts("sim contacts","phone contacts","log","recent","history","export contacts","import contacts","find","favourites")
owner.display()


if ("len of phonenumber" "<10"):
    raise ValueError ("Invalid number")
elif print("save"):
    if ("number already exists"):
        raise TypeError("already exists")

elif print("number successfully created"):

    print ("end")
    
        
        
