#!/usr/bin/env python3
# https://github.com/w-a-gomes/systemutils

class Color(object):
    """Create an object of type 'Color'

    Obtém sequências de escape ANSI para cores no terminal.
    """
    def __init__(self):
        """Class constructor"""
        self.__styles = {
            # 'none': '0',
            'bold': '1',
            'dark': '2',
            'underline': '4',
            'negative': '7'
        }
        self.__colors = {
            # 'none': '30',
            'red': '31',
            'green': '32',
            'yellow': '33',
            'blue': '34',
            'purple': '35',
            'cyan': '36',
            'white': '37'
        }
        self.__backgrounds = {
            # 'none': '40',
            'red': '41',
            'green': '42',
            'yellow': '43',
            'blue': '44',
            'purple': '45',
            'cyan': '46',
            'white': '47'
        }

    def get_style(self, style: str = None, color: str = None, background: str = None) -> str:
        """Text style ANSI escape code

        Get an ANSI escape code configured with the style, color and background of the text.

        :param style: Can be None, 'bold', 'dark', 'underline' or 'negative'
        :param color: Can be None, 'red', 'green', 'yellow', 'blue', 'purple', 'cyan' or 'white'
        :param background: Can be None, 'red', 'green', 'yellow', 'blue', 'purple', 'cyan' or 'white'
        :return: String containing ANSI escape code for the configured style
        """
        style = '{}'.format(self.__styles[style]) if style else ''
        color = ';{}'.format(self.__colors[color]) if color else ''
        background = ';{}'.format(self.__backgrounds[background]) if background else ''

        return '\033[{}{}{}m'.format(style, color, background)

    @staticmethod
    def reset_style():
        return '\033[m'


if __name__ == '__main__':
    c = Color()
    print(c.get_style(color='red') + 'red')
    print(c.get_style(color='blue') + 'blue')
    print(c.get_style(color='green') + 'green')
    print(c.get_style(color='green', style='bold') + 'green bold')
    print(c.get_style(color='purple') + 'purple')
    print(c.get_style(color='yellow', background='blue') + 'yellow + blue background' + c.reset_style())
    print(c.get_style(style='underline', color='cyan') + 'cyan underline')
    print(c.reset_style() + 'reset')
