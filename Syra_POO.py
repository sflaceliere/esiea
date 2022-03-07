from sys import stdout

class Syracuse:
    def __init__(self,value:int):
        self.value=value

    @classmethod
    def loadfile(cls,filename:str):
        try:
            f=open(filename,"r")
            value=int(f.read())
            f.close()
            return cls(value)
        except:
            return None
    
    def set_value(self,value:int):
        self.value=value

    def __call__(self,filename=None):
        if (filename==None):
            file=stdout
        else:
            try:
                file=open(filename,"w")
            except:
                return
        file.write("Conjecture de Syracuse\n")
        i=0
        checked=False
        while True:
            file.write(str(self.value)+'\n')
            if self.value==1:
                if checked:
                    break
                checked=True
            
            if (self.value&1):
                self.value*=3
                self.value+=1
            else:
                self.value>>=1
            if not checked:
                i+=1

        file.write("on est arrivé à 1 au bout de {} itérations\n".format(i))
        if file!=stdout:
            file.close()

  

test=Syracuse.loadfile("value.txt")
test("out.txt")