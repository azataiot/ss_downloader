import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print('当前工作路径:{}'.format(dir_path))
img_dir = os.path.join(dir_path,'images')
print("目标图片下载地址：{}".format(img_dir))