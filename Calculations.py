#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:28:24 2021

@author: alext.
"""
statedict ={}
numdist= {}
districtfile = open("DistrictData.csv","r")
totvotes=[]
dlines = districtfile.readlines()
allstates = []

for line in dlines[1:]:
    row = line.strip().split(',')
    name = row[0]
    if name not in statedict:
        statedict[name]= [] 
        allstates.append(name)
       
    statedict[name].append(int(row[1]))
    statedict[name].append(int(row[3])) 
    totvotes.append(row[4])
     

for state in statedict:
    numdist[state]= int(len(statedict[state])/4)

a = len(totvotes)

for i in range(a,0,-1):
    if i%2== 1:
        del totvotes[i]
green = []
red = []
blue = []
white = []

def gerryposs(ST):
    
    if numdist[ST] < 3:
        
        return False
    if numdist[ST] >= 3:
        
        return True

def statewastecount(jkl):
    startslice = 0

    for ynot in numdist:
        if ynot !=jkl:
            startslice += int(numdist[ynot])
            
        else:
            break
    distance = int(numdist[jkl])
    
    ending= startslice + distance 
    stuff = totvotes[startslice:ending]
    
    partyvotes = list(statedict[jkl])
    demwaste=0
    repwaste=0
    ind = 1
    statetotal = 0
    t =0
    for g in stuff:
        statetotal += int(g)
    
    for di in range(distance):
        half = (int(stuff[t]))/2
        if half % 1 ==0:
            threshold =half + 1
        else:
            threshold =half + 0.5 
        t+= 1
        demvotes= partyvotes[ind]
        ind+= 2
        repvotes= partyvotes[ind]
        ind +=2
        
        if demvotes > repvotes:
            wasted_dem= demvotes - threshold
            wasted_rep=repvotes
        if demvotes<repvotes:
            wasted_dem= demvotes
            wasted_rep=repvotes-threshold
        demwaste += wasted_dem
        repwaste += wasted_rep
    
    return(demwaste,repwaste,statetotal)


def gerrytest(abc):   
    (x,y,z)= statewastecount(abc)
    
    differ = x - y
    print(abc,x,y,differ)
    if differ < 0:
        differ = differ * (-1)
     
        
    percent= float(differ/z)
    print(abc,percent)
    if percent >= 0.07:
        return True
    else:
        return False

def bias(defo):
    (x,y,z)= statewastecount(defo) 
    what =""
    if gerrytest(defo) == False:
        what = ("No Gerrymandering Detected in", defo)
        green.append(defo)
        
    
    else: 
        if x > y:
            what = ("Detected Gerrymandering Bias Towards Republicans in", defo)
            
        if y > x:
            what = ("Detected Gerrymandering Bias Towards Democrats in",defo)
           
    return(what)

for stt in numdist:
    if gerryposs(stt) == True:
        ans = bias(stt)
    else:
        ans = ("Not Enough Districts For Gerrymandering in", stt)   
    
select = (input("Which state's data do you want to look at?")).upper()

while select not in allstates:
    print("Not a valid state, Please enter a valid state")
    #select = (input("Which state's data do you want to look at?")).upper()

