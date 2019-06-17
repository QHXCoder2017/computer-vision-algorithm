# Calculate Intersect over usion between boxes b1 and b2, here each box is defined with 2 points
# box(startX, startY, endX, endY), there are other definitions ie box(x,y,width,height)


def compute_iou(b1, b2):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(b1[0], b2[0])
    yA = max(b1[1], b2[1])
    xB = min(b1[2], b2[2])
    yB = min(b1[3], b2[3])
    area_intersect = (xB - xA + 1) * (yB - yA + 1)
    b1_area = (b1[2] - b1[0] + 1) * (b1[3] - b1[1] + 1)
    b2_area = (b2[2] - b2[0] + 1) * (b2[3] - b2[1] + 1)
    iou = area_intersect / float(b1_area + b2_area - area_intersect)
    return iou
