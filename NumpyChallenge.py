import numpy as np


np.random.seed(100)
array = np.random.randint(1,11,size=(6, 10))

numberToCount = np.arange(1,11)

outputArray = np.array([])

for row in range(0,array.shape[0]):
    for number, index in enumerate(numberToCount,start=1):
        outputArray = np.append(outputArray, np.count_nonzero((array[row] ==  int(number))))

print(outputArray.reshape(array.shape))
