import matplotlib.pyplot as plt


r = open('result.txt').read()
r = r.replace('[', '')
r = r.replace(']', '')
i = [1 - float(x)/70608.4195478807 for x in r.split(',')]



plt.plot(i)
plt.ylabel('Score')
plt.xlabel('Generations')
plt.show()

print(i)
