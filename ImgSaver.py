import xmlReader

NUMBER_OF_DIGITS_TO_TRUNCATE = 6
XML_FILE_PATH = "E:/2019BaoSight/PythonProject/xml-voc-_to_txt-yolo/firexml/"  # xml文件存放地址，可用sys.argv[1]代替
TXT_FILE_PATH = "E:/2019BaoSight/PythonProject/xml-voc-_to_txt-yolo/txt/"  # txt文件存放地址，可用sys.argv[2]代替

class ImgSaver():
    """
    通过ImgSaver实现对图片的保存
    """

    def __init__(self, xml_path):
        self.xmlReader = xmlReader.XmlReader(xml_path)

    def get_img_set(self):
        return self.xmlReader.img_set







XML_FILE_PATH = "E:/2019BaoSight/PythonProject/xml-voc-_to_txt-yolo/firexml/"  # xml文件存放地址，可用sys.argv[1]代替
xmlR = xmlReader.XmlReader(XML_FILE_PATH)
xmlR.generate_img_set("0")  # 入参为需要截取时，occluded的取值
print(xmlR.img_set[1].xtl)