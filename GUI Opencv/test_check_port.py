import cv2

list_ = []

for i in range(5):
    c = cv2.VideoCapture(i)

    valid,_ =c.read()
    if valid:
        list_.append(str(i))
tup = tuple(list_)
print(tup)