#ACTIVITY 1: DESIGN YOUR OWN CLASS

from abc import ABC, abstractmethod

class Phone(ABC):
    #abstraction
    @abstractmethod
    def spec(self): #polymorphism each class implements
        pass

class Samsung(Phone):
    #constructors
    def __init__(self,type,ram,year,rom):
        self.type=type
        self.ram=ram
        self.year=year
        self.rom=rom

    def spec(self):
          return f"This is a Samsung {self.type} with {self.ram}GB RAM and {self.rom}GB storage, from the year {self.year}"

class Iphone(Phone):
    #constructor
    def __init__(self,type,ram,year,rom):
        self.type=type
        self.ram=ram
        self.year=year
        self.rom=rom

    def spec(self):
         return f"This is an {self.type} with {self.ram}GB RAM and {self.rom}GB storage, from the year {self.year}"

class Huawei(Phone):
    #constuctor
    def __init__(self,type,ram,year,rom):
        self.type=type
        self.ram=ram
        self.year=year
        self.rom=rom

    def spec(self):
        return f"This is a {self.type} with {self.ram}GB RAM and {self.rom}GB storage, from the year {self.year}"

phones=[Samsung("s25",16,2025,256),
        Iphone("Iphone 16 pro max",8,2025,512),
       Huawei("Huawei mate XT",16,2025,1028)
       ]

for phone in phones:    
    print(phone.spec())

