import numpy as np


def cpu_nms(dets, thresh):
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    # 每一个检测框的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    # 按照置信度降序排列
    order = scores.argsort()[::-1]
    # 保留结果框的集合
    keep = []
    while order.size() > 0:
        i = order[0]
        keep.append(i)  # 保留该类剩余box中得分最高的一个
        # 得到相交区域，左上和右下
        xx1 = np.max(x1[i], x1[order[1:]])
        yy1 = np.max(y1[i], y1[order[1:]])
        xx2 = np.max(x2[i], x2[order[1:]])
        yy2 = np.max(y2[i], y2[order[1:]])
        # 计算相交的面积，不重叠时面积为0
        w = np.max(0.0, xx2-xx1+1)
        h = np.max(0.0, yy2-yy1+1)
        inter_area = w * h
        # 计算IOU：重叠面积/(面积1+面积2-重叠面积)
        iou = inter_area / (areas[i] + areas[order[1:]] - inter_area)
        # 保留IOU小于阈值的box
        inds = np.where(iou <= thresh)[0]
        order = order[inds+1]  # 因为iou数组的长度比order数组少一个，所以将所有下标后移1位
    return keep

