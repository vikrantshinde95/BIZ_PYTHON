class entry():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def val_a(self,a):
        try:
            if type(a) == str:
                if a.isalpha():
                    flg = True
                    msg = "VALID"
                else:
                    raise Exception()
                
        except:
            flg = False
            msg = "Invalid"

        return flg,msg