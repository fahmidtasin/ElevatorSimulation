import math
import numpy
import random
import queue



class Person:
  def __init__(self, serial,floor,duration):
    self.serial = serial
    self.floor=floor
    self.duration= duration

#p1 = Person(0, 36,3)

#print(p1.serial)
#print(p1.duration)

#---------------------------------

mint = 0
capacity = 0
count = 0
n = 0
lift_queue = []
waiting_queue = []
floor_1_queue = []
floor_2_queue = []
floor_3_queue = []
top_floor = 3
current_floor = 1
lift_pos = 1
lift_prior_pos=2
time = 0
service_time = 0
waiting_time = 0
p_choice =0;
service_per_floor = 0;
service_per_floor2 = 0;
service_per_floor3 = 0;

p = numpy.random.exponential(1)
c = math.ceil(p)
while mint < 15:
      if (c==mint):
          p = numpy.random.exponential(1)
          c = math.ceil(p)
          print("at time  : " + str(mint)+" a new person joins the que (Arrival time)")
          print("IAT:  " + str(c))
          print("------------------")
          count = count + 1
          
          c=mint+c
          print("Total passangers: " + str(count))

      #floor choice
          pf_choice = random.randint(2,3)
          print("Person: ",count)
          print("Choice: "+str(pf_choice))

      #service time
          service_per_floor = math.ceil(numpy.random.uniform(15, 120))
          
      #produce a person
          floor_1_queue.append(Person(count,pf_choice,service_per_floor))



        #if p_choice==2 and p_choice==3:
          # floor_1_queue = [floor_1_queue,count[capacity]]
            #print("Floor 1 queue: "+floor_1_queue)
        #else:
        #   waiting_queue = [waiting_queue,count[capacity]]
          #  waiting_time = waiting_time+1

      print("\n")
      mint = mint + 1
      print("the time is now "+str(mint))

     #Entering lift from floor_1_queue
      if(lift_pos==1):
        while(len(lift_queue)<6  and len(floor_1_queue)>0):
          lift_queue.append(floor_1_queue[0])
          floor_1_queue.pop(0)

      

      if(lift_pos==1 and lift_prior_pos==2):
        lift_pos = 2
        lift_prior_pos=1
        print("Lift Position: "+str(lift_pos))

      elif(lift_pos==2 and lift_prior_pos==1):
        lift_pos = 3
        lift_prior_pos=2
        print("Lift Position: "+str(lift_pos))
      
      elif(lift_pos==3 and lift_prior_pos==2):
        lift_pos = 2
        lift_prior_pos=3
        print("Lift Position: "+str(lift_pos))

      elif(lift_pos==2 and lift_prior_pos==3):
        lift_pos = 1
        lift_prior_pos=2
        print("Lift Position: "+str(lift_pos))

    # leave = numpy.random.uniform(15, 120)
    # if decision<1
    # lift = lift_pos + 1
    #print("Customers decision: " + str(decision))



print("lift que")
for x in floor_1_queue:
  print (x.serial,x.floor,x.duration)
  

print("lift inside")
for x in lift_queue:
  print (x.serial,x.floor,x.duration)
  

print(lift_pos)
print(lift_prior_pos)
