import random

while True:
   temperature = random.randint(900,1500)
   print("temperature is",temperature)
   humidity = random.randint(1,100)
   print("humidity is",humidity)
   if (temperature>1000 or humidity <50 ):
        print("Warning!!! temperaure too high",temperature)
        print("Warning!!! humidity too low",humidity)
   elif (temperature==1000):
        print("temperature is high",temperature)
   else:
        print ("temperature is low",temperature)
        print ("humidity is high ",humidity)
   
    
