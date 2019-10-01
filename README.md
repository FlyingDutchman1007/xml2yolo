# 按照xml对MP4进行图像截取用于YOLO训练

XmlReader 能解析xml文件
ImgSaver 用于根据 xmlReader 从 mp4 格式的视频中截取、保存 jpg 格式图片

测试执行：
运行ImgSaver.py即可，具体代码为：


imgSaver = ImgSaver(XML_FILE_PATH)


imgSaver.save_img()
