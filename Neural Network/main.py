from DolphinSwarm import DSO

i = DSO(popSize=20, soluSize=87, space=(-1, 1), T2=10, speed=0.01)
print(i.optimaze(100))