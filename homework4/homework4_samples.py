"""Sample solutions from various students"""


## checking channels for signal

# nice idea, doesn't quite work as implemented
for i in range (0, np.shape(nissl)[2], 1):
    if nissl[:,:,i].any() > 0:
        print('There is signal in channel %i' % i)
    else:
        print('There is NO signal in channel %i' % i)


#
for ch in range(3): #rgb
   print(nissl[:,:,ch].max())

print (nis[ :, :, 0] == 0)
print (nis[ :, :, 1] == 0)
print (nis[ :, :, 2] == 0)


## extract the green channel

# happens to work in this case, but only because red and blue channels are all zeros:
green = color.rgb2gray(nissl)


# don't confuse setting values in an array with simply extracting part of an array:
temp=image.copy()
temp[:,:,1] = 0 # still 3D? slicing did not work?!


## invert contrast ("brightness" or "intensity" would've been more accurate):

# inverts bits, not ideal, but works for uint data:
inv_nissl_gray = np.invert(nissl_gray)

# this works correctly:
from skimage import util
inv_nissl_gray = util.invert(nissl_gray)


## pandas

## find number of subjects

nsubjects = stroop['subject'].nunique() # is also valid

## average reaction time across subjects

av_reaction = stroop['reaction_time'].mean() # not valid! why?

