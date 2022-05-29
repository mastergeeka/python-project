



def lookup():
    state = input("Which state?:")
    data = open('voting.txt')
    file=data.readlines()
    found=False
    dem=0
    rep=0
    wasted_dem=0
    wasted_rep=0
    ger=0
    dem_sum = 0
    rep_sum = 0
    for line in file:
        line = line.split(",")
        if state == line[0]:
            found=True
            num=(len(line)-1)//3
            for i in range(0,num):
                dem=int(line[3*i+2])
                rep=int(line[3*i+3])
                if dem>rep:
                    wasted_dem=dem-(rep+dem)//2-1
                    wasted_rep=rep
                elif dem<rep:
                    wated_dem=dem
                    wasted_rep=rep-(rep+dem)//2-1
                dem_sum+=wasted_dem
                rep_sum+=rep
            print("Wasted Democratic votes:", dem_sum)
            print("Wasted Republican votes:", rep_sum)

            gerry(dem_sum, rep_sum)

def gerry(dem_sum, rep_sum):
    if dem_sum>rep_sum:
        ger = (dem_sum-rep_sum)/(rep_sum +dem_sum)
        if ger>=0.07:
            print("Gerrymandered for Rep")
    else:
        ger = (rep_sum - dem_sum) / (dem_sum + rep_sum)
        if ger>= 0.07:
            print("Gerrymandered for Dem")

lookup()       
