import cv2

kirby = cv2.imread("kirby_thing.png")
cv2.imshow("Kirby in mid life crisis", kirby)
#Center coordinates
center_coordinates = (120,50)

#Radius of circle
radius = 20

#Blue colour in bgr
color = (255,0,0)

#Line thickness
#putting a negative number makes the circle filled
thickness = 2

image = cv2.circle(kirby,center_coordinates,radius,color,thickness)

cv2.imshow("Kirby in mid life crisis but with a circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()