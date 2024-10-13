import cv2

photo = cv2.imread("SNIPERS ROOFF.png")
cv2.imshow("Exibit A", photo)

center_coordinates = (120,50)

radius = 20

color = (255,0,0)

thickness = 2

image = cv2.circle(photo,center_coordinates,radius,color,thickness)

cv2.imshow("Exibit A with a circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()