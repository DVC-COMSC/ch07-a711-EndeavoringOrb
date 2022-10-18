import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90] 
width = 0.2
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']
x = np.arange(len(names))

fig, ax = plt.subplots()
rect1 = ax.bar(x+width/2, Math, width, label='Math')
rect2 = ax.bar(x+width/2, English, width, label='English')
rect3= ax.bar(x+width/2, Physics, width, label='Physics')
rect4 = ax.bar(x+width/2, Computer, width, label='Computer')

ax.set_ylabel("Percent Score")
ax.set_title("Scores")
ax.set_xticks(x, names)
ax.legend(names)

ax.bar_label(rect1, padding=3)
ax.bar_label(rect2, padding=3)
ax.bar_label(rect3, padding=3)
ax.bar_label(rect4, padding=3)


# ******************************
# Make your code
# ******************************


fig.savefig('A11.png')
