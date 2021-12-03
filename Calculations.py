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


for line in dlines[1:]:
    row = line.strip().split(',')
    name = row[0]
    if name not in statedict:
        statedict[name]= []  
    statedict[name].append(row[1])
    statedict[name].append(row[3]) 
    totvotes.append(row[4])
     

for state in statedict:
    numdist[state]= int(len(statedict[state])/4)

a = len(totvotes)

for i in range(a,0,-1):
    if i%2== 1:
        del totvotes[i]
notposs=[]
poss=[]
allclear = []
repbias = []
dembias = []
def gerryposs(ST):
    if numdist[ST] < 3:
        if ST not in notposs:
            notposs.append(ST)
        return False
    else:
        if ST not in poss:
            poss.append(ST)
        return True
for key in numdist:
    gerryposs(key)
def statewastecount(jkl):
    startslice = 0
    statenum = 1
    for ynot in numdist:
        if ynot !=jkl:
            startslice += int(numdist[jkl])
            statenum += 1
        else:
            break
    distance = int(numdist[jkl])
    ending= startslice + distance 
    stuff = totvotes[startslice:ending]
    partyvotes = list(statedict(jkl))
    demwaste=0
    repwaste=0
    ind = 1
    for x in range(distance):
        threshold = int(stuff[0])/2
        demvotes= partyvotes[ind]
        ind+= 2
        repvotes= partyvotes[ind]
        ind +=2
        if demvotes>repvotes:
            wasted_dem= demvotes - threshold
            wasted_rep=repvotes
        elif demvotes<repvotes:
            wasted_dem= demvotes
            wasted_rep=repvotes-threshold
        demwaste += wasted_dem
        repwaste += wasted_rep
    
    return(demwaste,repwaste)
def gerrytest(abc):   
    (x,y)= statewastecount(abc)  
    differ = x - y
    if differ < 0:
        differ = differ * (-1)
        lower = x
    elif differ > 0:
        lower = y
    percent= float(differ/lower)
    if percent >= 0.07:
        return True
    else:
        return False
def bias(defo):
    (x,y)= statewastecount(defo)  
    if gerrytest(defo) == False:
        print("No Gerrymandering Detected")
        if defo not in allclear:
            allclear.append(defo)
    
    elif x > y:
        print("Detected Gerrymandering Bias Towards Republicans")
        repbias.append(defo)
    elif y < x:
        print("Detected Gerrymandering Bias Towards Democrats")
        dembias.append(defo)
        
    


