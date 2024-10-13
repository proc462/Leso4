import cv2

kirby = cv2.imread("kirby_thing.png")

pos = (150,150)

#font
font = cv2.FONT_HERSHEY_SIMPLEX

#fontScale
fontScale = 1

#Blue colour in BGR
color = (255,0,0)

#Line Thickness of 2px
thickness = 2

kirby = cv2.putText(kirby, "I'm Kirby",pos,font,fontScale,color,thickness)

cv2.imshow("a",kirby)

cv2.waitKey(0)
cv2.destroyAllWindows()
