import socket

class modules:
    
    def __init__(self, first, dirs):
        self.first = first
        self.dirs = dirs   

    def ret(self):
        return '{}\n{}'.format(self.first, self.dirs)

Mod_1 = modules('socket', dir(socket))

print("Choose from module list")
Modules1 = ("socket")
print(Modules1)

if "socket" == input("Enter Module Name to View Attributes: "):
    print(Mod_1.ret())



    
    
