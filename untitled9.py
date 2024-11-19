# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wDA-PX9rHa-mrbTFSWMaedZmIb1u92-o
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,6])
y=np.array([0,250])

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10])
y=np.array([2,1,8,1.5,7,0,9,4,7,0,7,3.5,9,1.25,2,2,2,2,2])

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y=np.array([2,7,1,9])

plt.plot(y, marker='o')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y=np.array([2,7,1,9])

plt.plot(y,'o:c' )
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y=np.array([2,7,1,9])

plt.plot(y, marker='o',ms=20)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y=np.array([2,7,1,9])

plt.plot(y, marker='o',ms=20,mec='c')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x1=np.array([1,2,3,4])
y1=np.array([2,5,1,9])
x2=np.array([1,2,3,4])
y2=np.array([4,9,2,10])

plt.plot(x1,y1,x2,y2)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([0,6,12,18,24,30])

plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([0,6,12,18,24,30])
plt.scatter(x,y,color='yellow')

x=np.array([3,7,9,12,5,8])
y=np.array([4,8,14,19,23,26])
plt.scatter(x,y,color='brown')

plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([0,6,12,18,24,30])
mycolor=['black','brown','red','green','blue','lime']

plt.scatter(x,y,color=mycolor)

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3,4,5])
y=np.array([0,6,12,18,24,30])
mycolor=['black','brown','red','green','blue','lime']
size=[20,60,100,160,40,90]
plt.scatter(x,y,color=mycolor,s=size)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C','D'])
y=np.array([2,4,6,8])
plt.bar(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C','D'])
y=np.array([2,4,6,8])
plt.barh(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C','D'])
y=np.array([2,4,6,8])
plt.bar(x,y,width=0.1 )
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([40,20,30,10])

plt.pie(x)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([40,20,30,10])
mylabels=["Apples","Bananas","Cherries","Dates"]

plt.pie(x, labels=mylabels,startangle=90)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([40,20,30,10])
mylabels=["Apples","Bananas","Cherries","Dates"]

myexplode=[0.4,0,0.6,0]
plt.pie(x, labels=mylabels,startangle=90)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([40,20,30,10])
mylabels=["Apples","Bananas","Cherries","Dates"]

myexplode=[0.2,0,0,0]
plt.pie(x, labels=mylabels,startangle=90,explode=myexplode,shadow=True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([40,20,30,10])
mylabels=["Apples","Bananas","Cherries","Dates"]
mycolors=['red','blue','green','yellow']
myexplode=[0.2,0,0,0]
plt.pie(x, labels=mylabels,startangle=90,explode=myexplode,shadow=True,colors=mycolors)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([40,20,30,10])
mylabels=["Apples","Bananas","Cherries","Dates"]


plt.pie(x, labels=mylabels)
plt.legend()
plt.show()