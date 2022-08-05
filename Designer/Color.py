from typing import Union
from .Values import colors

class Colors:
    def __init__(self) -> None:
        pass
    def fore_ground_color(text : str, style : int, r : int, g : int, b : int, background : Union[bool,str] = False) -> str:
        """ it's return the color code of the given text. it's return the color code based on given RGB.\n
            >> fore_ground_color(text : str, r : int, g : int, b : int, style : int = 0)\n
            How to use :\n
                text = it's need a string input\n
                r, b, g = This is the RGB color code like white RGB(255,255,255)\n
                Style = {
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5
                        }
        """
        if background:
            background_color : str = colors.get(background.upper())
            return "\033[{};48;2;{};{};{}m{}\033[0;38;2;{};{};{}m\033[0;48;0;0;0;0m".format(style,background_color[0], background_color[1], background_color[2], text,r,g,b)
        else:
            return "\033[{};38;2;{};{};{}m{}\033[0;38;2;255;255;255m".format(style,r, g, b, text)
    
    def back_ground_color(text : str, style : int, r : int, g : int, b : int) -> str :
        """ it's return the BackGround color code of the given text. it's return the color code based on given RGB.\n
            >> back_ground_color(text : str, r : int, g : int, b : int, style : int = 0)\n
            How to use :\n
                text = it's need a string input\n
                r, g, b = This is the RGB color code of background like white RGB(255,255,255)\n
                Style = {
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5
                        }
        """
        return "\033[{};48;2;{};{};{}m{}\033[0;48;0;255;255;255m".format(style,r, g, b, text)


 