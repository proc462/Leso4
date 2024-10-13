import cv2

photo = cv2.imread("SNIPERS ROOFF.png")
cv2.imshow("Exibit C",photo)
#top left corner
sp = (5,5)

#bottom right corner
ep = (220,220)

color = (255,0,0)

thickness = 4

rectangle = cv2.rectangle(photo,sp,ep,color,thickness)
cv2.imshow("Exibit C with a rectangle",rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()
