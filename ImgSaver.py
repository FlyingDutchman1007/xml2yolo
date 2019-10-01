import xmlReader
import cv2 as cv

NUMBER_OF_DIGITS_TO_TRUNCATE = 6
XML_FILE_PATH = "E:/2019BaoSight/PythonProject/xml2yolo/firexml/"  # xml文件存放地址，可用sys.argv[1]代替
TXT_FILE_PATH = "E:/2019BaoSight/PythonProject/xml2yolo/txt/"  # txt文件存放地址，可用sys.argv[2]代替
VIDEO_FILE_PATH = "E:/2019BaoSight/PythonProject/xml2yolo/video/"

class ImgSaver():
    """
    通过ImgSaver实现对图片的保存
    """

    def __init__(self, xml_path):
        self.xmlReader = xmlReader.XmlReader(xml_path)

    def get_img_set(self):
        return self.xmlReader.img_set


# cap =cv.VideoCapture("E:/fenjie/1.mp4")
# isOpened = cap.isOpened()  ##判断视频是否打开


XML_FILE_PATH = "E:/2019BaoSight/PythonProject/xml-voc-_to_txt-yolo/firexml/"  # xml文件存放地址，可用sys.argv[1]代替
xmlReader = xmlReader.XmlReader(XML_FILE_PATH)
xmlReader.generate_img_set("0")  # 入参为需要截取时，occluded的取值
print(xmlReader.img_set[1].xtl)
for img in xmlReader.img_set:
    print(img.id)