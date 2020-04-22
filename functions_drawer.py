from typing import List
from PIL import ImageColor, ImageDraw, Image
from coord_util import *


class Drawer:

    def __init__(self, width, height, background_color="white"):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height), ImageColor.getrgb(background_color))
        self.draw = ImageDraw.Draw(self.image)

    def clean(self, background_color="black"):
        self.image = self.image = Image.new("RGB", (self.width, self.height), ImageColor.getrgb(background_color))

    def save_image(self, name="Untitled"):
        name += ".png"
        self.image.save(name, "PNG")

    def draw_farn(self, color="purple"):
        self.__draw_sn1cka_farn(self.width / 5 * 2, self.height, self.height / 7, 180, 4, color)

    def draw_dragon_curve(self, color="white", ):
        lines = [Line(self.width / 4, self.height / 2 + self.height / 4, self.width / 4, self.height / 2 + self.height / 4 + 10)]
        lines = self.__get_dragon_curve_lines(lines)
        for line in lines:
            self.draw.line((line.x0, line.y0, line.x1, line.y1), width=5, fill=ImageColor.getrgb(color))

    def __draw_sn1cka_farn(self, x: int, y: int, line_length, angle, delta_angle, color):
        line_length *= 0.9
        if line_length > 1:
            main_line_end = get_coords(x, y, angle, 0, line_length)
            self.draw.line((x, y, main_line_end[0], main_line_end[1]), width=5, fill=ImageColor.getrgb(color))
            self.__draw_sn1cka_farn(main_line_end[0], main_line_end[1], line_length, angle + delta_angle,
                                    delta_angle, color)
            m_delta_x = main_line_end[0] - x
            m_delta_y = main_line_end[1] - y
            self.__draw_sn1cka_farn(x + m_delta_x / 5 * 4, y + m_delta_y / 5 * 4, line_length * 0.3, angle - 70, delta_angle, color)
            self.__draw_sn1cka_farn(x + m_delta_x / 5 * 2, y + m_delta_y / 5 * 2, line_length * 0.3, angle + 70, delta_angle, color)

    def __get_dragon_curve_lines(self, lines: List[Line]):
        try:
            rotate_point = Point(lines[-1].x1, lines[-1].y1)
            new_list = []
            for line in reversed(lines):
                new_coords_start = get_coords(rotate_point.x, rotate_point.y, -90, line.x1 - rotate_point.x, line.y1 - rotate_point.y)
                new_coords_end = get_coords(rotate_point.x, rotate_point.y, -90, line.x0 - rotate_point.x, line.y0 - rotate_point.y)
                new_list.append(Line(new_coords_start[0], new_coords_start[1], new_coords_end[0], new_coords_end[1]))
            lines += new_list
            self.__get_dragon_curve_lines(lines)
        except:
            print(len(lines))
            return lines
        finally:
            return lines
