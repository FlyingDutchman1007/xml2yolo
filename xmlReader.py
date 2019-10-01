import os
from xml.dom import minidom
from decimal import Decimal as dec
import xml.dom.minidom

NUMBER_OF_DIGITS_TO_TRUNCATE = 6
XML_FILE_PATH = "E:/2019BaoSight/PythonProject/xml2yolo/xml/"  # xml文件存放地址，可用sys.argv[1]代替
TXT_FILE_PATH = "E:/2019BaoSight/PythonProject/xml2yolo/txt/"  # txt文件存放地址，可用sys.argv[2]代替


class XmlReader():
    """
    读取单个Xml文件 将框的信息封装成对象Image传给ImgSaver
    """

    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.img_tree = get_img_from_xml(xml_path)
        self.img_set = []
        self.id = get_id_from_xml(xml_path)

    def generate_img_set(self, correct_sign): # 为xmlReader生成img_set
        """
        初始化xmlReader, 先生成img_set; 后对xmlReader的id进行读取、赋值
        :param correct_sign: 当且仅当occluded为0时添加至img_set列表，即occluded
        :return: None
        """
        self.img_set = [] # 初始化img_set为空

        # for img in self.img_tree.getElementsByTagName("image"):
        for img in self.img_tree:
            print("将 " + img.getAttribute("name") + "添加至img_set中...")
            img_box = img.childNodes[1]

            # 从xml获取image参数
            img_id = img.getAttribute("id").zfill(6)
            img_label = img_box.getAttribute("label")
            img_occluded = img_box.getAttribute("occluded")
            img_xtl = img_box.getAttribute("xtl")
            img_ytl = img_box.getAttribute("ytl")
            img_xbr = img_box.getAttribute("xbr")
            img_ybr = img_box.getAttribute("ybr")

            # 当且仅当occluded为0时添加至img_set列表
            if img_occluded == correct_sign: # 暂时还没加index异常抛出，要是一张图都不截会炸
                # 创建image对象并添加金img_set
                image = Image(self.id ,img_id, img_label, img_occluded, img_xtl, img_ytl, img_xbr, img_ybr)
                self.img_set.append(image)


class Image():
    """
    图片对象，保存的信息包括
    xml_id: 该xml文件的编号
    id: 图片的帧号
    label: 图片的label
    occluded: 图片是否为关键帧
    xtl: 左上顶点的x坐标
    ytl: 左上顶点的y坐标
    xbr: 右下顶点的x坐标
    ybr: 右下顶点的y坐标
    """

    def __init__(self, xml_id, id, label, occluded, xtl, ytl, xbr, ybr):

        self.xml_id = xml_id
        self.id = id
        self.label = label
        self.occluded = occluded
        self.xtl = xtl
        self.ytl = ytl
        self.xbr = xbr
        self.ybr = ybr


def truncate(num_list):
    for i, val in enumerate(num_list):
        num_list[i] = float(round(dec(val), NUMBER_OF_DIGITS_TO_TRUNCATE))



def handle_index_ValueError(class_name, classes_list, ob_class):
    for val in class_name:
        try:
            classes_list.index(val)
        except ValueError:
            classes_list.append(val)

        ob_class.append(classes_list.index(val))



# this function returns the value of a given tag in list format,
# the return format is a list even when there is only one number
def return_list_from_xml_field(xml_field):
    elements = []
    for i in xml_field:
        elements.append(i.toxml().split(">")[1].split("<")[0])  # this is ugly, i know
    return elements


def get_img_from_xml(path_to_xml_file):
    """
    从xml文件中加载图片集
    :param path_to_xml_file: xml文件的地址
    :return: 包含img DOM 的 list
    """
    # 加载 xml file
    for file in os.listdir(XML_FILE_PATH):  # 对文件夹内的每个文件进行判断，若为xml则将img添加进img_set
        if file.endswith(".xml"):
            # 获取img_tree
            DOMTree = xml.dom.minidom.parse(path_to_xml_file + file)
            collection = DOMTree.documentElement
            img_tree = collection.getElementsByTagName('image')

    return img_tree

def get_data_from_xml(path_to_xml_file):
    """
    从xml文件中加载图片集
    :param path_to_xml_file: xml文件的地址
    :return: 包含img DOM 的 list
    """
    # 加载 xml file
    for file in os.listdir(path_to_xml_file):  # 对文件夹内的每个文件进行判断，若为xml则将img添加进img_set
        if file.endswith(".xml"):
            DOMTree = xml.dom.minidom.parse(path_to_xml_file + file)
            collection = DOMTree.documentElement
            # img_tree = collection.getElementsByTagName('image')

    return collection

def get_id_from_xml(path_to_xml_file):
    """
    从xml文件中获取当前xml的id
    :param path_to_xml_file: xml文件的地址
    :return: 包含img DOM 的 list
    """
    # 加载 xml file
    for file in os.listdir(XML_FILE_PATH):  # 对文件夹内的每个文件进行判断，若为xml则将img添加进img_set
        if file.endswith(".xml"):
            DOMTree = xml.dom.minidom.parse(path_to_xml_file + file)
            collection = DOMTree.documentElement
            url = collection.getElementsByTagName('url')
            url = url[0].childNodes[0].data
            id = url.split("id=")[1]

    return id



