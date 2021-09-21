IMAGE_START = 352
IMAGE_END = 224 



def regulate_negtive_coordinates(startX, endX): 
    range_to_add = 0 
    if startX < 0 : 
        range_to_add = - startX 
        startX = 0 
        endX += range_to_add
    if(endX > IMAGE_START) : 
        range_to_add = IMAGE_START - endX
        endX = IMAGE_START - 1
        startX -= -range_to_add + 1

    return startX, endX 




def cropping_coordinates(startX, startY, endX, endY):
    xRange = endX - startX
    yRange = endY - startY 
    lacked_range = IMAGE_END - xRange
    if(lacked_range > 0 ) : 
        endX += lacked_range//2
        startX -= lacked_range//2 
        if (lacked_range %2 != 0): endX+=1
    else : 
        endX -= (-lacked_range)//2 
        startX += (-lacked_range)//2
        if (lacked_range %2 != 0): startX+=1
    lacked_range = IMAGE_END - yRange
    if(lacked_range > 0) :  
        endY += lacked_range//2
        startY -= lacked_range//2
        if (lacked_range %2 != 0): endY+=1
    else : 
        endY -= (-lacked_range)//2
        startY += (-lacked_range)//2
        if (lacked_range %2 != 0): startY+=1

    return startX, startY, endX, endY 