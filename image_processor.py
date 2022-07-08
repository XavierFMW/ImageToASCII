from collections import OrderedDict


class ImageProcessor:

    def __init__(self):
        self.initialize_char_set()

    def initialize_char_set(self):
        self.characters = OrderedDict()
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

    def image_to_ascii(self, image, pixels_per_char):
        self.validate_image(image)

        output = ""
        size = image.size

        y = 0
        while y < size[1]:

            x = 0
            while x < size[0]:
                luminosity = self.get_luminosity(image, x, y)
                output += self.get_char_of_luminosity(luminosity)
                x += pixels_per_char

            output += "\n"
            y += pixels_per_char * 2

        return output

    def get_char_of_luminosity(self, luminosity):
        for char_luminosity, character in self.characters.items():
            if luminosity <= char_luminosity:
                return character

    @staticmethod
    def get_luminosity(image, x, y):
        pixels = image.load()
        pixel = pixels[x, y][:3]
        luminosity = sum(pixel) // 3
        return luminosity

    @staticmethod
    def validate_image(image):
        if not image:
            raise Exception("attempted to process unset image")
