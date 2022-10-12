# function to return the shape of a high dimensional list in python
def shape(v):
  ans = []
  
  while True :
    if type(v)==type(ans):
      d = len(v)
      # print(d)
      ans.append(d)
      v = v[0]
    # print(v)
    # if :
    #   print('s')
    #   break
    else :
      break

  return ans

import numpy as np
ar = np.random.randint(1, 10, (2, 3, 2))

ar.tolist()
shape(v)
