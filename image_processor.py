from collections import OrderedDict


class ImageProcessor:

    characters = OrderedDict()

    def __init__(self, image, pixels_per_char):
        self.image = image
        self.pixels_per_char = pixels_per_char

        self.characters[25] = " "
        self.characters[50] = "."
        self.characters[75] = "^"
        self.characters[100] = ";"
        self.characters[125] = "/"
        self.characters[150] = "4"
        self.characters[175] = "X"
        self.characters[200] = "%"
        self.characters[225] = "#"
        self.characters[250] = "█"

    def image_to_ascii(self):
        self.check_for_invalid_image()

        output = ""
        size = self.image.size

        y = 0
        while y < size[1]:

            x = 0
            while x < size[0]:
                luminosity = self.get_luminosity(x, y)
                new_char = self.get_new_character(luminosity)
                output += new_char
                x += self.pixels_per_char

            output += "\n"
            y += self.pixels_per_char * 2

        return output

    @staticmethod
    def get_new_character(luminosity):
        if luminosity <= 25:
            return " "
        elif luminosity <= 50:
            return "."
        elif luminosity <= 75:
            return "^"
        elif luminosity <= 100:
            return ";"
        elif luminosity <= 125:
            return "/"
        elif luminosity <= 150:
            return "4"
        elif luminosity <= 175:
            return "X"
        elif luminosity <= 150:
            return "%"
        elif luminosity <= 225:
            return "#"
        else:
            return "█"

    def get_luminosity(self, x, y):
        self.check_for_invalid_image()
        pixel = self.image.load()
        rgb_values = pixel[x, y][:3]
        luminosity = sum(rgb_values) // 3
        return luminosity

    def check_for_invalid_image(self):
        if not self.image:
            raise Exception("attempted to process unset image")
