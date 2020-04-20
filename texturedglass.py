# Scope:
# Use Python to load and display images. Create functions that will do the textured glass effect by combining translation of image columns (swap), 
# and rotation of image columns (flip), as described in the previous email.
import numpy as np
import cv2 as cv
# Implementation:
# Chapter 1: loading and showing images
# Write a Python program that will produce images as shown in the previous email, given an input image and a configuration of operations as specified in code.
img = cv.imread('Rialto.jpg')
cv.namedWindow('Rialto', cv.WINDOW_NORMAL)
cv.imshow('Rialto', img)
cv.waitKey(0)
cv.destroyAllWindows()
# Step 1: load and show an image that came from a file on disk. We want to show the original before processing it. 
# Print to the command line output how many columns and how many rows the image has.
# Step 2: obtain the shape of the image (how many columns, and how many rows of pixels it has).
imageHeight, imageWidth, _ = img.shape
print('width:  ', imageWidth)
print('height: ', imageHeight)
print("total number of pixels: ", img.size)
print("These are the numbers to play with: ", img.shape)
leftmostSegment = img[:1200, :300]
centerSegment = img[:1200, 300:599]
rightmostSegment = img[:1200, 600:900]
# Chapter 2: translation function
# Step 3: create a copy of the image with the same shape, and copy the source image into the destination image in three steps: 
# 1) copy the rightmost third of the source into the leftmost third of the destination, 2) copy the center into the center, 
# and 3) copy the leftmost third of the source into the rightmost third of the destination.
# Step 4: display the modified image.
# # img[:1200, :300] = px3
rialto3 = cv.hconcat([cv.hconcat([rightmostSegment, centerSegment]), leftmostSegment])
cv.imshow("DUDE", rialto3)
cv.waitKey(0)
cv.destroyAllWindows()

def calculateSegments(numberOfSegments, width):
    segments = []
    segmentWidth = int(width / numberOfSegments)
    for s in range(numberOfSegments):
        segments.append((segmentWidth * s, (segmentWidth * (s + 1)) - 1))
    print (segments)
    return segments

def translate(segmentCount, img):
    segments = calculateSegments(segmentCount, imageWidth)
    copyImage = np.copy(img)
    for segment in range(int(segmentCount / 2) + 1):
        if segment % 2 != 0:
            continue
        leftSegment = segment
        rightSegment = segmentCount - 1 - segment
        copyImage[:imageHeight, segments[leftSegment][0]:segments[leftSegment][1]] = img[:imageHeight, segments[rightSegment][0]:segments[rightSegment][1]]
        copyImage[:imageHeight, segments[rightSegment][0]:segments[rightSegment][1]] = img[:imageHeight, segments[leftSegment][0]:segments[leftSegment][1]]
    return copyImage

translatedImage = translate(5, img)
cv.imshow("BRO", translatedImage)
cv.waitKey(0)
cv.destroyAllWindows()

# Step 5: generalize the function to take a number (such as 3) and the image, and do that amount of horizontal cuts with translation. 
# Validate that the number is >= 3, and the number is < N/2, where N is the number of columns in the shape of the image. 
# Then during the copying from source to destination, invert the locations of the columns from the outside in, skipping every other column and center columns. 
# For example, image with columns [1,2,3] will end up [3,2,1], image with columns [1,2,3,4] will end up [4,2,3,1], 
# image with columns [1,2,3,4,5] will end up [5,2,3,4,1], image with columns [1,2,3,4,5,6] will end up [6,2,4,3,5,1], and so on.
# Step 6: call the function with parameters 3 and image, and show the result, it should be the same as in step 4.
# Step 7: call the function with parameters 6 and image, and see that the result this as expected.

# Chapter 3: rotation function
# Step 8: create a copy of the image with the same shape, and copy the source image into the destination image in two steps: 1) copy the image as is, and 
# 2) take the center column and flip it. This can be achieved by copying a column of pixels at a time, and 
# simply placing them in the new location which is calculated based on the coordinates of the source column.
# Step 9: display the modified image, it should have the center third flipped (rotated) horizontally.
# Step 10: generalize the function to take a number of columns, same constraints as with the translation function regarding the valid values of the number.
#  Then, flip the columns from the inside out. For example, image with columns [1,2,3] will end up [1,2',3] where 2' is 2 but flipped horizontally; 
# image with columns [1,2,3,4]  will end up [1,2',3',4], image with columns [1,2,3,4,5] will end up [1',2,3',4,5'], image with columns [1,2,3,4,5,6] will end up 
# [1',2,3',4',5,6'], and so on.
# Step 11: call the function with parameters 3 and image, and show the result, it should be the same as in step 9.
# Step 12: call the function with parameters 5 and image, and see that the result is as expected/

# Chapter 4: the final output
# Step 13: load an image from a file and combine a call to the translation function with a call to the rotation function. Rotate 3 times and translate 5.
# Step 14: show the resulting image.
# Step 15: profit!

# Shoot me with any questions, I expect many.

# def translateDavid(inputImage, segmentCount):
#     if segmentCount < 3:
#         raise Exception("segmentCount must be equal to or greater than 3.")
#     segments = getSegments(segmentCount, inputImage.shape[1])    
#     copyImage = np.copy(inputImage)

#     for segmentIndex in range(int(segmentCount / 2)):
#         if segmentIndex % 2 != 0:
#             continue
#         for rowIndex in range(inputImage.shape[0]):
#             iteratorSourceColumn = segments[segmentIndex][0]
#             endSourceColumn = segments[segmentIndex][1]
#             iteratorDestinationColumn = segments[segmentCount - 1 - segmentIndex][0]
#             while iteratorSourceColumn <= endSourceColumn:
#                 copyImage[rowIndex][iteratorDestinationColumn] = inputImage[rowIndex][iteratorSourceColumn]
#                 copyImage[rowIndex][iteratorSourceColumn] = inputImage[rowIndex][iteratorDestinationColumn]
#                 iteratorDestinationColumn += 1
#                 iteratorSourceColumn += 1
#     return copyImage
