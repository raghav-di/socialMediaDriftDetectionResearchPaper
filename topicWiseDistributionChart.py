sum=0
for e in values1:sum+=e
li=[]
for e in values1:
    li.append((e/sum)*100)
import numpy as np

hmwb = 47188
lpg = 24533
es = 15879
wwi = 12675
labels = ["World Issues","Environment & Sustainability","Life & Personal Growth","Health & Mental Well-being"]
values1 = [12.935323383084576, 15.92039800995025, 24.378109452736318, 46.766169154228855]
values2 = [17.568668681824157, 18.426862925482983, 32.585096596136154, 31.41937179655671]

x = np.arange(len(labels)) # the label locations
width = 0.15  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, values1, width, label='Reddit', color='orange')
rects2 = ax.bar(x + width/2, values2, width, label='YouTube', color='red')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percentage(%)')
ax.set_title('Percentage by Topic Category and Platform')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=15, ha='right') # Rotate labels
ax.legend()

fig.tight_layout()

plt.show()
