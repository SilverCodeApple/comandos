import numpy as np

class linealizacion:
    def __init__(self,x,y ,xi, yi):
        if(len(x) > len(y)):
            for i in range(abs(len(x) - len(y))):
                x.pop()
        
        self.x = np.array(x)
        self.y = np.array(y)
        self.xi = xi
        self.yi = yi 
        self.m = 0
        self.b = 0
    def linea(self):
        sxx = 0
        sxy = 0
        self.m = 0
        self.b = 0
        prom = [ (sum(self.x))/self.x.size , sum(self.y)/self.y.size]
        for i in range(self.x.size):
            sxx += (self.x[i] - prom[0])**2
            sxy += (self.x[i] - prom[0])*(self.y[i] - prom[1])
        self.m =  sxy/sxx
        self.b = prom[1] - ((sxy/sxx)*prom[0])
        return self.m, self.b 
    def incertidumbre(self):
        n = self.x.size
        xi_2 = 0
        xi2 = 0
        for k in self.x:
            xi2 += (k**2)
            xi_2 += k
        xi_2 = xi_2**2
        sy = ((((self.yi)**2)*n)/(n-1))**(1/2)
        sm = sy*(((n / (n*xi2) - (xi_2)))**(1/2))
        sb = sy*(((xi2)/((n*xi2 - xi_2)))**(1/2))
        return sy,sm,sb
    def ejex(self):
        return self.x
    def ejey(self):
        return self.y
    def ajuste(self):
        y2 = []
        for i in range(self.x.size):
            y2.append(self.x[i] * self.m + self.b)
        return y2


        
    