import xmlReader
import cv2 as cv

NUMBER_OF_DIGITS_TO_TRUNCATE = 6
XML_FILE_PATH = "E:/2019BaoSight/PythonProject/xml2yolo/xml/"  # xml文件存放地址，可用sys.argv[1]代替
TXT_FILE_PATH = "E:/2019BaoSight/PythonProject/xml2yolo/txt/"  # txt文件存放地址，可用sys.argv[2]代替
VIDEO_FILE_PATH = "E:/2019BaoSight/PythonProject/xml2yolo/video/"
IMG_FILE_PATH = "E:/2019BaoSight/PythonProject/xml2yolo/img/"

class ImgSaver():
    """
    通过ImgSaver实现对图片的保存
    """

    def __init__(self, xml_path):
        self.xmlReader = xmlReader.XmlReader(xml_path)

    def get_img_set(self):
        return self.xmlReader.img_set

    def save_img(self):
        """
        保存图片的方法，将图片保存到指定文件目录
        :return: 是否成功
        """

        self.xmlReader.generate_img_set("0")  # 入参为需要截取时，occluded的取值

        cap = cv.VideoCapture(VIDEO_FILE_PATH + "fire4.mp4")  # 一个被写死的文件名
        isOpened = cap.isOpened()  # 判断视频是否打开
        print(isOpened)

        end_time = self.xmlReader.img_set[-1].id
        print(end_time)

        current_frame = 0
        while isOpened:
            if current_frame == len(self.xmlReader.img_set):  # 到最后一帧停止
                break
            else:
                current_frame = current_frame + 1

            (flag, frame) = cap.read()
            # 图片裁剪
            xtl = round(float(self.xmlReader.img_set[current_frame - 1].xtl))
            ytl = round(float(self.xmlReader.img_set[current_frame - 1].ytl))
            xbr = round(float(self.xmlReader.img_set[current_frame - 1].xbr))
            ybr = round(float(self.xmlReader.img_set[current_frame - 1].ybr))
            img_id = self.xmlReader.img_set[current_frame - 1].id
            frame = frame[xtl:xbr, ytl:ybr]

            # 图片命名格式
            fileName = "ID_" + str(self.xmlReader.id) + "_frame_" + str(img_id) + ".jpg"
            print(fileName)
            if flag == True:
                cv.imwrite(IMG_FILE_PATH + fileName, frame, [cv.IMWRITE_JPEG_CHROMA_QUALITY, 100])  ##命名 图片 图片质量
        print("finish")
        return True


# xmlReader = xmlReader.XmlReader(XML_FILE_PATH)
# xmlReader.generate_img_set("0")  # 入参为需要截取时，occluded的取值
#
# for img in xmlReader.img_set:
#     print(img.id)
#
# cap =cv.VideoCapture(VIDEO_FILE_PATH + "fire4.mp4") #一个被写死的文件名
# isOpened = cap.isOpened()  # 判断视频是否打开
# print(isOpened)
#
# end_time = xmlReader.img_set[-1].id
# print(end_time)
#
# current_frame = 0
# while isOpened :
#     if current_frame == len(xmlReader.img_set):   # 到最后一帧停止
#         break
#     else:
#         current_frame = current_frame + 1
#
#     (flag,frame)=cap.read()
#     # 图片裁剪
#     xtl = round(float(xmlReader.img_set[current_frame-1].xtl))
#     ytl = round(float(xmlReader.img_set[current_frame-1].ytl))
#     xbr = round(float(xmlReader.img_set[current_frame-1].xbr))
#     ybr = round(float(xmlReader.img_set[current_frame-1].ybr))
#     img_id = xmlReader.img_set[current_frame-1].id
#     frame = frame[xtl:xbr, ytl:ybr]
#
#     # 图片命名格式
#     fileName = "ID_"+ str(xmlReader.id)+ "_frame_" + str(img_id) + ".jpg"
#     print(fileName)
#     if flag == True :
#         cv.imwrite(IMG_FILE_PATH + fileName, frame, [cv.IMWRITE_JPEG_CHROMA_QUALITY,100])  ##命名 图片 图片质量
# print("finish")