import cv2

kirby = cv2.imread("kirby_thing.png")
cv2.imshow("Kirby in a mid_life crisis", kirby)
#top left corner
sp = (5,5)

#bottom right corner
ep = (220,220)

color = (255,0,0)

thickness = -2

rectangle = cv2.rectangle(kirby,sp,ep,color,thickness)
cv2.imshow("Kirby in a mid_life crisis with a rectangle",rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()


