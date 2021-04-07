# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 00:31:48 2021

@author: OZLEM
"""

import os

mylist = os.listdir("../kartacaalls")

sorted_list=sorted(mylist)

emptylist=[]
for name in mylist:
    if '==' in name:
        emptylist.append(name)

for name in emptylist:
    mylist.remove(name)
         
emptylist=sorted(emptylist)

emptylist2=[]
for name in mylist:
    if '=' in name:
        emptylist2.append(name)

for name in emptylist2:
    mylist.remove(name)
      
emptylist2=sorted(emptylist2)


        
result=[]
for name in emptylist:
    result.append(name)
for name in emptylist2:
    result.append(name)
    

