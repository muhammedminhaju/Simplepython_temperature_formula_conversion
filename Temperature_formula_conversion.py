def ctokf(celsius):
   kelvin=celsius + 273.15
   farenheit= celsius*(9/5) + 32
   print("celsius =",celsius,"kelvin =",kelvin,"farenheit =",farenheit)
def ftokc(farenheit):
   celsius= (farenheit- 32)*5/9 
   kelvin=celsius + 273.15
   print("celsius =",celsius,"kelvin =",kelvin,"farenheit =",farenheit)
def ktofc(kelvin):
   celsius=kelvin - 273.15
   farenheit= celsius*(9/5) + 32
   print("celsius =",celsius,"kelvin =",kelvin,"farenheit =",farenheit)   

print("Enter the choice")
print("1: celsius to convert farenheit and kelvin")
print("2: farenheit to convert celsius and kelvin")
print("3: kelvin  to convert farenheit and celsius")
choice=int(input(""))
if(choice==1):
   celsius=int(input("Enter the temperature in celsius"))
   ctokf(celsius)
elif(choice==2):
   farenheit=int(input("Enter the temperature in farenheit"))
   ftokc(farenheit)
elif(choice==3): 
   kelvin=int(input("Enter the temperature in kelvin")) 
   ktofc(kelvin)
