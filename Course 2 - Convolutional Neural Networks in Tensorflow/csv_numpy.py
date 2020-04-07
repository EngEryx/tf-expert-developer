
#In[]:
import numpy as np
import csv

def get_data(filename):
    images = []
    labels = []
    with open(filename) as training_file:
      # Your code starts here
        l_images = []
        l_labels = []
        
        csv_reader = csv.reader(training_file, delimiter=',')
        
        next(csv_reader)
        
        for row in csv_reader:
            l_images.append(np.array_split(np.asarray(row[1:785]),28))
            l_labels.append(row[0])
      
        images = np.asarray(l_images, dtype=float)
        labels = np.asarray(l_labels, dtype=float)

      # Your code ends here
    return images, labels
#In[]:
files, labels = get_data("")

#In[]:
images = [] 
with open("sign_mnist_train.csv") as training_file:
      # Your code starts here
        l_images = []
        l_labels = []
        
        csv_reader = csv.reader(training_file, delimiter=',')
        
        next(csv_reader)

        for row  in csv_reader:
          images.append(np.array_split(np.asarray(row[1:785], dtype=float), 28))


# %%
import matplotlib.pyplot as plt

plt.imshow(images[700])



# %%