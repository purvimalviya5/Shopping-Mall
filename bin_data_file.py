import pickle
f=open('dress.dat','wb')                                                      #file(dress) where details are present
x=[{"id":1001,"Name":"Tops","Available":10,"Price":250,"Original_Price":200},
   {"id":1002,"Name":"Pants","Available":12,"Price":500,"Original_Price":450},
   {"id":1003,"Name":"Sarees","Available":100,"Price":750,"Original_Price":700},
   {"id":1004,"Name":"Shorts","Available":20,"Price":350,"Original_Price":300},
   {"id":1005,"Name":"Kurtas","Available":15,"Price":400,"Original_Price":300}]
pickle.dump(x,f)
f.close()
                       
f=open('dress.dat','rb')
p=pickle.load(f)
print(p)
f.close()