def get_data_from_xml(path_to_xml_file):
    """
    原本用于xml硬转txt的方法，已被弃置
    :param path_to_xml_file:
    :return:
    """
    # 加载 xml file
    xmldoc = minidom.parse(path_to_xml_file)

    # 返回 xml classes names

    class_name = return_list_from_xml_field(xmldoc.getElementsByTagName('name'))

    # load images width and height from xml file

    image_width = return_list_from_xml_field(xmldoc.getElementsByTagName('width'))
    image_height = return_list_from_xml_field(xmldoc.getElementsByTagName('height'))

    image_width = list(map(float, image_width))
    image_height = list(map(float, image_height))

    # load bouding boxes width and height from xml file

    x_max = return_list_from_xml_field(xmldoc.getElementsByTagName('xmax'))
    x_min = return_list_from_xml_field(xmldoc.getElementsByTagName('xmin'))
    y_max = return_list_from_xml_field(xmldoc.getElementsByTagName('ymax'))
    y_min = return_list_from_xml_field(xmldoc.getElementsByTagName('ymin'))

    x_max = list(map(float, x_max))
    x_min = list(map(float, x_min))
    y_max = list(map(float, y_max))
    y_min = list(map(float, y_min))

    absolute_x = []
    absolute_y = []
    absolute_width = []
    absolute_height = []

    # if your xml has more than one labeled object, the x_max,x_min,y_max,y_min will be lists
    for i in range(len(x_max)):
        # calculate the bouding box center in x axis and y axis

        absolute_x.append(x_min[i] + 0.5 * (x_max[i] - x_min[i]))
        absolute_y.append(y_min[i] + 0.5 * (y_max[i] - y_min[i]))

        # calculate absolute width and height from bouding boxes

        absolute_width.append(x_max[i] - x_min[i])
        absolute_height.append(y_max[i] - y_min[i])

    return class_name, absolute_x, absolute_y, absolute_width, absolute_height, image_width, image_height


def transform_from_xml_to_txt_format(absolute_x, absolute_y, absolute_width, absolute_height, image_width,
                                     image_height):
    """
    已被弃置
    :param absolute_x:
    :param absolute_y:
    :param absolute_width:
    :param absolute_height:
    :param image_width:
    :param image_height:
    :return:
    """
    # yolo coordinates of the bouding boxes are relative to image,
    # so we have to divide the measures by the image measures
    x = []
    y = []
    width = []
    height = []
    for i in range(len(absolute_width)):
        x.append(absolute_x[i] / image_width[0])
        y.append(absolute_y[i] / image_height[0])
        width.append(absolute_width[i] / image_width[0])
        height.append(absolute_height[i] / image_height[0])

    return x, y, width, height


def create_txt_file(ob_class, x, y, width, height, path_of_file_creation, file_name):
    """
    已被弃置
    :param ob_class:
    :param x:
    :param y:
    :param width:
    :param height:
    :param path_of_file_creation:
    :param file_name:
    :return:
    """
    # open file on writing mode, write values received and close the file
    txt_file = open(path_of_file_creation + file_name, "w+")

    truncate(x)
    truncate(y)
    truncate(width)
    truncate(height)

    x = list(map(str, x))
    y = list(map(str, y))
    width = list(map(str, width))
    height = list(map(str, height))
    ob_class = list(map(str, ob_class))

    for i in range(len(ob_class)):
        # print("imagem:"+str(i))
        # print(x[i])
        # print(y[i])
        # print(width[i])
        # print(height[i])
        txt_file.write(ob_class[i] + " " + x[i] + " " + y[i] + " " + width[i] + " " + height[i])
        txt_file.write("\n")

    txt_file.close()



# 若需要单独测试xmlReader,可执行一下代码：

# if __name__ == "__main__":
#     # classes_list = []
#     # for file in os.listdir(XML_FILE_PATH):
#     #     if file.endswith(".xml"):
#     #         class_name,absolute_x,absolute_y,absolute_width,absolute_height, image_width, image_height = get_data_from_xml(XML_FILE_PATH+file)
#     #         ob_class = []
#     #
#     #         handle_index_ValueError(class_name,classes_list,ob_class)
#     #
#     #
#     #
#     #         x,y,width,height = transform_from_xml_to_txt_format(absolute_x,absolute_y,absolute_width,absolute_height, image_width, image_height)
#     #         create_txt_file(ob_class,x,y,width,height,TXT_FILE_PATH,file[:-4])
#     #
#     # generate_classes_file(classes_list,TXT_FILE_PATH)
#     # print("Conversão efetuada com sucesso.")
#
#     # for file in os.listdir(XML_FILE_PATH):
#     #     if file.endswith(".xml"):
#     #         img_set = get_img_from_xml(XML_FILE_PATH + file) # 获取xml文件中的img集合
#     #
#     #         for img in img_set:
#     #             print("准备处理 " + img.getAttribute("name"))
#     #             img_xtl = img.getAttribute("xtl")
#     #             img_ytl = img.getAttribute("ytl")
#     #             img_xbr = img.getAttribute("xbr")
#     #             img_ybr = img.getAttribute("ybr")
#
#     xmlReader = XmlReader(XML_FILE_PATH)
#     xmlReader.generate_img_set("0") #入参为需要截取时，occluded的取值
#     print(xmlReader.img_set[1].xtl)
#     print(str(xmlReader.id))

