import cv2
kirby = cv2.imread("kirby_thing.png")

cv2.imshow("Kirby in a mid_life crisis",kirby)

sp = (0,0)
ep = (300,250)
color = (0,255,0)
thickness = 10

line = cv2.line(kirby,sp,ep,color,thickness)
cv2.imshow("Kirby in a mid_life crisis but with a line", line)
cv2.waitKey(0)
cv2.destroyAllWindows()