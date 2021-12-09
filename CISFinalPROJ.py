#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:28:24 2021

@author: alext.
"""
import geopandas
import matplotlib.pyplot as plot
from PIL import Image
ALpic = Image.open("Alaska.png","r")
HIpic = Image.open("Hawaii.png","r")
ALpic = ALpic.resize((400,400))
HIpic = HIpic.resize((400,400))
statedict ={}
numdist= {}
districtfile = open("DistrictData.csv","r")
eligvoter = open("Voters.csv","r")

totvotes=[]
dlines = districtfile.readlines()
allstates = []
votpop = {}
states = geopandas.read_file('../data/usa-states-census-2014.shp')#https://jcutrer.com/python/learn-geopandas-plotting-usmaps
states = states.to_crs("EPSG:3395")
us_outline = states.boundary.plot(figsize=(18, 12), color="Gray")

for line in dlines[1:]:
    row = line.strip().split(',')
    name = row[0]
    if name not in statedict:
        statedict[name]= [] 
        allstates.append(name)
       
    statedict[name].append(int(row[1]))
    statedict[name].append(int(row[3])) 
    totvotes.append(row[4])
districtfile.close    
VEP = eligvoter.readlines()
for line in VEP[1:]:
    row = line.strip().split(',')
    place = row[0]
    numb = row[1]
    votpop[place]= int(numb)
        
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
   
    if differ < 0:
        differ = differ * (-1)
     
        
    percent= float(differ/z)
   
    if percent >= 0.07:
        return True
    else:
        return False
def effie(fgh):
    (x,y,z)= statewastecount(fgh)
    
    differ = x - y
   
    if differ < 0:
        differ = differ * (-1)
     
        
    percent= float(differ/z)
    return(percent)
def bias(defo):
    (x,y,z)= statewastecount(defo) 
    what =""
    if gerrytest(defo) == False:
        what = ("No Gerrymandering Detected in", defo)
        if defo not in green:
            green.append(defo)
        
    
    else: 
        if x > y:
           what = ("Detected Gerrymandering Bias Towards Republicans in", defo)
           if defo not in red:
               red.append(defo)
        if y > x:
           what = ("Detected Gerrymandering Bias Towards Democrats in",defo)
           if defo not in blue:
               blue.append(defo)
    return(what)

for stt in numdist:
    if gerryposs(stt) == True:
        ans = bias(stt)
    else:
        ans = ("Not Enough Districts For Gerrymandering in", stt) 
        
        if stt not in white:
            white.append(stt)

contin = "yes"

while contin == "yes":
    us_outline = states.boundary.plot(figsize=(18, 12), color="Gray")
    select = (input("Which state's data do you want to look at?")).upper()
    formatting= (select.lower()).title()
    while select not in allstates:
        print("Not a valid state, Please enter a valid state")
        select = (input("Which state's data do you want to look at?")).upper()
    print(select, " has ", numdist[select]," district(s).")
    if select in green:
        statecolor = "green" 
    elif select in white:
        statecolor = "black"
    elif select in red:
        statecolor = "red"
    elif select in blue:
        statecolor = "blue"
    if select =="ALASKA":
        ALpic.show()
    if select =="HAWAII":
        HIpic.show()  
    
    if numdist[select]<3:
        (m,f,o) = statewastecount(select)
        print(("Not Enough Districts For Gerrymandering in", select))
        print("State Voter Turnout",((o/votpop[formatting])*100),"%")
    else:
        (m,f,o) = statewastecount(select)
        print("Total Votes in",select,":",o)
        print("State Voter Turnout",((o/votpop[formatting])*100),"%")
        print("Total Votes Wasted for Democrats:",m)
        print("Total Votes Wasted for Republicans:",f)
        print("Wasted Vote Percent Difference:",(effie(select)*100),"%")
        print(bias(select))
      
    states[states['NAME']==formatting].plot(ax=us_outline, color=statecolor) #https://jcutrer.com/python/learn-geopandas-plotting-usmaps
    plot.show()
    plot.close()    
    contin = (input("Look at another state's data? Please enter yes or no.")).lower()
    plot.close()
    while contin != "yes" and contin != "no":
        contin = (input("Invalid Input. Try again.")).lower()
print("Goodbye!")


