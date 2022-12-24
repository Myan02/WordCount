import os
import re
import json
import time
from multiprocessing import Process, Manager
import multiprocessing 

list1 = list()
list2 = list()
list3 = list()
list4 = list()
list5 = list()
list6 = list()
list7 = list()
list8 = list()

#open a file, read it into "text" as a string, close the file
def ReadFile(fileName):
   file = open(fileName, encoding="utf8")
   text = file.read().lower()
   file.close()
   return text

# text file to open
def ListSplit():
   # split the string into a list using the regex
   tempList = re.split(r"[^a-z]+", ReadFile("war and peace.txt"))
   
   count = 0
   
   # split the large file into different lists and run them concurrently later
   for word in tempList:
      if (count % 8) == 0:
         list1.append(word)
         count += 1
      elif (count % 8) == 1:
         list2.append(word)
         count += 1
      elif (count % 8) == 2:
         list3.append(word)
         count += 1
      elif (count % 8) == 3:
         list4.append(word)
         count += 1
      elif (count % 8) == 4:
         list5.append(word)
         count += 1
      elif (count % 8) == 5:
         list6.append(word)
         count += 1
      elif (count % 8) == 6:
         list7.append(word)
         count += 1
      elif (count % 8) == 7:
         list8.append(word)
         count += 1
      
      
# adds a word to a dictionary, or increments it if it exists
def Count(list, dict):
   
   print("Worker assigned to task: {}".format(multiprocessing.current_process().name))
   print("ID of process running: {}\n".format(os.getpid()))
   
   for word in list:
      if word in dict:
         dict[word] += 1
      else:
         dict[word] = 1
   
   
if __name__ == "__main__":
   
   print("ID of main process: {}\n".format(os.getpid()))
   
   ListSplit()
   print("Total Word Count: {}\n".format(len(list1) + len(list2) + len(list3) + len(list4) + len(list5) + len(list6) + len(list7) + len(list8) - 1) )
   
   start_time = time.time()
   
   manager = Manager()
   
   myDict1 = manager.dict()
   myDict2 = manager.dict()
   myDict3 = manager.dict()
   myDict4 = manager.dict()
   myDict5 = manager.dict()
   myDict6 = manager.dict()
   myDict7 = manager.dict()
   myDict8 = manager.dict()
   
   p1 = Process(target = Count, name = "worker1", args = (list1, myDict1,))
   p2 = Process(target = Count, name = "worker2", args = (list2, myDict2,))
   p3 = Process(target = Count, name = "worker3", args = (list3, myDict3,))
   p4 = Process(target = Count, name = "worker4", args = (list4, myDict4,))
   p5 = Process(target = Count, name = "worker5", args = (list5, myDict5,))
   p6 = Process(target = Count, name = "worker6", args = (list6, myDict6,))
   p7 = Process(target = Count, name = "worker7", args = (list7, myDict7,))
   p8 = Process(target = Count, name = "worker8", args = (list8, myDict8,))

   p1.start()
   print("ID of process p1: {}".format(p1.pid))
   
   p2.start()
   print("ID of process p2: {}".format(p2.pid))
   
   p3.start()
   print("ID of process p3: {}".format(p3.pid))
   
   p4.start()
   print("ID of process p4: {}".format(p4.pid))
   
   p5.start()
   print("ID of process p5: {}".format(p5.pid))
   
   p6.start()
   print("ID of process p6: {}".format(p6.pid))
   
   p7.start()
   print("ID of process p7: {}".format(p7.pid))
   
   p8.start()
   print("ID of process p8: {}".format(p8.pid))
   
   
   
   p1.join()
   print("p1 complete!")
   
   p2.join()
   print("p2 complete!")
   
   p3.join()
   print("p3 complete!")
   
   p4.join()
   print("p4 complete!")
   
   p5.join()
   print("p5 complete!")
   
   p6.join()
   print("p6 complete!")
   
   p7.join()
   print("p7 complete!")
   
   p8.join()
   print("p8 complete!")
   


   end_time = time.time()

   #myDict = {**myDict1}
   #newDict = {**myDict1, **myDict2}
   #newDict = {**myDict1, **myDict2, **myDict3}
   #newDict = {**myDict1, **myDict2, **myDict3, **myDict4}
   #newDict = {**myDict1, **myDict2, **myDict3, **myDict4, **myDict5}
   #newDict = {**myDict1, **myDict2, **myDict3, **myDict4, **myDict5, **myDict6}
   #newDict = {**myDict1, **myDict2, **myDict3, **myDict4, **myDict5, **myDict6, **myDict7,}
   newDict = {**myDict1, **myDict2, **myDict3, **myDict4, **myDict5, **myDict6, **myDict7, **myDict8}
   
   #myDict = {key: myDict1.get(key, 0) for key in set(myDict1)}
   #myDict = {key: myDict1.get(key, 0) + myDict2.get(key, 0) for key in set(myDict1) | set(myDict2)}
   #myDict = {key: myDict1.get(key, 0) + myDict2.get(key, 0) + myDict3.get(key, 0) for key in set(myDict1) | set(myDict2) | set(myDict3)}
   #myDict = {key: myDict1.get(key, 0) + myDict2.get(key, 0) + myDict3.get(key, 0) + myDict4.get(key, 0) for key in set(myDict1) | set(myDict2) | set(myDict3) | set(myDict4)}
   #myDict = {key: myDict1.get(key, 0) + myDict2.get(key, 0) + myDict3.get(key, 0) + myDict4.get(key, 0) + myDict5.get(key, 0) for key in set(myDict1) | set(myDict2) | set(myDict3) | set(myDict4) | set(myDict5)}
   #myDict = {key: myDict1.get(key, 0) + myDict2.get(key, 0) + myDict3.get(key, 0) + myDict4.get(key, 0) + myDict5.get(key, 0) + myDict6.get(key, 0) for key in set(myDict1) | set(myDict2) | set(myDict3) | set(myDict4) | set(myDict5) | set(myDict6)}
   #myDict = {key: myDict1.get(key, 0) + myDict2.get(key, 0) + myDict3.get(key, 0) + myDict4.get(key, 0) + myDict5.get(key, 0) + myDict6.get(key, 0) + myDict7.get(key, 0) for key in set(myDict1) | set(myDict2) | set(myDict3) | set(myDict4) | set(myDict5) | set(myDict6) | set(myDict7)}
   myDict = {key: myDict1.get(key, 0) + myDict2.get(key, 0) + myDict3.get(key, 0) + myDict4.get(key, 0) + myDict5.get(key, 0) + myDict6.get(key, 0) + myDict7.get(key, 0) + myDict8.get(key, 0) for key in set(myDict1) | set(myDict2) | set(myDict3) | set(myDict4) | set(myDict5) | set(myDict6) | set(myDict7) | set(myDict8)}
   
   # sort the dict descending order
   myDict = sorted(myDict.items(), key=lambda x:x[1], reverse=True)

   # change the directory to any folder you want the file to get saved to 
   with open("C:\\Users\\babur\\Desktop\\text\\result.txt", "w") as file:
      file.write(json.dumps(myDict.copy()))

   print("\n")
   print("Process finished --- %s seconds ---" % (end_time - start_time))

