import numpy as np
import matplotlib.pyplot as plt

# Initialise the module with these two lines
import safe_colours
safe_colours = safe_colours.initialise()

# generate some x values for examples
x = np.linspace(0.,2*np.pi,100)

####################################################################################

# Here's how to use the distinct colours by naming them from a dictionary:
col_dict = safe_colours.distinct_named()

# You can print all the options like this:
print col_dict.keys()

# The colours are in a dictionary, which you can address like this:
plt.figure()
plt.plot(x,np.sin(x),c=col_dict['navy'])
plt.plot(x,np.sin(x+np.pi/2.),c=col_dict['coral'])
plt.show()

####################################################################################

# If you are plotting lots of lines, this method will give you a good combination
# of colours. Just tell it how many colours you want and it will give you a list
# of colours (in hex format) which go well together. Maximum 12 colours!
col_list = safe_colours.distinct_list(4)

# You can use the colours straight from the list in pyplot like this:
plt.figure()
for i in range(4):
    plt.plot(x,np.sin(x+i*np.pi/6.),c=col_list[i])
plt.show()

####################################################################################

testmap = np.arange(256).reshape(1,-1)

# There are three 'safe' colourmaps included for scatter plots and images:
# To use, just specify the colourmap name as below.

# 'rainbow' and 'heat' are for linear data
cmap = safe_colours.colourmap('rainbow')
plt.figure()
plt.imshow(testmap, cmap=cmap, aspect='auto')
plt.show()

cmap = safe_colours.colourmap('heat')
plt.figure()
plt.imshow(testmap, cmap=cmap, aspect='auto')
plt.show()

# 'diverging' is for data which diverges around zero
cmap = safe_colours.colourmap('diverging')
plt.figure()
plt.imshow(testmap, cmap=cmap, aspect='auto')
plt.show()

# You can invert any of the colourmaps using the kwarg 'invert'
cmap = safe_colours.colourmap('diverging',invert=True)
plt.figure()
plt.imshow(testmap, cmap=cmap, aspect='auto')
plt.show()

####################################################################################

