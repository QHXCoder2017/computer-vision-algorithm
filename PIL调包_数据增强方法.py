from PIL import Image
from PIL import ImageEnhance
import os
import cv2
import numpy as np


# 平移
def move(root_path, img_name, off):
    img = Image.open(os.path.join(root_path, img_name))
    off_set = img.offset(off, 0)
    return off_set


# 图像翻转
def rotation(root_path, img_name):
    img = Image.open(os.path.join(root_path, img_name))
    rotation_img = img.rotate(20)  # 旋转角度
    # rotation_img.save(os.path.join(root_path, img_name.split('.')[0]+'_rotation.jpg'))
    return rotation_img


# 随机颜色
def random_Color(root_path, img_name):
    img = Image.open(os.path.join(root_path, img_name))
    random_factor1 = np.random.randint(0, 31) / 10.  # 随机因子
    color_image = ImageEnhance.Color(img).enhance(random_factor1)  # 调整图像的饱和度
    random_factor2 = np.random.randint(10, 21) / 10.  # 随机因子
    brightness_image = ImageEnhance.Brightness(color_image).enhance(random_factor2)  # 调整图像的亮度
    contrast_image = ImageEnhance.Contrast(brightness_image).enhance(random_factor2)  # 调整图像的对比度
    return ImageEnhance.Sharpness(contrast_image).enhance(random_factor1)  # 调整图像的锐度


# 对比度增强
def contrast_Enhancement(root_path, img_name):
    img = Image.open(os.path.join(root_path, img_name))
    con_enhancement = ImageEnhance.Contrast(img)
    contrast = 1.5
    img_contrasted = con_enhancement.enhance(contrast)
    return img_contrasted


# 亮度增强
def bright_Enhancement(root_path, img_name):
    img = Image.open(os.path.join(root_path, img_name))
    bri_enhancement = ImageEnhance.Brightness(img)
    brightness = 1.5
    img_brightened = bri_enhancement.enhance(brightness)
    return img_brightened


# 颜色增强
def color_Enhancement(root_path, img_name):
    img = Image.open(os.path.join(root_path, img_name))
    col_Enhancement = ImageEnhance.Color(img)
    color = 1.5
    img_colored = col_Enhancement(color)
    return img_colored
