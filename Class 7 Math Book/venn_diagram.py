from matplotlib_venn import venn2
from matplotlib import pyplot as plt


U = {1,2,3,4,5,6}
A = {2,3}
B = {2,3,4,5}
AUB = A.union(B)

venn2(subsets=([2,3],[2,3,4,5],[1,6]), set_labels=('Group A', 'Group B'))
plt.show()