print ("\n\n <<<[ Pencarian Akar dengan Metode Biseksi ]>>> \n")
print (" Soal : cari akar f(x) = x3 + x2 -3x-3  ") #silahkan diganti dengan kebutuhan 
print (" Selang [1,2] dengan ε = 0.005 \n") #silahkan diganti dengan kebutuhan

def inputdata(a,b):
    a= float(input(" Masukan data selang awal a : "))
    b= float(input(" Masukan data selang awal b : "))
    return (a,b)

def y(x):
    return (x**3+x**2-x*3-3) #silahkan diganti dengan kebutuhan

def checkAB(a,b):
    if(y(a)*y(b)<0):
        return True
    else:
        return False

def updateData(a,b):
    c= (a+b)/2
    if(y(a)*y(c)<0):
        b = c
    else :
        a = c
    return (a,b)

def process(a,b,prc):
    while(abs(y(a))>prc or abs(y(b))>prc):
        a,b = updateData(a,b)

    if(abs(y(a))>abs(y(b))):
        return b
    else:
        return a
    # return (a,b)
    

def main():
    a= 0
    b= 0
    prc= 0
    result = 0
    a,b = inputdata(a,b)
    if(checkAB(a,b)):
        print ("  <<< Data sesuai >>>  ")
        prc = float(input(" Masukan nilai epsilon -> "))
        result = process(a,b,prc)
        print ("\n Hasil     = ",result," \n Nilai y(x) = ",y(result),"\n")
    else:
        print (" <<< Data tidak sesuai >>> ")

main()
