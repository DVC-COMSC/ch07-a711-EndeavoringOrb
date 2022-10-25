import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90]
x = np.arange(2) 
width = 0.2
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

# ******************************
fig, ax = plt.subplots()
rects1 = ax.bar(x - 3*width/2, Math, width, label='Math')
rects2 = ax.bar(x - width/2, English, width, label='English')
rects3 = ax.bar(x + width/2, Physics, width, label='Physics')
rects4 = ax.bar(x + 3*width/2, Computer, width, label='Computer')

ax.set_ylabel('Scores')
ax.set_title('Subject Scores')
ax.set_xticks(x, names)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)
# ******************************


fig.savefig('A11.png')