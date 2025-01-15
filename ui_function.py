from PySide6.QtGui import QColor

class UIFunctions:
    def uiDefinitions(self):
        super().__init__()

        self.ui.inpix.setParams(
            text= "导入图片",
            border_radius=5,
            full_color=QColor('#34495e'),
            font_anim_start_color=QColor('#34495e'),
            font_anim_finish_color=QColor("#ffffff"),
        )
        self.ui.mix.setParams(
            text="合成",
            border_radius=5,
            full_color=QColor('#34495e'),
            font_anim_start_color=QColor('#34495e'),
            font_anim_finish_color=QColor("#ffffff"),
        )
        self.ui.finder.setParams(
            text="寻找",
            border_radius=5,
            full_color=QColor('#34495e'),
            font_anim_start_color=QColor('#34495e'),
            font_anim_finish_color=QColor("#ffffff"),
        )
        self.ui.out.setParams(
            text="导出",
            border_radius=5,
            full_color=QColor('#34495e'),
            font_anim_start_color=QColor('#34495e'),
            font_anim_finish_color=QColor("#ffffff"),
        )
        self.ui.print.setParams(
            text="打印",
            border_radius=5,
            full_color=QColor('#34495e'),
            font_anim_start_color=QColor('#34495e'),
            font_anim_finish_color=QColor("#ffffff"),
        )
