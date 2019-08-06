import matplotlib.pyplot as plt


r = open('final.txt').read()
r = r.replace('[', '')
r = r.replace(']', '')
i = [float(x) for x in r.split(',')]



plt.plot(i)
plt.ylabel('Score')
plt.xlabel('Generations')
plt.show()

print(i)
