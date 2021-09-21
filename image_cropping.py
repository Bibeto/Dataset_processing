import cv2 
from cropping_coordinates import cropping_coordinates, regulate_negtive_coordinates

TRAIN_PATH = 'lightfield/train'
TEST_PATH = 'lightfield/test'

train_annotation_file = open("lightfield/train.txt", 'r')
test_annotation_file = open("lightfield/test.txt", 'r')

IMAGE_START = 352 



for line in train_annotation_file : 
    line = line.split()
    filename = line[0]
    startX = int(line[1]) 
    startY = int(line[2]) 
    endX = int(line[3]) 
    endY = int(line[4]) 

    image = cv2.imread(TRAIN_PATH + '/' + filename)

    startX, startY, endX, endY = cropping_coordinates(startX, startY, endX, endY)
    startX, endX = regulate_negtive_coordinates(startX, endX)
    startY, endY = regulate_negtive_coordinates(startY, endY)

    image_cropped = image[startY : endY, startX : endX]
    cropped_image_path = 'cropped_lightfield/train/'+filename

    cv2.imwrite(cropped_image_path, image_cropped)


train_annotation_file.close()
test_annotation_file.close()