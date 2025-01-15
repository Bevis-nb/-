from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QPixmap, Qt, QImage
from ui_untitled import Ui_MainWindow
import sys
from ui_function import UIFunctions
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from shutil import copy
from os.path import basename, exists

plt.rcParams['font.family'] = ['SimHei']  # 使用中文字体，例如黑体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class myapp(QMainWindow, UIFunctions):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 设置UI样式
        self.uiDefinitions()
        # 绑定按钮
        self.ui.inpix.clicked.connect(self.funciton_group)
        self.ui.mix.clicked.connect(self.funciton_group)
        self.ui.out.clicked.connect(self.funciton_group)
        self.ui.print.clicked.connect(self.funciton_group)
        self.ui.finder.clicked.connect(self.funciton_group)
    def funciton_group(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "inpix":
            pix_dialog = QFileDialog()
            self.pix_path, _ = pix_dialog.getOpenFileName(
                self,
                "选择图片",
                "",
                "图片文件(*.jpg *.png *.jpeg *.bmp *.gif)"
            )
            if self.pix_path:
                self.ui.out.setEnabled(False)
                self.ui.name.setText("")
                self.ui.PA.setText("")
                self.ui.PB.setText("")
                self.ui.PH.setText("")
                self.ui.PA2.setText("")
                self.ui.PB2.setText("")
                self.ui.PH2.setText("")
                self.ui.color.setText("")
                self.ui.weight.setText("")
                label_size = self.ui.label.size()
                print(f"选择了{self.pix_path}")
                pixmap = QPixmap(self.pix_path)
                scaled_pixmap = pixmap.scaled(
                    label_size,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.ui.label.setPixmap(scaled_pixmap)
            else:
                self.show_warning("没有选择图片")

        if btnName == "mix":
            pixmap = self.ui.label.pixmap()
            if pixmap:
                product_cun = self.ui.PA.text() + "x" + self.ui.PB.text() + "x" + self.ui.PH.text()
                package_cun = self.ui.PA2.text() + "x" + self.ui.PB2.text() + "x" + self.ui.PH2.text()
                name = self.ui.name.text()
                color = self.ui.color.text()
                weight = self.ui.weight.text()
                file_name, file_ext = basename(self.pix_path).split(".")
                if product_cun == "xx" or package_cun == "xx" or name == "" or weight == "":
                    self.show_warning("还有参数未填写")
                else:
                    if exists(f"./cool/{name}.{file_ext}"):
                        result = self.show_info("是否确认覆盖合成")
                        if result == QMessageBox.Yes:
                            self.mix_funciton(product_cun, package_cun, name, color, weight, file_ext)
                    else:
                        self.mix_funciton(product_cun, package_cun, name, color, weight, file_ext)
            else:
                self.show_warning("没有选择图片")

        if btnName == "out":
            print("导出图片中")
            image = self.ui.label.pixmap()
            if image:
                # 弹出文件保存对话框
                options = QFileDialog.Options()
                file_path, _ = QFileDialog.getSaveFileName(
                    None,
                    "保存图片",
                    self.ui.name.text() + ".jpg",  # 使用原文件名作为默认文件名
                    "Images (*.png *.xpm *.jpg *.bmp);;All Files (*)",
                    options=options
                )
                if file_path:
                    copy("temp.jpg", file_path)
                    print(f"图片已保存至 {file_path}")
                else:
                    print("用户取消了保存操作")
            else:
                print("没有可导出的图片")
                self.show_warning("没有可导出的图片")

        print(f"鼠标点击了:{btnName}")

    def mix_funciton(self, product_cun, package_cun, name, color, weight, file_ext):
        data = [["型号", name],
                ["产品尺寸", product_cun],
                ["包装尺寸", package_cun],
                ["颜色", color],
                ["重量", weight]
                ]
        self.create_table_chart(data)
        print(self.pix_path)
        new_pixmap = self.add_chart_to_image(self.pix_path)
        self.ui.label.setPixmap(new_pixmap)
        copy(self.pix_path, f"./cool/{name}.{file_ext}")
        temp_txt = "型号" + " " + name + "\n" + "产品尺寸" + " " + product_cun + "\n" + "包装尺寸" + " " + package_cun + "\n" + "颜色" + " " + color + "\n" + "重量" + weight
        with open(f"./cool/{name}.txt", "w", encoding="utf-8") as f:
            f.write(temp_txt)
        self.ui.out.setEnabled(True)

    def create_table_chart(self, data):
        # 创建图表
        fig, ax = plt.subplots(figsize=(3, 2))
        table = ax.table(cellText=data, loc='center', cellLoc='left')
        ax.axis('off')

        # 调整表格布局
        table.auto_set_column_width(col=list(range(len(data[0]))))
        table.scale(2.3, 4)  # 减小水平缩放比例，增加垂直缩放比例
        table.auto_set_font_size(False)
        table.set_fontsize(40)

        # 保存图表，使用 bbox_inches='tight' 和 pad_inches=0 减少空白部分
        # plt.savefig('chart.png', bbox_inches='tight', pad_inches=0)
        plt.savefig('chart.png', bbox_inches='tight')

    def add_chart_to_image(self, image_path):
        # 读取原始图像
        image = Image.open(image_path)
        image = image.convert('RGB')

        # 读取图表图像
        chart_image = Image.open('chart.png')
        chart_image = chart_image.convert('RGB')

        # 计算缩放比例
        max_size = (1600, 1200)
        image.thumbnail(max_size, Image.LANCZOS)

        # 获取图像和图表的尺寸
        image_width, image_height = image.size
        chart_width, chart_height = chart_image.size

        # 创建一个新的白色背景图像，其大小足以容纳原图像和表格
        new_image_height = max(image_height, chart_height)  # 保持最大的高
        new_image_width = image_width + chart_width + 20  # 增加一些额外的边距，可调整
        new_image = Image.new('RGB', (new_image_width, new_image_height), color='white')

        # 将原图像放在新图像的左上角
        new_image.paste(image, (0, 0))

        # 计算图表在新图像右下角的位置
        start_x = image_width + 10
        start_y = new_image_height - chart_height

        # 将图表图像粘贴到新图像
        new_image.paste(chart_image, (start_x, start_y))

        # Convert the result image to QPixmap
        result_image = np.array(new_image)
        height, width, channel = result_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(result_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        label_size = self.ui.label.size()
        pixmap.save("temp.jpg")
        scaled_pixmap = pixmap.scaled(
            label_size,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        return scaled_pixmap

    def show_warning(self, words):
        """
        words : str 显示的文字
        :param words:
        :return:
        """
        mes = QMessageBox()
        mes.setText(words)
        mes.setIcon(QMessageBox.Icon.Warning)
        mes.setWindowTitle("警告")
        mes.setWindowIcon(QIcon("image/警告.ico"))
        mes.setStandardButtons(QMessageBox.Ok)
        mes.exec()

    def show_successd(self, words):
        """
        words : str 显示的文字
        :param words:
        :return:
        """
        mes = QMessageBox()
        mes.setText(words)
        mes.setIcon(QMessageBox.Icon.Information)
        mes.setWindowTitle("成功")
        mes.setWindowIcon(QIcon("image/成功.ico"))
        mes.setStandardButtons(QMessageBox.Ok)
        mes.exec()

    def show_info(self, words):
        mes = QMessageBox()
        mes = QMessageBox()
        mes.setText(words)
        mes.setIcon(QMessageBox.Icon.Warning)
        mes.setWindowTitle("警告")
        mes.setWindowIcon(QIcon("image/警告.ico"))
        mes.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return mes.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = myapp()
    windows.show()
    sys.exit(app.exec())
