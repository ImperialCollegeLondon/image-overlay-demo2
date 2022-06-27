from PIL import Image, ImageDraw, ImageFont


class ImageOverlay:
    image_file = None

    TEXT_COLOURS = {
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'white': (255, 255, 255),
        'orange': (240, 120, 70)
    }

    text_colour = TEXT_COLOURS['black']

    def __init__(self, image_file):
        self.image_file = image_file[0]

    def set_style(self, text_size, set_text_colour=None):
        if set_text_colour:
            self.text_colour = set_text_colour

    def overlay_text(self, text):
        print('Image file: %s' % self.image_file)
        with Image.open(self.image_file) as image:
            image_draw = ImageDraw.Draw(image)
            image_font = ImageFont.truetype('HelveticaNeue.ttc')
            print('<%s>' % text)
            image_draw.text((150, 100), text[0], self.text_colour,
                            font=image_font)

            extn_loc = self.image_file.rfind('.')
            output_file_name = (self.image_file[:extn_loc] +
                                '_overlay' + self.image_file[extn_loc:])

            image.save(output_file_name)
