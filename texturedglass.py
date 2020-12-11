# Scope:
# Use Python to load and display images. Create functions that will do the textured glass effect by combining translation of image columns (swap), 
# and rotation of image columns (flip)
import numpy as np
import cv2 as cv

img = cv.imread('static/Rialto.jpg')
cv.namedWindow('Rialto', cv.WINDOW_NORMAL)
cv.imshow('Rialto', img)
cv.waitKey(0)
cv.destroyAllWindows()

imageHeight, imageWidth, _ = img.shape
print('width:  ', imageWidth)
print('height: ', imageHeight)

def calculateVSegments(numberOfSegments, width):
    segments = []
    segmentWidth = int(width / numberOfSegments)
    for s in range(numberOfSegments):
        segments.append((segmentWidth * s, (segmentWidth * (s + 1)) - 1))
    return segments

def vtranslate(segmentCount, img):
    segments = calculateVSegments(segmentCount, imageWidth)
    copyImage = np.copy(img)
    for segment in range(int(segmentCount / 2) + 1):
        if segment % 2 != 0:
            continue
        leftSegment = segment
        rightSegment = segmentCount - 1 - segment
        copyImage[:imageHeight, segments[leftSegment][0]:segments[leftSegment][1]] = img[:imageHeight, segments[rightSegment][0]:segments[rightSegment][1]]
        copyImage[:imageHeight, segments[rightSegment][0]:segments[rightSegment][1]] = img[:imageHeight, segments[leftSegment][0]:segments[leftSegment][1]]
    return copyImage

# Vertical translation
translatedImage = vtranslate(10, img)
cv.imshow("BRO", translatedImage)
cv.waitKey(0)
cv.destroyAllWindows()

def calculateHSegments(numberOfSegments, height):
    hsegments = []
    segmentHeight = int(height / numberOfSegments)
    for j in range(numberOfSegments):
        hsegments.append((segmentHeight * j, (segmentHeight * (j + 1)) - 1))
    return hsegments

def htranslate(segmentCount, img):
    hsegments = calculateHSegments(segmentCount, imageHeight)
    copyImage2 = np.copy(img)
    for hsegment in range(int(segmentCount / 2) + 1):
        if hsegment % 2 != 0:
            continue
        bottomsegment = hsegment
        topsegment = segmentCount - 1 - hsegment
        copyImage2[hsegments[bottomsegment][0]:hsegments[bottomsegment][1], :imageWidth] = img[hsegments[topsegment][0]:hsegments[topsegment][1], :imageWidth]
        copyImage2[hsegments[topsegment][0]:hsegments[topsegment][1], :imageWidth] = img[hsegments[bottomsegment][0]:hsegments[bottomsegment][1], :imageWidth]
    return copyImage2
# Horizontal Translation
translatedImage2 = htranslate(10, img)
(cv.imshow("Bruv", translatedImage2))
cv.waitKey(0)
cv.destroyAllWindows()

# Chapter 3: rotation function

def vflipud(segmentCount, img):
    segments = calculateVSegments(segmentCount, imageWidth)
    vflipudimage = np.flipud(np.copy(img))
    for segment in range(int(segmentCount / 2) + 1):
        if segment % 2 != 0:
            continue
        leftSegment = segment
        rightSegment = segmentCount - 1 - segment
        vflipudimage[:imageHeight, segments[leftSegment][0]:segments[leftSegment][1]] = img[:imageHeight, segments[rightSegment][0]:segments[rightSegment][1]]
        vflipudimage[:imageHeight, segments[rightSegment][0]:segments[rightSegment][1]] = img[:imageHeight, segments[leftSegment][0]:segments[leftSegment][1]]
    return vflipudimage
#Upside Down Flipped Image
flippedandchopped = vflipud(5, img)
(cv.imshow("quoi", flippedandchopped))
cv.waitKey(0)
cv.destroyAllWindows()

def hflip(segmentCount, img):
    hsegments = calculateHSegments(segmentCount, imageHeight)
    hflipimage = np.fliplr(np.copy(img))
    for hsegment in range(int(segmentCount / 2) + 1):
        if hsegment % 2 != 0:
            continue
        bottomsegment = hsegment
        topsegment = segmentCount - 1 - hsegment
        hflipimage[hsegments[bottomsegment][0]:hsegments[bottomsegment][1], :imageWidth] = img[hsegments[topsegment][0]:hsegments[topsegment][1], :imageWidth]
        hflipimage[hsegments[topsegment][0]:hsegments[topsegment][1], :imageWidth] = img[hsegments[bottomsegment][0]:hsegments[bottomsegment][1], :imageWidth]
    return hflipimage

# Left to Right flipped image
flipimage = hflip(5, img)
cv.imshow("Flipped", flipimage)
cv.waitKey(0)
cv.destroyAllWindows()

#Flipped and translated vertically
FinalImageUD = vflipud(3, (vtranslate(5, img)))
cv.imshow("Final", FinalImageUD)
cv.waitKey(0)
cv.destroyAllWindows()

#Flipped and translated horizontally
FinalImageLR = hflip(3, (htranslate(5, img)))
cv.imshow("Final", FinalImageLR)
cv.waitKey(0)
cv.destroyAllWindows()