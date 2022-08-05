from .Color import Colors

default_style = 0

def set_default_stylebg(Style : int) -> None :
        """  it's used to change the default values (or) change the value of style to all colors\n
        ----------------------------------------------------
        Ex : set_default_stylebg(3) then it chenge the Italicized style to all color_function\n
        ----------------------------------------------------
        Some style propertys :\n
        Normal     = 0 \n
        Bold       = 1 \n
        Light      = 2 \n
        Italicized = 3 \n
        UnderLined = 4 \n        
        Blink      = 5 \n
        ~~~~~~~
        Return: it's return None Value,it's not return any values just it change the changes in BackGroundColor file.
        """
        global default_style
        default_style = Style
        
def greybg( text : str, style : int = default_style ) -> str :
        """
        It will return the greybg colored BackGround text.\n
        greybg() is a BackGround Function, if You add ForeGround property given text you can use Grey .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                greybg("Hello World", Style = 0 ) = it's return greybg color text without any style       \n
                greybg("Hello World", Style = 1 ) = it's return greybg color text with bold text          \n
                greybg("Hello World", Style = 2 ) = it's return greybg color text with light text         \n
                greybg("Hello World", Style = 3 ) = it's return greybg color text with Italicized style   \n
                greybg("Hello World", Style = 4 ) = it's return greybg color text with UnderLine          \n
                greybg("Hello World", Style = 5 ) = it's return Blinking greybg color text                \n
        """
        return Colors.back_ground_color(text, style, 84, 84, 84)
                


def grey_silverbg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey_silverbg colored BackGround text.\n
        grey_silverbg() is a BackGround Function, if You add ForeGround property given text you can use Grey_Silver .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey_silverbg("Hello World", Style = 0 ) = it's return grey_silverbg color text without any style       \n
                grey_silverbg("Hello World", Style = 1 ) = it's return grey_silverbg color text with bold text          \n
                grey_silverbg("Hello World", Style = 2 ) = it's return grey_silverbg color text with light text         \n
                grey_silverbg("Hello World", Style = 3 ) = it's return grey_silverbg color text with Italicized style   \n
                grey_silverbg("Hello World", Style = 4 ) = it's return grey_silverbg color text with UnderLine          \n
                grey_silverbg("Hello World", Style = 5 ) = it's return Blinking grey_silverbg color text                \n
        """
        return Colors.back_ground_color(text, style, 192, 192, 192)
                


def greybg( text : str, style : int = default_style ) -> str :
        """
        It will return the greybg colored BackGround text.\n
        greybg() is a BackGround Function, if You add ForeGround property given text you can use grey .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                greybg("Hello World", Style = 0 ) = it's return greybg color text without any style       \n
                greybg("Hello World", Style = 1 ) = it's return greybg color text with bold text          \n
                greybg("Hello World", Style = 2 ) = it's return greybg color text with light text         \n
                greybg("Hello World", Style = 3 ) = it's return greybg color text with Italicized style   \n
                greybg("Hello World", Style = 4 ) = it's return greybg color text with UnderLine          \n
                greybg("Hello World", Style = 5 ) = it's return Blinking greybg color text                \n
        """
        return Colors.back_ground_color(text, style, 190, 190, 190)
                


def lightgraybg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightgraybg colored BackGround text.\n
        lightgraybg() is a BackGround Function, if You add ForeGround property given text you can use LightGray .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightgraybg("Hello World", Style = 0 ) = it's return lightgraybg color text without any style       \n
                lightgraybg("Hello World", Style = 1 ) = it's return lightgraybg color text with bold text          \n
                lightgraybg("Hello World", Style = 2 ) = it's return lightgraybg color text with light text         \n
                lightgraybg("Hello World", Style = 3 ) = it's return lightgraybg color text with Italicized style   \n
                lightgraybg("Hello World", Style = 4 ) = it's return lightgraybg color text with UnderLine          \n
                lightgraybg("Hello World", Style = 5 ) = it's return Blinking lightgraybg color text                \n
        """
        return Colors.back_ground_color(text, style, 211, 211, 211)
                


def lightslategreybg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightslategreybg colored BackGround text.\n
        lightslategreybg() is a BackGround Function, if You add ForeGround property given text you can use LightSlateGrey .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightslategreybg("Hello World", Style = 0 ) = it's return lightslategreybg color text without any style       \n
                lightslategreybg("Hello World", Style = 1 ) = it's return lightslategreybg color text with bold text          \n
                lightslategreybg("Hello World", Style = 2 ) = it's return lightslategreybg color text with light text         \n
                lightslategreybg("Hello World", Style = 3 ) = it's return lightslategreybg color text with Italicized style   \n
                lightslategreybg("Hello World", Style = 4 ) = it's return lightslategreybg color text with UnderLine          \n
                lightslategreybg("Hello World", Style = 5 ) = it's return Blinking lightslategreybg color text                \n
        """
        return Colors.back_ground_color(text, style, 119, 136, 153)
                


def slategraybg( text : str, style : int = default_style ) -> str :
        """
        It will return the slategraybg colored BackGround text.\n
        slategraybg() is a BackGround Function, if You add ForeGround property given text you can use SlateGray .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slategraybg("Hello World", Style = 0 ) = it's return slategraybg color text without any style       \n
                slategraybg("Hello World", Style = 1 ) = it's return slategraybg color text with bold text          \n
                slategraybg("Hello World", Style = 2 ) = it's return slategraybg color text with light text         \n
                slategraybg("Hello World", Style = 3 ) = it's return slategraybg color text with Italicized style   \n
                slategraybg("Hello World", Style = 4 ) = it's return slategraybg color text with UnderLine          \n
                slategraybg("Hello World", Style = 5 ) = it's return Blinking slategraybg color text                \n
        """
        return Colors.back_ground_color(text, style, 112, 128, 144)
                


def slategray1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the slategray1bg colored BackGround text.\n
        slategray1bg() is a BackGround Function, if You add ForeGround property given text you can use SlateGray1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slategray1bg("Hello World", Style = 0 ) = it's return slategray1bg color text without any style       \n
                slategray1bg("Hello World", Style = 1 ) = it's return slategray1bg color text with bold text          \n
                slategray1bg("Hello World", Style = 2 ) = it's return slategray1bg color text with light text         \n
                slategray1bg("Hello World", Style = 3 ) = it's return slategray1bg color text with Italicized style   \n
                slategray1bg("Hello World", Style = 4 ) = it's return slategray1bg color text with UnderLine          \n
                slategray1bg("Hello World", Style = 5 ) = it's return Blinking slategray1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 198, 226, 255)
                


def slategray2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the slategray2bg colored BackGround text.\n
        slategray2bg() is a BackGround Function, if You add ForeGround property given text you can use SlateGray2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slategray2bg("Hello World", Style = 0 ) = it's return slategray2bg color text without any style       \n
                slategray2bg("Hello World", Style = 1 ) = it's return slategray2bg color text with bold text          \n
                slategray2bg("Hello World", Style = 2 ) = it's return slategray2bg color text with light text         \n
                slategray2bg("Hello World", Style = 3 ) = it's return slategray2bg color text with Italicized style   \n
                slategray2bg("Hello World", Style = 4 ) = it's return slategray2bg color text with UnderLine          \n
                slategray2bg("Hello World", Style = 5 ) = it's return Blinking slategray2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 185, 211, 238)
                


def slategray3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the slategray3bg colored BackGround text.\n
        slategray3bg() is a BackGround Function, if You add ForeGround property given text you can use SlateGray3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slategray3bg("Hello World", Style = 0 ) = it's return slategray3bg color text without any style       \n
                slategray3bg("Hello World", Style = 1 ) = it's return slategray3bg color text with bold text          \n
                slategray3bg("Hello World", Style = 2 ) = it's return slategray3bg color text with light text         \n
                slategray3bg("Hello World", Style = 3 ) = it's return slategray3bg color text with Italicized style   \n
                slategray3bg("Hello World", Style = 4 ) = it's return slategray3bg color text with UnderLine          \n
                slategray3bg("Hello World", Style = 5 ) = it's return Blinking slategray3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 159, 182, 205)
                


def slategray4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the slategray4bg colored BackGround text.\n
        slategray4bg() is a BackGround Function, if You add ForeGround property given text you can use SlateGray4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slategray4bg("Hello World", Style = 0 ) = it's return slategray4bg color text without any style       \n
                slategray4bg("Hello World", Style = 1 ) = it's return slategray4bg color text with bold text          \n
                slategray4bg("Hello World", Style = 2 ) = it's return slategray4bg color text with light text         \n
                slategray4bg("Hello World", Style = 3 ) = it's return slategray4bg color text with Italicized style   \n
                slategray4bg("Hello World", Style = 4 ) = it's return slategray4bg color text with UnderLine          \n
                slategray4bg("Hello World", Style = 5 ) = it's return Blinking slategray4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 108, 123, 139)
                


def blackbg( text : str, style : int = default_style ) -> str :
        """
        It will return the blackbg colored BackGround text.\n
        blackbg() is a BackGround Function, if You add ForeGround property given text you can use black .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                blackbg("Hello World", Style = 0 ) = it's return blackbg color text without any style       \n
                blackbg("Hello World", Style = 1 ) = it's return blackbg color text with bold text          \n
                blackbg("Hello World", Style = 2 ) = it's return blackbg color text with light text         \n
                blackbg("Hello World", Style = 3 ) = it's return blackbg color text with Italicized style   \n
                blackbg("Hello World", Style = 4 ) = it's return blackbg color text with UnderLine          \n
                blackbg("Hello World", Style = 5 ) = it's return Blinking blackbg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 0)
                


def grey0bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey0bg colored BackGround text.\n
        grey0bg() is a BackGround Function, if You add ForeGround property given text you can use grey0 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey0bg("Hello World", Style = 0 ) = it's return grey0bg color text without any style       \n
                grey0bg("Hello World", Style = 1 ) = it's return grey0bg color text with bold text          \n
                grey0bg("Hello World", Style = 2 ) = it's return grey0bg color text with light text         \n
                grey0bg("Hello World", Style = 3 ) = it's return grey0bg color text with Italicized style   \n
                grey0bg("Hello World", Style = 4 ) = it's return grey0bg color text with UnderLine          \n
                grey0bg("Hello World", Style = 5 ) = it's return Blinking grey0bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 0)
                


def grey1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey1bg colored BackGround text.\n
        grey1bg() is a BackGround Function, if You add ForeGround property given text you can use grey1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey1bg("Hello World", Style = 0 ) = it's return grey1bg color text without any style       \n
                grey1bg("Hello World", Style = 1 ) = it's return grey1bg color text with bold text          \n
                grey1bg("Hello World", Style = 2 ) = it's return grey1bg color text with light text         \n
                grey1bg("Hello World", Style = 3 ) = it's return grey1bg color text with Italicized style   \n
                grey1bg("Hello World", Style = 4 ) = it's return grey1bg color text with UnderLine          \n
                grey1bg("Hello World", Style = 5 ) = it's return Blinking grey1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 3, 3, 3)
                


def grey2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey2bg colored BackGround text.\n
        grey2bg() is a BackGround Function, if You add ForeGround property given text you can use grey2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey2bg("Hello World", Style = 0 ) = it's return grey2bg color text without any style       \n
                grey2bg("Hello World", Style = 1 ) = it's return grey2bg color text with bold text          \n
                grey2bg("Hello World", Style = 2 ) = it's return grey2bg color text with light text         \n
                grey2bg("Hello World", Style = 3 ) = it's return grey2bg color text with Italicized style   \n
                grey2bg("Hello World", Style = 4 ) = it's return grey2bg color text with UnderLine          \n
                grey2bg("Hello World", Style = 5 ) = it's return Blinking grey2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 5, 5, 5)
                


def grey3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey3bg colored BackGround text.\n
        grey3bg() is a BackGround Function, if You add ForeGround property given text you can use grey3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey3bg("Hello World", Style = 0 ) = it's return grey3bg color text without any style       \n
                grey3bg("Hello World", Style = 1 ) = it's return grey3bg color text with bold text          \n
                grey3bg("Hello World", Style = 2 ) = it's return grey3bg color text with light text         \n
                grey3bg("Hello World", Style = 3 ) = it's return grey3bg color text with Italicized style   \n
                grey3bg("Hello World", Style = 4 ) = it's return grey3bg color text with UnderLine          \n
                grey3bg("Hello World", Style = 5 ) = it's return Blinking grey3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 8, 8, 8)
                


def grey4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey4bg colored BackGround text.\n
        grey4bg() is a BackGround Function, if You add ForeGround property given text you can use grey4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey4bg("Hello World", Style = 0 ) = it's return grey4bg color text without any style       \n
                grey4bg("Hello World", Style = 1 ) = it's return grey4bg color text with bold text          \n
                grey4bg("Hello World", Style = 2 ) = it's return grey4bg color text with light text         \n
                grey4bg("Hello World", Style = 3 ) = it's return grey4bg color text with Italicized style   \n
                grey4bg("Hello World", Style = 4 ) = it's return grey4bg color text with UnderLine          \n
                grey4bg("Hello World", Style = 5 ) = it's return Blinking grey4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 10, 10, 10)
                


def grey5bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey5bg colored BackGround text.\n
        grey5bg() is a BackGround Function, if You add ForeGround property given text you can use grey5 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey5bg("Hello World", Style = 0 ) = it's return grey5bg color text without any style       \n
                grey5bg("Hello World", Style = 1 ) = it's return grey5bg color text with bold text          \n
                grey5bg("Hello World", Style = 2 ) = it's return grey5bg color text with light text         \n
                grey5bg("Hello World", Style = 3 ) = it's return grey5bg color text with Italicized style   \n
                grey5bg("Hello World", Style = 4 ) = it's return grey5bg color text with UnderLine          \n
                grey5bg("Hello World", Style = 5 ) = it's return Blinking grey5bg color text                \n
        """
        return Colors.back_ground_color(text, style, 13, 13, 13)
                


def grey6bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey6bg colored BackGround text.\n
        grey6bg() is a BackGround Function, if You add ForeGround property given text you can use grey6 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey6bg("Hello World", Style = 0 ) = it's return grey6bg color text without any style       \n
                grey6bg("Hello World", Style = 1 ) = it's return grey6bg color text with bold text          \n
                grey6bg("Hello World", Style = 2 ) = it's return grey6bg color text with light text         \n
                grey6bg("Hello World", Style = 3 ) = it's return grey6bg color text with Italicized style   \n
                grey6bg("Hello World", Style = 4 ) = it's return grey6bg color text with UnderLine          \n
                grey6bg("Hello World", Style = 5 ) = it's return Blinking grey6bg color text                \n
        """
        return Colors.back_ground_color(text, style, 15, 15, 15)
                


def grey7bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey7bg colored BackGround text.\n
        grey7bg() is a BackGround Function, if You add ForeGround property given text you can use grey7 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey7bg("Hello World", Style = 0 ) = it's return grey7bg color text without any style       \n
                grey7bg("Hello World", Style = 1 ) = it's return grey7bg color text with bold text          \n
                grey7bg("Hello World", Style = 2 ) = it's return grey7bg color text with light text         \n
                grey7bg("Hello World", Style = 3 ) = it's return grey7bg color text with Italicized style   \n
                grey7bg("Hello World", Style = 4 ) = it's return grey7bg color text with UnderLine          \n
                grey7bg("Hello World", Style = 5 ) = it's return Blinking grey7bg color text                \n
        """
        return Colors.back_ground_color(text, style, 18, 18, 18)
                


def grey8bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey8bg colored BackGround text.\n
        grey8bg() is a BackGround Function, if You add ForeGround property given text you can use grey8 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey8bg("Hello World", Style = 0 ) = it's return grey8bg color text without any style       \n
                grey8bg("Hello World", Style = 1 ) = it's return grey8bg color text with bold text          \n
                grey8bg("Hello World", Style = 2 ) = it's return grey8bg color text with light text         \n
                grey8bg("Hello World", Style = 3 ) = it's return grey8bg color text with Italicized style   \n
                grey8bg("Hello World", Style = 4 ) = it's return grey8bg color text with UnderLine          \n
                grey8bg("Hello World", Style = 5 ) = it's return Blinking grey8bg color text                \n
        """
        return Colors.back_ground_color(text, style, 20, 20, 20)
                


def grey9bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey9bg colored BackGround text.\n
        grey9bg() is a BackGround Function, if You add ForeGround property given text you can use grey9 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey9bg("Hello World", Style = 0 ) = it's return grey9bg color text without any style       \n
                grey9bg("Hello World", Style = 1 ) = it's return grey9bg color text with bold text          \n
                grey9bg("Hello World", Style = 2 ) = it's return grey9bg color text with light text         \n
                grey9bg("Hello World", Style = 3 ) = it's return grey9bg color text with Italicized style   \n
                grey9bg("Hello World", Style = 4 ) = it's return grey9bg color text with UnderLine          \n
                grey9bg("Hello World", Style = 5 ) = it's return Blinking grey9bg color text                \n
        """
        return Colors.back_ground_color(text, style, 23, 23, 23)
                


def grey10bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey10bg colored BackGround text.\n
        grey10bg() is a BackGround Function, if You add ForeGround property given text you can use grey10 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey10bg("Hello World", Style = 0 ) = it's return grey10bg color text without any style       \n
                grey10bg("Hello World", Style = 1 ) = it's return grey10bg color text with bold text          \n
                grey10bg("Hello World", Style = 2 ) = it's return grey10bg color text with light text         \n
                grey10bg("Hello World", Style = 3 ) = it's return grey10bg color text with Italicized style   \n
                grey10bg("Hello World", Style = 4 ) = it's return grey10bg color text with UnderLine          \n
                grey10bg("Hello World", Style = 5 ) = it's return Blinking grey10bg color text                \n
        """
        return Colors.back_ground_color(text, style, 26, 26, 26)
                


def grey11bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey11bg colored BackGround text.\n
        grey11bg() is a BackGround Function, if You add ForeGround property given text you can use grey11 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey11bg("Hello World", Style = 0 ) = it's return grey11bg color text without any style       \n
                grey11bg("Hello World", Style = 1 ) = it's return grey11bg color text with bold text          \n
                grey11bg("Hello World", Style = 2 ) = it's return grey11bg color text with light text         \n
                grey11bg("Hello World", Style = 3 ) = it's return grey11bg color text with Italicized style   \n
                grey11bg("Hello World", Style = 4 ) = it's return grey11bg color text with UnderLine          \n
                grey11bg("Hello World", Style = 5 ) = it's return Blinking grey11bg color text                \n
        """
        return Colors.back_ground_color(text, style, 28, 28, 28)
                


def grey12bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey12bg colored BackGround text.\n
        grey12bg() is a BackGround Function, if You add ForeGround property given text you can use grey12 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey12bg("Hello World", Style = 0 ) = it's return grey12bg color text without any style       \n
                grey12bg("Hello World", Style = 1 ) = it's return grey12bg color text with bold text          \n
                grey12bg("Hello World", Style = 2 ) = it's return grey12bg color text with light text         \n
                grey12bg("Hello World", Style = 3 ) = it's return grey12bg color text with Italicized style   \n
                grey12bg("Hello World", Style = 4 ) = it's return grey12bg color text with UnderLine          \n
                grey12bg("Hello World", Style = 5 ) = it's return Blinking grey12bg color text                \n
        """
        return Colors.back_ground_color(text, style, 31, 31, 31)
                


def grey13bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey13bg colored BackGround text.\n
        grey13bg() is a BackGround Function, if You add ForeGround property given text you can use grey13 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey13bg("Hello World", Style = 0 ) = it's return grey13bg color text without any style       \n
                grey13bg("Hello World", Style = 1 ) = it's return grey13bg color text with bold text          \n
                grey13bg("Hello World", Style = 2 ) = it's return grey13bg color text with light text         \n
                grey13bg("Hello World", Style = 3 ) = it's return grey13bg color text with Italicized style   \n
                grey13bg("Hello World", Style = 4 ) = it's return grey13bg color text with UnderLine          \n
                grey13bg("Hello World", Style = 5 ) = it's return Blinking grey13bg color text                \n
        """
        return Colors.back_ground_color(text, style, 33, 33, 33)
                


def light_blackbg( text : str, style : int = default_style ) -> str :
        """
        It will return the light_blackbg colored BackGround text.\n
        light_blackbg() is a BackGround Function, if You add ForeGround property given text you can use light_black .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                light_blackbg("Hello World", Style = 0 ) = it's return light_blackbg color text without any style       \n
                light_blackbg("Hello World", Style = 1 ) = it's return light_blackbg color text with bold text          \n
                light_blackbg("Hello World", Style = 2 ) = it's return light_blackbg color text with light text         \n
                light_blackbg("Hello World", Style = 3 ) = it's return light_blackbg color text with Italicized style   \n
                light_blackbg("Hello World", Style = 4 ) = it's return light_blackbg color text with UnderLine          \n
                light_blackbg("Hello World", Style = 5 ) = it's return Blinking light_blackbg color text                \n
        """
        return Colors.back_ground_color(text, style, 34, 34, 34)
                


def grey14bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey14bg colored BackGround text.\n
        grey14bg() is a BackGround Function, if You add ForeGround property given text you can use grey14 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey14bg("Hello World", Style = 0 ) = it's return grey14bg color text without any style       \n
                grey14bg("Hello World", Style = 1 ) = it's return grey14bg color text with bold text          \n
                grey14bg("Hello World", Style = 2 ) = it's return grey14bg color text with light text         \n
                grey14bg("Hello World", Style = 3 ) = it's return grey14bg color text with Italicized style   \n
                grey14bg("Hello World", Style = 4 ) = it's return grey14bg color text with UnderLine          \n
                grey14bg("Hello World", Style = 5 ) = it's return Blinking grey14bg color text                \n
        """
        return Colors.back_ground_color(text, style, 36, 36, 36)
                


def grey15bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey15bg colored BackGround text.\n
        grey15bg() is a BackGround Function, if You add ForeGround property given text you can use grey15 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey15bg("Hello World", Style = 0 ) = it's return grey15bg color text without any style       \n
                grey15bg("Hello World", Style = 1 ) = it's return grey15bg color text with bold text          \n
                grey15bg("Hello World", Style = 2 ) = it's return grey15bg color text with light text         \n
                grey15bg("Hello World", Style = 3 ) = it's return grey15bg color text with Italicized style   \n
                grey15bg("Hello World", Style = 4 ) = it's return grey15bg color text with UnderLine          \n
                grey15bg("Hello World", Style = 5 ) = it's return Blinking grey15bg color text                \n
        """
        return Colors.back_ground_color(text, style, 38, 38, 38)
                


def grey16bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey16bg colored BackGround text.\n
        grey16bg() is a BackGround Function, if You add ForeGround property given text you can use grey16 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey16bg("Hello World", Style = 0 ) = it's return grey16bg color text without any style       \n
                grey16bg("Hello World", Style = 1 ) = it's return grey16bg color text with bold text          \n
                grey16bg("Hello World", Style = 2 ) = it's return grey16bg color text with light text         \n
                grey16bg("Hello World", Style = 3 ) = it's return grey16bg color text with Italicized style   \n
                grey16bg("Hello World", Style = 4 ) = it's return grey16bg color text with UnderLine          \n
                grey16bg("Hello World", Style = 5 ) = it's return Blinking grey16bg color text                \n
        """
        return Colors.back_ground_color(text, style, 41, 41, 41)
                


def grey17bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey17bg colored BackGround text.\n
        grey17bg() is a BackGround Function, if You add ForeGround property given text you can use grey17 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey17bg("Hello World", Style = 0 ) = it's return grey17bg color text without any style       \n
                grey17bg("Hello World", Style = 1 ) = it's return grey17bg color text with bold text          \n
                grey17bg("Hello World", Style = 2 ) = it's return grey17bg color text with light text         \n
                grey17bg("Hello World", Style = 3 ) = it's return grey17bg color text with Italicized style   \n
                grey17bg("Hello World", Style = 4 ) = it's return grey17bg color text with UnderLine          \n
                grey17bg("Hello World", Style = 5 ) = it's return Blinking grey17bg color text                \n
        """
        return Colors.back_ground_color(text, style, 43, 43, 43)
                


def grey18bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey18bg colored BackGround text.\n
        grey18bg() is a BackGround Function, if You add ForeGround property given text you can use grey18 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey18bg("Hello World", Style = 0 ) = it's return grey18bg color text without any style       \n
                grey18bg("Hello World", Style = 1 ) = it's return grey18bg color text with bold text          \n
                grey18bg("Hello World", Style = 2 ) = it's return grey18bg color text with light text         \n
                grey18bg("Hello World", Style = 3 ) = it's return grey18bg color text with Italicized style   \n
                grey18bg("Hello World", Style = 4 ) = it's return grey18bg color text with UnderLine          \n
                grey18bg("Hello World", Style = 5 ) = it's return Blinking grey18bg color text                \n
        """
        return Colors.back_ground_color(text, style, 46, 46, 46)
                


def grey19bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey19bg colored BackGround text.\n
        grey19bg() is a BackGround Function, if You add ForeGround property given text you can use grey19 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey19bg("Hello World", Style = 0 ) = it's return grey19bg color text without any style       \n
                grey19bg("Hello World", Style = 1 ) = it's return grey19bg color text with bold text          \n
                grey19bg("Hello World", Style = 2 ) = it's return grey19bg color text with light text         \n
                grey19bg("Hello World", Style = 3 ) = it's return grey19bg color text with Italicized style   \n
                grey19bg("Hello World", Style = 4 ) = it's return grey19bg color text with UnderLine          \n
                grey19bg("Hello World", Style = 5 ) = it's return Blinking grey19bg color text                \n
        """
        return Colors.back_ground_color(text, style, 48, 48, 48)
                


def grey20bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey20bg colored BackGround text.\n
        grey20bg() is a BackGround Function, if You add ForeGround property given text you can use grey20 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey20bg("Hello World", Style = 0 ) = it's return grey20bg color text without any style       \n
                grey20bg("Hello World", Style = 1 ) = it's return grey20bg color text with bold text          \n
                grey20bg("Hello World", Style = 2 ) = it's return grey20bg color text with light text         \n
                grey20bg("Hello World", Style = 3 ) = it's return grey20bg color text with Italicized style   \n
                grey20bg("Hello World", Style = 4 ) = it's return grey20bg color text with UnderLine          \n
                grey20bg("Hello World", Style = 5 ) = it's return Blinking grey20bg color text                \n
        """
        return Colors.back_ground_color(text, style, 51, 51, 51)
                


def grey21bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey21bg colored BackGround text.\n
        grey21bg() is a BackGround Function, if You add ForeGround property given text you can use grey21 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey21bg("Hello World", Style = 0 ) = it's return grey21bg color text without any style       \n
                grey21bg("Hello World", Style = 1 ) = it's return grey21bg color text with bold text          \n
                grey21bg("Hello World", Style = 2 ) = it's return grey21bg color text with light text         \n
                grey21bg("Hello World", Style = 3 ) = it's return grey21bg color text with Italicized style   \n
                grey21bg("Hello World", Style = 4 ) = it's return grey21bg color text with UnderLine          \n
                grey21bg("Hello World", Style = 5 ) = it's return Blinking grey21bg color text                \n
        """
        return Colors.back_ground_color(text, style, 54, 54, 54)
                


def grey22bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey22bg colored BackGround text.\n
        grey22bg() is a BackGround Function, if You add ForeGround property given text you can use grey22 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey22bg("Hello World", Style = 0 ) = it's return grey22bg color text without any style       \n
                grey22bg("Hello World", Style = 1 ) = it's return grey22bg color text with bold text          \n
                grey22bg("Hello World", Style = 2 ) = it's return grey22bg color text with light text         \n
                grey22bg("Hello World", Style = 3 ) = it's return grey22bg color text with Italicized style   \n
                grey22bg("Hello World", Style = 4 ) = it's return grey22bg color text with UnderLine          \n
                grey22bg("Hello World", Style = 5 ) = it's return Blinking grey22bg color text                \n
        """
        return Colors.back_ground_color(text, style, 56, 56, 56)
                


def grey23bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey23bg colored BackGround text.\n
        grey23bg() is a BackGround Function, if You add ForeGround property given text you can use grey23 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey23bg("Hello World", Style = 0 ) = it's return grey23bg color text without any style       \n
                grey23bg("Hello World", Style = 1 ) = it's return grey23bg color text with bold text          \n
                grey23bg("Hello World", Style = 2 ) = it's return grey23bg color text with light text         \n
                grey23bg("Hello World", Style = 3 ) = it's return grey23bg color text with Italicized style   \n
                grey23bg("Hello World", Style = 4 ) = it's return grey23bg color text with UnderLine          \n
                grey23bg("Hello World", Style = 5 ) = it's return Blinking grey23bg color text                \n
        """
        return Colors.back_ground_color(text, style, 59, 59, 59)
                


def grey24bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey24bg colored BackGround text.\n
        grey24bg() is a BackGround Function, if You add ForeGround property given text you can use grey24 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey24bg("Hello World", Style = 0 ) = it's return grey24bg color text without any style       \n
                grey24bg("Hello World", Style = 1 ) = it's return grey24bg color text with bold text          \n
                grey24bg("Hello World", Style = 2 ) = it's return grey24bg color text with light text         \n
                grey24bg("Hello World", Style = 3 ) = it's return grey24bg color text with Italicized style   \n
                grey24bg("Hello World", Style = 4 ) = it's return grey24bg color text with UnderLine          \n
                grey24bg("Hello World", Style = 5 ) = it's return Blinking grey24bg color text                \n
        """
        return Colors.back_ground_color(text, style, 61, 61, 61)
                


def grey25bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey25bg colored BackGround text.\n
        grey25bg() is a BackGround Function, if You add ForeGround property given text you can use grey25 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey25bg("Hello World", Style = 0 ) = it's return grey25bg color text without any style       \n
                grey25bg("Hello World", Style = 1 ) = it's return grey25bg color text with bold text          \n
                grey25bg("Hello World", Style = 2 ) = it's return grey25bg color text with light text         \n
                grey25bg("Hello World", Style = 3 ) = it's return grey25bg color text with Italicized style   \n
                grey25bg("Hello World", Style = 4 ) = it's return grey25bg color text with UnderLine          \n
                grey25bg("Hello World", Style = 5 ) = it's return Blinking grey25bg color text                \n
        """
        return Colors.back_ground_color(text, style, 64, 64, 64)
                


def grey26bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey26bg colored BackGround text.\n
        grey26bg() is a BackGround Function, if You add ForeGround property given text you can use grey26 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey26bg("Hello World", Style = 0 ) = it's return grey26bg color text without any style       \n
                grey26bg("Hello World", Style = 1 ) = it's return grey26bg color text with bold text          \n
                grey26bg("Hello World", Style = 2 ) = it's return grey26bg color text with light text         \n
                grey26bg("Hello World", Style = 3 ) = it's return grey26bg color text with Italicized style   \n
                grey26bg("Hello World", Style = 4 ) = it's return grey26bg color text with UnderLine          \n
                grey26bg("Hello World", Style = 5 ) = it's return Blinking grey26bg color text                \n
        """
        return Colors.back_ground_color(text, style, 66, 66, 66)
                


def grey27bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey27bg colored BackGround text.\n
        grey27bg() is a BackGround Function, if You add ForeGround property given text you can use grey27 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey27bg("Hello World", Style = 0 ) = it's return grey27bg color text without any style       \n
                grey27bg("Hello World", Style = 1 ) = it's return grey27bg color text with bold text          \n
                grey27bg("Hello World", Style = 2 ) = it's return grey27bg color text with light text         \n
                grey27bg("Hello World", Style = 3 ) = it's return grey27bg color text with Italicized style   \n
                grey27bg("Hello World", Style = 4 ) = it's return grey27bg color text with UnderLine          \n
                grey27bg("Hello World", Style = 5 ) = it's return Blinking grey27bg color text                \n
        """
        return Colors.back_ground_color(text, style, 69, 69, 69)
                


def grey28bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey28bg colored BackGround text.\n
        grey28bg() is a BackGround Function, if You add ForeGround property given text you can use grey28 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey28bg("Hello World", Style = 0 ) = it's return grey28bg color text without any style       \n
                grey28bg("Hello World", Style = 1 ) = it's return grey28bg color text with bold text          \n
                grey28bg("Hello World", Style = 2 ) = it's return grey28bg color text with light text         \n
                grey28bg("Hello World", Style = 3 ) = it's return grey28bg color text with Italicized style   \n
                grey28bg("Hello World", Style = 4 ) = it's return grey28bg color text with UnderLine          \n
                grey28bg("Hello World", Style = 5 ) = it's return Blinking grey28bg color text                \n
        """
        return Colors.back_ground_color(text, style, 71, 71, 71)
                


def grey29bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey29bg colored BackGround text.\n
        grey29bg() is a BackGround Function, if You add ForeGround property given text you can use grey29 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey29bg("Hello World", Style = 0 ) = it's return grey29bg color text without any style       \n
                grey29bg("Hello World", Style = 1 ) = it's return grey29bg color text with bold text          \n
                grey29bg("Hello World", Style = 2 ) = it's return grey29bg color text with light text         \n
                grey29bg("Hello World", Style = 3 ) = it's return grey29bg color text with Italicized style   \n
                grey29bg("Hello World", Style = 4 ) = it's return grey29bg color text with UnderLine          \n
                grey29bg("Hello World", Style = 5 ) = it's return Blinking grey29bg color text                \n
        """
        return Colors.back_ground_color(text, style, 74, 74, 74)
                


def grey30bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey30bg colored BackGround text.\n
        grey30bg() is a BackGround Function, if You add ForeGround property given text you can use grey30 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey30bg("Hello World", Style = 0 ) = it's return grey30bg color text without any style       \n
                grey30bg("Hello World", Style = 1 ) = it's return grey30bg color text with bold text          \n
                grey30bg("Hello World", Style = 2 ) = it's return grey30bg color text with light text         \n
                grey30bg("Hello World", Style = 3 ) = it's return grey30bg color text with Italicized style   \n
                grey30bg("Hello World", Style = 4 ) = it's return grey30bg color text with UnderLine          \n
                grey30bg("Hello World", Style = 5 ) = it's return Blinking grey30bg color text                \n
        """
        return Colors.back_ground_color(text, style, 77, 77, 77)
                


def grey31bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey31bg colored BackGround text.\n
        grey31bg() is a BackGround Function, if You add ForeGround property given text you can use grey31 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey31bg("Hello World", Style = 0 ) = it's return grey31bg color text without any style       \n
                grey31bg("Hello World", Style = 1 ) = it's return grey31bg color text with bold text          \n
                grey31bg("Hello World", Style = 2 ) = it's return grey31bg color text with light text         \n
                grey31bg("Hello World", Style = 3 ) = it's return grey31bg color text with Italicized style   \n
                grey31bg("Hello World", Style = 4 ) = it's return grey31bg color text with UnderLine          \n
                grey31bg("Hello World", Style = 5 ) = it's return Blinking grey31bg color text                \n
        """
        return Colors.back_ground_color(text, style, 79, 79, 79)
                


def grey32bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey32bg colored BackGround text.\n
        grey32bg() is a BackGround Function, if You add ForeGround property given text you can use grey32 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey32bg("Hello World", Style = 0 ) = it's return grey32bg color text without any style       \n
                grey32bg("Hello World", Style = 1 ) = it's return grey32bg color text with bold text          \n
                grey32bg("Hello World", Style = 2 ) = it's return grey32bg color text with light text         \n
                grey32bg("Hello World", Style = 3 ) = it's return grey32bg color text with Italicized style   \n
                grey32bg("Hello World", Style = 4 ) = it's return grey32bg color text with UnderLine          \n
                grey32bg("Hello World", Style = 5 ) = it's return Blinking grey32bg color text                \n
        """
        return Colors.back_ground_color(text, style, 82, 82, 82)
                


def grey33bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey33bg colored BackGround text.\n
        grey33bg() is a BackGround Function, if You add ForeGround property given text you can use grey33 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey33bg("Hello World", Style = 0 ) = it's return grey33bg color text without any style       \n
                grey33bg("Hello World", Style = 1 ) = it's return grey33bg color text with bold text          \n
                grey33bg("Hello World", Style = 2 ) = it's return grey33bg color text with light text         \n
                grey33bg("Hello World", Style = 3 ) = it's return grey33bg color text with Italicized style   \n
                grey33bg("Hello World", Style = 4 ) = it's return grey33bg color text with UnderLine          \n
                grey33bg("Hello World", Style = 5 ) = it's return Blinking grey33bg color text                \n
        """
        return Colors.back_ground_color(text, style, 84, 84, 84)
                


def light_graybg( text : str, style : int = default_style ) -> str :
        """
        It will return the light_graybg colored BackGround text.\n
        light_graybg() is a BackGround Function, if You add ForeGround property given text you can use light_gray .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                light_graybg("Hello World", Style = 0 ) = it's return light_graybg color text without any style       \n
                light_graybg("Hello World", Style = 1 ) = it's return light_graybg color text with bold text          \n
                light_graybg("Hello World", Style = 2 ) = it's return light_graybg color text with light text         \n
                light_graybg("Hello World", Style = 3 ) = it's return light_graybg color text with Italicized style   \n
                light_graybg("Hello World", Style = 4 ) = it's return light_graybg color text with UnderLine          \n
                light_graybg("Hello World", Style = 5 ) = it's return Blinking light_graybg color text                \n
        """
        return Colors.back_ground_color(text, style, 85, 85, 85)
                


def grey34bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey34bg colored BackGround text.\n
        grey34bg() is a BackGround Function, if You add ForeGround property given text you can use grey34 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey34bg("Hello World", Style = 0 ) = it's return grey34bg color text without any style       \n
                grey34bg("Hello World", Style = 1 ) = it's return grey34bg color text with bold text          \n
                grey34bg("Hello World", Style = 2 ) = it's return grey34bg color text with light text         \n
                grey34bg("Hello World", Style = 3 ) = it's return grey34bg color text with Italicized style   \n
                grey34bg("Hello World", Style = 4 ) = it's return grey34bg color text with UnderLine          \n
                grey34bg("Hello World", Style = 5 ) = it's return Blinking grey34bg color text                \n
        """
        return Colors.back_ground_color(text, style, 87, 87, 87)
                


def grey35bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey35bg colored BackGround text.\n
        grey35bg() is a BackGround Function, if You add ForeGround property given text you can use grey35 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey35bg("Hello World", Style = 0 ) = it's return grey35bg color text without any style       \n
                grey35bg("Hello World", Style = 1 ) = it's return grey35bg color text with bold text          \n
                grey35bg("Hello World", Style = 2 ) = it's return grey35bg color text with light text         \n
                grey35bg("Hello World", Style = 3 ) = it's return grey35bg color text with Italicized style   \n
                grey35bg("Hello World", Style = 4 ) = it's return grey35bg color text with UnderLine          \n
                grey35bg("Hello World", Style = 5 ) = it's return Blinking grey35bg color text                \n
        """
        return Colors.back_ground_color(text, style, 89, 89, 89)
                


def grey36bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey36bg colored BackGround text.\n
        grey36bg() is a BackGround Function, if You add ForeGround property given text you can use grey36 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey36bg("Hello World", Style = 0 ) = it's return grey36bg color text without any style       \n
                grey36bg("Hello World", Style = 1 ) = it's return grey36bg color text with bold text          \n
                grey36bg("Hello World", Style = 2 ) = it's return grey36bg color text with light text         \n
                grey36bg("Hello World", Style = 3 ) = it's return grey36bg color text with Italicized style   \n
                grey36bg("Hello World", Style = 4 ) = it's return grey36bg color text with UnderLine          \n
                grey36bg("Hello World", Style = 5 ) = it's return Blinking grey36bg color text                \n
        """
        return Colors.back_ground_color(text, style, 92, 92, 92)
                


def grey37bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey37bg colored BackGround text.\n
        grey37bg() is a BackGround Function, if You add ForeGround property given text you can use grey37 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey37bg("Hello World", Style = 0 ) = it's return grey37bg color text without any style       \n
                grey37bg("Hello World", Style = 1 ) = it's return grey37bg color text with bold text          \n
                grey37bg("Hello World", Style = 2 ) = it's return grey37bg color text with light text         \n
                grey37bg("Hello World", Style = 3 ) = it's return grey37bg color text with Italicized style   \n
                grey37bg("Hello World", Style = 4 ) = it's return grey37bg color text with UnderLine          \n
                grey37bg("Hello World", Style = 5 ) = it's return Blinking grey37bg color text                \n
        """
        return Colors.back_ground_color(text, style, 94, 94, 94)
                


def grey38bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey38bg colored BackGround text.\n
        grey38bg() is a BackGround Function, if You add ForeGround property given text you can use grey38 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey38bg("Hello World", Style = 0 ) = it's return grey38bg color text without any style       \n
                grey38bg("Hello World", Style = 1 ) = it's return grey38bg color text with bold text          \n
                grey38bg("Hello World", Style = 2 ) = it's return grey38bg color text with light text         \n
                grey38bg("Hello World", Style = 3 ) = it's return grey38bg color text with Italicized style   \n
                grey38bg("Hello World", Style = 4 ) = it's return grey38bg color text with UnderLine          \n
                grey38bg("Hello World", Style = 5 ) = it's return Blinking grey38bg color text                \n
        """
        return Colors.back_ground_color(text, style, 97, 97, 97)
                


def grey39bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey39bg colored BackGround text.\n
        grey39bg() is a BackGround Function, if You add ForeGround property given text you can use grey39 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey39bg("Hello World", Style = 0 ) = it's return grey39bg color text without any style       \n
                grey39bg("Hello World", Style = 1 ) = it's return grey39bg color text with bold text          \n
                grey39bg("Hello World", Style = 2 ) = it's return grey39bg color text with light text         \n
                grey39bg("Hello World", Style = 3 ) = it's return grey39bg color text with Italicized style   \n
                grey39bg("Hello World", Style = 4 ) = it's return grey39bg color text with UnderLine          \n
                grey39bg("Hello World", Style = 5 ) = it's return Blinking grey39bg color text                \n
        """
        return Colors.back_ground_color(text, style, 99, 99, 99)
                


def grey40bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey40bg colored BackGround text.\n
        grey40bg() is a BackGround Function, if You add ForeGround property given text you can use grey40 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey40bg("Hello World", Style = 0 ) = it's return grey40bg color text without any style       \n
                grey40bg("Hello World", Style = 1 ) = it's return grey40bg color text with bold text          \n
                grey40bg("Hello World", Style = 2 ) = it's return grey40bg color text with light text         \n
                grey40bg("Hello World", Style = 3 ) = it's return grey40bg color text with Italicized style   \n
                grey40bg("Hello World", Style = 4 ) = it's return grey40bg color text with UnderLine          \n
                grey40bg("Hello World", Style = 5 ) = it's return Blinking grey40bg color text                \n
        """
        return Colors.back_ground_color(text, style, 102, 102, 102)
                


def grey41_dimgreybg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey41_dimgreybg colored BackGround text.\n
        grey41_dimgreybg() is a BackGround Function, if You add ForeGround property given text you can use grey41_DimGrey .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey41_dimgreybg("Hello World", Style = 0 ) = it's return grey41_dimgreybg color text without any style       \n
                grey41_dimgreybg("Hello World", Style = 1 ) = it's return grey41_dimgreybg color text with bold text          \n
                grey41_dimgreybg("Hello World", Style = 2 ) = it's return grey41_dimgreybg color text with light text         \n
                grey41_dimgreybg("Hello World", Style = 3 ) = it's return grey41_dimgreybg color text with Italicized style   \n
                grey41_dimgreybg("Hello World", Style = 4 ) = it's return grey41_dimgreybg color text with UnderLine          \n
                grey41_dimgreybg("Hello World", Style = 5 ) = it's return Blinking grey41_dimgreybg color text                \n
        """
        return Colors.back_ground_color(text, style, 105, 105, 105)
                


def grey42bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey42bg colored BackGround text.\n
        grey42bg() is a BackGround Function, if You add ForeGround property given text you can use grey42 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey42bg("Hello World", Style = 0 ) = it's return grey42bg color text without any style       \n
                grey42bg("Hello World", Style = 1 ) = it's return grey42bg color text with bold text          \n
                grey42bg("Hello World", Style = 2 ) = it's return grey42bg color text with light text         \n
                grey42bg("Hello World", Style = 3 ) = it's return grey42bg color text with Italicized style   \n
                grey42bg("Hello World", Style = 4 ) = it's return grey42bg color text with UnderLine          \n
                grey42bg("Hello World", Style = 5 ) = it's return Blinking grey42bg color text                \n
        """
        return Colors.back_ground_color(text, style, 107, 107, 107)
                


def grey43bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey43bg colored BackGround text.\n
        grey43bg() is a BackGround Function, if You add ForeGround property given text you can use grey43 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey43bg("Hello World", Style = 0 ) = it's return grey43bg color text without any style       \n
                grey43bg("Hello World", Style = 1 ) = it's return grey43bg color text with bold text          \n
                grey43bg("Hello World", Style = 2 ) = it's return grey43bg color text with light text         \n
                grey43bg("Hello World", Style = 3 ) = it's return grey43bg color text with Italicized style   \n
                grey43bg("Hello World", Style = 4 ) = it's return grey43bg color text with UnderLine          \n
                grey43bg("Hello World", Style = 5 ) = it's return Blinking grey43bg color text                \n
        """
        return Colors.back_ground_color(text, style, 110, 110, 110)
                


def grey44bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey44bg colored BackGround text.\n
        grey44bg() is a BackGround Function, if You add ForeGround property given text you can use grey44 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey44bg("Hello World", Style = 0 ) = it's return grey44bg color text without any style       \n
                grey44bg("Hello World", Style = 1 ) = it's return grey44bg color text with bold text          \n
                grey44bg("Hello World", Style = 2 ) = it's return grey44bg color text with light text         \n
                grey44bg("Hello World", Style = 3 ) = it's return grey44bg color text with Italicized style   \n
                grey44bg("Hello World", Style = 4 ) = it's return grey44bg color text with UnderLine          \n
                grey44bg("Hello World", Style = 5 ) = it's return Blinking grey44bg color text                \n
        """
        return Colors.back_ground_color(text, style, 112, 112, 112)
                


def grey45bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey45bg colored BackGround text.\n
        grey45bg() is a BackGround Function, if You add ForeGround property given text you can use grey45 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey45bg("Hello World", Style = 0 ) = it's return grey45bg color text without any style       \n
                grey45bg("Hello World", Style = 1 ) = it's return grey45bg color text with bold text          \n
                grey45bg("Hello World", Style = 2 ) = it's return grey45bg color text with light text         \n
                grey45bg("Hello World", Style = 3 ) = it's return grey45bg color text with Italicized style   \n
                grey45bg("Hello World", Style = 4 ) = it's return grey45bg color text with UnderLine          \n
                grey45bg("Hello World", Style = 5 ) = it's return Blinking grey45bg color text                \n
        """
        return Colors.back_ground_color(text, style, 115, 115, 115)
                


def grey46bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey46bg colored BackGround text.\n
        grey46bg() is a BackGround Function, if You add ForeGround property given text you can use grey46 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey46bg("Hello World", Style = 0 ) = it's return grey46bg color text without any style       \n
                grey46bg("Hello World", Style = 1 ) = it's return grey46bg color text with bold text          \n
                grey46bg("Hello World", Style = 2 ) = it's return grey46bg color text with light text         \n
                grey46bg("Hello World", Style = 3 ) = it's return grey46bg color text with Italicized style   \n
                grey46bg("Hello World", Style = 4 ) = it's return grey46bg color text with UnderLine          \n
                grey46bg("Hello World", Style = 5 ) = it's return Blinking grey46bg color text                \n
        """
        return Colors.back_ground_color(text, style, 117, 117, 117)
                


def grey47bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey47bg colored BackGround text.\n
        grey47bg() is a BackGround Function, if You add ForeGround property given text you can use grey47 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey47bg("Hello World", Style = 0 ) = it's return grey47bg color text without any style       \n
                grey47bg("Hello World", Style = 1 ) = it's return grey47bg color text with bold text          \n
                grey47bg("Hello World", Style = 2 ) = it's return grey47bg color text with light text         \n
                grey47bg("Hello World", Style = 3 ) = it's return grey47bg color text with Italicized style   \n
                grey47bg("Hello World", Style = 4 ) = it's return grey47bg color text with UnderLine          \n
                grey47bg("Hello World", Style = 5 ) = it's return Blinking grey47bg color text                \n
        """
        return Colors.back_ground_color(text, style, 120, 120, 120)
                


def grey48bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey48bg colored BackGround text.\n
        grey48bg() is a BackGround Function, if You add ForeGround property given text you can use grey48 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey48bg("Hello World", Style = 0 ) = it's return grey48bg color text without any style       \n
                grey48bg("Hello World", Style = 1 ) = it's return grey48bg color text with bold text          \n
                grey48bg("Hello World", Style = 2 ) = it's return grey48bg color text with light text         \n
                grey48bg("Hello World", Style = 3 ) = it's return grey48bg color text with Italicized style   \n
                grey48bg("Hello World", Style = 4 ) = it's return grey48bg color text with UnderLine          \n
                grey48bg("Hello World", Style = 5 ) = it's return Blinking grey48bg color text                \n
        """
        return Colors.back_ground_color(text, style, 122, 122, 122)
                


def grey49bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey49bg colored BackGround text.\n
        grey49bg() is a BackGround Function, if You add ForeGround property given text you can use grey49 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey49bg("Hello World", Style = 0 ) = it's return grey49bg color text without any style       \n
                grey49bg("Hello World", Style = 1 ) = it's return grey49bg color text with bold text          \n
                grey49bg("Hello World", Style = 2 ) = it's return grey49bg color text with light text         \n
                grey49bg("Hello World", Style = 3 ) = it's return grey49bg color text with Italicized style   \n
                grey49bg("Hello World", Style = 4 ) = it's return grey49bg color text with UnderLine          \n
                grey49bg("Hello World", Style = 5 ) = it's return Blinking grey49bg color text                \n
        """
        return Colors.back_ground_color(text, style, 125, 125, 125)
                


def grey50bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey50bg colored BackGround text.\n
        grey50bg() is a BackGround Function, if You add ForeGround property given text you can use grey50 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey50bg("Hello World", Style = 0 ) = it's return grey50bg color text without any style       \n
                grey50bg("Hello World", Style = 1 ) = it's return grey50bg color text with bold text          \n
                grey50bg("Hello World", Style = 2 ) = it's return grey50bg color text with light text         \n
                grey50bg("Hello World", Style = 3 ) = it's return grey50bg color text with Italicized style   \n
                grey50bg("Hello World", Style = 4 ) = it's return grey50bg color text with UnderLine          \n
                grey50bg("Hello World", Style = 5 ) = it's return Blinking grey50bg color text                \n
        """
        return Colors.back_ground_color(text, style, 127, 127, 127)
                


def grey51bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey51bg colored BackGround text.\n
        grey51bg() is a BackGround Function, if You add ForeGround property given text you can use grey51 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey51bg("Hello World", Style = 0 ) = it's return grey51bg color text without any style       \n
                grey51bg("Hello World", Style = 1 ) = it's return grey51bg color text with bold text          \n
                grey51bg("Hello World", Style = 2 ) = it's return grey51bg color text with light text         \n
                grey51bg("Hello World", Style = 3 ) = it's return grey51bg color text with Italicized style   \n
                grey51bg("Hello World", Style = 4 ) = it's return grey51bg color text with UnderLine          \n
                grey51bg("Hello World", Style = 5 ) = it's return Blinking grey51bg color text                \n
        """
        return Colors.back_ground_color(text, style, 130, 130, 130)
                


def grey52bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey52bg colored BackGround text.\n
        grey52bg() is a BackGround Function, if You add ForeGround property given text you can use grey52 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey52bg("Hello World", Style = 0 ) = it's return grey52bg color text without any style       \n
                grey52bg("Hello World", Style = 1 ) = it's return grey52bg color text with bold text          \n
                grey52bg("Hello World", Style = 2 ) = it's return grey52bg color text with light text         \n
                grey52bg("Hello World", Style = 3 ) = it's return grey52bg color text with Italicized style   \n
                grey52bg("Hello World", Style = 4 ) = it's return grey52bg color text with UnderLine          \n
                grey52bg("Hello World", Style = 5 ) = it's return Blinking grey52bg color text                \n
        """
        return Colors.back_ground_color(text, style, 133, 133, 133)
                


def grey53bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey53bg colored BackGround text.\n
        grey53bg() is a BackGround Function, if You add ForeGround property given text you can use grey53 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey53bg("Hello World", Style = 0 ) = it's return grey53bg color text without any style       \n
                grey53bg("Hello World", Style = 1 ) = it's return grey53bg color text with bold text          \n
                grey53bg("Hello World", Style = 2 ) = it's return grey53bg color text with light text         \n
                grey53bg("Hello World", Style = 3 ) = it's return grey53bg color text with Italicized style   \n
                grey53bg("Hello World", Style = 4 ) = it's return grey53bg color text with UnderLine          \n
                grey53bg("Hello World", Style = 5 ) = it's return Blinking grey53bg color text                \n
        """
        return Colors.back_ground_color(text, style, 135, 135, 135)
                


def grey54bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey54bg colored BackGround text.\n
        grey54bg() is a BackGround Function, if You add ForeGround property given text you can use grey54 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey54bg("Hello World", Style = 0 ) = it's return grey54bg color text without any style       \n
                grey54bg("Hello World", Style = 1 ) = it's return grey54bg color text with bold text          \n
                grey54bg("Hello World", Style = 2 ) = it's return grey54bg color text with light text         \n
                grey54bg("Hello World", Style = 3 ) = it's return grey54bg color text with Italicized style   \n
                grey54bg("Hello World", Style = 4 ) = it's return grey54bg color text with UnderLine          \n
                grey54bg("Hello World", Style = 5 ) = it's return Blinking grey54bg color text                \n
        """
        return Colors.back_ground_color(text, style, 138, 138, 138)
                


def grey55bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey55bg colored BackGround text.\n
        grey55bg() is a BackGround Function, if You add ForeGround property given text you can use grey55 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey55bg("Hello World", Style = 0 ) = it's return grey55bg color text without any style       \n
                grey55bg("Hello World", Style = 1 ) = it's return grey55bg color text with bold text          \n
                grey55bg("Hello World", Style = 2 ) = it's return grey55bg color text with light text         \n
                grey55bg("Hello World", Style = 3 ) = it's return grey55bg color text with Italicized style   \n
                grey55bg("Hello World", Style = 4 ) = it's return grey55bg color text with UnderLine          \n
                grey55bg("Hello World", Style = 5 ) = it's return Blinking grey55bg color text                \n
        """
        return Colors.back_ground_color(text, style, 140, 140, 140)
                


def grey56bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey56bg colored BackGround text.\n
        grey56bg() is a BackGround Function, if You add ForeGround property given text you can use grey56 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey56bg("Hello World", Style = 0 ) = it's return grey56bg color text without any style       \n
                grey56bg("Hello World", Style = 1 ) = it's return grey56bg color text with bold text          \n
                grey56bg("Hello World", Style = 2 ) = it's return grey56bg color text with light text         \n
                grey56bg("Hello World", Style = 3 ) = it's return grey56bg color text with Italicized style   \n
                grey56bg("Hello World", Style = 4 ) = it's return grey56bg color text with UnderLine          \n
                grey56bg("Hello World", Style = 5 ) = it's return Blinking grey56bg color text                \n
        """
        return Colors.back_ground_color(text, style, 143, 143, 143)
                


def grey57bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey57bg colored BackGround text.\n
        grey57bg() is a BackGround Function, if You add ForeGround property given text you can use grey57 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey57bg("Hello World", Style = 0 ) = it's return grey57bg color text without any style       \n
                grey57bg("Hello World", Style = 1 ) = it's return grey57bg color text with bold text          \n
                grey57bg("Hello World", Style = 2 ) = it's return grey57bg color text with light text         \n
                grey57bg("Hello World", Style = 3 ) = it's return grey57bg color text with Italicized style   \n
                grey57bg("Hello World", Style = 4 ) = it's return grey57bg color text with UnderLine          \n
                grey57bg("Hello World", Style = 5 ) = it's return Blinking grey57bg color text                \n
        """
        return Colors.back_ground_color(text, style, 145, 145, 145)
                


def grey58bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey58bg colored BackGround text.\n
        grey58bg() is a BackGround Function, if You add ForeGround property given text you can use grey58 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey58bg("Hello World", Style = 0 ) = it's return grey58bg color text without any style       \n
                grey58bg("Hello World", Style = 1 ) = it's return grey58bg color text with bold text          \n
                grey58bg("Hello World", Style = 2 ) = it's return grey58bg color text with light text         \n
                grey58bg("Hello World", Style = 3 ) = it's return grey58bg color text with Italicized style   \n
                grey58bg("Hello World", Style = 4 ) = it's return grey58bg color text with UnderLine          \n
                grey58bg("Hello World", Style = 5 ) = it's return Blinking grey58bg color text                \n
        """
        return Colors.back_ground_color(text, style, 148, 148, 148)
                


def grey59bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey59bg colored BackGround text.\n
        grey59bg() is a BackGround Function, if You add ForeGround property given text you can use grey59 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey59bg("Hello World", Style = 0 ) = it's return grey59bg color text without any style       \n
                grey59bg("Hello World", Style = 1 ) = it's return grey59bg color text with bold text          \n
                grey59bg("Hello World", Style = 2 ) = it's return grey59bg color text with light text         \n
                grey59bg("Hello World", Style = 3 ) = it's return grey59bg color text with Italicized style   \n
                grey59bg("Hello World", Style = 4 ) = it's return grey59bg color text with UnderLine          \n
                grey59bg("Hello World", Style = 5 ) = it's return Blinking grey59bg color text                \n
        """
        return Colors.back_ground_color(text, style, 150, 150, 150)
                


def grey60bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey60bg colored BackGround text.\n
        grey60bg() is a BackGround Function, if You add ForeGround property given text you can use grey60 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey60bg("Hello World", Style = 0 ) = it's return grey60bg color text without any style       \n
                grey60bg("Hello World", Style = 1 ) = it's return grey60bg color text with bold text          \n
                grey60bg("Hello World", Style = 2 ) = it's return grey60bg color text with light text         \n
                grey60bg("Hello World", Style = 3 ) = it's return grey60bg color text with Italicized style   \n
                grey60bg("Hello World", Style = 4 ) = it's return grey60bg color text with UnderLine          \n
                grey60bg("Hello World", Style = 5 ) = it's return Blinking grey60bg color text                \n
        """
        return Colors.back_ground_color(text, style, 153, 153, 153)
                


def grey61bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey61bg colored BackGround text.\n
        grey61bg() is a BackGround Function, if You add ForeGround property given text you can use grey61 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey61bg("Hello World", Style = 0 ) = it's return grey61bg color text without any style       \n
                grey61bg("Hello World", Style = 1 ) = it's return grey61bg color text with bold text          \n
                grey61bg("Hello World", Style = 2 ) = it's return grey61bg color text with light text         \n
                grey61bg("Hello World", Style = 3 ) = it's return grey61bg color text with Italicized style   \n
                grey61bg("Hello World", Style = 4 ) = it's return grey61bg color text with UnderLine          \n
                grey61bg("Hello World", Style = 5 ) = it's return Blinking grey61bg color text                \n
        """
        return Colors.back_ground_color(text, style, 156, 156, 156)
                


def grey62bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey62bg colored BackGround text.\n
        grey62bg() is a BackGround Function, if You add ForeGround property given text you can use grey62 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey62bg("Hello World", Style = 0 ) = it's return grey62bg color text without any style       \n
                grey62bg("Hello World", Style = 1 ) = it's return grey62bg color text with bold text          \n
                grey62bg("Hello World", Style = 2 ) = it's return grey62bg color text with light text         \n
                grey62bg("Hello World", Style = 3 ) = it's return grey62bg color text with Italicized style   \n
                grey62bg("Hello World", Style = 4 ) = it's return grey62bg color text with UnderLine          \n
                grey62bg("Hello World", Style = 5 ) = it's return Blinking grey62bg color text                \n
        """
        return Colors.back_ground_color(text, style, 158, 158, 158)
                


def grey63bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey63bg colored BackGround text.\n
        grey63bg() is a BackGround Function, if You add ForeGround property given text you can use grey63 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey63bg("Hello World", Style = 0 ) = it's return grey63bg color text without any style       \n
                grey63bg("Hello World", Style = 1 ) = it's return grey63bg color text with bold text          \n
                grey63bg("Hello World", Style = 2 ) = it's return grey63bg color text with light text         \n
                grey63bg("Hello World", Style = 3 ) = it's return grey63bg color text with Italicized style   \n
                grey63bg("Hello World", Style = 4 ) = it's return grey63bg color text with UnderLine          \n
                grey63bg("Hello World", Style = 5 ) = it's return Blinking grey63bg color text                \n
        """
        return Colors.back_ground_color(text, style, 161, 161, 161)
                


def grey64bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey64bg colored BackGround text.\n
        grey64bg() is a BackGround Function, if You add ForeGround property given text you can use grey64 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey64bg("Hello World", Style = 0 ) = it's return grey64bg color text without any style       \n
                grey64bg("Hello World", Style = 1 ) = it's return grey64bg color text with bold text          \n
                grey64bg("Hello World", Style = 2 ) = it's return grey64bg color text with light text         \n
                grey64bg("Hello World", Style = 3 ) = it's return grey64bg color text with Italicized style   \n
                grey64bg("Hello World", Style = 4 ) = it's return grey64bg color text with UnderLine          \n
                grey64bg("Hello World", Style = 5 ) = it's return Blinking grey64bg color text                \n
        """
        return Colors.back_ground_color(text, style, 163, 163, 163)
                


def grey65bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey65bg colored BackGround text.\n
        grey65bg() is a BackGround Function, if You add ForeGround property given text you can use grey65 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey65bg("Hello World", Style = 0 ) = it's return grey65bg color text without any style       \n
                grey65bg("Hello World", Style = 1 ) = it's return grey65bg color text with bold text          \n
                grey65bg("Hello World", Style = 2 ) = it's return grey65bg color text with light text         \n
                grey65bg("Hello World", Style = 3 ) = it's return grey65bg color text with Italicized style   \n
                grey65bg("Hello World", Style = 4 ) = it's return grey65bg color text with UnderLine          \n
                grey65bg("Hello World", Style = 5 ) = it's return Blinking grey65bg color text                \n
        """
        return Colors.back_ground_color(text, style, 166, 166, 166)
                


def grey66bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey66bg colored BackGround text.\n
        grey66bg() is a BackGround Function, if You add ForeGround property given text you can use grey66 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey66bg("Hello World", Style = 0 ) = it's return grey66bg color text without any style       \n
                grey66bg("Hello World", Style = 1 ) = it's return grey66bg color text with bold text          \n
                grey66bg("Hello World", Style = 2 ) = it's return grey66bg color text with light text         \n
                grey66bg("Hello World", Style = 3 ) = it's return grey66bg color text with Italicized style   \n
                grey66bg("Hello World", Style = 4 ) = it's return grey66bg color text with UnderLine          \n
                grey66bg("Hello World", Style = 5 ) = it's return Blinking grey66bg color text                \n
        """
        return Colors.back_ground_color(text, style, 168, 168, 168)
                


def grey67bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey67bg colored BackGround text.\n
        grey67bg() is a BackGround Function, if You add ForeGround property given text you can use grey67 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey67bg("Hello World", Style = 0 ) = it's return grey67bg color text without any style       \n
                grey67bg("Hello World", Style = 1 ) = it's return grey67bg color text with bold text          \n
                grey67bg("Hello World", Style = 2 ) = it's return grey67bg color text with light text         \n
                grey67bg("Hello World", Style = 3 ) = it's return grey67bg color text with Italicized style   \n
                grey67bg("Hello World", Style = 4 ) = it's return grey67bg color text with UnderLine          \n
                grey67bg("Hello World", Style = 5 ) = it's return Blinking grey67bg color text                \n
        """
        return Colors.back_ground_color(text, style, 171, 171, 171)
                


def grey68bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey68bg colored BackGround text.\n
        grey68bg() is a BackGround Function, if You add ForeGround property given text you can use grey68 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey68bg("Hello World", Style = 0 ) = it's return grey68bg color text without any style       \n
                grey68bg("Hello World", Style = 1 ) = it's return grey68bg color text with bold text          \n
                grey68bg("Hello World", Style = 2 ) = it's return grey68bg color text with light text         \n
                grey68bg("Hello World", Style = 3 ) = it's return grey68bg color text with Italicized style   \n
                grey68bg("Hello World", Style = 4 ) = it's return grey68bg color text with UnderLine          \n
                grey68bg("Hello World", Style = 5 ) = it's return Blinking grey68bg color text                \n
        """
        return Colors.back_ground_color(text, style, 173, 173, 173)
                


def grey69bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey69bg colored BackGround text.\n
        grey69bg() is a BackGround Function, if You add ForeGround property given text you can use grey69 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey69bg("Hello World", Style = 0 ) = it's return grey69bg color text without any style       \n
                grey69bg("Hello World", Style = 1 ) = it's return grey69bg color text with bold text          \n
                grey69bg("Hello World", Style = 2 ) = it's return grey69bg color text with light text         \n
                grey69bg("Hello World", Style = 3 ) = it's return grey69bg color text with Italicized style   \n
                grey69bg("Hello World", Style = 4 ) = it's return grey69bg color text with UnderLine          \n
                grey69bg("Hello World", Style = 5 ) = it's return Blinking grey69bg color text                \n
        """
        return Colors.back_ground_color(text, style, 176, 176, 176)
                


def grey70bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey70bg colored BackGround text.\n
        grey70bg() is a BackGround Function, if You add ForeGround property given text you can use grey70 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey70bg("Hello World", Style = 0 ) = it's return grey70bg color text without any style       \n
                grey70bg("Hello World", Style = 1 ) = it's return grey70bg color text with bold text          \n
                grey70bg("Hello World", Style = 2 ) = it's return grey70bg color text with light text         \n
                grey70bg("Hello World", Style = 3 ) = it's return grey70bg color text with Italicized style   \n
                grey70bg("Hello World", Style = 4 ) = it's return grey70bg color text with UnderLine          \n
                grey70bg("Hello World", Style = 5 ) = it's return Blinking grey70bg color text                \n
        """
        return Colors.back_ground_color(text, style, 179, 179, 179)
                


def grey71bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey71bg colored BackGround text.\n
        grey71bg() is a BackGround Function, if You add ForeGround property given text you can use grey71 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey71bg("Hello World", Style = 0 ) = it's return grey71bg color text without any style       \n
                grey71bg("Hello World", Style = 1 ) = it's return grey71bg color text with bold text          \n
                grey71bg("Hello World", Style = 2 ) = it's return grey71bg color text with light text         \n
                grey71bg("Hello World", Style = 3 ) = it's return grey71bg color text with Italicized style   \n
                grey71bg("Hello World", Style = 4 ) = it's return grey71bg color text with UnderLine          \n
                grey71bg("Hello World", Style = 5 ) = it's return Blinking grey71bg color text                \n
        """
        return Colors.back_ground_color(text, style, 181, 181, 181)
                


def grey72bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey72bg colored BackGround text.\n
        grey72bg() is a BackGround Function, if You add ForeGround property given text you can use grey72 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey72bg("Hello World", Style = 0 ) = it's return grey72bg color text without any style       \n
                grey72bg("Hello World", Style = 1 ) = it's return grey72bg color text with bold text          \n
                grey72bg("Hello World", Style = 2 ) = it's return grey72bg color text with light text         \n
                grey72bg("Hello World", Style = 3 ) = it's return grey72bg color text with Italicized style   \n
                grey72bg("Hello World", Style = 4 ) = it's return grey72bg color text with UnderLine          \n
                grey72bg("Hello World", Style = 5 ) = it's return Blinking grey72bg color text                \n
        """
        return Colors.back_ground_color(text, style, 184, 184, 184)
                


def grey73bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey73bg colored BackGround text.\n
        grey73bg() is a BackGround Function, if You add ForeGround property given text you can use grey73 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey73bg("Hello World", Style = 0 ) = it's return grey73bg color text without any style       \n
                grey73bg("Hello World", Style = 1 ) = it's return grey73bg color text with bold text          \n
                grey73bg("Hello World", Style = 2 ) = it's return grey73bg color text with light text         \n
                grey73bg("Hello World", Style = 3 ) = it's return grey73bg color text with Italicized style   \n
                grey73bg("Hello World", Style = 4 ) = it's return grey73bg color text with UnderLine          \n
                grey73bg("Hello World", Style = 5 ) = it's return Blinking grey73bg color text                \n
        """
        return Colors.back_ground_color(text, style, 186, 186, 186)
                


def grey74bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey74bg colored BackGround text.\n
        grey74bg() is a BackGround Function, if You add ForeGround property given text you can use grey74 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey74bg("Hello World", Style = 0 ) = it's return grey74bg color text without any style       \n
                grey74bg("Hello World", Style = 1 ) = it's return grey74bg color text with bold text          \n
                grey74bg("Hello World", Style = 2 ) = it's return grey74bg color text with light text         \n
                grey74bg("Hello World", Style = 3 ) = it's return grey74bg color text with Italicized style   \n
                grey74bg("Hello World", Style = 4 ) = it's return grey74bg color text with UnderLine          \n
                grey74bg("Hello World", Style = 5 ) = it's return Blinking grey74bg color text                \n
        """
        return Colors.back_ground_color(text, style, 189, 189, 189)
                


def grey75bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey75bg colored BackGround text.\n
        grey75bg() is a BackGround Function, if You add ForeGround property given text you can use grey75 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey75bg("Hello World", Style = 0 ) = it's return grey75bg color text without any style       \n
                grey75bg("Hello World", Style = 1 ) = it's return grey75bg color text with bold text          \n
                grey75bg("Hello World", Style = 2 ) = it's return grey75bg color text with light text         \n
                grey75bg("Hello World", Style = 3 ) = it's return grey75bg color text with Italicized style   \n
                grey75bg("Hello World", Style = 4 ) = it's return grey75bg color text with UnderLine          \n
                grey75bg("Hello World", Style = 5 ) = it's return Blinking grey75bg color text                \n
        """
        return Colors.back_ground_color(text, style, 191, 191, 191)
                


def grey76bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey76bg colored BackGround text.\n
        grey76bg() is a BackGround Function, if You add ForeGround property given text you can use grey76 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey76bg("Hello World", Style = 0 ) = it's return grey76bg color text without any style       \n
                grey76bg("Hello World", Style = 1 ) = it's return grey76bg color text with bold text          \n
                grey76bg("Hello World", Style = 2 ) = it's return grey76bg color text with light text         \n
                grey76bg("Hello World", Style = 3 ) = it's return grey76bg color text with Italicized style   \n
                grey76bg("Hello World", Style = 4 ) = it's return grey76bg color text with UnderLine          \n
                grey76bg("Hello World", Style = 5 ) = it's return Blinking grey76bg color text                \n
        """
        return Colors.back_ground_color(text, style, 194, 194, 194)
                


def grey77bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey77bg colored BackGround text.\n
        grey77bg() is a BackGround Function, if You add ForeGround property given text you can use grey77 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey77bg("Hello World", Style = 0 ) = it's return grey77bg color text without any style       \n
                grey77bg("Hello World", Style = 1 ) = it's return grey77bg color text with bold text          \n
                grey77bg("Hello World", Style = 2 ) = it's return grey77bg color text with light text         \n
                grey77bg("Hello World", Style = 3 ) = it's return grey77bg color text with Italicized style   \n
                grey77bg("Hello World", Style = 4 ) = it's return grey77bg color text with UnderLine          \n
                grey77bg("Hello World", Style = 5 ) = it's return Blinking grey77bg color text                \n
        """
        return Colors.back_ground_color(text, style, 196, 196, 196)
                


def grey78bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey78bg colored BackGround text.\n
        grey78bg() is a BackGround Function, if You add ForeGround property given text you can use grey78 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey78bg("Hello World", Style = 0 ) = it's return grey78bg color text without any style       \n
                grey78bg("Hello World", Style = 1 ) = it's return grey78bg color text with bold text          \n
                grey78bg("Hello World", Style = 2 ) = it's return grey78bg color text with light text         \n
                grey78bg("Hello World", Style = 3 ) = it's return grey78bg color text with Italicized style   \n
                grey78bg("Hello World", Style = 4 ) = it's return grey78bg color text with UnderLine          \n
                grey78bg("Hello World", Style = 5 ) = it's return Blinking grey78bg color text                \n
        """
        return Colors.back_ground_color(text, style, 199, 199, 199)
                


def grey79bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey79bg colored BackGround text.\n
        grey79bg() is a BackGround Function, if You add ForeGround property given text you can use grey79 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey79bg("Hello World", Style = 0 ) = it's return grey79bg color text without any style       \n
                grey79bg("Hello World", Style = 1 ) = it's return grey79bg color text with bold text          \n
                grey79bg("Hello World", Style = 2 ) = it's return grey79bg color text with light text         \n
                grey79bg("Hello World", Style = 3 ) = it's return grey79bg color text with Italicized style   \n
                grey79bg("Hello World", Style = 4 ) = it's return grey79bg color text with UnderLine          \n
                grey79bg("Hello World", Style = 5 ) = it's return Blinking grey79bg color text                \n
        """
        return Colors.back_ground_color(text, style, 201, 201, 201)
                


def grey80bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey80bg colored BackGround text.\n
        grey80bg() is a BackGround Function, if You add ForeGround property given text you can use grey80 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey80bg("Hello World", Style = 0 ) = it's return grey80bg color text without any style       \n
                grey80bg("Hello World", Style = 1 ) = it's return grey80bg color text with bold text          \n
                grey80bg("Hello World", Style = 2 ) = it's return grey80bg color text with light text         \n
                grey80bg("Hello World", Style = 3 ) = it's return grey80bg color text with Italicized style   \n
                grey80bg("Hello World", Style = 4 ) = it's return grey80bg color text with UnderLine          \n
                grey80bg("Hello World", Style = 5 ) = it's return Blinking grey80bg color text                \n
        """
        return Colors.back_ground_color(text, style, 204, 204, 204)
                


def grey81bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey81bg colored BackGround text.\n
        grey81bg() is a BackGround Function, if You add ForeGround property given text you can use grey81 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey81bg("Hello World", Style = 0 ) = it's return grey81bg color text without any style       \n
                grey81bg("Hello World", Style = 1 ) = it's return grey81bg color text with bold text          \n
                grey81bg("Hello World", Style = 2 ) = it's return grey81bg color text with light text         \n
                grey81bg("Hello World", Style = 3 ) = it's return grey81bg color text with Italicized style   \n
                grey81bg("Hello World", Style = 4 ) = it's return grey81bg color text with UnderLine          \n
                grey81bg("Hello World", Style = 5 ) = it's return Blinking grey81bg color text                \n
        """
        return Colors.back_ground_color(text, style, 207, 207, 207)
                


def grey82bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey82bg colored BackGround text.\n
        grey82bg() is a BackGround Function, if You add ForeGround property given text you can use grey82 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey82bg("Hello World", Style = 0 ) = it's return grey82bg color text without any style       \n
                grey82bg("Hello World", Style = 1 ) = it's return grey82bg color text with bold text          \n
                grey82bg("Hello World", Style = 2 ) = it's return grey82bg color text with light text         \n
                grey82bg("Hello World", Style = 3 ) = it's return grey82bg color text with Italicized style   \n
                grey82bg("Hello World", Style = 4 ) = it's return grey82bg color text with UnderLine          \n
                grey82bg("Hello World", Style = 5 ) = it's return Blinking grey82bg color text                \n
        """
        return Colors.back_ground_color(text, style, 209, 209, 209)
                


def grey83bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey83bg colored BackGround text.\n
        grey83bg() is a BackGround Function, if You add ForeGround property given text you can use grey83 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey83bg("Hello World", Style = 0 ) = it's return grey83bg color text without any style       \n
                grey83bg("Hello World", Style = 1 ) = it's return grey83bg color text with bold text          \n
                grey83bg("Hello World", Style = 2 ) = it's return grey83bg color text with light text         \n
                grey83bg("Hello World", Style = 3 ) = it's return grey83bg color text with Italicized style   \n
                grey83bg("Hello World", Style = 4 ) = it's return grey83bg color text with UnderLine          \n
                grey83bg("Hello World", Style = 5 ) = it's return Blinking grey83bg color text                \n
        """
        return Colors.back_ground_color(text, style, 212, 212, 212)
                


def grey84bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey84bg colored BackGround text.\n
        grey84bg() is a BackGround Function, if You add ForeGround property given text you can use grey84 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey84bg("Hello World", Style = 0 ) = it's return grey84bg color text without any style       \n
                grey84bg("Hello World", Style = 1 ) = it's return grey84bg color text with bold text          \n
                grey84bg("Hello World", Style = 2 ) = it's return grey84bg color text with light text         \n
                grey84bg("Hello World", Style = 3 ) = it's return grey84bg color text with Italicized style   \n
                grey84bg("Hello World", Style = 4 ) = it's return grey84bg color text with UnderLine          \n
                grey84bg("Hello World", Style = 5 ) = it's return Blinking grey84bg color text                \n
        """
        return Colors.back_ground_color(text, style, 214, 214, 214)
                


def grey85bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey85bg colored BackGround text.\n
        grey85bg() is a BackGround Function, if You add ForeGround property given text you can use grey85 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey85bg("Hello World", Style = 0 ) = it's return grey85bg color text without any style       \n
                grey85bg("Hello World", Style = 1 ) = it's return grey85bg color text with bold text          \n
                grey85bg("Hello World", Style = 2 ) = it's return grey85bg color text with light text         \n
                grey85bg("Hello World", Style = 3 ) = it's return grey85bg color text with Italicized style   \n
                grey85bg("Hello World", Style = 4 ) = it's return grey85bg color text with UnderLine          \n
                grey85bg("Hello World", Style = 5 ) = it's return Blinking grey85bg color text                \n
        """
        return Colors.back_ground_color(text, style, 217, 217, 217)
                


def grey86bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey86bg colored BackGround text.\n
        grey86bg() is a BackGround Function, if You add ForeGround property given text you can use grey86 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey86bg("Hello World", Style = 0 ) = it's return grey86bg color text without any style       \n
                grey86bg("Hello World", Style = 1 ) = it's return grey86bg color text with bold text          \n
                grey86bg("Hello World", Style = 2 ) = it's return grey86bg color text with light text         \n
                grey86bg("Hello World", Style = 3 ) = it's return grey86bg color text with Italicized style   \n
                grey86bg("Hello World", Style = 4 ) = it's return grey86bg color text with UnderLine          \n
                grey86bg("Hello World", Style = 5 ) = it's return Blinking grey86bg color text                \n
        """
        return Colors.back_ground_color(text, style, 219, 219, 219)
                


def grey87bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey87bg colored BackGround text.\n
        grey87bg() is a BackGround Function, if You add ForeGround property given text you can use grey87 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey87bg("Hello World", Style = 0 ) = it's return grey87bg color text without any style       \n
                grey87bg("Hello World", Style = 1 ) = it's return grey87bg color text with bold text          \n
                grey87bg("Hello World", Style = 2 ) = it's return grey87bg color text with light text         \n
                grey87bg("Hello World", Style = 3 ) = it's return grey87bg color text with Italicized style   \n
                grey87bg("Hello World", Style = 4 ) = it's return grey87bg color text with UnderLine          \n
                grey87bg("Hello World", Style = 5 ) = it's return Blinking grey87bg color text                \n
        """
        return Colors.back_ground_color(text, style, 222, 222, 222)
                


def grey88bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey88bg colored BackGround text.\n
        grey88bg() is a BackGround Function, if You add ForeGround property given text you can use grey88 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey88bg("Hello World", Style = 0 ) = it's return grey88bg color text without any style       \n
                grey88bg("Hello World", Style = 1 ) = it's return grey88bg color text with bold text          \n
                grey88bg("Hello World", Style = 2 ) = it's return grey88bg color text with light text         \n
                grey88bg("Hello World", Style = 3 ) = it's return grey88bg color text with Italicized style   \n
                grey88bg("Hello World", Style = 4 ) = it's return grey88bg color text with UnderLine          \n
                grey88bg("Hello World", Style = 5 ) = it's return Blinking grey88bg color text                \n
        """
        return Colors.back_ground_color(text, style, 224, 224, 224)
                


def grey89bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey89bg colored BackGround text.\n
        grey89bg() is a BackGround Function, if You add ForeGround property given text you can use grey89 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey89bg("Hello World", Style = 0 ) = it's return grey89bg color text without any style       \n
                grey89bg("Hello World", Style = 1 ) = it's return grey89bg color text with bold text          \n
                grey89bg("Hello World", Style = 2 ) = it's return grey89bg color text with light text         \n
                grey89bg("Hello World", Style = 3 ) = it's return grey89bg color text with Italicized style   \n
                grey89bg("Hello World", Style = 4 ) = it's return grey89bg color text with UnderLine          \n
                grey89bg("Hello World", Style = 5 ) = it's return Blinking grey89bg color text                \n
        """
        return Colors.back_ground_color(text, style, 227, 227, 227)
                


def grey90bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey90bg colored BackGround text.\n
        grey90bg() is a BackGround Function, if You add ForeGround property given text you can use grey90 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey90bg("Hello World", Style = 0 ) = it's return grey90bg color text without any style       \n
                grey90bg("Hello World", Style = 1 ) = it's return grey90bg color text with bold text          \n
                grey90bg("Hello World", Style = 2 ) = it's return grey90bg color text with light text         \n
                grey90bg("Hello World", Style = 3 ) = it's return grey90bg color text with Italicized style   \n
                grey90bg("Hello World", Style = 4 ) = it's return grey90bg color text with UnderLine          \n
                grey90bg("Hello World", Style = 5 ) = it's return Blinking grey90bg color text                \n
        """
        return Colors.back_ground_color(text, style, 229, 229, 229)
                


def grey91bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey91bg colored BackGround text.\n
        grey91bg() is a BackGround Function, if You add ForeGround property given text you can use grey91 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey91bg("Hello World", Style = 0 ) = it's return grey91bg color text without any style       \n
                grey91bg("Hello World", Style = 1 ) = it's return grey91bg color text with bold text          \n
                grey91bg("Hello World", Style = 2 ) = it's return grey91bg color text with light text         \n
                grey91bg("Hello World", Style = 3 ) = it's return grey91bg color text with Italicized style   \n
                grey91bg("Hello World", Style = 4 ) = it's return grey91bg color text with UnderLine          \n
                grey91bg("Hello World", Style = 5 ) = it's return Blinking grey91bg color text                \n
        """
        return Colors.back_ground_color(text, style, 232, 232, 232)
                


def grey92bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey92bg colored BackGround text.\n
        grey92bg() is a BackGround Function, if You add ForeGround property given text you can use grey92 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey92bg("Hello World", Style = 0 ) = it's return grey92bg color text without any style       \n
                grey92bg("Hello World", Style = 1 ) = it's return grey92bg color text with bold text          \n
                grey92bg("Hello World", Style = 2 ) = it's return grey92bg color text with light text         \n
                grey92bg("Hello World", Style = 3 ) = it's return grey92bg color text with Italicized style   \n
                grey92bg("Hello World", Style = 4 ) = it's return grey92bg color text with UnderLine          \n
                grey92bg("Hello World", Style = 5 ) = it's return Blinking grey92bg color text                \n
        """
        return Colors.back_ground_color(text, style, 235, 235, 235)
                


def grey93bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey93bg colored BackGround text.\n
        grey93bg() is a BackGround Function, if You add ForeGround property given text you can use grey93 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey93bg("Hello World", Style = 0 ) = it's return grey93bg color text without any style       \n
                grey93bg("Hello World", Style = 1 ) = it's return grey93bg color text with bold text          \n
                grey93bg("Hello World", Style = 2 ) = it's return grey93bg color text with light text         \n
                grey93bg("Hello World", Style = 3 ) = it's return grey93bg color text with Italicized style   \n
                grey93bg("Hello World", Style = 4 ) = it's return grey93bg color text with UnderLine          \n
                grey93bg("Hello World", Style = 5 ) = it's return Blinking grey93bg color text                \n
        """
        return Colors.back_ground_color(text, style, 237, 237, 237)
                


def grey94bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey94bg colored BackGround text.\n
        grey94bg() is a BackGround Function, if You add ForeGround property given text you can use grey94 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey94bg("Hello World", Style = 0 ) = it's return grey94bg color text without any style       \n
                grey94bg("Hello World", Style = 1 ) = it's return grey94bg color text with bold text          \n
                grey94bg("Hello World", Style = 2 ) = it's return grey94bg color text with light text         \n
                grey94bg("Hello World", Style = 3 ) = it's return grey94bg color text with Italicized style   \n
                grey94bg("Hello World", Style = 4 ) = it's return grey94bg color text with UnderLine          \n
                grey94bg("Hello World", Style = 5 ) = it's return Blinking grey94bg color text                \n
        """
        return Colors.back_ground_color(text, style, 240, 240, 240)
                


def grey95bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey95bg colored BackGround text.\n
        grey95bg() is a BackGround Function, if You add ForeGround property given text you can use grey95 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey95bg("Hello World", Style = 0 ) = it's return grey95bg color text without any style       \n
                grey95bg("Hello World", Style = 1 ) = it's return grey95bg color text with bold text          \n
                grey95bg("Hello World", Style = 2 ) = it's return grey95bg color text with light text         \n
                grey95bg("Hello World", Style = 3 ) = it's return grey95bg color text with Italicized style   \n
                grey95bg("Hello World", Style = 4 ) = it's return grey95bg color text with UnderLine          \n
                grey95bg("Hello World", Style = 5 ) = it's return Blinking grey95bg color text                \n
        """
        return Colors.back_ground_color(text, style, 242, 242, 242)
                


def grey96bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey96bg colored BackGround text.\n
        grey96bg() is a BackGround Function, if You add ForeGround property given text you can use grey96 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey96bg("Hello World", Style = 0 ) = it's return grey96bg color text without any style       \n
                grey96bg("Hello World", Style = 1 ) = it's return grey96bg color text with bold text          \n
                grey96bg("Hello World", Style = 2 ) = it's return grey96bg color text with light text         \n
                grey96bg("Hello World", Style = 3 ) = it's return grey96bg color text with Italicized style   \n
                grey96bg("Hello World", Style = 4 ) = it's return grey96bg color text with UnderLine          \n
                grey96bg("Hello World", Style = 5 ) = it's return Blinking grey96bg color text                \n
        """
        return Colors.back_ground_color(text, style, 245, 245, 245)
                


def grey97bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey97bg colored BackGround text.\n
        grey97bg() is a BackGround Function, if You add ForeGround property given text you can use grey97 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey97bg("Hello World", Style = 0 ) = it's return grey97bg color text without any style       \n
                grey97bg("Hello World", Style = 1 ) = it's return grey97bg color text with bold text          \n
                grey97bg("Hello World", Style = 2 ) = it's return grey97bg color text with light text         \n
                grey97bg("Hello World", Style = 3 ) = it's return grey97bg color text with Italicized style   \n
                grey97bg("Hello World", Style = 4 ) = it's return grey97bg color text with UnderLine          \n
                grey97bg("Hello World", Style = 5 ) = it's return Blinking grey97bg color text                \n
        """
        return Colors.back_ground_color(text, style, 247, 247, 247)
                


def grey98bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey98bg colored BackGround text.\n
        grey98bg() is a BackGround Function, if You add ForeGround property given text you can use grey98 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey98bg("Hello World", Style = 0 ) = it's return grey98bg color text without any style       \n
                grey98bg("Hello World", Style = 1 ) = it's return grey98bg color text with bold text          \n
                grey98bg("Hello World", Style = 2 ) = it's return grey98bg color text with light text         \n
                grey98bg("Hello World", Style = 3 ) = it's return grey98bg color text with Italicized style   \n
                grey98bg("Hello World", Style = 4 ) = it's return grey98bg color text with UnderLine          \n
                grey98bg("Hello World", Style = 5 ) = it's return Blinking grey98bg color text                \n
        """
        return Colors.back_ground_color(text, style, 250, 250, 250)
                


def grey99bg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey99bg colored BackGround text.\n
        grey99bg() is a BackGround Function, if You add ForeGround property given text you can use grey99 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey99bg("Hello World", Style = 0 ) = it's return grey99bg color text without any style       \n
                grey99bg("Hello World", Style = 1 ) = it's return grey99bg color text with bold text          \n
                grey99bg("Hello World", Style = 2 ) = it's return grey99bg color text with light text         \n
                grey99bg("Hello World", Style = 3 ) = it's return grey99bg color text with Italicized style   \n
                grey99bg("Hello World", Style = 4 ) = it's return grey99bg color text with UnderLine          \n
                grey99bg("Hello World", Style = 5 ) = it's return Blinking grey99bg color text                \n
        """
        return Colors.back_ground_color(text, style, 252, 252, 252)
                


def grey100_whitebg( text : str, style : int = default_style ) -> str :
        """
        It will return the grey100_whitebg colored BackGround text.\n
        grey100_whitebg() is a BackGround Function, if You add ForeGround property given text you can use grey100_White .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                grey100_whitebg("Hello World", Style = 0 ) = it's return grey100_whitebg color text without any style       \n
                grey100_whitebg("Hello World", Style = 1 ) = it's return grey100_whitebg color text with bold text          \n
                grey100_whitebg("Hello World", Style = 2 ) = it's return grey100_whitebg color text with light text         \n
                grey100_whitebg("Hello World", Style = 3 ) = it's return grey100_whitebg color text with Italicized style   \n
                grey100_whitebg("Hello World", Style = 4 ) = it's return grey100_whitebg color text with UnderLine          \n
                grey100_whitebg("Hello World", Style = 5 ) = it's return Blinking grey100_whitebg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 255, 255)
                


def dark_slate_greybg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_slate_greybg colored BackGround text.\n
        dark_slate_greybg() is a BackGround Function, if You add ForeGround property given text you can use Dark_Slate_Grey .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_slate_greybg("Hello World", Style = 0 ) = it's return dark_slate_greybg color text without any style       \n
                dark_slate_greybg("Hello World", Style = 1 ) = it's return dark_slate_greybg color text with bold text          \n
                dark_slate_greybg("Hello World", Style = 2 ) = it's return dark_slate_greybg color text with light text         \n
                dark_slate_greybg("Hello World", Style = 3 ) = it's return dark_slate_greybg color text with Italicized style   \n
                dark_slate_greybg("Hello World", Style = 4 ) = it's return dark_slate_greybg color text with UnderLine          \n
                dark_slate_greybg("Hello World", Style = 5 ) = it's return Blinking dark_slate_greybg color text                \n
        """
        return Colors.back_ground_color(text, style, 47, 79, 79)
                


def dim_greybg( text : str, style : int = default_style ) -> str :
        """
        It will return the dim_greybg colored BackGround text.\n
        dim_greybg() is a BackGround Function, if You add ForeGround property given text you can use Dim_Grey .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dim_greybg("Hello World", Style = 0 ) = it's return dim_greybg color text without any style       \n
                dim_greybg("Hello World", Style = 1 ) = it's return dim_greybg color text with bold text          \n
                dim_greybg("Hello World", Style = 2 ) = it's return dim_greybg color text with light text         \n
                dim_greybg("Hello World", Style = 3 ) = it's return dim_greybg color text with Italicized style   \n
                dim_greybg("Hello World", Style = 4 ) = it's return dim_greybg color text with UnderLine          \n
                dim_greybg("Hello World", Style = 5 ) = it's return Blinking dim_greybg color text                \n
        """
        return Colors.back_ground_color(text, style, 84, 84, 84)
                


def light_greybg( text : str, style : int = default_style ) -> str :
        """
        It will return the light_greybg colored BackGround text.\n
        light_greybg() is a BackGround Function, if You add ForeGround property given text you can use Light_Grey .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                light_greybg("Hello World", Style = 0 ) = it's return light_greybg color text without any style       \n
                light_greybg("Hello World", Style = 1 ) = it's return light_greybg color text with bold text          \n
                light_greybg("Hello World", Style = 2 ) = it's return light_greybg color text with light text         \n
                light_greybg("Hello World", Style = 3 ) = it's return light_greybg color text with Italicized style   \n
                light_greybg("Hello World", Style = 4 ) = it's return light_greybg color text with UnderLine          \n
                light_greybg("Hello World", Style = 5 ) = it's return Blinking light_greybg color text                \n
        """
        return Colors.back_ground_color(text, style, 219, 219, 112)
                


def very_light_greybg( text : str, style : int = default_style ) -> str :
        """
        It will return the very_light_greybg colored BackGround text.\n
        very_light_greybg() is a BackGround Function, if You add ForeGround property given text you can use Very_Light_Grey .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                very_light_greybg("Hello World", Style = 0 ) = it's return very_light_greybg color text without any style       \n
                very_light_greybg("Hello World", Style = 1 ) = it's return very_light_greybg color text with bold text          \n
                very_light_greybg("Hello World", Style = 2 ) = it's return very_light_greybg color text with light text         \n
                very_light_greybg("Hello World", Style = 3 ) = it's return very_light_greybg color text with Italicized style   \n
                very_light_greybg("Hello World", Style = 4 ) = it's return very_light_greybg color text with UnderLine          \n
                very_light_greybg("Hello World", Style = 5 ) = it's return Blinking very_light_greybg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 205, 205)
                


def free_speech_greybg( text : str, style : int = default_style ) -> str :
        """
        It will return the free_speech_greybg colored BackGround text.\n
        free_speech_greybg() is a BackGround Function, if You add ForeGround property given text you can use Free_Speech_Grey .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                free_speech_greybg("Hello World", Style = 0 ) = it's return free_speech_greybg color text without any style       \n
                free_speech_greybg("Hello World", Style = 1 ) = it's return free_speech_greybg color text with bold text          \n
                free_speech_greybg("Hello World", Style = 2 ) = it's return free_speech_greybg color text with light text         \n
                free_speech_greybg("Hello World", Style = 3 ) = it's return free_speech_greybg color text with Italicized style   \n
                free_speech_greybg("Hello World", Style = 4 ) = it's return free_speech_greybg color text with UnderLine          \n
                free_speech_greybg("Hello World", Style = 5 ) = it's return Blinking free_speech_greybg color text                \n
        """
        return Colors.back_ground_color(text, style, 99, 86, 136)
                


def alicebluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the alicebluebg colored BackGround text.\n
        alicebluebg() is a BackGround Function, if You add ForeGround property given text you can use AliceBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                alicebluebg("Hello World", Style = 0 ) = it's return alicebluebg color text without any style       \n
                alicebluebg("Hello World", Style = 1 ) = it's return alicebluebg color text with bold text          \n
                alicebluebg("Hello World", Style = 2 ) = it's return alicebluebg color text with light text         \n
                alicebluebg("Hello World", Style = 3 ) = it's return alicebluebg color text with Italicized style   \n
                alicebluebg("Hello World", Style = 4 ) = it's return alicebluebg color text with UnderLine          \n
                alicebluebg("Hello World", Style = 5 ) = it's return Blinking alicebluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 240, 248, 255)
                


def bluevioletbg( text : str, style : int = default_style ) -> str :
        """
        It will return the bluevioletbg colored BackGround text.\n
        bluevioletbg() is a BackGround Function, if You add ForeGround property given text you can use BlueViolet .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                bluevioletbg("Hello World", Style = 0 ) = it's return bluevioletbg color text without any style       \n
                bluevioletbg("Hello World", Style = 1 ) = it's return bluevioletbg color text with bold text          \n
                bluevioletbg("Hello World", Style = 2 ) = it's return bluevioletbg color text with light text         \n
                bluevioletbg("Hello World", Style = 3 ) = it's return bluevioletbg color text with Italicized style   \n
                bluevioletbg("Hello World", Style = 4 ) = it's return bluevioletbg color text with UnderLine          \n
                bluevioletbg("Hello World", Style = 5 ) = it's return Blinking bluevioletbg color text                \n
        """
        return Colors.back_ground_color(text, style, 138, 43, 226)
                


def cadet_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the cadet_bluebg colored BackGround text.\n
        cadet_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Cadet_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cadet_bluebg("Hello World", Style = 0 ) = it's return cadet_bluebg color text without any style       \n
                cadet_bluebg("Hello World", Style = 1 ) = it's return cadet_bluebg color text with bold text          \n
                cadet_bluebg("Hello World", Style = 2 ) = it's return cadet_bluebg color text with light text         \n
                cadet_bluebg("Hello World", Style = 3 ) = it's return cadet_bluebg color text with Italicized style   \n
                cadet_bluebg("Hello World", Style = 4 ) = it's return cadet_bluebg color text with UnderLine          \n
                cadet_bluebg("Hello World", Style = 5 ) = it's return Blinking cadet_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 95, 159, 159)
                


def cadetbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the cadetbluebg colored BackGround text.\n
        cadetbluebg() is a BackGround Function, if You add ForeGround property given text you can use CadetBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cadetbluebg("Hello World", Style = 0 ) = it's return cadetbluebg color text without any style       \n
                cadetbluebg("Hello World", Style = 1 ) = it's return cadetbluebg color text with bold text          \n
                cadetbluebg("Hello World", Style = 2 ) = it's return cadetbluebg color text with light text         \n
                cadetbluebg("Hello World", Style = 3 ) = it's return cadetbluebg color text with Italicized style   \n
                cadetbluebg("Hello World", Style = 4 ) = it's return cadetbluebg color text with UnderLine          \n
                cadetbluebg("Hello World", Style = 5 ) = it's return Blinking cadetbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 95, 158, 160)
                


def cadetbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the cadetbluebg colored BackGround text.\n
        cadetbluebg() is a BackGround Function, if You add ForeGround property given text you can use CadetBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cadetbluebg("Hello World", Style = 0 ) = it's return cadetbluebg color text without any style       \n
                cadetbluebg("Hello World", Style = 1 ) = it's return cadetbluebg color text with bold text          \n
                cadetbluebg("Hello World", Style = 2 ) = it's return cadetbluebg color text with light text         \n
                cadetbluebg("Hello World", Style = 3 ) = it's return cadetbluebg color text with Italicized style   \n
                cadetbluebg("Hello World", Style = 4 ) = it's return cadetbluebg color text with UnderLine          \n
                cadetbluebg("Hello World", Style = 5 ) = it's return Blinking cadetbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 95, 158, 160)
                


def cadetblue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cadetblue1bg colored BackGround text.\n
        cadetblue1bg() is a BackGround Function, if You add ForeGround property given text you can use CadetBlue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cadetblue1bg("Hello World", Style = 0 ) = it's return cadetblue1bg color text without any style       \n
                cadetblue1bg("Hello World", Style = 1 ) = it's return cadetblue1bg color text with bold text          \n
                cadetblue1bg("Hello World", Style = 2 ) = it's return cadetblue1bg color text with light text         \n
                cadetblue1bg("Hello World", Style = 3 ) = it's return cadetblue1bg color text with Italicized style   \n
                cadetblue1bg("Hello World", Style = 4 ) = it's return cadetblue1bg color text with UnderLine          \n
                cadetblue1bg("Hello World", Style = 5 ) = it's return Blinking cadetblue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 152, 245, 255)
                


def cadetblue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cadetblue2bg colored BackGround text.\n
        cadetblue2bg() is a BackGround Function, if You add ForeGround property given text you can use CadetBlue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cadetblue2bg("Hello World", Style = 0 ) = it's return cadetblue2bg color text without any style       \n
                cadetblue2bg("Hello World", Style = 1 ) = it's return cadetblue2bg color text with bold text          \n
                cadetblue2bg("Hello World", Style = 2 ) = it's return cadetblue2bg color text with light text         \n
                cadetblue2bg("Hello World", Style = 3 ) = it's return cadetblue2bg color text with Italicized style   \n
                cadetblue2bg("Hello World", Style = 4 ) = it's return cadetblue2bg color text with UnderLine          \n
                cadetblue2bg("Hello World", Style = 5 ) = it's return Blinking cadetblue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 142, 229, 238)
                


def cadetblue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cadetblue3bg colored BackGround text.\n
        cadetblue3bg() is a BackGround Function, if You add ForeGround property given text you can use CadetBlue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cadetblue3bg("Hello World", Style = 0 ) = it's return cadetblue3bg color text without any style       \n
                cadetblue3bg("Hello World", Style = 1 ) = it's return cadetblue3bg color text with bold text          \n
                cadetblue3bg("Hello World", Style = 2 ) = it's return cadetblue3bg color text with light text         \n
                cadetblue3bg("Hello World", Style = 3 ) = it's return cadetblue3bg color text with Italicized style   \n
                cadetblue3bg("Hello World", Style = 4 ) = it's return cadetblue3bg color text with UnderLine          \n
                cadetblue3bg("Hello World", Style = 5 ) = it's return Blinking cadetblue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 122, 197, 205)
                


def cadetblue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cadetblue4bg colored BackGround text.\n
        cadetblue4bg() is a BackGround Function, if You add ForeGround property given text you can use CadetBlue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cadetblue4bg("Hello World", Style = 0 ) = it's return cadetblue4bg color text without any style       \n
                cadetblue4bg("Hello World", Style = 1 ) = it's return cadetblue4bg color text with bold text          \n
                cadetblue4bg("Hello World", Style = 2 ) = it's return cadetblue4bg color text with light text         \n
                cadetblue4bg("Hello World", Style = 3 ) = it's return cadetblue4bg color text with Italicized style   \n
                cadetblue4bg("Hello World", Style = 4 ) = it's return cadetblue4bg color text with UnderLine          \n
                cadetblue4bg("Hello World", Style = 5 ) = it's return Blinking cadetblue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 83, 134, 139)
                


def corn_flower_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the corn_flower_bluebg colored BackGround text.\n
        corn_flower_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Corn_Flower_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                corn_flower_bluebg("Hello World", Style = 0 ) = it's return corn_flower_bluebg color text without any style       \n
                corn_flower_bluebg("Hello World", Style = 1 ) = it's return corn_flower_bluebg color text with bold text          \n
                corn_flower_bluebg("Hello World", Style = 2 ) = it's return corn_flower_bluebg color text with light text         \n
                corn_flower_bluebg("Hello World", Style = 3 ) = it's return corn_flower_bluebg color text with Italicized style   \n
                corn_flower_bluebg("Hello World", Style = 4 ) = it's return corn_flower_bluebg color text with UnderLine          \n
                corn_flower_bluebg("Hello World", Style = 5 ) = it's return Blinking corn_flower_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 66, 66, 111)
                


def cornflowerbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the cornflowerbluebg colored BackGround text.\n
        cornflowerbluebg() is a BackGround Function, if You add ForeGround property given text you can use CornflowerBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cornflowerbluebg("Hello World", Style = 0 ) = it's return cornflowerbluebg color text without any style       \n
                cornflowerbluebg("Hello World", Style = 1 ) = it's return cornflowerbluebg color text with bold text          \n
                cornflowerbluebg("Hello World", Style = 2 ) = it's return cornflowerbluebg color text with light text         \n
                cornflowerbluebg("Hello World", Style = 3 ) = it's return cornflowerbluebg color text with Italicized style   \n
                cornflowerbluebg("Hello World", Style = 4 ) = it's return cornflowerbluebg color text with UnderLine          \n
                cornflowerbluebg("Hello World", Style = 5 ) = it's return Blinking cornflowerbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 100, 149, 237)
                


def darkslatebluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkslatebluebg colored BackGround text.\n
        darkslatebluebg() is a BackGround Function, if You add ForeGround property given text you can use DarkSlateBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkslatebluebg("Hello World", Style = 0 ) = it's return darkslatebluebg color text without any style       \n
                darkslatebluebg("Hello World", Style = 1 ) = it's return darkslatebluebg color text with bold text          \n
                darkslatebluebg("Hello World", Style = 2 ) = it's return darkslatebluebg color text with light text         \n
                darkslatebluebg("Hello World", Style = 3 ) = it's return darkslatebluebg color text with Italicized style   \n
                darkslatebluebg("Hello World", Style = 4 ) = it's return darkslatebluebg color text with UnderLine          \n
                darkslatebluebg("Hello World", Style = 5 ) = it's return Blinking darkslatebluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 72, 61, 139)
                


def darkturquoisebg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkturquoisebg colored BackGround text.\n
        darkturquoisebg() is a BackGround Function, if You add ForeGround property given text you can use DarkTurquoise .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkturquoisebg("Hello World", Style = 0 ) = it's return darkturquoisebg color text without any style       \n
                darkturquoisebg("Hello World", Style = 1 ) = it's return darkturquoisebg color text with bold text          \n
                darkturquoisebg("Hello World", Style = 2 ) = it's return darkturquoisebg color text with light text         \n
                darkturquoisebg("Hello World", Style = 3 ) = it's return darkturquoisebg color text with Italicized style   \n
                darkturquoisebg("Hello World", Style = 4 ) = it's return darkturquoisebg color text with UnderLine          \n
                darkturquoisebg("Hello World", Style = 5 ) = it's return Blinking darkturquoisebg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 206, 209)
                


def deepskybluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the deepskybluebg colored BackGround text.\n
        deepskybluebg() is a BackGround Function, if You add ForeGround property given text you can use DeepSkyBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                deepskybluebg("Hello World", Style = 0 ) = it's return deepskybluebg color text without any style       \n
                deepskybluebg("Hello World", Style = 1 ) = it's return deepskybluebg color text with bold text          \n
                deepskybluebg("Hello World", Style = 2 ) = it's return deepskybluebg color text with light text         \n
                deepskybluebg("Hello World", Style = 3 ) = it's return deepskybluebg color text with Italicized style   \n
                deepskybluebg("Hello World", Style = 4 ) = it's return deepskybluebg color text with UnderLine          \n
                deepskybluebg("Hello World", Style = 5 ) = it's return Blinking deepskybluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 191, 255)
                


def deepskyblue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the deepskyblue1bg colored BackGround text.\n
        deepskyblue1bg() is a BackGround Function, if You add ForeGround property given text you can use DeepSkyBlue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                deepskyblue1bg("Hello World", Style = 0 ) = it's return deepskyblue1bg color text without any style       \n
                deepskyblue1bg("Hello World", Style = 1 ) = it's return deepskyblue1bg color text with bold text          \n
                deepskyblue1bg("Hello World", Style = 2 ) = it's return deepskyblue1bg color text with light text         \n
                deepskyblue1bg("Hello World", Style = 3 ) = it's return deepskyblue1bg color text with Italicized style   \n
                deepskyblue1bg("Hello World", Style = 4 ) = it's return deepskyblue1bg color text with UnderLine          \n
                deepskyblue1bg("Hello World", Style = 5 ) = it's return Blinking deepskyblue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 191, 255)
                


def deepskyblue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the deepskyblue2bg colored BackGround text.\n
        deepskyblue2bg() is a BackGround Function, if You add ForeGround property given text you can use DeepSkyBlue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                deepskyblue2bg("Hello World", Style = 0 ) = it's return deepskyblue2bg color text without any style       \n
                deepskyblue2bg("Hello World", Style = 1 ) = it's return deepskyblue2bg color text with bold text          \n
                deepskyblue2bg("Hello World", Style = 2 ) = it's return deepskyblue2bg color text with light text         \n
                deepskyblue2bg("Hello World", Style = 3 ) = it's return deepskyblue2bg color text with Italicized style   \n
                deepskyblue2bg("Hello World", Style = 4 ) = it's return deepskyblue2bg color text with UnderLine          \n
                deepskyblue2bg("Hello World", Style = 5 ) = it's return Blinking deepskyblue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 178, 238)
                


def deepskyblue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the deepskyblue3bg colored BackGround text.\n
        deepskyblue3bg() is a BackGround Function, if You add ForeGround property given text you can use DeepSkyBlue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                deepskyblue3bg("Hello World", Style = 0 ) = it's return deepskyblue3bg color text without any style       \n
                deepskyblue3bg("Hello World", Style = 1 ) = it's return deepskyblue3bg color text with bold text          \n
                deepskyblue3bg("Hello World", Style = 2 ) = it's return deepskyblue3bg color text with light text         \n
                deepskyblue3bg("Hello World", Style = 3 ) = it's return deepskyblue3bg color text with Italicized style   \n
                deepskyblue3bg("Hello World", Style = 4 ) = it's return deepskyblue3bg color text with UnderLine          \n
                deepskyblue3bg("Hello World", Style = 5 ) = it's return Blinking deepskyblue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 154, 205)
                


def deepskyblue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the deepskyblue4bg colored BackGround text.\n
        deepskyblue4bg() is a BackGround Function, if You add ForeGround property given text you can use DeepSkyBlue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                deepskyblue4bg("Hello World", Style = 0 ) = it's return deepskyblue4bg color text without any style       \n
                deepskyblue4bg("Hello World", Style = 1 ) = it's return deepskyblue4bg color text with bold text          \n
                deepskyblue4bg("Hello World", Style = 2 ) = it's return deepskyblue4bg color text with light text         \n
                deepskyblue4bg("Hello World", Style = 3 ) = it's return deepskyblue4bg color text with Italicized style   \n
                deepskyblue4bg("Hello World", Style = 4 ) = it's return deepskyblue4bg color text with UnderLine          \n
                deepskyblue4bg("Hello World", Style = 5 ) = it's return Blinking deepskyblue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 104, 139)
                


def dodgerbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the dodgerbluebg colored BackGround text.\n
        dodgerbluebg() is a BackGround Function, if You add ForeGround property given text you can use DodgerBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dodgerbluebg("Hello World", Style = 0 ) = it's return dodgerbluebg color text without any style       \n
                dodgerbluebg("Hello World", Style = 1 ) = it's return dodgerbluebg color text with bold text          \n
                dodgerbluebg("Hello World", Style = 2 ) = it's return dodgerbluebg color text with light text         \n
                dodgerbluebg("Hello World", Style = 3 ) = it's return dodgerbluebg color text with Italicized style   \n
                dodgerbluebg("Hello World", Style = 4 ) = it's return dodgerbluebg color text with UnderLine          \n
                dodgerbluebg("Hello World", Style = 5 ) = it's return Blinking dodgerbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 30, 144, 255)
                


def dodgerblue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the dodgerblue1bg colored BackGround text.\n
        dodgerblue1bg() is a BackGround Function, if You add ForeGround property given text you can use DodgerBlue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dodgerblue1bg("Hello World", Style = 0 ) = it's return dodgerblue1bg color text without any style       \n
                dodgerblue1bg("Hello World", Style = 1 ) = it's return dodgerblue1bg color text with bold text          \n
                dodgerblue1bg("Hello World", Style = 2 ) = it's return dodgerblue1bg color text with light text         \n
                dodgerblue1bg("Hello World", Style = 3 ) = it's return dodgerblue1bg color text with Italicized style   \n
                dodgerblue1bg("Hello World", Style = 4 ) = it's return dodgerblue1bg color text with UnderLine          \n
                dodgerblue1bg("Hello World", Style = 5 ) = it's return Blinking dodgerblue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 30, 144, 255)
                


def dodgerblue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the dodgerblue2bg colored BackGround text.\n
        dodgerblue2bg() is a BackGround Function, if You add ForeGround property given text you can use DodgerBlue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dodgerblue2bg("Hello World", Style = 0 ) = it's return dodgerblue2bg color text without any style       \n
                dodgerblue2bg("Hello World", Style = 1 ) = it's return dodgerblue2bg color text with bold text          \n
                dodgerblue2bg("Hello World", Style = 2 ) = it's return dodgerblue2bg color text with light text         \n
                dodgerblue2bg("Hello World", Style = 3 ) = it's return dodgerblue2bg color text with Italicized style   \n
                dodgerblue2bg("Hello World", Style = 4 ) = it's return dodgerblue2bg color text with UnderLine          \n
                dodgerblue2bg("Hello World", Style = 5 ) = it's return Blinking dodgerblue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 28, 134, 238)
                


def dodgerblue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the dodgerblue3bg colored BackGround text.\n
        dodgerblue3bg() is a BackGround Function, if You add ForeGround property given text you can use DodgerBlue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dodgerblue3bg("Hello World", Style = 0 ) = it's return dodgerblue3bg color text without any style       \n
                dodgerblue3bg("Hello World", Style = 1 ) = it's return dodgerblue3bg color text with bold text          \n
                dodgerblue3bg("Hello World", Style = 2 ) = it's return dodgerblue3bg color text with light text         \n
                dodgerblue3bg("Hello World", Style = 3 ) = it's return dodgerblue3bg color text with Italicized style   \n
                dodgerblue3bg("Hello World", Style = 4 ) = it's return dodgerblue3bg color text with UnderLine          \n
                dodgerblue3bg("Hello World", Style = 5 ) = it's return Blinking dodgerblue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 24, 116, 205)
                


def dodgerblue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the dodgerblue4bg colored BackGround text.\n
        dodgerblue4bg() is a BackGround Function, if You add ForeGround property given text you can use DodgerBlue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dodgerblue4bg("Hello World", Style = 0 ) = it's return dodgerblue4bg color text without any style       \n
                dodgerblue4bg("Hello World", Style = 1 ) = it's return dodgerblue4bg color text with bold text          \n
                dodgerblue4bg("Hello World", Style = 2 ) = it's return dodgerblue4bg color text with light text         \n
                dodgerblue4bg("Hello World", Style = 3 ) = it's return dodgerblue4bg color text with Italicized style   \n
                dodgerblue4bg("Hello World", Style = 4 ) = it's return dodgerblue4bg color text with UnderLine          \n
                dodgerblue4bg("Hello World", Style = 5 ) = it's return Blinking dodgerblue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 16, 78, 139)
                


def lightbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightbluebg colored BackGround text.\n
        lightbluebg() is a BackGround Function, if You add ForeGround property given text you can use LightBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightbluebg("Hello World", Style = 0 ) = it's return lightbluebg color text without any style       \n
                lightbluebg("Hello World", Style = 1 ) = it's return lightbluebg color text with bold text          \n
                lightbluebg("Hello World", Style = 2 ) = it's return lightbluebg color text with light text         \n
                lightbluebg("Hello World", Style = 3 ) = it's return lightbluebg color text with Italicized style   \n
                lightbluebg("Hello World", Style = 4 ) = it's return lightbluebg color text with UnderLine          \n
                lightbluebg("Hello World", Style = 5 ) = it's return Blinking lightbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 173, 216, 230)
                


def lightblue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightblue1bg colored BackGround text.\n
        lightblue1bg() is a BackGround Function, if You add ForeGround property given text you can use LightBlue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightblue1bg("Hello World", Style = 0 ) = it's return lightblue1bg color text without any style       \n
                lightblue1bg("Hello World", Style = 1 ) = it's return lightblue1bg color text with bold text          \n
                lightblue1bg("Hello World", Style = 2 ) = it's return lightblue1bg color text with light text         \n
                lightblue1bg("Hello World", Style = 3 ) = it's return lightblue1bg color text with Italicized style   \n
                lightblue1bg("Hello World", Style = 4 ) = it's return lightblue1bg color text with UnderLine          \n
                lightblue1bg("Hello World", Style = 5 ) = it's return Blinking lightblue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 191, 239, 255)
                


def lightblue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightblue2bg colored BackGround text.\n
        lightblue2bg() is a BackGround Function, if You add ForeGround property given text you can use LightBlue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightblue2bg("Hello World", Style = 0 ) = it's return lightblue2bg color text without any style       \n
                lightblue2bg("Hello World", Style = 1 ) = it's return lightblue2bg color text with bold text          \n
                lightblue2bg("Hello World", Style = 2 ) = it's return lightblue2bg color text with light text         \n
                lightblue2bg("Hello World", Style = 3 ) = it's return lightblue2bg color text with Italicized style   \n
                lightblue2bg("Hello World", Style = 4 ) = it's return lightblue2bg color text with UnderLine          \n
                lightblue2bg("Hello World", Style = 5 ) = it's return Blinking lightblue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 178, 223, 238)
                


def lightblue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightblue3bg colored BackGround text.\n
        lightblue3bg() is a BackGround Function, if You add ForeGround property given text you can use LightBlue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightblue3bg("Hello World", Style = 0 ) = it's return lightblue3bg color text without any style       \n
                lightblue3bg("Hello World", Style = 1 ) = it's return lightblue3bg color text with bold text          \n
                lightblue3bg("Hello World", Style = 2 ) = it's return lightblue3bg color text with light text         \n
                lightblue3bg("Hello World", Style = 3 ) = it's return lightblue3bg color text with Italicized style   \n
                lightblue3bg("Hello World", Style = 4 ) = it's return lightblue3bg color text with UnderLine          \n
                lightblue3bg("Hello World", Style = 5 ) = it's return Blinking lightblue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 154, 192, 205)
                


def lightblue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightblue4bg colored BackGround text.\n
        lightblue4bg() is a BackGround Function, if You add ForeGround property given text you can use LightBlue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightblue4bg("Hello World", Style = 0 ) = it's return lightblue4bg color text without any style       \n
                lightblue4bg("Hello World", Style = 1 ) = it's return lightblue4bg color text with bold text          \n
                lightblue4bg("Hello World", Style = 2 ) = it's return lightblue4bg color text with light text         \n
                lightblue4bg("Hello World", Style = 3 ) = it's return lightblue4bg color text with Italicized style   \n
                lightblue4bg("Hello World", Style = 4 ) = it's return lightblue4bg color text with UnderLine          \n
                lightblue4bg("Hello World", Style = 5 ) = it's return Blinking lightblue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 104, 131, 139)
                


def lightcyanbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightcyanbg colored BackGround text.\n
        lightcyanbg() is a BackGround Function, if You add ForeGround property given text you can use LightCyan .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightcyanbg("Hello World", Style = 0 ) = it's return lightcyanbg color text without any style       \n
                lightcyanbg("Hello World", Style = 1 ) = it's return lightcyanbg color text with bold text          \n
                lightcyanbg("Hello World", Style = 2 ) = it's return lightcyanbg color text with light text         \n
                lightcyanbg("Hello World", Style = 3 ) = it's return lightcyanbg color text with Italicized style   \n
                lightcyanbg("Hello World", Style = 4 ) = it's return lightcyanbg color text with UnderLine          \n
                lightcyanbg("Hello World", Style = 5 ) = it's return Blinking lightcyanbg color text                \n
        """
        return Colors.back_ground_color(text, style, 224, 255, 255)
                


def lightcyan1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightcyan1bg colored BackGround text.\n
        lightcyan1bg() is a BackGround Function, if You add ForeGround property given text you can use LightCyan1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightcyan1bg("Hello World", Style = 0 ) = it's return lightcyan1bg color text without any style       \n
                lightcyan1bg("Hello World", Style = 1 ) = it's return lightcyan1bg color text with bold text          \n
                lightcyan1bg("Hello World", Style = 2 ) = it's return lightcyan1bg color text with light text         \n
                lightcyan1bg("Hello World", Style = 3 ) = it's return lightcyan1bg color text with Italicized style   \n
                lightcyan1bg("Hello World", Style = 4 ) = it's return lightcyan1bg color text with UnderLine          \n
                lightcyan1bg("Hello World", Style = 5 ) = it's return Blinking lightcyan1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 224, 255, 255)
                


def lightcyan2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightcyan2bg colored BackGround text.\n
        lightcyan2bg() is a BackGround Function, if You add ForeGround property given text you can use LightCyan2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightcyan2bg("Hello World", Style = 0 ) = it's return lightcyan2bg color text without any style       \n
                lightcyan2bg("Hello World", Style = 1 ) = it's return lightcyan2bg color text with bold text          \n
                lightcyan2bg("Hello World", Style = 2 ) = it's return lightcyan2bg color text with light text         \n
                lightcyan2bg("Hello World", Style = 3 ) = it's return lightcyan2bg color text with Italicized style   \n
                lightcyan2bg("Hello World", Style = 4 ) = it's return lightcyan2bg color text with UnderLine          \n
                lightcyan2bg("Hello World", Style = 5 ) = it's return Blinking lightcyan2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 209, 238, 238)
                


def lightcyan3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightcyan3bg colored BackGround text.\n
        lightcyan3bg() is a BackGround Function, if You add ForeGround property given text you can use LightCyan3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightcyan3bg("Hello World", Style = 0 ) = it's return lightcyan3bg color text without any style       \n
                lightcyan3bg("Hello World", Style = 1 ) = it's return lightcyan3bg color text with bold text          \n
                lightcyan3bg("Hello World", Style = 2 ) = it's return lightcyan3bg color text with light text         \n
                lightcyan3bg("Hello World", Style = 3 ) = it's return lightcyan3bg color text with Italicized style   \n
                lightcyan3bg("Hello World", Style = 4 ) = it's return lightcyan3bg color text with UnderLine          \n
                lightcyan3bg("Hello World", Style = 5 ) = it's return Blinking lightcyan3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 180, 205, 205)
                


def lightcyan4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightcyan4bg colored BackGround text.\n
        lightcyan4bg() is a BackGround Function, if You add ForeGround property given text you can use LightCyan4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightcyan4bg("Hello World", Style = 0 ) = it's return lightcyan4bg color text without any style       \n
                lightcyan4bg("Hello World", Style = 1 ) = it's return lightcyan4bg color text with bold text          \n
                lightcyan4bg("Hello World", Style = 2 ) = it's return lightcyan4bg color text with light text         \n
                lightcyan4bg("Hello World", Style = 3 ) = it's return lightcyan4bg color text with Italicized style   \n
                lightcyan4bg("Hello World", Style = 4 ) = it's return lightcyan4bg color text with UnderLine          \n
                lightcyan4bg("Hello World", Style = 5 ) = it's return Blinking lightcyan4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 122, 139, 139)
                


def lightskybluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightskybluebg colored BackGround text.\n
        lightskybluebg() is a BackGround Function, if You add ForeGround property given text you can use LightSkyBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightskybluebg("Hello World", Style = 0 ) = it's return lightskybluebg color text without any style       \n
                lightskybluebg("Hello World", Style = 1 ) = it's return lightskybluebg color text with bold text          \n
                lightskybluebg("Hello World", Style = 2 ) = it's return lightskybluebg color text with light text         \n
                lightskybluebg("Hello World", Style = 3 ) = it's return lightskybluebg color text with Italicized style   \n
                lightskybluebg("Hello World", Style = 4 ) = it's return lightskybluebg color text with UnderLine          \n
                lightskybluebg("Hello World", Style = 5 ) = it's return Blinking lightskybluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 135, 206, 250)
                


def lightskyblue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightskyblue1bg colored BackGround text.\n
        lightskyblue1bg() is a BackGround Function, if You add ForeGround property given text you can use LightSkyBlue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightskyblue1bg("Hello World", Style = 0 ) = it's return lightskyblue1bg color text without any style       \n
                lightskyblue1bg("Hello World", Style = 1 ) = it's return lightskyblue1bg color text with bold text          \n
                lightskyblue1bg("Hello World", Style = 2 ) = it's return lightskyblue1bg color text with light text         \n
                lightskyblue1bg("Hello World", Style = 3 ) = it's return lightskyblue1bg color text with Italicized style   \n
                lightskyblue1bg("Hello World", Style = 4 ) = it's return lightskyblue1bg color text with UnderLine          \n
                lightskyblue1bg("Hello World", Style = 5 ) = it's return Blinking lightskyblue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 176, 226, 255)
                


def lightskyblue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightskyblue2bg colored BackGround text.\n
        lightskyblue2bg() is a BackGround Function, if You add ForeGround property given text you can use LightSkyBlue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightskyblue2bg("Hello World", Style = 0 ) = it's return lightskyblue2bg color text without any style       \n
                lightskyblue2bg("Hello World", Style = 1 ) = it's return lightskyblue2bg color text with bold text          \n
                lightskyblue2bg("Hello World", Style = 2 ) = it's return lightskyblue2bg color text with light text         \n
                lightskyblue2bg("Hello World", Style = 3 ) = it's return lightskyblue2bg color text with Italicized style   \n
                lightskyblue2bg("Hello World", Style = 4 ) = it's return lightskyblue2bg color text with UnderLine          \n
                lightskyblue2bg("Hello World", Style = 5 ) = it's return Blinking lightskyblue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 164, 211, 238)
                


def lightskyblue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightskyblue3bg colored BackGround text.\n
        lightskyblue3bg() is a BackGround Function, if You add ForeGround property given text you can use LightSkyBlue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightskyblue3bg("Hello World", Style = 0 ) = it's return lightskyblue3bg color text without any style       \n
                lightskyblue3bg("Hello World", Style = 1 ) = it's return lightskyblue3bg color text with bold text          \n
                lightskyblue3bg("Hello World", Style = 2 ) = it's return lightskyblue3bg color text with light text         \n
                lightskyblue3bg("Hello World", Style = 3 ) = it's return lightskyblue3bg color text with Italicized style   \n
                lightskyblue3bg("Hello World", Style = 4 ) = it's return lightskyblue3bg color text with UnderLine          \n
                lightskyblue3bg("Hello World", Style = 5 ) = it's return Blinking lightskyblue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 141, 182, 205)
                


def lightskyblue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightskyblue4bg colored BackGround text.\n
        lightskyblue4bg() is a BackGround Function, if You add ForeGround property given text you can use LightSkyBlue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightskyblue4bg("Hello World", Style = 0 ) = it's return lightskyblue4bg color text without any style       \n
                lightskyblue4bg("Hello World", Style = 1 ) = it's return lightskyblue4bg color text with bold text          \n
                lightskyblue4bg("Hello World", Style = 2 ) = it's return lightskyblue4bg color text with light text         \n
                lightskyblue4bg("Hello World", Style = 3 ) = it's return lightskyblue4bg color text with Italicized style   \n
                lightskyblue4bg("Hello World", Style = 4 ) = it's return lightskyblue4bg color text with UnderLine          \n
                lightskyblue4bg("Hello World", Style = 5 ) = it's return Blinking lightskyblue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 96, 123, 139)
                


def lightslatebluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightslatebluebg colored BackGround text.\n
        lightslatebluebg() is a BackGround Function, if You add ForeGround property given text you can use LightSlateBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightslatebluebg("Hello World", Style = 0 ) = it's return lightslatebluebg color text without any style       \n
                lightslatebluebg("Hello World", Style = 1 ) = it's return lightslatebluebg color text with bold text          \n
                lightslatebluebg("Hello World", Style = 2 ) = it's return lightslatebluebg color text with light text         \n
                lightslatebluebg("Hello World", Style = 3 ) = it's return lightslatebluebg color text with Italicized style   \n
                lightslatebluebg("Hello World", Style = 4 ) = it's return lightslatebluebg color text with UnderLine          \n
                lightslatebluebg("Hello World", Style = 5 ) = it's return Blinking lightslatebluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 132, 112, 255)
                


def lightsteelbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightsteelbluebg colored BackGround text.\n
        lightsteelbluebg() is a BackGround Function, if You add ForeGround property given text you can use LightSteelBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightsteelbluebg("Hello World", Style = 0 ) = it's return lightsteelbluebg color text without any style       \n
                lightsteelbluebg("Hello World", Style = 1 ) = it's return lightsteelbluebg color text with bold text          \n
                lightsteelbluebg("Hello World", Style = 2 ) = it's return lightsteelbluebg color text with light text         \n
                lightsteelbluebg("Hello World", Style = 3 ) = it's return lightsteelbluebg color text with Italicized style   \n
                lightsteelbluebg("Hello World", Style = 4 ) = it's return lightsteelbluebg color text with UnderLine          \n
                lightsteelbluebg("Hello World", Style = 5 ) = it's return Blinking lightsteelbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 176, 196, 222)
                


def lightsteelblue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightsteelblue1bg colored BackGround text.\n
        lightsteelblue1bg() is a BackGround Function, if You add ForeGround property given text you can use LightSteelBlue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightsteelblue1bg("Hello World", Style = 0 ) = it's return lightsteelblue1bg color text without any style       \n
                lightsteelblue1bg("Hello World", Style = 1 ) = it's return lightsteelblue1bg color text with bold text          \n
                lightsteelblue1bg("Hello World", Style = 2 ) = it's return lightsteelblue1bg color text with light text         \n
                lightsteelblue1bg("Hello World", Style = 3 ) = it's return lightsteelblue1bg color text with Italicized style   \n
                lightsteelblue1bg("Hello World", Style = 4 ) = it's return lightsteelblue1bg color text with UnderLine          \n
                lightsteelblue1bg("Hello World", Style = 5 ) = it's return Blinking lightsteelblue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 202, 225, 255)
                


def lightsteelblue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightsteelblue2bg colored BackGround text.\n
        lightsteelblue2bg() is a BackGround Function, if You add ForeGround property given text you can use LightSteelBlue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightsteelblue2bg("Hello World", Style = 0 ) = it's return lightsteelblue2bg color text without any style       \n
                lightsteelblue2bg("Hello World", Style = 1 ) = it's return lightsteelblue2bg color text with bold text          \n
                lightsteelblue2bg("Hello World", Style = 2 ) = it's return lightsteelblue2bg color text with light text         \n
                lightsteelblue2bg("Hello World", Style = 3 ) = it's return lightsteelblue2bg color text with Italicized style   \n
                lightsteelblue2bg("Hello World", Style = 4 ) = it's return lightsteelblue2bg color text with UnderLine          \n
                lightsteelblue2bg("Hello World", Style = 5 ) = it's return Blinking lightsteelblue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 188, 210, 238)
                


def lightsteelblue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightsteelblue3bg colored BackGround text.\n
        lightsteelblue3bg() is a BackGround Function, if You add ForeGround property given text you can use LightSteelBlue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightsteelblue3bg("Hello World", Style = 0 ) = it's return lightsteelblue3bg color text without any style       \n
                lightsteelblue3bg("Hello World", Style = 1 ) = it's return lightsteelblue3bg color text with bold text          \n
                lightsteelblue3bg("Hello World", Style = 2 ) = it's return lightsteelblue3bg color text with light text         \n
                lightsteelblue3bg("Hello World", Style = 3 ) = it's return lightsteelblue3bg color text with Italicized style   \n
                lightsteelblue3bg("Hello World", Style = 4 ) = it's return lightsteelblue3bg color text with UnderLine          \n
                lightsteelblue3bg("Hello World", Style = 5 ) = it's return Blinking lightsteelblue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 162, 181, 205)
                


def lightsteelblue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightsteelblue4bg colored BackGround text.\n
        lightsteelblue4bg() is a BackGround Function, if You add ForeGround property given text you can use LightSteelBlue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightsteelblue4bg("Hello World", Style = 0 ) = it's return lightsteelblue4bg color text without any style       \n
                lightsteelblue4bg("Hello World", Style = 1 ) = it's return lightsteelblue4bg color text with bold text          \n
                lightsteelblue4bg("Hello World", Style = 2 ) = it's return lightsteelblue4bg color text with light text         \n
                lightsteelblue4bg("Hello World", Style = 3 ) = it's return lightsteelblue4bg color text with Italicized style   \n
                lightsteelblue4bg("Hello World", Style = 4 ) = it's return lightsteelblue4bg color text with UnderLine          \n
                lightsteelblue4bg("Hello World", Style = 5 ) = it's return Blinking lightsteelblue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 110, 123, 139)
                


def aquamarinebg( text : str, style : int = default_style ) -> str :
        """
        It will return the aquamarinebg colored BackGround text.\n
        aquamarinebg() is a BackGround Function, if You add ForeGround property given text you can use Aquamarine .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                aquamarinebg("Hello World", Style = 0 ) = it's return aquamarinebg color text without any style       \n
                aquamarinebg("Hello World", Style = 1 ) = it's return aquamarinebg color text with bold text          \n
                aquamarinebg("Hello World", Style = 2 ) = it's return aquamarinebg color text with light text         \n
                aquamarinebg("Hello World", Style = 3 ) = it's return aquamarinebg color text with Italicized style   \n
                aquamarinebg("Hello World", Style = 4 ) = it's return aquamarinebg color text with UnderLine          \n
                aquamarinebg("Hello World", Style = 5 ) = it's return Blinking aquamarinebg color text                \n
        """
        return Colors.back_ground_color(text, style, 2, 157, 116)
                


def mediumbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumbluebg colored BackGround text.\n
        mediumbluebg() is a BackGround Function, if You add ForeGround property given text you can use MediumBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumbluebg("Hello World", Style = 0 ) = it's return mediumbluebg color text without any style       \n
                mediumbluebg("Hello World", Style = 1 ) = it's return mediumbluebg color text with bold text          \n
                mediumbluebg("Hello World", Style = 2 ) = it's return mediumbluebg color text with light text         \n
                mediumbluebg("Hello World", Style = 3 ) = it's return mediumbluebg color text with Italicized style   \n
                mediumbluebg("Hello World", Style = 4 ) = it's return mediumbluebg color text with UnderLine          \n
                mediumbluebg("Hello World", Style = 5 ) = it's return Blinking mediumbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 205)
                


def mediumslatebluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumslatebluebg colored BackGround text.\n
        mediumslatebluebg() is a BackGround Function, if You add ForeGround property given text you can use MediumSlateBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumslatebluebg("Hello World", Style = 0 ) = it's return mediumslatebluebg color text without any style       \n
                mediumslatebluebg("Hello World", Style = 1 ) = it's return mediumslatebluebg color text with bold text          \n
                mediumslatebluebg("Hello World", Style = 2 ) = it's return mediumslatebluebg color text with light text         \n
                mediumslatebluebg("Hello World", Style = 3 ) = it's return mediumslatebluebg color text with Italicized style   \n
                mediumslatebluebg("Hello World", Style = 4 ) = it's return mediumslatebluebg color text with UnderLine          \n
                mediumslatebluebg("Hello World", Style = 5 ) = it's return Blinking mediumslatebluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 123, 104, 238)
                


def mediumturquoisebg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumturquoisebg colored BackGround text.\n
        mediumturquoisebg() is a BackGround Function, if You add ForeGround property given text you can use MediumTurquoise .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumturquoisebg("Hello World", Style = 0 ) = it's return mediumturquoisebg color text without any style       \n
                mediumturquoisebg("Hello World", Style = 1 ) = it's return mediumturquoisebg color text with bold text          \n
                mediumturquoisebg("Hello World", Style = 2 ) = it's return mediumturquoisebg color text with light text         \n
                mediumturquoisebg("Hello World", Style = 3 ) = it's return mediumturquoisebg color text with Italicized style   \n
                mediumturquoisebg("Hello World", Style = 4 ) = it's return mediumturquoisebg color text with UnderLine          \n
                mediumturquoisebg("Hello World", Style = 5 ) = it's return Blinking mediumturquoisebg color text                \n
        """
        return Colors.back_ground_color(text, style, 72, 209, 204)
                


def midnightbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the midnightbluebg colored BackGround text.\n
        midnightbluebg() is a BackGround Function, if You add ForeGround property given text you can use MidnightBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                midnightbluebg("Hello World", Style = 0 ) = it's return midnightbluebg color text without any style       \n
                midnightbluebg("Hello World", Style = 1 ) = it's return midnightbluebg color text with bold text          \n
                midnightbluebg("Hello World", Style = 2 ) = it's return midnightbluebg color text with light text         \n
                midnightbluebg("Hello World", Style = 3 ) = it's return midnightbluebg color text with Italicized style   \n
                midnightbluebg("Hello World", Style = 4 ) = it's return midnightbluebg color text with UnderLine          \n
                midnightbluebg("Hello World", Style = 5 ) = it's return Blinking midnightbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 25, 25, 112)
                


def navybluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the navybluebg colored BackGround text.\n
        navybluebg() is a BackGround Function, if You add ForeGround property given text you can use NavyBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                navybluebg("Hello World", Style = 0 ) = it's return navybluebg color text without any style       \n
                navybluebg("Hello World", Style = 1 ) = it's return navybluebg color text with bold text          \n
                navybluebg("Hello World", Style = 2 ) = it's return navybluebg color text with light text         \n
                navybluebg("Hello World", Style = 3 ) = it's return navybluebg color text with Italicized style   \n
                navybluebg("Hello World", Style = 4 ) = it's return navybluebg color text with UnderLine          \n
                navybluebg("Hello World", Style = 5 ) = it's return Blinking navybluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 128)
                


def paleturquoisebg( text : str, style : int = default_style ) -> str :
        """
        It will return the paleturquoisebg colored BackGround text.\n
        paleturquoisebg() is a BackGround Function, if You add ForeGround property given text you can use PaleTurquoise .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                paleturquoisebg("Hello World", Style = 0 ) = it's return paleturquoisebg color text without any style       \n
                paleturquoisebg("Hello World", Style = 1 ) = it's return paleturquoisebg color text with bold text          \n
                paleturquoisebg("Hello World", Style = 2 ) = it's return paleturquoisebg color text with light text         \n
                paleturquoisebg("Hello World", Style = 3 ) = it's return paleturquoisebg color text with Italicized style   \n
                paleturquoisebg("Hello World", Style = 4 ) = it's return paleturquoisebg color text with UnderLine          \n
                paleturquoisebg("Hello World", Style = 5 ) = it's return Blinking paleturquoisebg color text                \n
        """
        return Colors.back_ground_color(text, style, 175, 238, 238)
                


def paleturquoise1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the paleturquoise1bg colored BackGround text.\n
        paleturquoise1bg() is a BackGround Function, if You add ForeGround property given text you can use PaleTurquoise1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                paleturquoise1bg("Hello World", Style = 0 ) = it's return paleturquoise1bg color text without any style       \n
                paleturquoise1bg("Hello World", Style = 1 ) = it's return paleturquoise1bg color text with bold text          \n
                paleturquoise1bg("Hello World", Style = 2 ) = it's return paleturquoise1bg color text with light text         \n
                paleturquoise1bg("Hello World", Style = 3 ) = it's return paleturquoise1bg color text with Italicized style   \n
                paleturquoise1bg("Hello World", Style = 4 ) = it's return paleturquoise1bg color text with UnderLine          \n
                paleturquoise1bg("Hello World", Style = 5 ) = it's return Blinking paleturquoise1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 187, 255, 255)
                


def paleturquoise2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the paleturquoise2bg colored BackGround text.\n
        paleturquoise2bg() is a BackGround Function, if You add ForeGround property given text you can use PaleTurquoise2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                paleturquoise2bg("Hello World", Style = 0 ) = it's return paleturquoise2bg color text without any style       \n
                paleturquoise2bg("Hello World", Style = 1 ) = it's return paleturquoise2bg color text with bold text          \n
                paleturquoise2bg("Hello World", Style = 2 ) = it's return paleturquoise2bg color text with light text         \n
                paleturquoise2bg("Hello World", Style = 3 ) = it's return paleturquoise2bg color text with Italicized style   \n
                paleturquoise2bg("Hello World", Style = 4 ) = it's return paleturquoise2bg color text with UnderLine          \n
                paleturquoise2bg("Hello World", Style = 5 ) = it's return Blinking paleturquoise2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 174, 238, 238)
                


def paleturquoise3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the paleturquoise3bg colored BackGround text.\n
        paleturquoise3bg() is a BackGround Function, if You add ForeGround property given text you can use PaleTurquoise3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                paleturquoise3bg("Hello World", Style = 0 ) = it's return paleturquoise3bg color text without any style       \n
                paleturquoise3bg("Hello World", Style = 1 ) = it's return paleturquoise3bg color text with bold text          \n
                paleturquoise3bg("Hello World", Style = 2 ) = it's return paleturquoise3bg color text with light text         \n
                paleturquoise3bg("Hello World", Style = 3 ) = it's return paleturquoise3bg color text with Italicized style   \n
                paleturquoise3bg("Hello World", Style = 4 ) = it's return paleturquoise3bg color text with UnderLine          \n
                paleturquoise3bg("Hello World", Style = 5 ) = it's return Blinking paleturquoise3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 150, 205, 205)
                


def paleturquoise4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the paleturquoise4bg colored BackGround text.\n
        paleturquoise4bg() is a BackGround Function, if You add ForeGround property given text you can use PaleTurquoise4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                paleturquoise4bg("Hello World", Style = 0 ) = it's return paleturquoise4bg color text without any style       \n
                paleturquoise4bg("Hello World", Style = 1 ) = it's return paleturquoise4bg color text with bold text          \n
                paleturquoise4bg("Hello World", Style = 2 ) = it's return paleturquoise4bg color text with light text         \n
                paleturquoise4bg("Hello World", Style = 3 ) = it's return paleturquoise4bg color text with Italicized style   \n
                paleturquoise4bg("Hello World", Style = 4 ) = it's return paleturquoise4bg color text with UnderLine          \n
                paleturquoise4bg("Hello World", Style = 5 ) = it's return Blinking paleturquoise4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 102, 139, 139)
                


def powderbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the powderbluebg colored BackGround text.\n
        powderbluebg() is a BackGround Function, if You add ForeGround property given text you can use PowderBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                powderbluebg("Hello World", Style = 0 ) = it's return powderbluebg color text without any style       \n
                powderbluebg("Hello World", Style = 1 ) = it's return powderbluebg color text with bold text          \n
                powderbluebg("Hello World", Style = 2 ) = it's return powderbluebg color text with light text         \n
                powderbluebg("Hello World", Style = 3 ) = it's return powderbluebg color text with Italicized style   \n
                powderbluebg("Hello World", Style = 4 ) = it's return powderbluebg color text with UnderLine          \n
                powderbluebg("Hello World", Style = 5 ) = it's return Blinking powderbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 176, 224, 230)
                


def royalbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the royalbluebg colored BackGround text.\n
        royalbluebg() is a BackGround Function, if You add ForeGround property given text you can use RoyalBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                royalbluebg("Hello World", Style = 0 ) = it's return royalbluebg color text without any style       \n
                royalbluebg("Hello World", Style = 1 ) = it's return royalbluebg color text with bold text          \n
                royalbluebg("Hello World", Style = 2 ) = it's return royalbluebg color text with light text         \n
                royalbluebg("Hello World", Style = 3 ) = it's return royalbluebg color text with Italicized style   \n
                royalbluebg("Hello World", Style = 4 ) = it's return royalbluebg color text with UnderLine          \n
                royalbluebg("Hello World", Style = 5 ) = it's return Blinking royalbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 65, 105, 225)
                


def royalblue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the royalblue1bg colored BackGround text.\n
        royalblue1bg() is a BackGround Function, if You add ForeGround property given text you can use RoyalBlue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                royalblue1bg("Hello World", Style = 0 ) = it's return royalblue1bg color text without any style       \n
                royalblue1bg("Hello World", Style = 1 ) = it's return royalblue1bg color text with bold text          \n
                royalblue1bg("Hello World", Style = 2 ) = it's return royalblue1bg color text with light text         \n
                royalblue1bg("Hello World", Style = 3 ) = it's return royalblue1bg color text with Italicized style   \n
                royalblue1bg("Hello World", Style = 4 ) = it's return royalblue1bg color text with UnderLine          \n
                royalblue1bg("Hello World", Style = 5 ) = it's return Blinking royalblue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 72, 118, 255)
                


def royalblue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the royalblue2bg colored BackGround text.\n
        royalblue2bg() is a BackGround Function, if You add ForeGround property given text you can use RoyalBlue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                royalblue2bg("Hello World", Style = 0 ) = it's return royalblue2bg color text without any style       \n
                royalblue2bg("Hello World", Style = 1 ) = it's return royalblue2bg color text with bold text          \n
                royalblue2bg("Hello World", Style = 2 ) = it's return royalblue2bg color text with light text         \n
                royalblue2bg("Hello World", Style = 3 ) = it's return royalblue2bg color text with Italicized style   \n
                royalblue2bg("Hello World", Style = 4 ) = it's return royalblue2bg color text with UnderLine          \n
                royalblue2bg("Hello World", Style = 5 ) = it's return Blinking royalblue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 67, 110, 238)
                


def royalblue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the royalblue3bg colored BackGround text.\n
        royalblue3bg() is a BackGround Function, if You add ForeGround property given text you can use RoyalBlue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                royalblue3bg("Hello World", Style = 0 ) = it's return royalblue3bg color text without any style       \n
                royalblue3bg("Hello World", Style = 1 ) = it's return royalblue3bg color text with bold text          \n
                royalblue3bg("Hello World", Style = 2 ) = it's return royalblue3bg color text with light text         \n
                royalblue3bg("Hello World", Style = 3 ) = it's return royalblue3bg color text with Italicized style   \n
                royalblue3bg("Hello World", Style = 4 ) = it's return royalblue3bg color text with UnderLine          \n
                royalblue3bg("Hello World", Style = 5 ) = it's return Blinking royalblue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 58, 95, 205)
                


def royalblue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the royalblue4bg colored BackGround text.\n
        royalblue4bg() is a BackGround Function, if You add ForeGround property given text you can use RoyalBlue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                royalblue4bg("Hello World", Style = 0 ) = it's return royalblue4bg color text without any style       \n
                royalblue4bg("Hello World", Style = 1 ) = it's return royalblue4bg color text with bold text          \n
                royalblue4bg("Hello World", Style = 2 ) = it's return royalblue4bg color text with light text         \n
                royalblue4bg("Hello World", Style = 3 ) = it's return royalblue4bg color text with Italicized style   \n
                royalblue4bg("Hello World", Style = 4 ) = it's return royalblue4bg color text with UnderLine          \n
                royalblue4bg("Hello World", Style = 5 ) = it's return Blinking royalblue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 39, 64, 139)
                


def royalblue5bg( text : str, style : int = default_style ) -> str :
        """
        It will return the royalblue5bg colored BackGround text.\n
        royalblue5bg() is a BackGround Function, if You add ForeGround property given text you can use RoyalBlue5 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                royalblue5bg("Hello World", Style = 0 ) = it's return royalblue5bg color text without any style       \n
                royalblue5bg("Hello World", Style = 1 ) = it's return royalblue5bg color text with bold text          \n
                royalblue5bg("Hello World", Style = 2 ) = it's return royalblue5bg color text with light text         \n
                royalblue5bg("Hello World", Style = 3 ) = it's return royalblue5bg color text with Italicized style   \n
                royalblue5bg("Hello World", Style = 4 ) = it's return royalblue5bg color text with UnderLine          \n
                royalblue5bg("Hello World", Style = 5 ) = it's return Blinking royalblue5bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 34, 102)
                


def skybluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the skybluebg colored BackGround text.\n
        skybluebg() is a BackGround Function, if You add ForeGround property given text you can use SkyBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                skybluebg("Hello World", Style = 0 ) = it's return skybluebg color text without any style       \n
                skybluebg("Hello World", Style = 1 ) = it's return skybluebg color text with bold text          \n
                skybluebg("Hello World", Style = 2 ) = it's return skybluebg color text with light text         \n
                skybluebg("Hello World", Style = 3 ) = it's return skybluebg color text with Italicized style   \n
                skybluebg("Hello World", Style = 4 ) = it's return skybluebg color text with UnderLine          \n
                skybluebg("Hello World", Style = 5 ) = it's return Blinking skybluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 135, 206, 235)
                


def skyblue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the skyblue1bg colored BackGround text.\n
        skyblue1bg() is a BackGround Function, if You add ForeGround property given text you can use SkyBlue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                skyblue1bg("Hello World", Style = 0 ) = it's return skyblue1bg color text without any style       \n
                skyblue1bg("Hello World", Style = 1 ) = it's return skyblue1bg color text with bold text          \n
                skyblue1bg("Hello World", Style = 2 ) = it's return skyblue1bg color text with light text         \n
                skyblue1bg("Hello World", Style = 3 ) = it's return skyblue1bg color text with Italicized style   \n
                skyblue1bg("Hello World", Style = 4 ) = it's return skyblue1bg color text with UnderLine          \n
                skyblue1bg("Hello World", Style = 5 ) = it's return Blinking skyblue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 135, 206, 255)
                


def skyblue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the skyblue2bg colored BackGround text.\n
        skyblue2bg() is a BackGround Function, if You add ForeGround property given text you can use SkyBlue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                skyblue2bg("Hello World", Style = 0 ) = it's return skyblue2bg color text without any style       \n
                skyblue2bg("Hello World", Style = 1 ) = it's return skyblue2bg color text with bold text          \n
                skyblue2bg("Hello World", Style = 2 ) = it's return skyblue2bg color text with light text         \n
                skyblue2bg("Hello World", Style = 3 ) = it's return skyblue2bg color text with Italicized style   \n
                skyblue2bg("Hello World", Style = 4 ) = it's return skyblue2bg color text with UnderLine          \n
                skyblue2bg("Hello World", Style = 5 ) = it's return Blinking skyblue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 126, 192, 238)
                


def skyblue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the skyblue3bg colored BackGround text.\n
        skyblue3bg() is a BackGround Function, if You add ForeGround property given text you can use SkyBlue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                skyblue3bg("Hello World", Style = 0 ) = it's return skyblue3bg color text without any style       \n
                skyblue3bg("Hello World", Style = 1 ) = it's return skyblue3bg color text with bold text          \n
                skyblue3bg("Hello World", Style = 2 ) = it's return skyblue3bg color text with light text         \n
                skyblue3bg("Hello World", Style = 3 ) = it's return skyblue3bg color text with Italicized style   \n
                skyblue3bg("Hello World", Style = 4 ) = it's return skyblue3bg color text with UnderLine          \n
                skyblue3bg("Hello World", Style = 5 ) = it's return Blinking skyblue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 108, 166, 205)
                


def skyblue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the skyblue4bg colored BackGround text.\n
        skyblue4bg() is a BackGround Function, if You add ForeGround property given text you can use SkyBlue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                skyblue4bg("Hello World", Style = 0 ) = it's return skyblue4bg color text without any style       \n
                skyblue4bg("Hello World", Style = 1 ) = it's return skyblue4bg color text with bold text          \n
                skyblue4bg("Hello World", Style = 2 ) = it's return skyblue4bg color text with light text         \n
                skyblue4bg("Hello World", Style = 3 ) = it's return skyblue4bg color text with Italicized style   \n
                skyblue4bg("Hello World", Style = 4 ) = it's return skyblue4bg color text with UnderLine          \n
                skyblue4bg("Hello World", Style = 5 ) = it's return Blinking skyblue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 74, 112, 139)
                


def slatebluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the slatebluebg colored BackGround text.\n
        slatebluebg() is a BackGround Function, if You add ForeGround property given text you can use SlateBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slatebluebg("Hello World", Style = 0 ) = it's return slatebluebg color text without any style       \n
                slatebluebg("Hello World", Style = 1 ) = it's return slatebluebg color text with bold text          \n
                slatebluebg("Hello World", Style = 2 ) = it's return slatebluebg color text with light text         \n
                slatebluebg("Hello World", Style = 3 ) = it's return slatebluebg color text with Italicized style   \n
                slatebluebg("Hello World", Style = 4 ) = it's return slatebluebg color text with UnderLine          \n
                slatebluebg("Hello World", Style = 5 ) = it's return Blinking slatebluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 106, 90, 205)
                


def slateblue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the slateblue1bg colored BackGround text.\n
        slateblue1bg() is a BackGround Function, if You add ForeGround property given text you can use SlateBlue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slateblue1bg("Hello World", Style = 0 ) = it's return slateblue1bg color text without any style       \n
                slateblue1bg("Hello World", Style = 1 ) = it's return slateblue1bg color text with bold text          \n
                slateblue1bg("Hello World", Style = 2 ) = it's return slateblue1bg color text with light text         \n
                slateblue1bg("Hello World", Style = 3 ) = it's return slateblue1bg color text with Italicized style   \n
                slateblue1bg("Hello World", Style = 4 ) = it's return slateblue1bg color text with UnderLine          \n
                slateblue1bg("Hello World", Style = 5 ) = it's return Blinking slateblue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 131, 111, 255)
                


def slateblue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the slateblue2bg colored BackGround text.\n
        slateblue2bg() is a BackGround Function, if You add ForeGround property given text you can use SlateBlue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slateblue2bg("Hello World", Style = 0 ) = it's return slateblue2bg color text without any style       \n
                slateblue2bg("Hello World", Style = 1 ) = it's return slateblue2bg color text with bold text          \n
                slateblue2bg("Hello World", Style = 2 ) = it's return slateblue2bg color text with light text         \n
                slateblue2bg("Hello World", Style = 3 ) = it's return slateblue2bg color text with Italicized style   \n
                slateblue2bg("Hello World", Style = 4 ) = it's return slateblue2bg color text with UnderLine          \n
                slateblue2bg("Hello World", Style = 5 ) = it's return Blinking slateblue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 122, 103, 238)
                


def slateblue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the slateblue3bg colored BackGround text.\n
        slateblue3bg() is a BackGround Function, if You add ForeGround property given text you can use SlateBlue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slateblue3bg("Hello World", Style = 0 ) = it's return slateblue3bg color text without any style       \n
                slateblue3bg("Hello World", Style = 1 ) = it's return slateblue3bg color text with bold text          \n
                slateblue3bg("Hello World", Style = 2 ) = it's return slateblue3bg color text with light text         \n
                slateblue3bg("Hello World", Style = 3 ) = it's return slateblue3bg color text with Italicized style   \n
                slateblue3bg("Hello World", Style = 4 ) = it's return slateblue3bg color text with UnderLine          \n
                slateblue3bg("Hello World", Style = 5 ) = it's return Blinking slateblue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 105, 89, 205)
                


def slateblue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the slateblue4bg colored BackGround text.\n
        slateblue4bg() is a BackGround Function, if You add ForeGround property given text you can use SlateBlue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slateblue4bg("Hello World", Style = 0 ) = it's return slateblue4bg color text without any style       \n
                slateblue4bg("Hello World", Style = 1 ) = it's return slateblue4bg color text with bold text          \n
                slateblue4bg("Hello World", Style = 2 ) = it's return slateblue4bg color text with light text         \n
                slateblue4bg("Hello World", Style = 3 ) = it's return slateblue4bg color text with Italicized style   \n
                slateblue4bg("Hello World", Style = 4 ) = it's return slateblue4bg color text with UnderLine          \n
                slateblue4bg("Hello World", Style = 5 ) = it's return Blinking slateblue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 71, 60, 139)
                


def steelbluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the steelbluebg colored BackGround text.\n
        steelbluebg() is a BackGround Function, if You add ForeGround property given text you can use SteelBlue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                steelbluebg("Hello World", Style = 0 ) = it's return steelbluebg color text without any style       \n
                steelbluebg("Hello World", Style = 1 ) = it's return steelbluebg color text with bold text          \n
                steelbluebg("Hello World", Style = 2 ) = it's return steelbluebg color text with light text         \n
                steelbluebg("Hello World", Style = 3 ) = it's return steelbluebg color text with Italicized style   \n
                steelbluebg("Hello World", Style = 4 ) = it's return steelbluebg color text with UnderLine          \n
                steelbluebg("Hello World", Style = 5 ) = it's return Blinking steelbluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 70, 130, 180)
                


def steelblue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the steelblue1bg colored BackGround text.\n
        steelblue1bg() is a BackGround Function, if You add ForeGround property given text you can use SteelBlue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                steelblue1bg("Hello World", Style = 0 ) = it's return steelblue1bg color text without any style       \n
                steelblue1bg("Hello World", Style = 1 ) = it's return steelblue1bg color text with bold text          \n
                steelblue1bg("Hello World", Style = 2 ) = it's return steelblue1bg color text with light text         \n
                steelblue1bg("Hello World", Style = 3 ) = it's return steelblue1bg color text with Italicized style   \n
                steelblue1bg("Hello World", Style = 4 ) = it's return steelblue1bg color text with UnderLine          \n
                steelblue1bg("Hello World", Style = 5 ) = it's return Blinking steelblue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 99, 184, 255)
                


def steelblue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the steelblue2bg colored BackGround text.\n
        steelblue2bg() is a BackGround Function, if You add ForeGround property given text you can use SteelBlue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                steelblue2bg("Hello World", Style = 0 ) = it's return steelblue2bg color text without any style       \n
                steelblue2bg("Hello World", Style = 1 ) = it's return steelblue2bg color text with bold text          \n
                steelblue2bg("Hello World", Style = 2 ) = it's return steelblue2bg color text with light text         \n
                steelblue2bg("Hello World", Style = 3 ) = it's return steelblue2bg color text with Italicized style   \n
                steelblue2bg("Hello World", Style = 4 ) = it's return steelblue2bg color text with UnderLine          \n
                steelblue2bg("Hello World", Style = 5 ) = it's return Blinking steelblue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 92, 172, 238)
                


def steelblue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the steelblue3bg colored BackGround text.\n
        steelblue3bg() is a BackGround Function, if You add ForeGround property given text you can use SteelBlue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                steelblue3bg("Hello World", Style = 0 ) = it's return steelblue3bg color text without any style       \n
                steelblue3bg("Hello World", Style = 1 ) = it's return steelblue3bg color text with bold text          \n
                steelblue3bg("Hello World", Style = 2 ) = it's return steelblue3bg color text with light text         \n
                steelblue3bg("Hello World", Style = 3 ) = it's return steelblue3bg color text with Italicized style   \n
                steelblue3bg("Hello World", Style = 4 ) = it's return steelblue3bg color text with UnderLine          \n
                steelblue3bg("Hello World", Style = 5 ) = it's return Blinking steelblue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 79, 148, 205)
                


def steelblue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the steelblue4bg colored BackGround text.\n
        steelblue4bg() is a BackGround Function, if You add ForeGround property given text you can use SteelBlue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                steelblue4bg("Hello World", Style = 0 ) = it's return steelblue4bg color text without any style       \n
                steelblue4bg("Hello World", Style = 1 ) = it's return steelblue4bg color text with bold text          \n
                steelblue4bg("Hello World", Style = 2 ) = it's return steelblue4bg color text with light text         \n
                steelblue4bg("Hello World", Style = 3 ) = it's return steelblue4bg color text with Italicized style   \n
                steelblue4bg("Hello World", Style = 4 ) = it's return steelblue4bg color text with UnderLine          \n
                steelblue4bg("Hello World", Style = 5 ) = it's return Blinking steelblue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 54, 100, 139)
                


def aquamarinebg( text : str, style : int = default_style ) -> str :
        """
        It will return the aquamarinebg colored BackGround text.\n
        aquamarinebg() is a BackGround Function, if You add ForeGround property given text you can use aquamarine .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                aquamarinebg("Hello World", Style = 0 ) = it's return aquamarinebg color text without any style       \n
                aquamarinebg("Hello World", Style = 1 ) = it's return aquamarinebg color text with bold text          \n
                aquamarinebg("Hello World", Style = 2 ) = it's return aquamarinebg color text with light text         \n
                aquamarinebg("Hello World", Style = 3 ) = it's return aquamarinebg color text with Italicized style   \n
                aquamarinebg("Hello World", Style = 4 ) = it's return aquamarinebg color text with UnderLine          \n
                aquamarinebg("Hello World", Style = 5 ) = it's return Blinking aquamarinebg color text                \n
        """
        return Colors.back_ground_color(text, style, 127, 255, 212)
                


def aquamarine1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the aquamarine1bg colored BackGround text.\n
        aquamarine1bg() is a BackGround Function, if You add ForeGround property given text you can use aquamarine1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                aquamarine1bg("Hello World", Style = 0 ) = it's return aquamarine1bg color text without any style       \n
                aquamarine1bg("Hello World", Style = 1 ) = it's return aquamarine1bg color text with bold text          \n
                aquamarine1bg("Hello World", Style = 2 ) = it's return aquamarine1bg color text with light text         \n
                aquamarine1bg("Hello World", Style = 3 ) = it's return aquamarine1bg color text with Italicized style   \n
                aquamarine1bg("Hello World", Style = 4 ) = it's return aquamarine1bg color text with UnderLine          \n
                aquamarine1bg("Hello World", Style = 5 ) = it's return Blinking aquamarine1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 127, 255, 212)
                


def aquamarine2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the aquamarine2bg colored BackGround text.\n
        aquamarine2bg() is a BackGround Function, if You add ForeGround property given text you can use aquamarine2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                aquamarine2bg("Hello World", Style = 0 ) = it's return aquamarine2bg color text without any style       \n
                aquamarine2bg("Hello World", Style = 1 ) = it's return aquamarine2bg color text with bold text          \n
                aquamarine2bg("Hello World", Style = 2 ) = it's return aquamarine2bg color text with light text         \n
                aquamarine2bg("Hello World", Style = 3 ) = it's return aquamarine2bg color text with Italicized style   \n
                aquamarine2bg("Hello World", Style = 4 ) = it's return aquamarine2bg color text with UnderLine          \n
                aquamarine2bg("Hello World", Style = 5 ) = it's return Blinking aquamarine2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 118, 238, 198)
                


def mediumaquamarinebg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumaquamarinebg colored BackGround text.\n
        mediumaquamarinebg() is a BackGround Function, if You add ForeGround property given text you can use MediumAquamarine .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumaquamarinebg("Hello World", Style = 0 ) = it's return mediumaquamarinebg color text without any style       \n
                mediumaquamarinebg("Hello World", Style = 1 ) = it's return mediumaquamarinebg color text with bold text          \n
                mediumaquamarinebg("Hello World", Style = 2 ) = it's return mediumaquamarinebg color text with light text         \n
                mediumaquamarinebg("Hello World", Style = 3 ) = it's return mediumaquamarinebg color text with Italicized style   \n
                mediumaquamarinebg("Hello World", Style = 4 ) = it's return mediumaquamarinebg color text with UnderLine          \n
                mediumaquamarinebg("Hello World", Style = 5 ) = it's return Blinking mediumaquamarinebg color text                \n
        """
        return Colors.back_ground_color(text, style, 102, 205, 170)
                


def aquamarine4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the aquamarine4bg colored BackGround text.\n
        aquamarine4bg() is a BackGround Function, if You add ForeGround property given text you can use aquamarine4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                aquamarine4bg("Hello World", Style = 0 ) = it's return aquamarine4bg color text without any style       \n
                aquamarine4bg("Hello World", Style = 1 ) = it's return aquamarine4bg color text with bold text          \n
                aquamarine4bg("Hello World", Style = 2 ) = it's return aquamarine4bg color text with light text         \n
                aquamarine4bg("Hello World", Style = 3 ) = it's return aquamarine4bg color text with Italicized style   \n
                aquamarine4bg("Hello World", Style = 4 ) = it's return aquamarine4bg color text with UnderLine          \n
                aquamarine4bg("Hello World", Style = 5 ) = it's return Blinking aquamarine4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 69, 139, 116)
                


def azurebg( text : str, style : int = default_style ) -> str :
        """
        It will return the azurebg colored BackGround text.\n
        azurebg() is a BackGround Function, if You add ForeGround property given text you can use azure .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                azurebg("Hello World", Style = 0 ) = it's return azurebg color text without any style       \n
                azurebg("Hello World", Style = 1 ) = it's return azurebg color text with bold text          \n
                azurebg("Hello World", Style = 2 ) = it's return azurebg color text with light text         \n
                azurebg("Hello World", Style = 3 ) = it's return azurebg color text with Italicized style   \n
                azurebg("Hello World", Style = 4 ) = it's return azurebg color text with UnderLine          \n
                azurebg("Hello World", Style = 5 ) = it's return Blinking azurebg color text                \n
        """
        return Colors.back_ground_color(text, style, 240, 255, 255)
                


def azure1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the azure1bg colored BackGround text.\n
        azure1bg() is a BackGround Function, if You add ForeGround property given text you can use azure1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                azure1bg("Hello World", Style = 0 ) = it's return azure1bg color text without any style       \n
                azure1bg("Hello World", Style = 1 ) = it's return azure1bg color text with bold text          \n
                azure1bg("Hello World", Style = 2 ) = it's return azure1bg color text with light text         \n
                azure1bg("Hello World", Style = 3 ) = it's return azure1bg color text with Italicized style   \n
                azure1bg("Hello World", Style = 4 ) = it's return azure1bg color text with UnderLine          \n
                azure1bg("Hello World", Style = 5 ) = it's return Blinking azure1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 240, 255, 255)
                


def azure2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the azure2bg colored BackGround text.\n
        azure2bg() is a BackGround Function, if You add ForeGround property given text you can use azure2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                azure2bg("Hello World", Style = 0 ) = it's return azure2bg color text without any style       \n
                azure2bg("Hello World", Style = 1 ) = it's return azure2bg color text with bold text          \n
                azure2bg("Hello World", Style = 2 ) = it's return azure2bg color text with light text         \n
                azure2bg("Hello World", Style = 3 ) = it's return azure2bg color text with Italicized style   \n
                azure2bg("Hello World", Style = 4 ) = it's return azure2bg color text with UnderLine          \n
                azure2bg("Hello World", Style = 5 ) = it's return Blinking azure2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 224, 238, 238)
                


def azure3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the azure3bg colored BackGround text.\n
        azure3bg() is a BackGround Function, if You add ForeGround property given text you can use azure3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                azure3bg("Hello World", Style = 0 ) = it's return azure3bg color text without any style       \n
                azure3bg("Hello World", Style = 1 ) = it's return azure3bg color text with bold text          \n
                azure3bg("Hello World", Style = 2 ) = it's return azure3bg color text with light text         \n
                azure3bg("Hello World", Style = 3 ) = it's return azure3bg color text with Italicized style   \n
                azure3bg("Hello World", Style = 4 ) = it's return azure3bg color text with UnderLine          \n
                azure3bg("Hello World", Style = 5 ) = it's return Blinking azure3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 193, 205, 205)
                


def azure4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the azure4bg colored BackGround text.\n
        azure4bg() is a BackGround Function, if You add ForeGround property given text you can use azure4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                azure4bg("Hello World", Style = 0 ) = it's return azure4bg color text without any style       \n
                azure4bg("Hello World", Style = 1 ) = it's return azure4bg color text with bold text          \n
                azure4bg("Hello World", Style = 2 ) = it's return azure4bg color text with light text         \n
                azure4bg("Hello World", Style = 3 ) = it's return azure4bg color text with Italicized style   \n
                azure4bg("Hello World", Style = 4 ) = it's return azure4bg color text with UnderLine          \n
                azure4bg("Hello World", Style = 5 ) = it's return Blinking azure4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 131, 139, 139)
                


def bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the bluebg colored BackGround text.\n
        bluebg() is a BackGround Function, if You add ForeGround property given text you can use blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                bluebg("Hello World", Style = 0 ) = it's return bluebg color text without any style       \n
                bluebg("Hello World", Style = 1 ) = it's return bluebg color text with bold text          \n
                bluebg("Hello World", Style = 2 ) = it's return bluebg color text with light text         \n
                bluebg("Hello World", Style = 3 ) = it's return bluebg color text with Italicized style   \n
                bluebg("Hello World", Style = 4 ) = it's return bluebg color text with UnderLine          \n
                bluebg("Hello World", Style = 5 ) = it's return Blinking bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 255)
                


def blue1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the blue1bg colored BackGround text.\n
        blue1bg() is a BackGround Function, if You add ForeGround property given text you can use blue1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                blue1bg("Hello World", Style = 0 ) = it's return blue1bg color text without any style       \n
                blue1bg("Hello World", Style = 1 ) = it's return blue1bg color text with bold text          \n
                blue1bg("Hello World", Style = 2 ) = it's return blue1bg color text with light text         \n
                blue1bg("Hello World", Style = 3 ) = it's return blue1bg color text with Italicized style   \n
                blue1bg("Hello World", Style = 4 ) = it's return blue1bg color text with UnderLine          \n
                blue1bg("Hello World", Style = 5 ) = it's return Blinking blue1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 255)
                


def blue2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the blue2bg colored BackGround text.\n
        blue2bg() is a BackGround Function, if You add ForeGround property given text you can use blue2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                blue2bg("Hello World", Style = 0 ) = it's return blue2bg color text without any style       \n
                blue2bg("Hello World", Style = 1 ) = it's return blue2bg color text with bold text          \n
                blue2bg("Hello World", Style = 2 ) = it's return blue2bg color text with light text         \n
                blue2bg("Hello World", Style = 3 ) = it's return blue2bg color text with Italicized style   \n
                blue2bg("Hello World", Style = 4 ) = it's return blue2bg color text with UnderLine          \n
                blue2bg("Hello World", Style = 5 ) = it's return Blinking blue2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 238)
                


def blue3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the blue3bg colored BackGround text.\n
        blue3bg() is a BackGround Function, if You add ForeGround property given text you can use blue3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                blue3bg("Hello World", Style = 0 ) = it's return blue3bg color text without any style       \n
                blue3bg("Hello World", Style = 1 ) = it's return blue3bg color text with bold text          \n
                blue3bg("Hello World", Style = 2 ) = it's return blue3bg color text with light text         \n
                blue3bg("Hello World", Style = 3 ) = it's return blue3bg color text with Italicized style   \n
                blue3bg("Hello World", Style = 4 ) = it's return blue3bg color text with UnderLine          \n
                blue3bg("Hello World", Style = 5 ) = it's return Blinking blue3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 205)
                


def blue4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the blue4bg colored BackGround text.\n
        blue4bg() is a BackGround Function, if You add ForeGround property given text you can use blue4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                blue4bg("Hello World", Style = 0 ) = it's return blue4bg color text without any style       \n
                blue4bg("Hello World", Style = 1 ) = it's return blue4bg color text with bold text          \n
                blue4bg("Hello World", Style = 2 ) = it's return blue4bg color text with light text         \n
                blue4bg("Hello World", Style = 3 ) = it's return blue4bg color text with Italicized style   \n
                blue4bg("Hello World", Style = 4 ) = it's return blue4bg color text with UnderLine          \n
                blue4bg("Hello World", Style = 5 ) = it's return Blinking blue4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 139)
                


def aquabg( text : str, style : int = default_style ) -> str :
        """
        It will return the aquabg colored BackGround text.\n
        aquabg() is a BackGround Function, if You add ForeGround property given text you can use aqua .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                aquabg("Hello World", Style = 0 ) = it's return aquabg color text without any style       \n
                aquabg("Hello World", Style = 1 ) = it's return aquabg color text with bold text          \n
                aquabg("Hello World", Style = 2 ) = it's return aquabg color text with light text         \n
                aquabg("Hello World", Style = 3 ) = it's return aquabg color text with Italicized style   \n
                aquabg("Hello World", Style = 4 ) = it's return aquabg color text with UnderLine          \n
                aquabg("Hello World", Style = 5 ) = it's return Blinking aquabg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 255, 255)
                


def cyanbg( text : str, style : int = default_style ) -> str :
        """
        It will return the cyanbg colored BackGround text.\n
        cyanbg() is a BackGround Function, if You add ForeGround property given text you can use cyan .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cyanbg("Hello World", Style = 0 ) = it's return cyanbg color text without any style       \n
                cyanbg("Hello World", Style = 1 ) = it's return cyanbg color text with bold text          \n
                cyanbg("Hello World", Style = 2 ) = it's return cyanbg color text with light text         \n
                cyanbg("Hello World", Style = 3 ) = it's return cyanbg color text with Italicized style   \n
                cyanbg("Hello World", Style = 4 ) = it's return cyanbg color text with UnderLine          \n
                cyanbg("Hello World", Style = 5 ) = it's return Blinking cyanbg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 255, 255)
                


def cyan1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cyan1bg colored BackGround text.\n
        cyan1bg() is a BackGround Function, if You add ForeGround property given text you can use cyan1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cyan1bg("Hello World", Style = 0 ) = it's return cyan1bg color text without any style       \n
                cyan1bg("Hello World", Style = 1 ) = it's return cyan1bg color text with bold text          \n
                cyan1bg("Hello World", Style = 2 ) = it's return cyan1bg color text with light text         \n
                cyan1bg("Hello World", Style = 3 ) = it's return cyan1bg color text with Italicized style   \n
                cyan1bg("Hello World", Style = 4 ) = it's return cyan1bg color text with UnderLine          \n
                cyan1bg("Hello World", Style = 5 ) = it's return Blinking cyan1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 255, 255)
                


def cyan2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cyan2bg colored BackGround text.\n
        cyan2bg() is a BackGround Function, if You add ForeGround property given text you can use cyan2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cyan2bg("Hello World", Style = 0 ) = it's return cyan2bg color text without any style       \n
                cyan2bg("Hello World", Style = 1 ) = it's return cyan2bg color text with bold text          \n
                cyan2bg("Hello World", Style = 2 ) = it's return cyan2bg color text with light text         \n
                cyan2bg("Hello World", Style = 3 ) = it's return cyan2bg color text with Italicized style   \n
                cyan2bg("Hello World", Style = 4 ) = it's return cyan2bg color text with UnderLine          \n
                cyan2bg("Hello World", Style = 5 ) = it's return Blinking cyan2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 238, 238)
                


def cyan3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cyan3bg colored BackGround text.\n
        cyan3bg() is a BackGround Function, if You add ForeGround property given text you can use cyan3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cyan3bg("Hello World", Style = 0 ) = it's return cyan3bg color text without any style       \n
                cyan3bg("Hello World", Style = 1 ) = it's return cyan3bg color text with bold text          \n
                cyan3bg("Hello World", Style = 2 ) = it's return cyan3bg color text with light text         \n
                cyan3bg("Hello World", Style = 3 ) = it's return cyan3bg color text with Italicized style   \n
                cyan3bg("Hello World", Style = 4 ) = it's return cyan3bg color text with UnderLine          \n
                cyan3bg("Hello World", Style = 5 ) = it's return Blinking cyan3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 205, 205)
                


def cyan4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cyan4bg colored BackGround text.\n
        cyan4bg() is a BackGround Function, if You add ForeGround property given text you can use cyan4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cyan4bg("Hello World", Style = 0 ) = it's return cyan4bg color text without any style       \n
                cyan4bg("Hello World", Style = 1 ) = it's return cyan4bg color text with bold text          \n
                cyan4bg("Hello World", Style = 2 ) = it's return cyan4bg color text with light text         \n
                cyan4bg("Hello World", Style = 3 ) = it's return cyan4bg color text with Italicized style   \n
                cyan4bg("Hello World", Style = 4 ) = it's return cyan4bg color text with UnderLine          \n
                cyan4bg("Hello World", Style = 5 ) = it's return Blinking cyan4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 139, 139)
                


def navybg( text : str, style : int = default_style ) -> str :
        """
        It will return the navybg colored BackGround text.\n
        navybg() is a BackGround Function, if You add ForeGround property given text you can use navy .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                navybg("Hello World", Style = 0 ) = it's return navybg color text without any style       \n
                navybg("Hello World", Style = 1 ) = it's return navybg color text with bold text          \n
                navybg("Hello World", Style = 2 ) = it's return navybg color text with light text         \n
                navybg("Hello World", Style = 3 ) = it's return navybg color text with Italicized style   \n
                navybg("Hello World", Style = 4 ) = it's return navybg color text with UnderLine          \n
                navybg("Hello World", Style = 5 ) = it's return Blinking navybg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 128)
                


def tealbg( text : str, style : int = default_style ) -> str :
        """
        It will return the tealbg colored BackGround text.\n
        tealbg() is a BackGround Function, if You add ForeGround property given text you can use teal .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tealbg("Hello World", Style = 0 ) = it's return tealbg color text without any style       \n
                tealbg("Hello World", Style = 1 ) = it's return tealbg color text with bold text          \n
                tealbg("Hello World", Style = 2 ) = it's return tealbg color text with light text         \n
                tealbg("Hello World", Style = 3 ) = it's return tealbg color text with Italicized style   \n
                tealbg("Hello World", Style = 4 ) = it's return tealbg color text with UnderLine          \n
                tealbg("Hello World", Style = 5 ) = it's return Blinking tealbg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 128, 128)
                


def turquoisebg( text : str, style : int = default_style ) -> str :
        """
        It will return the turquoisebg colored BackGround text.\n
        turquoisebg() is a BackGround Function, if You add ForeGround property given text you can use turquoise .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                turquoisebg("Hello World", Style = 0 ) = it's return turquoisebg color text without any style       \n
                turquoisebg("Hello World", Style = 1 ) = it's return turquoisebg color text with bold text          \n
                turquoisebg("Hello World", Style = 2 ) = it's return turquoisebg color text with light text         \n
                turquoisebg("Hello World", Style = 3 ) = it's return turquoisebg color text with Italicized style   \n
                turquoisebg("Hello World", Style = 4 ) = it's return turquoisebg color text with UnderLine          \n
                turquoisebg("Hello World", Style = 5 ) = it's return Blinking turquoisebg color text                \n
        """
        return Colors.back_ground_color(text, style, 64, 224, 208)
                


def turquoise1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the turquoise1bg colored BackGround text.\n
        turquoise1bg() is a BackGround Function, if You add ForeGround property given text you can use turquoise1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                turquoise1bg("Hello World", Style = 0 ) = it's return turquoise1bg color text without any style       \n
                turquoise1bg("Hello World", Style = 1 ) = it's return turquoise1bg color text with bold text          \n
                turquoise1bg("Hello World", Style = 2 ) = it's return turquoise1bg color text with light text         \n
                turquoise1bg("Hello World", Style = 3 ) = it's return turquoise1bg color text with Italicized style   \n
                turquoise1bg("Hello World", Style = 4 ) = it's return turquoise1bg color text with UnderLine          \n
                turquoise1bg("Hello World", Style = 5 ) = it's return Blinking turquoise1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 245, 255)
                


def turquoise2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the turquoise2bg colored BackGround text.\n
        turquoise2bg() is a BackGround Function, if You add ForeGround property given text you can use turquoise2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                turquoise2bg("Hello World", Style = 0 ) = it's return turquoise2bg color text without any style       \n
                turquoise2bg("Hello World", Style = 1 ) = it's return turquoise2bg color text with bold text          \n
                turquoise2bg("Hello World", Style = 2 ) = it's return turquoise2bg color text with light text         \n
                turquoise2bg("Hello World", Style = 3 ) = it's return turquoise2bg color text with Italicized style   \n
                turquoise2bg("Hello World", Style = 4 ) = it's return turquoise2bg color text with UnderLine          \n
                turquoise2bg("Hello World", Style = 5 ) = it's return Blinking turquoise2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 229, 238)
                


def turquoise3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the turquoise3bg colored BackGround text.\n
        turquoise3bg() is a BackGround Function, if You add ForeGround property given text you can use turquoise3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                turquoise3bg("Hello World", Style = 0 ) = it's return turquoise3bg color text without any style       \n
                turquoise3bg("Hello World", Style = 1 ) = it's return turquoise3bg color text with bold text          \n
                turquoise3bg("Hello World", Style = 2 ) = it's return turquoise3bg color text with light text         \n
                turquoise3bg("Hello World", Style = 3 ) = it's return turquoise3bg color text with Italicized style   \n
                turquoise3bg("Hello World", Style = 4 ) = it's return turquoise3bg color text with UnderLine          \n
                turquoise3bg("Hello World", Style = 5 ) = it's return Blinking turquoise3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 197, 205)
                


def turquoise4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the turquoise4bg colored BackGround text.\n
        turquoise4bg() is a BackGround Function, if You add ForeGround property given text you can use turquoise4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                turquoise4bg("Hello World", Style = 0 ) = it's return turquoise4bg color text without any style       \n
                turquoise4bg("Hello World", Style = 1 ) = it's return turquoise4bg color text with bold text          \n
                turquoise4bg("Hello World", Style = 2 ) = it's return turquoise4bg color text with light text         \n
                turquoise4bg("Hello World", Style = 3 ) = it's return turquoise4bg color text with Italicized style   \n
                turquoise4bg("Hello World", Style = 4 ) = it's return turquoise4bg color text with UnderLine          \n
                turquoise4bg("Hello World", Style = 5 ) = it's return Blinking turquoise4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 134, 139)
                


def darkslategraybg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkslategraybg colored BackGround text.\n
        darkslategraybg() is a BackGround Function, if You add ForeGround property given text you can use DarkSlateGray .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkslategraybg("Hello World", Style = 0 ) = it's return darkslategraybg color text without any style       \n
                darkslategraybg("Hello World", Style = 1 ) = it's return darkslategraybg color text with bold text          \n
                darkslategraybg("Hello World", Style = 2 ) = it's return darkslategraybg color text with light text         \n
                darkslategraybg("Hello World", Style = 3 ) = it's return darkslategraybg color text with Italicized style   \n
                darkslategraybg("Hello World", Style = 4 ) = it's return darkslategraybg color text with UnderLine          \n
                darkslategraybg("Hello World", Style = 5 ) = it's return Blinking darkslategraybg color text                \n
        """
        return Colors.back_ground_color(text, style, 47, 79, 79)
                


def darkslategray1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkslategray1bg colored BackGround text.\n
        darkslategray1bg() is a BackGround Function, if You add ForeGround property given text you can use DarkSlateGray1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkslategray1bg("Hello World", Style = 0 ) = it's return darkslategray1bg color text without any style       \n
                darkslategray1bg("Hello World", Style = 1 ) = it's return darkslategray1bg color text with bold text          \n
                darkslategray1bg("Hello World", Style = 2 ) = it's return darkslategray1bg color text with light text         \n
                darkslategray1bg("Hello World", Style = 3 ) = it's return darkslategray1bg color text with Italicized style   \n
                darkslategray1bg("Hello World", Style = 4 ) = it's return darkslategray1bg color text with UnderLine          \n
                darkslategray1bg("Hello World", Style = 5 ) = it's return Blinking darkslategray1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 151, 255, 255)
                


def darkslategray2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkslategray2bg colored BackGround text.\n
        darkslategray2bg() is a BackGround Function, if You add ForeGround property given text you can use DarkSlateGray2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkslategray2bg("Hello World", Style = 0 ) = it's return darkslategray2bg color text without any style       \n
                darkslategray2bg("Hello World", Style = 1 ) = it's return darkslategray2bg color text with bold text          \n
                darkslategray2bg("Hello World", Style = 2 ) = it's return darkslategray2bg color text with light text         \n
                darkslategray2bg("Hello World", Style = 3 ) = it's return darkslategray2bg color text with Italicized style   \n
                darkslategray2bg("Hello World", Style = 4 ) = it's return darkslategray2bg color text with UnderLine          \n
                darkslategray2bg("Hello World", Style = 5 ) = it's return Blinking darkslategray2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 141, 238, 238)
                


def darkslategray3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkslategray3bg colored BackGround text.\n
        darkslategray3bg() is a BackGround Function, if You add ForeGround property given text you can use DarkSlateGray3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkslategray3bg("Hello World", Style = 0 ) = it's return darkslategray3bg color text without any style       \n
                darkslategray3bg("Hello World", Style = 1 ) = it's return darkslategray3bg color text with bold text          \n
                darkslategray3bg("Hello World", Style = 2 ) = it's return darkslategray3bg color text with light text         \n
                darkslategray3bg("Hello World", Style = 3 ) = it's return darkslategray3bg color text with Italicized style   \n
                darkslategray3bg("Hello World", Style = 4 ) = it's return darkslategray3bg color text with UnderLine          \n
                darkslategray3bg("Hello World", Style = 5 ) = it's return Blinking darkslategray3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 121, 205, 205)
                


def darkslategray4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkslategray4bg colored BackGround text.\n
        darkslategray4bg() is a BackGround Function, if You add ForeGround property given text you can use DarkSlateGray4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkslategray4bg("Hello World", Style = 0 ) = it's return darkslategray4bg color text without any style       \n
                darkslategray4bg("Hello World", Style = 1 ) = it's return darkslategray4bg color text with bold text          \n
                darkslategray4bg("Hello World", Style = 2 ) = it's return darkslategray4bg color text with light text         \n
                darkslategray4bg("Hello World", Style = 3 ) = it's return darkslategray4bg color text with Italicized style   \n
                darkslategray4bg("Hello World", Style = 4 ) = it's return darkslategray4bg color text with UnderLine          \n
                darkslategray4bg("Hello World", Style = 5 ) = it's return Blinking darkslategray4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 82, 139, 139)
                


def dark_slate_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_slate_bluebg colored BackGround text.\n
        dark_slate_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Dark_Slate_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_slate_bluebg("Hello World", Style = 0 ) = it's return dark_slate_bluebg color text without any style       \n
                dark_slate_bluebg("Hello World", Style = 1 ) = it's return dark_slate_bluebg color text with bold text          \n
                dark_slate_bluebg("Hello World", Style = 2 ) = it's return dark_slate_bluebg color text with light text         \n
                dark_slate_bluebg("Hello World", Style = 3 ) = it's return dark_slate_bluebg color text with Italicized style   \n
                dark_slate_bluebg("Hello World", Style = 4 ) = it's return dark_slate_bluebg color text with UnderLine          \n
                dark_slate_bluebg("Hello World", Style = 5 ) = it's return Blinking dark_slate_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 36, 24, 130)
                


def dark_turquoisebg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_turquoisebg colored BackGround text.\n
        dark_turquoisebg() is a BackGround Function, if You add ForeGround property given text you can use Dark_Turquoise .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_turquoisebg("Hello World", Style = 0 ) = it's return dark_turquoisebg color text without any style       \n
                dark_turquoisebg("Hello World", Style = 1 ) = it's return dark_turquoisebg color text with bold text          \n
                dark_turquoisebg("Hello World", Style = 2 ) = it's return dark_turquoisebg color text with light text         \n
                dark_turquoisebg("Hello World", Style = 3 ) = it's return dark_turquoisebg color text with Italicized style   \n
                dark_turquoisebg("Hello World", Style = 4 ) = it's return dark_turquoisebg color text with UnderLine          \n
                dark_turquoisebg("Hello World", Style = 5 ) = it's return Blinking dark_turquoisebg color text                \n
        """
        return Colors.back_ground_color(text, style, 112, 147, 219)
                


def medium_slate_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the medium_slate_bluebg colored BackGround text.\n
        medium_slate_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Medium_Slate_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                medium_slate_bluebg("Hello World", Style = 0 ) = it's return medium_slate_bluebg color text without any style       \n
                medium_slate_bluebg("Hello World", Style = 1 ) = it's return medium_slate_bluebg color text with bold text          \n
                medium_slate_bluebg("Hello World", Style = 2 ) = it's return medium_slate_bluebg color text with light text         \n
                medium_slate_bluebg("Hello World", Style = 3 ) = it's return medium_slate_bluebg color text with Italicized style   \n
                medium_slate_bluebg("Hello World", Style = 4 ) = it's return medium_slate_bluebg color text with UnderLine          \n
                medium_slate_bluebg("Hello World", Style = 5 ) = it's return Blinking medium_slate_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 127, 0, 255)
                


def medium_turquoisebg( text : str, style : int = default_style ) -> str :
        """
        It will return the medium_turquoisebg colored BackGround text.\n
        medium_turquoisebg() is a BackGround Function, if You add ForeGround property given text you can use Medium_Turquoise .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                medium_turquoisebg("Hello World", Style = 0 ) = it's return medium_turquoisebg color text without any style       \n
                medium_turquoisebg("Hello World", Style = 1 ) = it's return medium_turquoisebg color text with bold text          \n
                medium_turquoisebg("Hello World", Style = 2 ) = it's return medium_turquoisebg color text with light text         \n
                medium_turquoisebg("Hello World", Style = 3 ) = it's return medium_turquoisebg color text with Italicized style   \n
                medium_turquoisebg("Hello World", Style = 4 ) = it's return medium_turquoisebg color text with UnderLine          \n
                medium_turquoisebg("Hello World", Style = 5 ) = it's return Blinking medium_turquoisebg color text                \n
        """
        return Colors.back_ground_color(text, style, 112, 219, 219)
                


def midnight_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the midnight_bluebg colored BackGround text.\n
        midnight_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Midnight_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                midnight_bluebg("Hello World", Style = 0 ) = it's return midnight_bluebg color text without any style       \n
                midnight_bluebg("Hello World", Style = 1 ) = it's return midnight_bluebg color text with bold text          \n
                midnight_bluebg("Hello World", Style = 2 ) = it's return midnight_bluebg color text with light text         \n
                midnight_bluebg("Hello World", Style = 3 ) = it's return midnight_bluebg color text with Italicized style   \n
                midnight_bluebg("Hello World", Style = 4 ) = it's return midnight_bluebg color text with UnderLine          \n
                midnight_bluebg("Hello World", Style = 5 ) = it's return Blinking midnight_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 47, 47, 79)
                


def navy_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the navy_bluebg colored BackGround text.\n
        navy_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Navy_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                navy_bluebg("Hello World", Style = 0 ) = it's return navy_bluebg color text without any style       \n
                navy_bluebg("Hello World", Style = 1 ) = it's return navy_bluebg color text with bold text          \n
                navy_bluebg("Hello World", Style = 2 ) = it's return navy_bluebg color text with light text         \n
                navy_bluebg("Hello World", Style = 3 ) = it's return navy_bluebg color text with Italicized style   \n
                navy_bluebg("Hello World", Style = 4 ) = it's return navy_bluebg color text with UnderLine          \n
                navy_bluebg("Hello World", Style = 5 ) = it's return Blinking navy_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 35, 35, 142)
                


def neon_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the neon_bluebg colored BackGround text.\n
        neon_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Neon_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                neon_bluebg("Hello World", Style = 0 ) = it's return neon_bluebg color text without any style       \n
                neon_bluebg("Hello World", Style = 1 ) = it's return neon_bluebg color text with bold text          \n
                neon_bluebg("Hello World", Style = 2 ) = it's return neon_bluebg color text with light text         \n
                neon_bluebg("Hello World", Style = 3 ) = it's return neon_bluebg color text with Italicized style   \n
                neon_bluebg("Hello World", Style = 4 ) = it's return neon_bluebg color text with UnderLine          \n
                neon_bluebg("Hello World", Style = 5 ) = it's return Blinking neon_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 77, 77, 255)
                


def new_midnight_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the new_midnight_bluebg colored BackGround text.\n
        new_midnight_bluebg() is a BackGround Function, if You add ForeGround property given text you can use New_Midnight_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                new_midnight_bluebg("Hello World", Style = 0 ) = it's return new_midnight_bluebg color text without any style       \n
                new_midnight_bluebg("Hello World", Style = 1 ) = it's return new_midnight_bluebg color text with bold text          \n
                new_midnight_bluebg("Hello World", Style = 2 ) = it's return new_midnight_bluebg color text with light text         \n
                new_midnight_bluebg("Hello World", Style = 3 ) = it's return new_midnight_bluebg color text with Italicized style   \n
                new_midnight_bluebg("Hello World", Style = 4 ) = it's return new_midnight_bluebg color text with UnderLine          \n
                new_midnight_bluebg("Hello World", Style = 5 ) = it's return Blinking new_midnight_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 0, 156)
                


def rich_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the rich_bluebg colored BackGround text.\n
        rich_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Rich_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                rich_bluebg("Hello World", Style = 0 ) = it's return rich_bluebg color text without any style       \n
                rich_bluebg("Hello World", Style = 1 ) = it's return rich_bluebg color text with bold text          \n
                rich_bluebg("Hello World", Style = 2 ) = it's return rich_bluebg color text with light text         \n
                rich_bluebg("Hello World", Style = 3 ) = it's return rich_bluebg color text with Italicized style   \n
                rich_bluebg("Hello World", Style = 4 ) = it's return rich_bluebg color text with UnderLine          \n
                rich_bluebg("Hello World", Style = 5 ) = it's return Blinking rich_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 89, 89, 171)
                


def sky_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the sky_bluebg colored BackGround text.\n
        sky_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Sky_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                sky_bluebg("Hello World", Style = 0 ) = it's return sky_bluebg color text without any style       \n
                sky_bluebg("Hello World", Style = 1 ) = it's return sky_bluebg color text with bold text          \n
                sky_bluebg("Hello World", Style = 2 ) = it's return sky_bluebg color text with light text         \n
                sky_bluebg("Hello World", Style = 3 ) = it's return sky_bluebg color text with Italicized style   \n
                sky_bluebg("Hello World", Style = 4 ) = it's return sky_bluebg color text with UnderLine          \n
                sky_bluebg("Hello World", Style = 5 ) = it's return Blinking sky_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 50, 153, 204)
                


def slate_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the slate_bluebg colored BackGround text.\n
        slate_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Slate_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                slate_bluebg("Hello World", Style = 0 ) = it's return slate_bluebg color text without any style       \n
                slate_bluebg("Hello World", Style = 1 ) = it's return slate_bluebg color text with bold text          \n
                slate_bluebg("Hello World", Style = 2 ) = it's return slate_bluebg color text with light text         \n
                slate_bluebg("Hello World", Style = 3 ) = it's return slate_bluebg color text with Italicized style   \n
                slate_bluebg("Hello World", Style = 4 ) = it's return slate_bluebg color text with UnderLine          \n
                slate_bluebg("Hello World", Style = 5 ) = it's return Blinking slate_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 127, 255)
                


def summer_skybg( text : str, style : int = default_style ) -> str :
        """
        It will return the summer_skybg colored BackGround text.\n
        summer_skybg() is a BackGround Function, if You add ForeGround property given text you can use Summer_Sky .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                summer_skybg("Hello World", Style = 0 ) = it's return summer_skybg color text without any style       \n
                summer_skybg("Hello World", Style = 1 ) = it's return summer_skybg color text with bold text          \n
                summer_skybg("Hello World", Style = 2 ) = it's return summer_skybg color text with light text         \n
                summer_skybg("Hello World", Style = 3 ) = it's return summer_skybg color text with Italicized style   \n
                summer_skybg("Hello World", Style = 4 ) = it's return summer_skybg color text with UnderLine          \n
                summer_skybg("Hello World", Style = 5 ) = it's return Blinking summer_skybg color text                \n
        """
        return Colors.back_ground_color(text, style, 56, 176, 222)
                


def iris_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the iris_bluebg colored BackGround text.\n
        iris_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Iris_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                iris_bluebg("Hello World", Style = 0 ) = it's return iris_bluebg color text without any style       \n
                iris_bluebg("Hello World", Style = 1 ) = it's return iris_bluebg color text with bold text          \n
                iris_bluebg("Hello World", Style = 2 ) = it's return iris_bluebg color text with light text         \n
                iris_bluebg("Hello World", Style = 3 ) = it's return iris_bluebg color text with Italicized style   \n
                iris_bluebg("Hello World", Style = 4 ) = it's return iris_bluebg color text with UnderLine          \n
                iris_bluebg("Hello World", Style = 5 ) = it's return Blinking iris_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 3, 180, 200)
                


def free_speech_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the free_speech_bluebg colored BackGround text.\n
        free_speech_bluebg() is a BackGround Function, if You add ForeGround property given text you can use Free_Speech_Blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                free_speech_bluebg("Hello World", Style = 0 ) = it's return free_speech_bluebg color text without any style       \n
                free_speech_bluebg("Hello World", Style = 1 ) = it's return free_speech_bluebg color text with bold text          \n
                free_speech_bluebg("Hello World", Style = 2 ) = it's return free_speech_bluebg color text with light text         \n
                free_speech_bluebg("Hello World", Style = 3 ) = it's return free_speech_bluebg color text with Italicized style   \n
                free_speech_bluebg("Hello World", Style = 4 ) = it's return free_speech_bluebg color text with UnderLine          \n
                free_speech_bluebg("Hello World", Style = 5 ) = it's return Blinking free_speech_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 65, 86, 197)
                


def rosybrownbg( text : str, style : int = default_style ) -> str :
        """
        It will return the rosybrownbg colored BackGround text.\n
        rosybrownbg() is a BackGround Function, if You add ForeGround property given text you can use RosyBrown .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                rosybrownbg("Hello World", Style = 0 ) = it's return rosybrownbg color text without any style       \n
                rosybrownbg("Hello World", Style = 1 ) = it's return rosybrownbg color text with bold text          \n
                rosybrownbg("Hello World", Style = 2 ) = it's return rosybrownbg color text with light text         \n
                rosybrownbg("Hello World", Style = 3 ) = it's return rosybrownbg color text with Italicized style   \n
                rosybrownbg("Hello World", Style = 4 ) = it's return rosybrownbg color text with UnderLine          \n
                rosybrownbg("Hello World", Style = 5 ) = it's return Blinking rosybrownbg color text                \n
        """
        return Colors.back_ground_color(text, style, 188, 143, 143)
                


def rosybrown1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the rosybrown1bg colored BackGround text.\n
        rosybrown1bg() is a BackGround Function, if You add ForeGround property given text you can use RosyBrown1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                rosybrown1bg("Hello World", Style = 0 ) = it's return rosybrown1bg color text without any style       \n
                rosybrown1bg("Hello World", Style = 1 ) = it's return rosybrown1bg color text with bold text          \n
                rosybrown1bg("Hello World", Style = 2 ) = it's return rosybrown1bg color text with light text         \n
                rosybrown1bg("Hello World", Style = 3 ) = it's return rosybrown1bg color text with Italicized style   \n
                rosybrown1bg("Hello World", Style = 4 ) = it's return rosybrown1bg color text with UnderLine          \n
                rosybrown1bg("Hello World", Style = 5 ) = it's return Blinking rosybrown1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 193, 193)
                


def rosybrown2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the rosybrown2bg colored BackGround text.\n
        rosybrown2bg() is a BackGround Function, if You add ForeGround property given text you can use RosyBrown2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                rosybrown2bg("Hello World", Style = 0 ) = it's return rosybrown2bg color text without any style       \n
                rosybrown2bg("Hello World", Style = 1 ) = it's return rosybrown2bg color text with bold text          \n
                rosybrown2bg("Hello World", Style = 2 ) = it's return rosybrown2bg color text with light text         \n
                rosybrown2bg("Hello World", Style = 3 ) = it's return rosybrown2bg color text with Italicized style   \n
                rosybrown2bg("Hello World", Style = 4 ) = it's return rosybrown2bg color text with UnderLine          \n
                rosybrown2bg("Hello World", Style = 5 ) = it's return Blinking rosybrown2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 180, 180)
                


def rosybrown3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the rosybrown3bg colored BackGround text.\n
        rosybrown3bg() is a BackGround Function, if You add ForeGround property given text you can use RosyBrown3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                rosybrown3bg("Hello World", Style = 0 ) = it's return rosybrown3bg color text without any style       \n
                rosybrown3bg("Hello World", Style = 1 ) = it's return rosybrown3bg color text with bold text          \n
                rosybrown3bg("Hello World", Style = 2 ) = it's return rosybrown3bg color text with light text         \n
                rosybrown3bg("Hello World", Style = 3 ) = it's return rosybrown3bg color text with Italicized style   \n
                rosybrown3bg("Hello World", Style = 4 ) = it's return rosybrown3bg color text with UnderLine          \n
                rosybrown3bg("Hello World", Style = 5 ) = it's return Blinking rosybrown3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 155, 155)
                


def rosybrown4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the rosybrown4bg colored BackGround text.\n
        rosybrown4bg() is a BackGround Function, if You add ForeGround property given text you can use RosyBrown4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                rosybrown4bg("Hello World", Style = 0 ) = it's return rosybrown4bg color text without any style       \n
                rosybrown4bg("Hello World", Style = 1 ) = it's return rosybrown4bg color text with bold text          \n
                rosybrown4bg("Hello World", Style = 2 ) = it's return rosybrown4bg color text with light text         \n
                rosybrown4bg("Hello World", Style = 3 ) = it's return rosybrown4bg color text with Italicized style   \n
                rosybrown4bg("Hello World", Style = 4 ) = it's return rosybrown4bg color text with UnderLine          \n
                rosybrown4bg("Hello World", Style = 5 ) = it's return Blinking rosybrown4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 105, 105)
                


def saddlebrownbg( text : str, style : int = default_style ) -> str :
        """
        It will return the saddlebrownbg colored BackGround text.\n
        saddlebrownbg() is a BackGround Function, if You add ForeGround property given text you can use SaddleBrown .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                saddlebrownbg("Hello World", Style = 0 ) = it's return saddlebrownbg color text without any style       \n
                saddlebrownbg("Hello World", Style = 1 ) = it's return saddlebrownbg color text with bold text          \n
                saddlebrownbg("Hello World", Style = 2 ) = it's return saddlebrownbg color text with light text         \n
                saddlebrownbg("Hello World", Style = 3 ) = it's return saddlebrownbg color text with Italicized style   \n
                saddlebrownbg("Hello World", Style = 4 ) = it's return saddlebrownbg color text with UnderLine          \n
                saddlebrownbg("Hello World", Style = 5 ) = it's return Blinking saddlebrownbg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 69, 19)
                


def sandybrownbg( text : str, style : int = default_style ) -> str :
        """
        It will return the sandybrownbg colored BackGround text.\n
        sandybrownbg() is a BackGround Function, if You add ForeGround property given text you can use SandyBrown .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                sandybrownbg("Hello World", Style = 0 ) = it's return sandybrownbg color text without any style       \n
                sandybrownbg("Hello World", Style = 1 ) = it's return sandybrownbg color text with bold text          \n
                sandybrownbg("Hello World", Style = 2 ) = it's return sandybrownbg color text with light text         \n
                sandybrownbg("Hello World", Style = 3 ) = it's return sandybrownbg color text with Italicized style   \n
                sandybrownbg("Hello World", Style = 4 ) = it's return sandybrownbg color text with UnderLine          \n
                sandybrownbg("Hello World", Style = 5 ) = it's return Blinking sandybrownbg color text                \n
        """
        return Colors.back_ground_color(text, style, 244, 164, 96)
                


def beigebg( text : str, style : int = default_style ) -> str :
        """
        It will return the beigebg colored BackGround text.\n
        beigebg() is a BackGround Function, if You add ForeGround property given text you can use beige .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                beigebg("Hello World", Style = 0 ) = it's return beigebg color text without any style       \n
                beigebg("Hello World", Style = 1 ) = it's return beigebg color text with bold text          \n
                beigebg("Hello World", Style = 2 ) = it's return beigebg color text with light text         \n
                beigebg("Hello World", Style = 3 ) = it's return beigebg color text with Italicized style   \n
                beigebg("Hello World", Style = 4 ) = it's return beigebg color text with UnderLine          \n
                beigebg("Hello World", Style = 5 ) = it's return Blinking beigebg color text                \n
        """
        return Colors.back_ground_color(text, style, 245, 245, 220)
                


def brownbg( text : str, style : int = default_style ) -> str :
        """
        It will return the brownbg colored BackGround text.\n
        brownbg() is a BackGround Function, if You add ForeGround property given text you can use brown .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                brownbg("Hello World", Style = 0 ) = it's return brownbg color text without any style       \n
                brownbg("Hello World", Style = 1 ) = it's return brownbg color text with bold text          \n
                brownbg("Hello World", Style = 2 ) = it's return brownbg color text with light text         \n
                brownbg("Hello World", Style = 3 ) = it's return brownbg color text with Italicized style   \n
                brownbg("Hello World", Style = 4 ) = it's return brownbg color text with UnderLine          \n
                brownbg("Hello World", Style = 5 ) = it's return Blinking brownbg color text                \n
        """
        return Colors.back_ground_color(text, style, 166, 42, 42)
                


def brownbg( text : str, style : int = default_style ) -> str :
        """
        It will return the brownbg colored BackGround text.\n
        brownbg() is a BackGround Function, if You add ForeGround property given text you can use brown .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                brownbg("Hello World", Style = 0 ) = it's return brownbg color text without any style       \n
                brownbg("Hello World", Style = 1 ) = it's return brownbg color text with bold text          \n
                brownbg("Hello World", Style = 2 ) = it's return brownbg color text with light text         \n
                brownbg("Hello World", Style = 3 ) = it's return brownbg color text with Italicized style   \n
                brownbg("Hello World", Style = 4 ) = it's return brownbg color text with UnderLine          \n
                brownbg("Hello World", Style = 5 ) = it's return Blinking brownbg color text                \n
        """
        return Colors.back_ground_color(text, style, 166, 42, 42)
                


def brown1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the brown1bg colored BackGround text.\n
        brown1bg() is a BackGround Function, if You add ForeGround property given text you can use brown1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                brown1bg("Hello World", Style = 0 ) = it's return brown1bg color text without any style       \n
                brown1bg("Hello World", Style = 1 ) = it's return brown1bg color text with bold text          \n
                brown1bg("Hello World", Style = 2 ) = it's return brown1bg color text with light text         \n
                brown1bg("Hello World", Style = 3 ) = it's return brown1bg color text with Italicized style   \n
                brown1bg("Hello World", Style = 4 ) = it's return brown1bg color text with UnderLine          \n
                brown1bg("Hello World", Style = 5 ) = it's return Blinking brown1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 64, 64)
                


def brown2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the brown2bg colored BackGround text.\n
        brown2bg() is a BackGround Function, if You add ForeGround property given text you can use brown2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                brown2bg("Hello World", Style = 0 ) = it's return brown2bg color text without any style       \n
                brown2bg("Hello World", Style = 1 ) = it's return brown2bg color text with bold text          \n
                brown2bg("Hello World", Style = 2 ) = it's return brown2bg color text with light text         \n
                brown2bg("Hello World", Style = 3 ) = it's return brown2bg color text with Italicized style   \n
                brown2bg("Hello World", Style = 4 ) = it's return brown2bg color text with UnderLine          \n
                brown2bg("Hello World", Style = 5 ) = it's return Blinking brown2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 59, 59)
                


def brown3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the brown3bg colored BackGround text.\n
        brown3bg() is a BackGround Function, if You add ForeGround property given text you can use brown3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                brown3bg("Hello World", Style = 0 ) = it's return brown3bg color text without any style       \n
                brown3bg("Hello World", Style = 1 ) = it's return brown3bg color text with bold text          \n
                brown3bg("Hello World", Style = 2 ) = it's return brown3bg color text with light text         \n
                brown3bg("Hello World", Style = 3 ) = it's return brown3bg color text with Italicized style   \n
                brown3bg("Hello World", Style = 4 ) = it's return brown3bg color text with UnderLine          \n
                brown3bg("Hello World", Style = 5 ) = it's return Blinking brown3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 51, 51)
                


def brown4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the brown4bg colored BackGround text.\n
        brown4bg() is a BackGround Function, if You add ForeGround property given text you can use brown4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                brown4bg("Hello World", Style = 0 ) = it's return brown4bg color text without any style       \n
                brown4bg("Hello World", Style = 1 ) = it's return brown4bg color text with bold text          \n
                brown4bg("Hello World", Style = 2 ) = it's return brown4bg color text with light text         \n
                brown4bg("Hello World", Style = 3 ) = it's return brown4bg color text with Italicized style   \n
                brown4bg("Hello World", Style = 4 ) = it's return brown4bg color text with UnderLine          \n
                brown4bg("Hello World", Style = 5 ) = it's return Blinking brown4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 35, 35)
                


def dark_brownbg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_brownbg colored BackGround text.\n
        dark_brownbg() is a BackGround Function, if You add ForeGround property given text you can use dark_brown .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_brownbg("Hello World", Style = 0 ) = it's return dark_brownbg color text without any style       \n
                dark_brownbg("Hello World", Style = 1 ) = it's return dark_brownbg color text with bold text          \n
                dark_brownbg("Hello World", Style = 2 ) = it's return dark_brownbg color text with light text         \n
                dark_brownbg("Hello World", Style = 3 ) = it's return dark_brownbg color text with Italicized style   \n
                dark_brownbg("Hello World", Style = 4 ) = it's return dark_brownbg color text with UnderLine          \n
                dark_brownbg("Hello World", Style = 5 ) = it's return Blinking dark_brownbg color text                \n
        """
        return Colors.back_ground_color(text, style, 92, 64, 51)
                


def burlywoodbg( text : str, style : int = default_style ) -> str :
        """
        It will return the burlywoodbg colored BackGround text.\n
        burlywoodbg() is a BackGround Function, if You add ForeGround property given text you can use burlywood .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                burlywoodbg("Hello World", Style = 0 ) = it's return burlywoodbg color text without any style       \n
                burlywoodbg("Hello World", Style = 1 ) = it's return burlywoodbg color text with bold text          \n
                burlywoodbg("Hello World", Style = 2 ) = it's return burlywoodbg color text with light text         \n
                burlywoodbg("Hello World", Style = 3 ) = it's return burlywoodbg color text with Italicized style   \n
                burlywoodbg("Hello World", Style = 4 ) = it's return burlywoodbg color text with UnderLine          \n
                burlywoodbg("Hello World", Style = 5 ) = it's return Blinking burlywoodbg color text                \n
        """
        return Colors.back_ground_color(text, style, 222, 184, 135)
                


def burlywood1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the burlywood1bg colored BackGround text.\n
        burlywood1bg() is a BackGround Function, if You add ForeGround property given text you can use burlywood1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                burlywood1bg("Hello World", Style = 0 ) = it's return burlywood1bg color text without any style       \n
                burlywood1bg("Hello World", Style = 1 ) = it's return burlywood1bg color text with bold text          \n
                burlywood1bg("Hello World", Style = 2 ) = it's return burlywood1bg color text with light text         \n
                burlywood1bg("Hello World", Style = 3 ) = it's return burlywood1bg color text with Italicized style   \n
                burlywood1bg("Hello World", Style = 4 ) = it's return burlywood1bg color text with UnderLine          \n
                burlywood1bg("Hello World", Style = 5 ) = it's return Blinking burlywood1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 211, 155)
                


def burlywood2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the burlywood2bg colored BackGround text.\n
        burlywood2bg() is a BackGround Function, if You add ForeGround property given text you can use burlywood2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                burlywood2bg("Hello World", Style = 0 ) = it's return burlywood2bg color text without any style       \n
                burlywood2bg("Hello World", Style = 1 ) = it's return burlywood2bg color text with bold text          \n
                burlywood2bg("Hello World", Style = 2 ) = it's return burlywood2bg color text with light text         \n
                burlywood2bg("Hello World", Style = 3 ) = it's return burlywood2bg color text with Italicized style   \n
                burlywood2bg("Hello World", Style = 4 ) = it's return burlywood2bg color text with UnderLine          \n
                burlywood2bg("Hello World", Style = 5 ) = it's return Blinking burlywood2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 197, 145)
                


def burlywood3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the burlywood3bg colored BackGround text.\n
        burlywood3bg() is a BackGround Function, if You add ForeGround property given text you can use burlywood3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                burlywood3bg("Hello World", Style = 0 ) = it's return burlywood3bg color text without any style       \n
                burlywood3bg("Hello World", Style = 1 ) = it's return burlywood3bg color text with bold text          \n
                burlywood3bg("Hello World", Style = 2 ) = it's return burlywood3bg color text with light text         \n
                burlywood3bg("Hello World", Style = 3 ) = it's return burlywood3bg color text with Italicized style   \n
                burlywood3bg("Hello World", Style = 4 ) = it's return burlywood3bg color text with UnderLine          \n
                burlywood3bg("Hello World", Style = 5 ) = it's return Blinking burlywood3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 170, 125)
                


def burlywood4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the burlywood4bg colored BackGround text.\n
        burlywood4bg() is a BackGround Function, if You add ForeGround property given text you can use burlywood4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                burlywood4bg("Hello World", Style = 0 ) = it's return burlywood4bg color text without any style       \n
                burlywood4bg("Hello World", Style = 1 ) = it's return burlywood4bg color text with bold text          \n
                burlywood4bg("Hello World", Style = 2 ) = it's return burlywood4bg color text with light text         \n
                burlywood4bg("Hello World", Style = 3 ) = it's return burlywood4bg color text with Italicized style   \n
                burlywood4bg("Hello World", Style = 4 ) = it's return burlywood4bg color text with UnderLine          \n
                burlywood4bg("Hello World", Style = 5 ) = it's return Blinking burlywood4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 115, 85)
                


def baker_chocolatebg( text : str, style : int = default_style ) -> str :
        """
        It will return the baker_chocolatebg colored BackGround text.\n
        baker_chocolatebg() is a BackGround Function, if You add ForeGround property given text you can use baker_chocolate .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                baker_chocolatebg("Hello World", Style = 0 ) = it's return baker_chocolatebg color text without any style       \n
                baker_chocolatebg("Hello World", Style = 1 ) = it's return baker_chocolatebg color text with bold text          \n
                baker_chocolatebg("Hello World", Style = 2 ) = it's return baker_chocolatebg color text with light text         \n
                baker_chocolatebg("Hello World", Style = 3 ) = it's return baker_chocolatebg color text with Italicized style   \n
                baker_chocolatebg("Hello World", Style = 4 ) = it's return baker_chocolatebg color text with UnderLine          \n
                baker_chocolatebg("Hello World", Style = 5 ) = it's return Blinking baker_chocolatebg color text                \n
        """
        return Colors.back_ground_color(text, style, 92, 51, 23)
                


def chocolatebg( text : str, style : int = default_style ) -> str :
        """
        It will return the chocolatebg colored BackGround text.\n
        chocolatebg() is a BackGround Function, if You add ForeGround property given text you can use chocolate .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                chocolatebg("Hello World", Style = 0 ) = it's return chocolatebg color text without any style       \n
                chocolatebg("Hello World", Style = 1 ) = it's return chocolatebg color text with bold text          \n
                chocolatebg("Hello World", Style = 2 ) = it's return chocolatebg color text with light text         \n
                chocolatebg("Hello World", Style = 3 ) = it's return chocolatebg color text with Italicized style   \n
                chocolatebg("Hello World", Style = 4 ) = it's return chocolatebg color text with UnderLine          \n
                chocolatebg("Hello World", Style = 5 ) = it's return Blinking chocolatebg color text                \n
        """
        return Colors.back_ground_color(text, style, 210, 105, 30)
                


def chocolate1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the chocolate1bg colored BackGround text.\n
        chocolate1bg() is a BackGround Function, if You add ForeGround property given text you can use chocolate1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                chocolate1bg("Hello World", Style = 0 ) = it's return chocolate1bg color text without any style       \n
                chocolate1bg("Hello World", Style = 1 ) = it's return chocolate1bg color text with bold text          \n
                chocolate1bg("Hello World", Style = 2 ) = it's return chocolate1bg color text with light text         \n
                chocolate1bg("Hello World", Style = 3 ) = it's return chocolate1bg color text with Italicized style   \n
                chocolate1bg("Hello World", Style = 4 ) = it's return chocolate1bg color text with UnderLine          \n
                chocolate1bg("Hello World", Style = 5 ) = it's return Blinking chocolate1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 127, 36)
                


def chocolate2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the chocolate2bg colored BackGround text.\n
        chocolate2bg() is a BackGround Function, if You add ForeGround property given text you can use chocolate2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                chocolate2bg("Hello World", Style = 0 ) = it's return chocolate2bg color text without any style       \n
                chocolate2bg("Hello World", Style = 1 ) = it's return chocolate2bg color text with bold text          \n
                chocolate2bg("Hello World", Style = 2 ) = it's return chocolate2bg color text with light text         \n
                chocolate2bg("Hello World", Style = 3 ) = it's return chocolate2bg color text with Italicized style   \n
                chocolate2bg("Hello World", Style = 4 ) = it's return chocolate2bg color text with UnderLine          \n
                chocolate2bg("Hello World", Style = 5 ) = it's return Blinking chocolate2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 118, 33)
                


def chocolate3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the chocolate3bg colored BackGround text.\n
        chocolate3bg() is a BackGround Function, if You add ForeGround property given text you can use chocolate3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                chocolate3bg("Hello World", Style = 0 ) = it's return chocolate3bg color text without any style       \n
                chocolate3bg("Hello World", Style = 1 ) = it's return chocolate3bg color text with bold text          \n
                chocolate3bg("Hello World", Style = 2 ) = it's return chocolate3bg color text with light text         \n
                chocolate3bg("Hello World", Style = 3 ) = it's return chocolate3bg color text with Italicized style   \n
                chocolate3bg("Hello World", Style = 4 ) = it's return chocolate3bg color text with UnderLine          \n
                chocolate3bg("Hello World", Style = 5 ) = it's return Blinking chocolate3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 102, 29)
                


def chocolate4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the chocolate4bg colored BackGround text.\n
        chocolate4bg() is a BackGround Function, if You add ForeGround property given text you can use chocolate4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                chocolate4bg("Hello World", Style = 0 ) = it's return chocolate4bg color text without any style       \n
                chocolate4bg("Hello World", Style = 1 ) = it's return chocolate4bg color text with bold text          \n
                chocolate4bg("Hello World", Style = 2 ) = it's return chocolate4bg color text with light text         \n
                chocolate4bg("Hello World", Style = 3 ) = it's return chocolate4bg color text with Italicized style   \n
                chocolate4bg("Hello World", Style = 4 ) = it's return chocolate4bg color text with UnderLine          \n
                chocolate4bg("Hello World", Style = 5 ) = it's return Blinking chocolate4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 69, 19)
                


def perubg( text : str, style : int = default_style ) -> str :
        """
        It will return the perubg colored BackGround text.\n
        perubg() is a BackGround Function, if You add ForeGround property given text you can use peru .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                perubg("Hello World", Style = 0 ) = it's return perubg color text without any style       \n
                perubg("Hello World", Style = 1 ) = it's return perubg color text with bold text          \n
                perubg("Hello World", Style = 2 ) = it's return perubg color text with light text         \n
                perubg("Hello World", Style = 3 ) = it's return perubg color text with Italicized style   \n
                perubg("Hello World", Style = 4 ) = it's return perubg color text with UnderLine          \n
                perubg("Hello World", Style = 5 ) = it's return Blinking perubg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 133, 63)
                


def tanbg( text : str, style : int = default_style ) -> str :
        """
        It will return the tanbg colored BackGround text.\n
        tanbg() is a BackGround Function, if You add ForeGround property given text you can use tan .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tanbg("Hello World", Style = 0 ) = it's return tanbg color text without any style       \n
                tanbg("Hello World", Style = 1 ) = it's return tanbg color text with bold text          \n
                tanbg("Hello World", Style = 2 ) = it's return tanbg color text with light text         \n
                tanbg("Hello World", Style = 3 ) = it's return tanbg color text with Italicized style   \n
                tanbg("Hello World", Style = 4 ) = it's return tanbg color text with UnderLine          \n
                tanbg("Hello World", Style = 5 ) = it's return Blinking tanbg color text                \n
        """
        return Colors.back_ground_color(text, style, 210, 180, 140)
                


def tan1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the tan1bg colored BackGround text.\n
        tan1bg() is a BackGround Function, if You add ForeGround property given text you can use tan1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tan1bg("Hello World", Style = 0 ) = it's return tan1bg color text without any style       \n
                tan1bg("Hello World", Style = 1 ) = it's return tan1bg color text with bold text          \n
                tan1bg("Hello World", Style = 2 ) = it's return tan1bg color text with light text         \n
                tan1bg("Hello World", Style = 3 ) = it's return tan1bg color text with Italicized style   \n
                tan1bg("Hello World", Style = 4 ) = it's return tan1bg color text with UnderLine          \n
                tan1bg("Hello World", Style = 5 ) = it's return Blinking tan1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 165, 79)
                


def tan2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the tan2bg colored BackGround text.\n
        tan2bg() is a BackGround Function, if You add ForeGround property given text you can use tan2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tan2bg("Hello World", Style = 0 ) = it's return tan2bg color text without any style       \n
                tan2bg("Hello World", Style = 1 ) = it's return tan2bg color text with bold text          \n
                tan2bg("Hello World", Style = 2 ) = it's return tan2bg color text with light text         \n
                tan2bg("Hello World", Style = 3 ) = it's return tan2bg color text with Italicized style   \n
                tan2bg("Hello World", Style = 4 ) = it's return tan2bg color text with UnderLine          \n
                tan2bg("Hello World", Style = 5 ) = it's return Blinking tan2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 154, 73)
                


def tan3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the tan3bg colored BackGround text.\n
        tan3bg() is a BackGround Function, if You add ForeGround property given text you can use tan3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tan3bg("Hello World", Style = 0 ) = it's return tan3bg color text without any style       \n
                tan3bg("Hello World", Style = 1 ) = it's return tan3bg color text with bold text          \n
                tan3bg("Hello World", Style = 2 ) = it's return tan3bg color text with light text         \n
                tan3bg("Hello World", Style = 3 ) = it's return tan3bg color text with Italicized style   \n
                tan3bg("Hello World", Style = 4 ) = it's return tan3bg color text with UnderLine          \n
                tan3bg("Hello World", Style = 5 ) = it's return Blinking tan3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 133, 63)
                


def tan4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the tan4bg colored BackGround text.\n
        tan4bg() is a BackGround Function, if You add ForeGround property given text you can use tan4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tan4bg("Hello World", Style = 0 ) = it's return tan4bg color text without any style       \n
                tan4bg("Hello World", Style = 1 ) = it's return tan4bg color text with bold text          \n
                tan4bg("Hello World", Style = 2 ) = it's return tan4bg color text with light text         \n
                tan4bg("Hello World", Style = 3 ) = it's return tan4bg color text with Italicized style   \n
                tan4bg("Hello World", Style = 4 ) = it's return tan4bg color text with UnderLine          \n
                tan4bg("Hello World", Style = 5 ) = it's return Blinking tan4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 90, 43)
                


def dark_tanbg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_tanbg colored BackGround text.\n
        dark_tanbg() is a BackGround Function, if You add ForeGround property given text you can use Dark_Tan .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_tanbg("Hello World", Style = 0 ) = it's return dark_tanbg color text without any style       \n
                dark_tanbg("Hello World", Style = 1 ) = it's return dark_tanbg color text with bold text          \n
                dark_tanbg("Hello World", Style = 2 ) = it's return dark_tanbg color text with light text         \n
                dark_tanbg("Hello World", Style = 3 ) = it's return dark_tanbg color text with Italicized style   \n
                dark_tanbg("Hello World", Style = 4 ) = it's return dark_tanbg color text with UnderLine          \n
                dark_tanbg("Hello World", Style = 5 ) = it's return Blinking dark_tanbg color text                \n
        """
        return Colors.back_ground_color(text, style, 151, 105, 79)
                


def dark_woodbg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_woodbg colored BackGround text.\n
        dark_woodbg() is a BackGround Function, if You add ForeGround property given text you can use Dark_Wood .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_woodbg("Hello World", Style = 0 ) = it's return dark_woodbg color text without any style       \n
                dark_woodbg("Hello World", Style = 1 ) = it's return dark_woodbg color text with bold text          \n
                dark_woodbg("Hello World", Style = 2 ) = it's return dark_woodbg color text with light text         \n
                dark_woodbg("Hello World", Style = 3 ) = it's return dark_woodbg color text with Italicized style   \n
                dark_woodbg("Hello World", Style = 4 ) = it's return dark_woodbg color text with UnderLine          \n
                dark_woodbg("Hello World", Style = 5 ) = it's return Blinking dark_woodbg color text                \n
        """
        return Colors.back_ground_color(text, style, 133, 94, 66)
                


def light_woodbg( text : str, style : int = default_style ) -> str :
        """
        It will return the light_woodbg colored BackGround text.\n
        light_woodbg() is a BackGround Function, if You add ForeGround property given text you can use Light_Wood .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                light_woodbg("Hello World", Style = 0 ) = it's return light_woodbg color text without any style       \n
                light_woodbg("Hello World", Style = 1 ) = it's return light_woodbg color text with bold text          \n
                light_woodbg("Hello World", Style = 2 ) = it's return light_woodbg color text with light text         \n
                light_woodbg("Hello World", Style = 3 ) = it's return light_woodbg color text with Italicized style   \n
                light_woodbg("Hello World", Style = 4 ) = it's return light_woodbg color text with UnderLine          \n
                light_woodbg("Hello World", Style = 5 ) = it's return Blinking light_woodbg color text                \n
        """
        return Colors.back_ground_color(text, style, 133, 99, 99)
                


def medium_woodbg( text : str, style : int = default_style ) -> str :
        """
        It will return the medium_woodbg colored BackGround text.\n
        medium_woodbg() is a BackGround Function, if You add ForeGround property given text you can use Medium_Wood .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                medium_woodbg("Hello World", Style = 0 ) = it's return medium_woodbg color text without any style       \n
                medium_woodbg("Hello World", Style = 1 ) = it's return medium_woodbg color text with bold text          \n
                medium_woodbg("Hello World", Style = 2 ) = it's return medium_woodbg color text with light text         \n
                medium_woodbg("Hello World", Style = 3 ) = it's return medium_woodbg color text with Italicized style   \n
                medium_woodbg("Hello World", Style = 4 ) = it's return medium_woodbg color text with UnderLine          \n
                medium_woodbg("Hello World", Style = 5 ) = it's return Blinking medium_woodbg color text                \n
        """
        return Colors.back_ground_color(text, style, 166, 128, 100)
                


def new_tanbg( text : str, style : int = default_style ) -> str :
        """
        It will return the new_tanbg colored BackGround text.\n
        new_tanbg() is a BackGround Function, if You add ForeGround property given text you can use New_Tan .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                new_tanbg("Hello World", Style = 0 ) = it's return new_tanbg color text without any style       \n
                new_tanbg("Hello World", Style = 1 ) = it's return new_tanbg color text with bold text          \n
                new_tanbg("Hello World", Style = 2 ) = it's return new_tanbg color text with light text         \n
                new_tanbg("Hello World", Style = 3 ) = it's return new_tanbg color text with Italicized style   \n
                new_tanbg("Hello World", Style = 4 ) = it's return new_tanbg color text with UnderLine          \n
                new_tanbg("Hello World", Style = 5 ) = it's return Blinking new_tanbg color text                \n
        """
        return Colors.back_ground_color(text, style, 235, 199, 158)
                


def semi_sweet_chocolatebg( text : str, style : int = default_style ) -> str :
        """
        It will return the semi_sweet_chocolatebg colored BackGround text.\n
        semi_sweet_chocolatebg() is a BackGround Function, if You add ForeGround property given text you can use Semi_Sweet_Chocolate .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                semi_sweet_chocolatebg("Hello World", Style = 0 ) = it's return semi_sweet_chocolatebg color text without any style       \n
                semi_sweet_chocolatebg("Hello World", Style = 1 ) = it's return semi_sweet_chocolatebg color text with bold text          \n
                semi_sweet_chocolatebg("Hello World", Style = 2 ) = it's return semi_sweet_chocolatebg color text with light text         \n
                semi_sweet_chocolatebg("Hello World", Style = 3 ) = it's return semi_sweet_chocolatebg color text with Italicized style   \n
                semi_sweet_chocolatebg("Hello World", Style = 4 ) = it's return semi_sweet_chocolatebg color text with UnderLine          \n
                semi_sweet_chocolatebg("Hello World", Style = 5 ) = it's return Blinking semi_sweet_chocolatebg color text                \n
        """
        return Colors.back_ground_color(text, style, 107, 66, 38)
                


def siennabg( text : str, style : int = default_style ) -> str :
        """
        It will return the siennabg colored BackGround text.\n
        siennabg() is a BackGround Function, if You add ForeGround property given text you can use Sienna .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                siennabg("Hello World", Style = 0 ) = it's return siennabg color text without any style       \n
                siennabg("Hello World", Style = 1 ) = it's return siennabg color text with bold text          \n
                siennabg("Hello World", Style = 2 ) = it's return siennabg color text with light text         \n
                siennabg("Hello World", Style = 3 ) = it's return siennabg color text with Italicized style   \n
                siennabg("Hello World", Style = 4 ) = it's return siennabg color text with UnderLine          \n
                siennabg("Hello World", Style = 5 ) = it's return Blinking siennabg color text                \n
        """
        return Colors.back_ground_color(text, style, 142, 107, 35)
                


def tanbg( text : str, style : int = default_style ) -> str :
        """
        It will return the tanbg colored BackGround text.\n
        tanbg() is a BackGround Function, if You add ForeGround property given text you can use Tan .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tanbg("Hello World", Style = 0 ) = it's return tanbg color text without any style       \n
                tanbg("Hello World", Style = 1 ) = it's return tanbg color text with bold text          \n
                tanbg("Hello World", Style = 2 ) = it's return tanbg color text with light text         \n
                tanbg("Hello World", Style = 3 ) = it's return tanbg color text with Italicized style   \n
                tanbg("Hello World", Style = 4 ) = it's return tanbg color text with UnderLine          \n
                tanbg("Hello World", Style = 5 ) = it's return Blinking tanbg color text                \n
        """
        return Colors.back_ground_color(text, style, 219, 147, 112)
                


def very_dark_brownbg( text : str, style : int = default_style ) -> str :
        """
        It will return the very_dark_brownbg colored BackGround text.\n
        very_dark_brownbg() is a BackGround Function, if You add ForeGround property given text you can use Very_Dark_Brown .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                very_dark_brownbg("Hello World", Style = 0 ) = it's return very_dark_brownbg color text without any style       \n
                very_dark_brownbg("Hello World", Style = 1 ) = it's return very_dark_brownbg color text with bold text          \n
                very_dark_brownbg("Hello World", Style = 2 ) = it's return very_dark_brownbg color text with light text         \n
                very_dark_brownbg("Hello World", Style = 3 ) = it's return very_dark_brownbg color text with Italicized style   \n
                very_dark_brownbg("Hello World", Style = 4 ) = it's return very_dark_brownbg color text with UnderLine          \n
                very_dark_brownbg("Hello World", Style = 5 ) = it's return Blinking very_dark_brownbg color text                \n
        """
        return Colors.back_ground_color(text, style, 92, 64, 51)
                


def dark_greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_greenbg colored BackGround text.\n
        dark_greenbg() is a BackGround Function, if You add ForeGround property given text you can use Dark_Green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_greenbg("Hello World", Style = 0 ) = it's return dark_greenbg color text without any style       \n
                dark_greenbg("Hello World", Style = 1 ) = it's return dark_greenbg color text with bold text          \n
                dark_greenbg("Hello World", Style = 2 ) = it's return dark_greenbg color text with light text         \n
                dark_greenbg("Hello World", Style = 3 ) = it's return dark_greenbg color text with Italicized style   \n
                dark_greenbg("Hello World", Style = 4 ) = it's return dark_greenbg color text with UnderLine          \n
                dark_greenbg("Hello World", Style = 5 ) = it's return Blinking dark_greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 47, 79, 47)
                


def darkgreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkgreenbg colored BackGround text.\n
        darkgreenbg() is a BackGround Function, if You add ForeGround property given text you can use DarkGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkgreenbg("Hello World", Style = 0 ) = it's return darkgreenbg color text without any style       \n
                darkgreenbg("Hello World", Style = 1 ) = it's return darkgreenbg color text with bold text          \n
                darkgreenbg("Hello World", Style = 2 ) = it's return darkgreenbg color text with light text         \n
                darkgreenbg("Hello World", Style = 3 ) = it's return darkgreenbg color text with Italicized style   \n
                darkgreenbg("Hello World", Style = 4 ) = it's return darkgreenbg color text with UnderLine          \n
                darkgreenbg("Hello World", Style = 5 ) = it's return Blinking darkgreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 100, 0)
                


def dark_green_copperbg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_green_copperbg colored BackGround text.\n
        dark_green_copperbg() is a BackGround Function, if You add ForeGround property given text you can use dark_green_copper .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_green_copperbg("Hello World", Style = 0 ) = it's return dark_green_copperbg color text without any style       \n
                dark_green_copperbg("Hello World", Style = 1 ) = it's return dark_green_copperbg color text with bold text          \n
                dark_green_copperbg("Hello World", Style = 2 ) = it's return dark_green_copperbg color text with light text         \n
                dark_green_copperbg("Hello World", Style = 3 ) = it's return dark_green_copperbg color text with Italicized style   \n
                dark_green_copperbg("Hello World", Style = 4 ) = it's return dark_green_copperbg color text with UnderLine          \n
                dark_green_copperbg("Hello World", Style = 5 ) = it's return Blinking dark_green_copperbg color text                \n
        """
        return Colors.back_ground_color(text, style, 74, 118, 110)
                


def darkkhakibg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkkhakibg colored BackGround text.\n
        darkkhakibg() is a BackGround Function, if You add ForeGround property given text you can use DarkKhaki .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkkhakibg("Hello World", Style = 0 ) = it's return darkkhakibg color text without any style       \n
                darkkhakibg("Hello World", Style = 1 ) = it's return darkkhakibg color text with bold text          \n
                darkkhakibg("Hello World", Style = 2 ) = it's return darkkhakibg color text with light text         \n
                darkkhakibg("Hello World", Style = 3 ) = it's return darkkhakibg color text with Italicized style   \n
                darkkhakibg("Hello World", Style = 4 ) = it's return darkkhakibg color text with UnderLine          \n
                darkkhakibg("Hello World", Style = 5 ) = it's return Blinking darkkhakibg color text                \n
        """
        return Colors.back_ground_color(text, style, 189, 183, 107)
                


def darkolivegreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkolivegreenbg colored BackGround text.\n
        darkolivegreenbg() is a BackGround Function, if You add ForeGround property given text you can use DarkOliveGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkolivegreenbg("Hello World", Style = 0 ) = it's return darkolivegreenbg color text without any style       \n
                darkolivegreenbg("Hello World", Style = 1 ) = it's return darkolivegreenbg color text with bold text          \n
                darkolivegreenbg("Hello World", Style = 2 ) = it's return darkolivegreenbg color text with light text         \n
                darkolivegreenbg("Hello World", Style = 3 ) = it's return darkolivegreenbg color text with Italicized style   \n
                darkolivegreenbg("Hello World", Style = 4 ) = it's return darkolivegreenbg color text with UnderLine          \n
                darkolivegreenbg("Hello World", Style = 5 ) = it's return Blinking darkolivegreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 85, 107, 47)
                


def darkolivegreen1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkolivegreen1bg colored BackGround text.\n
        darkolivegreen1bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOliveGreen1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkolivegreen1bg("Hello World", Style = 0 ) = it's return darkolivegreen1bg color text without any style       \n
                darkolivegreen1bg("Hello World", Style = 1 ) = it's return darkolivegreen1bg color text with bold text          \n
                darkolivegreen1bg("Hello World", Style = 2 ) = it's return darkolivegreen1bg color text with light text         \n
                darkolivegreen1bg("Hello World", Style = 3 ) = it's return darkolivegreen1bg color text with Italicized style   \n
                darkolivegreen1bg("Hello World", Style = 4 ) = it's return darkolivegreen1bg color text with UnderLine          \n
                darkolivegreen1bg("Hello World", Style = 5 ) = it's return Blinking darkolivegreen1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 202, 255, 112)
                


def darkolivegreen2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkolivegreen2bg colored BackGround text.\n
        darkolivegreen2bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOliveGreen2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkolivegreen2bg("Hello World", Style = 0 ) = it's return darkolivegreen2bg color text without any style       \n
                darkolivegreen2bg("Hello World", Style = 1 ) = it's return darkolivegreen2bg color text with bold text          \n
                darkolivegreen2bg("Hello World", Style = 2 ) = it's return darkolivegreen2bg color text with light text         \n
                darkolivegreen2bg("Hello World", Style = 3 ) = it's return darkolivegreen2bg color text with Italicized style   \n
                darkolivegreen2bg("Hello World", Style = 4 ) = it's return darkolivegreen2bg color text with UnderLine          \n
                darkolivegreen2bg("Hello World", Style = 5 ) = it's return Blinking darkolivegreen2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 188, 238, 104)
                


def darkolivegreen3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkolivegreen3bg colored BackGround text.\n
        darkolivegreen3bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOliveGreen3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkolivegreen3bg("Hello World", Style = 0 ) = it's return darkolivegreen3bg color text without any style       \n
                darkolivegreen3bg("Hello World", Style = 1 ) = it's return darkolivegreen3bg color text with bold text          \n
                darkolivegreen3bg("Hello World", Style = 2 ) = it's return darkolivegreen3bg color text with light text         \n
                darkolivegreen3bg("Hello World", Style = 3 ) = it's return darkolivegreen3bg color text with Italicized style   \n
                darkolivegreen3bg("Hello World", Style = 4 ) = it's return darkolivegreen3bg color text with UnderLine          \n
                darkolivegreen3bg("Hello World", Style = 5 ) = it's return Blinking darkolivegreen3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 162, 205, 90)
                


def darkolivegreen4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkolivegreen4bg colored BackGround text.\n
        darkolivegreen4bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOliveGreen4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkolivegreen4bg("Hello World", Style = 0 ) = it's return darkolivegreen4bg color text without any style       \n
                darkolivegreen4bg("Hello World", Style = 1 ) = it's return darkolivegreen4bg color text with bold text          \n
                darkolivegreen4bg("Hello World", Style = 2 ) = it's return darkolivegreen4bg color text with light text         \n
                darkolivegreen4bg("Hello World", Style = 3 ) = it's return darkolivegreen4bg color text with Italicized style   \n
                darkolivegreen4bg("Hello World", Style = 4 ) = it's return darkolivegreen4bg color text with UnderLine          \n
                darkolivegreen4bg("Hello World", Style = 5 ) = it's return Blinking darkolivegreen4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 110, 139, 61)
                


def olivebg( text : str, style : int = default_style ) -> str :
        """
        It will return the olivebg colored BackGround text.\n
        olivebg() is a BackGround Function, if You add ForeGround property given text you can use olive .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                olivebg("Hello World", Style = 0 ) = it's return olivebg color text without any style       \n
                olivebg("Hello World", Style = 1 ) = it's return olivebg color text with bold text          \n
                olivebg("Hello World", Style = 2 ) = it's return olivebg color text with light text         \n
                olivebg("Hello World", Style = 3 ) = it's return olivebg color text with Italicized style   \n
                olivebg("Hello World", Style = 4 ) = it's return olivebg color text with UnderLine          \n
                olivebg("Hello World", Style = 5 ) = it's return Blinking olivebg color text                \n
        """
        return Colors.back_ground_color(text, style, 128, 128, 0)
                


def darkseagreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkseagreenbg colored BackGround text.\n
        darkseagreenbg() is a BackGround Function, if You add ForeGround property given text you can use DarkSeaGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkseagreenbg("Hello World", Style = 0 ) = it's return darkseagreenbg color text without any style       \n
                darkseagreenbg("Hello World", Style = 1 ) = it's return darkseagreenbg color text with bold text          \n
                darkseagreenbg("Hello World", Style = 2 ) = it's return darkseagreenbg color text with light text         \n
                darkseagreenbg("Hello World", Style = 3 ) = it's return darkseagreenbg color text with Italicized style   \n
                darkseagreenbg("Hello World", Style = 4 ) = it's return darkseagreenbg color text with UnderLine          \n
                darkseagreenbg("Hello World", Style = 5 ) = it's return Blinking darkseagreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 143, 188, 143)
                


def darkseagreen1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkseagreen1bg colored BackGround text.\n
        darkseagreen1bg() is a BackGround Function, if You add ForeGround property given text you can use DarkSeaGreen1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkseagreen1bg("Hello World", Style = 0 ) = it's return darkseagreen1bg color text without any style       \n
                darkseagreen1bg("Hello World", Style = 1 ) = it's return darkseagreen1bg color text with bold text          \n
                darkseagreen1bg("Hello World", Style = 2 ) = it's return darkseagreen1bg color text with light text         \n
                darkseagreen1bg("Hello World", Style = 3 ) = it's return darkseagreen1bg color text with Italicized style   \n
                darkseagreen1bg("Hello World", Style = 4 ) = it's return darkseagreen1bg color text with UnderLine          \n
                darkseagreen1bg("Hello World", Style = 5 ) = it's return Blinking darkseagreen1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 193, 255, 193)
                


def darkseagreen2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkseagreen2bg colored BackGround text.\n
        darkseagreen2bg() is a BackGround Function, if You add ForeGround property given text you can use DarkSeaGreen2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkseagreen2bg("Hello World", Style = 0 ) = it's return darkseagreen2bg color text without any style       \n
                darkseagreen2bg("Hello World", Style = 1 ) = it's return darkseagreen2bg color text with bold text          \n
                darkseagreen2bg("Hello World", Style = 2 ) = it's return darkseagreen2bg color text with light text         \n
                darkseagreen2bg("Hello World", Style = 3 ) = it's return darkseagreen2bg color text with Italicized style   \n
                darkseagreen2bg("Hello World", Style = 4 ) = it's return darkseagreen2bg color text with UnderLine          \n
                darkseagreen2bg("Hello World", Style = 5 ) = it's return Blinking darkseagreen2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 180, 238, 180)
                


def darkseagreen3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkseagreen3bg colored BackGround text.\n
        darkseagreen3bg() is a BackGround Function, if You add ForeGround property given text you can use DarkSeaGreen3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkseagreen3bg("Hello World", Style = 0 ) = it's return darkseagreen3bg color text without any style       \n
                darkseagreen3bg("Hello World", Style = 1 ) = it's return darkseagreen3bg color text with bold text          \n
                darkseagreen3bg("Hello World", Style = 2 ) = it's return darkseagreen3bg color text with light text         \n
                darkseagreen3bg("Hello World", Style = 3 ) = it's return darkseagreen3bg color text with Italicized style   \n
                darkseagreen3bg("Hello World", Style = 4 ) = it's return darkseagreen3bg color text with UnderLine          \n
                darkseagreen3bg("Hello World", Style = 5 ) = it's return Blinking darkseagreen3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 155, 205, 155)
                


def darkseagreen4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkseagreen4bg colored BackGround text.\n
        darkseagreen4bg() is a BackGround Function, if You add ForeGround property given text you can use DarkSeaGreen4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkseagreen4bg("Hello World", Style = 0 ) = it's return darkseagreen4bg color text without any style       \n
                darkseagreen4bg("Hello World", Style = 1 ) = it's return darkseagreen4bg color text with bold text          \n
                darkseagreen4bg("Hello World", Style = 2 ) = it's return darkseagreen4bg color text with light text         \n
                darkseagreen4bg("Hello World", Style = 3 ) = it's return darkseagreen4bg color text with Italicized style   \n
                darkseagreen4bg("Hello World", Style = 4 ) = it's return darkseagreen4bg color text with UnderLine          \n
                darkseagreen4bg("Hello World", Style = 5 ) = it's return Blinking darkseagreen4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 105, 139, 105)
                


def forestgreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the forestgreenbg colored BackGround text.\n
        forestgreenbg() is a BackGround Function, if You add ForeGround property given text you can use ForestGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                forestgreenbg("Hello World", Style = 0 ) = it's return forestgreenbg color text without any style       \n
                forestgreenbg("Hello World", Style = 1 ) = it's return forestgreenbg color text with bold text          \n
                forestgreenbg("Hello World", Style = 2 ) = it's return forestgreenbg color text with light text         \n
                forestgreenbg("Hello World", Style = 3 ) = it's return forestgreenbg color text with Italicized style   \n
                forestgreenbg("Hello World", Style = 4 ) = it's return forestgreenbg color text with UnderLine          \n
                forestgreenbg("Hello World", Style = 5 ) = it's return Blinking forestgreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 34, 139, 34)
                


def greenyellowbg( text : str, style : int = default_style ) -> str :
        """
        It will return the greenyellowbg colored BackGround text.\n
        greenyellowbg() is a BackGround Function, if You add ForeGround property given text you can use GreenYellow .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                greenyellowbg("Hello World", Style = 0 ) = it's return greenyellowbg color text without any style       \n
                greenyellowbg("Hello World", Style = 1 ) = it's return greenyellowbg color text with bold text          \n
                greenyellowbg("Hello World", Style = 2 ) = it's return greenyellowbg color text with light text         \n
                greenyellowbg("Hello World", Style = 3 ) = it's return greenyellowbg color text with Italicized style   \n
                greenyellowbg("Hello World", Style = 4 ) = it's return greenyellowbg color text with UnderLine          \n
                greenyellowbg("Hello World", Style = 5 ) = it's return Blinking greenyellowbg color text                \n
        """
        return Colors.back_ground_color(text, style, 173, 255, 47)
                


def lawngreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lawngreenbg colored BackGround text.\n
        lawngreenbg() is a BackGround Function, if You add ForeGround property given text you can use LawnGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lawngreenbg("Hello World", Style = 0 ) = it's return lawngreenbg color text without any style       \n
                lawngreenbg("Hello World", Style = 1 ) = it's return lawngreenbg color text with bold text          \n
                lawngreenbg("Hello World", Style = 2 ) = it's return lawngreenbg color text with light text         \n
                lawngreenbg("Hello World", Style = 3 ) = it's return lawngreenbg color text with Italicized style   \n
                lawngreenbg("Hello World", Style = 4 ) = it's return lawngreenbg color text with UnderLine          \n
                lawngreenbg("Hello World", Style = 5 ) = it's return Blinking lawngreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 124, 252, 0)
                


def lightseagreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightseagreenbg colored BackGround text.\n
        lightseagreenbg() is a BackGround Function, if You add ForeGround property given text you can use LightSeaGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightseagreenbg("Hello World", Style = 0 ) = it's return lightseagreenbg color text without any style       \n
                lightseagreenbg("Hello World", Style = 1 ) = it's return lightseagreenbg color text with bold text          \n
                lightseagreenbg("Hello World", Style = 2 ) = it's return lightseagreenbg color text with light text         \n
                lightseagreenbg("Hello World", Style = 3 ) = it's return lightseagreenbg color text with Italicized style   \n
                lightseagreenbg("Hello World", Style = 4 ) = it's return lightseagreenbg color text with UnderLine          \n
                lightseagreenbg("Hello World", Style = 5 ) = it's return Blinking lightseagreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 32, 178, 170)
                


def limegreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the limegreenbg colored BackGround text.\n
        limegreenbg() is a BackGround Function, if You add ForeGround property given text you can use LimeGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                limegreenbg("Hello World", Style = 0 ) = it's return limegreenbg color text without any style       \n
                limegreenbg("Hello World", Style = 1 ) = it's return limegreenbg color text with bold text          \n
                limegreenbg("Hello World", Style = 2 ) = it's return limegreenbg color text with light text         \n
                limegreenbg("Hello World", Style = 3 ) = it's return limegreenbg color text with Italicized style   \n
                limegreenbg("Hello World", Style = 4 ) = it's return limegreenbg color text with UnderLine          \n
                limegreenbg("Hello World", Style = 5 ) = it's return Blinking limegreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 50, 205, 50)
                


def mediumseagreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumseagreenbg colored BackGround text.\n
        mediumseagreenbg() is a BackGround Function, if You add ForeGround property given text you can use MediumSeaGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumseagreenbg("Hello World", Style = 0 ) = it's return mediumseagreenbg color text without any style       \n
                mediumseagreenbg("Hello World", Style = 1 ) = it's return mediumseagreenbg color text with bold text          \n
                mediumseagreenbg("Hello World", Style = 2 ) = it's return mediumseagreenbg color text with light text         \n
                mediumseagreenbg("Hello World", Style = 3 ) = it's return mediumseagreenbg color text with Italicized style   \n
                mediumseagreenbg("Hello World", Style = 4 ) = it's return mediumseagreenbg color text with UnderLine          \n
                mediumseagreenbg("Hello World", Style = 5 ) = it's return Blinking mediumseagreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 60, 179, 113)
                


def mediumspringgreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumspringgreenbg colored BackGround text.\n
        mediumspringgreenbg() is a BackGround Function, if You add ForeGround property given text you can use MediumSpringGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumspringgreenbg("Hello World", Style = 0 ) = it's return mediumspringgreenbg color text without any style       \n
                mediumspringgreenbg("Hello World", Style = 1 ) = it's return mediumspringgreenbg color text with bold text          \n
                mediumspringgreenbg("Hello World", Style = 2 ) = it's return mediumspringgreenbg color text with light text         \n
                mediumspringgreenbg("Hello World", Style = 3 ) = it's return mediumspringgreenbg color text with Italicized style   \n
                mediumspringgreenbg("Hello World", Style = 4 ) = it's return mediumspringgreenbg color text with UnderLine          \n
                mediumspringgreenbg("Hello World", Style = 5 ) = it's return Blinking mediumspringgreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 250, 154)
                


def mintcreambg( text : str, style : int = default_style ) -> str :
        """
        It will return the mintcreambg colored BackGround text.\n
        mintcreambg() is a BackGround Function, if You add ForeGround property given text you can use MintCream .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mintcreambg("Hello World", Style = 0 ) = it's return mintcreambg color text without any style       \n
                mintcreambg("Hello World", Style = 1 ) = it's return mintcreambg color text with bold text          \n
                mintcreambg("Hello World", Style = 2 ) = it's return mintcreambg color text with light text         \n
                mintcreambg("Hello World", Style = 3 ) = it's return mintcreambg color text with Italicized style   \n
                mintcreambg("Hello World", Style = 4 ) = it's return mintcreambg color text with UnderLine          \n
                mintcreambg("Hello World", Style = 5 ) = it's return Blinking mintcreambg color text                \n
        """
        return Colors.back_ground_color(text, style, 245, 255, 250)
                


def olivedrabbg( text : str, style : int = default_style ) -> str :
        """
        It will return the olivedrabbg colored BackGround text.\n
        olivedrabbg() is a BackGround Function, if You add ForeGround property given text you can use OliveDrab .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                olivedrabbg("Hello World", Style = 0 ) = it's return olivedrabbg color text without any style       \n
                olivedrabbg("Hello World", Style = 1 ) = it's return olivedrabbg color text with bold text          \n
                olivedrabbg("Hello World", Style = 2 ) = it's return olivedrabbg color text with light text         \n
                olivedrabbg("Hello World", Style = 3 ) = it's return olivedrabbg color text with Italicized style   \n
                olivedrabbg("Hello World", Style = 4 ) = it's return olivedrabbg color text with UnderLine          \n
                olivedrabbg("Hello World", Style = 5 ) = it's return Blinking olivedrabbg color text                \n
        """
        return Colors.back_ground_color(text, style, 107, 142, 35)
                


def olivedrab1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the olivedrab1bg colored BackGround text.\n
        olivedrab1bg() is a BackGround Function, if You add ForeGround property given text you can use OliveDrab1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                olivedrab1bg("Hello World", Style = 0 ) = it's return olivedrab1bg color text without any style       \n
                olivedrab1bg("Hello World", Style = 1 ) = it's return olivedrab1bg color text with bold text          \n
                olivedrab1bg("Hello World", Style = 2 ) = it's return olivedrab1bg color text with light text         \n
                olivedrab1bg("Hello World", Style = 3 ) = it's return olivedrab1bg color text with Italicized style   \n
                olivedrab1bg("Hello World", Style = 4 ) = it's return olivedrab1bg color text with UnderLine          \n
                olivedrab1bg("Hello World", Style = 5 ) = it's return Blinking olivedrab1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 192, 255, 62)
                


def olivedrab2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the olivedrab2bg colored BackGround text.\n
        olivedrab2bg() is a BackGround Function, if You add ForeGround property given text you can use OliveDrab2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                olivedrab2bg("Hello World", Style = 0 ) = it's return olivedrab2bg color text without any style       \n
                olivedrab2bg("Hello World", Style = 1 ) = it's return olivedrab2bg color text with bold text          \n
                olivedrab2bg("Hello World", Style = 2 ) = it's return olivedrab2bg color text with light text         \n
                olivedrab2bg("Hello World", Style = 3 ) = it's return olivedrab2bg color text with Italicized style   \n
                olivedrab2bg("Hello World", Style = 4 ) = it's return olivedrab2bg color text with UnderLine          \n
                olivedrab2bg("Hello World", Style = 5 ) = it's return Blinking olivedrab2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 179, 238, 58)
                


def olivedrab3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the olivedrab3bg colored BackGround text.\n
        olivedrab3bg() is a BackGround Function, if You add ForeGround property given text you can use OliveDrab3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                olivedrab3bg("Hello World", Style = 0 ) = it's return olivedrab3bg color text without any style       \n
                olivedrab3bg("Hello World", Style = 1 ) = it's return olivedrab3bg color text with bold text          \n
                olivedrab3bg("Hello World", Style = 2 ) = it's return olivedrab3bg color text with light text         \n
                olivedrab3bg("Hello World", Style = 3 ) = it's return olivedrab3bg color text with Italicized style   \n
                olivedrab3bg("Hello World", Style = 4 ) = it's return olivedrab3bg color text with UnderLine          \n
                olivedrab3bg("Hello World", Style = 5 ) = it's return Blinking olivedrab3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 154, 205, 50)
                


def olivedrab4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the olivedrab4bg colored BackGround text.\n
        olivedrab4bg() is a BackGround Function, if You add ForeGround property given text you can use OliveDrab4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                olivedrab4bg("Hello World", Style = 0 ) = it's return olivedrab4bg color text without any style       \n
                olivedrab4bg("Hello World", Style = 1 ) = it's return olivedrab4bg color text with bold text          \n
                olivedrab4bg("Hello World", Style = 2 ) = it's return olivedrab4bg color text with light text         \n
                olivedrab4bg("Hello World", Style = 3 ) = it's return olivedrab4bg color text with Italicized style   \n
                olivedrab4bg("Hello World", Style = 4 ) = it's return olivedrab4bg color text with UnderLine          \n
                olivedrab4bg("Hello World", Style = 5 ) = it's return Blinking olivedrab4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 105, 139, 34)
                


def palegreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the palegreenbg colored BackGround text.\n
        palegreenbg() is a BackGround Function, if You add ForeGround property given text you can use PaleGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palegreenbg("Hello World", Style = 0 ) = it's return palegreenbg color text without any style       \n
                palegreenbg("Hello World", Style = 1 ) = it's return palegreenbg color text with bold text          \n
                palegreenbg("Hello World", Style = 2 ) = it's return palegreenbg color text with light text         \n
                palegreenbg("Hello World", Style = 3 ) = it's return palegreenbg color text with Italicized style   \n
                palegreenbg("Hello World", Style = 4 ) = it's return palegreenbg color text with UnderLine          \n
                palegreenbg("Hello World", Style = 5 ) = it's return Blinking palegreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 152, 251, 152)
                


def palegreen1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the palegreen1bg colored BackGround text.\n
        palegreen1bg() is a BackGround Function, if You add ForeGround property given text you can use PaleGreen1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palegreen1bg("Hello World", Style = 0 ) = it's return palegreen1bg color text without any style       \n
                palegreen1bg("Hello World", Style = 1 ) = it's return palegreen1bg color text with bold text          \n
                palegreen1bg("Hello World", Style = 2 ) = it's return palegreen1bg color text with light text         \n
                palegreen1bg("Hello World", Style = 3 ) = it's return palegreen1bg color text with Italicized style   \n
                palegreen1bg("Hello World", Style = 4 ) = it's return palegreen1bg color text with UnderLine          \n
                palegreen1bg("Hello World", Style = 5 ) = it's return Blinking palegreen1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 154, 255, 154)
                


def palegreen2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the palegreen2bg colored BackGround text.\n
        palegreen2bg() is a BackGround Function, if You add ForeGround property given text you can use PaleGreen2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palegreen2bg("Hello World", Style = 0 ) = it's return palegreen2bg color text without any style       \n
                palegreen2bg("Hello World", Style = 1 ) = it's return palegreen2bg color text with bold text          \n
                palegreen2bg("Hello World", Style = 2 ) = it's return palegreen2bg color text with light text         \n
                palegreen2bg("Hello World", Style = 3 ) = it's return palegreen2bg color text with Italicized style   \n
                palegreen2bg("Hello World", Style = 4 ) = it's return palegreen2bg color text with UnderLine          \n
                palegreen2bg("Hello World", Style = 5 ) = it's return Blinking palegreen2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 144, 238, 144)
                


def palegreen3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the palegreen3bg colored BackGround text.\n
        palegreen3bg() is a BackGround Function, if You add ForeGround property given text you can use PaleGreen3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palegreen3bg("Hello World", Style = 0 ) = it's return palegreen3bg color text without any style       \n
                palegreen3bg("Hello World", Style = 1 ) = it's return palegreen3bg color text with bold text          \n
                palegreen3bg("Hello World", Style = 2 ) = it's return palegreen3bg color text with light text         \n
                palegreen3bg("Hello World", Style = 3 ) = it's return palegreen3bg color text with Italicized style   \n
                palegreen3bg("Hello World", Style = 4 ) = it's return palegreen3bg color text with UnderLine          \n
                palegreen3bg("Hello World", Style = 5 ) = it's return Blinking palegreen3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 124, 205, 124)
                


def palegreen4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the palegreen4bg colored BackGround text.\n
        palegreen4bg() is a BackGround Function, if You add ForeGround property given text you can use PaleGreen4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palegreen4bg("Hello World", Style = 0 ) = it's return palegreen4bg color text without any style       \n
                palegreen4bg("Hello World", Style = 1 ) = it's return palegreen4bg color text with bold text          \n
                palegreen4bg("Hello World", Style = 2 ) = it's return palegreen4bg color text with light text         \n
                palegreen4bg("Hello World", Style = 3 ) = it's return palegreen4bg color text with Italicized style   \n
                palegreen4bg("Hello World", Style = 4 ) = it's return palegreen4bg color text with UnderLine          \n
                palegreen4bg("Hello World", Style = 5 ) = it's return Blinking palegreen4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 84, 139, 84)
                


def seagreen_seagreen4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the seagreen_seagreen4bg colored BackGround text.\n
        seagreen_seagreen4bg() is a BackGround Function, if You add ForeGround property given text you can use SeaGreen_SeaGreen4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                seagreen_seagreen4bg("Hello World", Style = 0 ) = it's return seagreen_seagreen4bg color text without any style       \n
                seagreen_seagreen4bg("Hello World", Style = 1 ) = it's return seagreen_seagreen4bg color text with bold text          \n
                seagreen_seagreen4bg("Hello World", Style = 2 ) = it's return seagreen_seagreen4bg color text with light text         \n
                seagreen_seagreen4bg("Hello World", Style = 3 ) = it's return seagreen_seagreen4bg color text with Italicized style   \n
                seagreen_seagreen4bg("Hello World", Style = 4 ) = it's return seagreen_seagreen4bg color text with UnderLine          \n
                seagreen_seagreen4bg("Hello World", Style = 5 ) = it's return Blinking seagreen_seagreen4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 46, 139, 87)
                


def seagreen1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the seagreen1bg colored BackGround text.\n
        seagreen1bg() is a BackGround Function, if You add ForeGround property given text you can use SeaGreen1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                seagreen1bg("Hello World", Style = 0 ) = it's return seagreen1bg color text without any style       \n
                seagreen1bg("Hello World", Style = 1 ) = it's return seagreen1bg color text with bold text          \n
                seagreen1bg("Hello World", Style = 2 ) = it's return seagreen1bg color text with light text         \n
                seagreen1bg("Hello World", Style = 3 ) = it's return seagreen1bg color text with Italicized style   \n
                seagreen1bg("Hello World", Style = 4 ) = it's return seagreen1bg color text with UnderLine          \n
                seagreen1bg("Hello World", Style = 5 ) = it's return Blinking seagreen1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 84, 255, 159)
                


def seagreen2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the seagreen2bg colored BackGround text.\n
        seagreen2bg() is a BackGround Function, if You add ForeGround property given text you can use SeaGreen2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                seagreen2bg("Hello World", Style = 0 ) = it's return seagreen2bg color text without any style       \n
                seagreen2bg("Hello World", Style = 1 ) = it's return seagreen2bg color text with bold text          \n
                seagreen2bg("Hello World", Style = 2 ) = it's return seagreen2bg color text with light text         \n
                seagreen2bg("Hello World", Style = 3 ) = it's return seagreen2bg color text with Italicized style   \n
                seagreen2bg("Hello World", Style = 4 ) = it's return seagreen2bg color text with UnderLine          \n
                seagreen2bg("Hello World", Style = 5 ) = it's return Blinking seagreen2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 78, 238, 148)
                


def seagreen3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the seagreen3bg colored BackGround text.\n
        seagreen3bg() is a BackGround Function, if You add ForeGround property given text you can use SeaGreen3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                seagreen3bg("Hello World", Style = 0 ) = it's return seagreen3bg color text without any style       \n
                seagreen3bg("Hello World", Style = 1 ) = it's return seagreen3bg color text with bold text          \n
                seagreen3bg("Hello World", Style = 2 ) = it's return seagreen3bg color text with light text         \n
                seagreen3bg("Hello World", Style = 3 ) = it's return seagreen3bg color text with Italicized style   \n
                seagreen3bg("Hello World", Style = 4 ) = it's return seagreen3bg color text with UnderLine          \n
                seagreen3bg("Hello World", Style = 5 ) = it's return Blinking seagreen3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 67, 205, 128)
                


def springgreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the springgreenbg colored BackGround text.\n
        springgreenbg() is a BackGround Function, if You add ForeGround property given text you can use SpringGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                springgreenbg("Hello World", Style = 0 ) = it's return springgreenbg color text without any style       \n
                springgreenbg("Hello World", Style = 1 ) = it's return springgreenbg color text with bold text          \n
                springgreenbg("Hello World", Style = 2 ) = it's return springgreenbg color text with light text         \n
                springgreenbg("Hello World", Style = 3 ) = it's return springgreenbg color text with Italicized style   \n
                springgreenbg("Hello World", Style = 4 ) = it's return springgreenbg color text with UnderLine          \n
                springgreenbg("Hello World", Style = 5 ) = it's return Blinking springgreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 255, 127)
                


def springgreen1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the springgreen1bg colored BackGround text.\n
        springgreen1bg() is a BackGround Function, if You add ForeGround property given text you can use SpringGreen1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                springgreen1bg("Hello World", Style = 0 ) = it's return springgreen1bg color text without any style       \n
                springgreen1bg("Hello World", Style = 1 ) = it's return springgreen1bg color text with bold text          \n
                springgreen1bg("Hello World", Style = 2 ) = it's return springgreen1bg color text with light text         \n
                springgreen1bg("Hello World", Style = 3 ) = it's return springgreen1bg color text with Italicized style   \n
                springgreen1bg("Hello World", Style = 4 ) = it's return springgreen1bg color text with UnderLine          \n
                springgreen1bg("Hello World", Style = 5 ) = it's return Blinking springgreen1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 255, 127)
                


def springgreen2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the springgreen2bg colored BackGround text.\n
        springgreen2bg() is a BackGround Function, if You add ForeGround property given text you can use SpringGreen2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                springgreen2bg("Hello World", Style = 0 ) = it's return springgreen2bg color text without any style       \n
                springgreen2bg("Hello World", Style = 1 ) = it's return springgreen2bg color text with bold text          \n
                springgreen2bg("Hello World", Style = 2 ) = it's return springgreen2bg color text with light text         \n
                springgreen2bg("Hello World", Style = 3 ) = it's return springgreen2bg color text with Italicized style   \n
                springgreen2bg("Hello World", Style = 4 ) = it's return springgreen2bg color text with UnderLine          \n
                springgreen2bg("Hello World", Style = 5 ) = it's return Blinking springgreen2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 238, 118)
                


def springgreen3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the springgreen3bg colored BackGround text.\n
        springgreen3bg() is a BackGround Function, if You add ForeGround property given text you can use SpringGreen3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                springgreen3bg("Hello World", Style = 0 ) = it's return springgreen3bg color text without any style       \n
                springgreen3bg("Hello World", Style = 1 ) = it's return springgreen3bg color text with bold text          \n
                springgreen3bg("Hello World", Style = 2 ) = it's return springgreen3bg color text with light text         \n
                springgreen3bg("Hello World", Style = 3 ) = it's return springgreen3bg color text with Italicized style   \n
                springgreen3bg("Hello World", Style = 4 ) = it's return springgreen3bg color text with UnderLine          \n
                springgreen3bg("Hello World", Style = 5 ) = it's return Blinking springgreen3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 205, 102)
                


def springgreen4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the springgreen4bg colored BackGround text.\n
        springgreen4bg() is a BackGround Function, if You add ForeGround property given text you can use SpringGreen4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                springgreen4bg("Hello World", Style = 0 ) = it's return springgreen4bg color text without any style       \n
                springgreen4bg("Hello World", Style = 1 ) = it's return springgreen4bg color text with bold text          \n
                springgreen4bg("Hello World", Style = 2 ) = it's return springgreen4bg color text with light text         \n
                springgreen4bg("Hello World", Style = 3 ) = it's return springgreen4bg color text with Italicized style   \n
                springgreen4bg("Hello World", Style = 4 ) = it's return springgreen4bg color text with UnderLine          \n
                springgreen4bg("Hello World", Style = 5 ) = it's return Blinking springgreen4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 139, 69)
                


def yellowgreenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the yellowgreenbg colored BackGround text.\n
        yellowgreenbg() is a BackGround Function, if You add ForeGround property given text you can use YellowGreen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                yellowgreenbg("Hello World", Style = 0 ) = it's return yellowgreenbg color text without any style       \n
                yellowgreenbg("Hello World", Style = 1 ) = it's return yellowgreenbg color text with bold text          \n
                yellowgreenbg("Hello World", Style = 2 ) = it's return yellowgreenbg color text with light text         \n
                yellowgreenbg("Hello World", Style = 3 ) = it's return yellowgreenbg color text with Italicized style   \n
                yellowgreenbg("Hello World", Style = 4 ) = it's return yellowgreenbg color text with UnderLine          \n
                yellowgreenbg("Hello World", Style = 5 ) = it's return Blinking yellowgreenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 154, 205, 50)
                


def chartreusebg( text : str, style : int = default_style ) -> str :
        """
        It will return the chartreusebg colored BackGround text.\n
        chartreusebg() is a BackGround Function, if You add ForeGround property given text you can use chartreuse .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                chartreusebg("Hello World", Style = 0 ) = it's return chartreusebg color text without any style       \n
                chartreusebg("Hello World", Style = 1 ) = it's return chartreusebg color text with bold text          \n
                chartreusebg("Hello World", Style = 2 ) = it's return chartreusebg color text with light text         \n
                chartreusebg("Hello World", Style = 3 ) = it's return chartreusebg color text with Italicized style   \n
                chartreusebg("Hello World", Style = 4 ) = it's return chartreusebg color text with UnderLine          \n
                chartreusebg("Hello World", Style = 5 ) = it's return Blinking chartreusebg color text                \n
        """
        return Colors.back_ground_color(text, style, 127, 255, 0)
                


def chartreuse1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the chartreuse1bg colored BackGround text.\n
        chartreuse1bg() is a BackGround Function, if You add ForeGround property given text you can use chartreuse1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                chartreuse1bg("Hello World", Style = 0 ) = it's return chartreuse1bg color text without any style       \n
                chartreuse1bg("Hello World", Style = 1 ) = it's return chartreuse1bg color text with bold text          \n
                chartreuse1bg("Hello World", Style = 2 ) = it's return chartreuse1bg color text with light text         \n
                chartreuse1bg("Hello World", Style = 3 ) = it's return chartreuse1bg color text with Italicized style   \n
                chartreuse1bg("Hello World", Style = 4 ) = it's return chartreuse1bg color text with UnderLine          \n
                chartreuse1bg("Hello World", Style = 5 ) = it's return Blinking chartreuse1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 127, 255, 0)
                


def chartreuse2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the chartreuse2bg colored BackGround text.\n
        chartreuse2bg() is a BackGround Function, if You add ForeGround property given text you can use chartreuse2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                chartreuse2bg("Hello World", Style = 0 ) = it's return chartreuse2bg color text without any style       \n
                chartreuse2bg("Hello World", Style = 1 ) = it's return chartreuse2bg color text with bold text          \n
                chartreuse2bg("Hello World", Style = 2 ) = it's return chartreuse2bg color text with light text         \n
                chartreuse2bg("Hello World", Style = 3 ) = it's return chartreuse2bg color text with Italicized style   \n
                chartreuse2bg("Hello World", Style = 4 ) = it's return chartreuse2bg color text with UnderLine          \n
                chartreuse2bg("Hello World", Style = 5 ) = it's return Blinking chartreuse2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 118, 238, 0)
                


def chartreuse3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the chartreuse3bg colored BackGround text.\n
        chartreuse3bg() is a BackGround Function, if You add ForeGround property given text you can use chartreuse3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                chartreuse3bg("Hello World", Style = 0 ) = it's return chartreuse3bg color text without any style       \n
                chartreuse3bg("Hello World", Style = 1 ) = it's return chartreuse3bg color text with bold text          \n
                chartreuse3bg("Hello World", Style = 2 ) = it's return chartreuse3bg color text with light text         \n
                chartreuse3bg("Hello World", Style = 3 ) = it's return chartreuse3bg color text with Italicized style   \n
                chartreuse3bg("Hello World", Style = 4 ) = it's return chartreuse3bg color text with UnderLine          \n
                chartreuse3bg("Hello World", Style = 5 ) = it's return Blinking chartreuse3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 102, 205, 0)
                


def chartreuse4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the chartreuse4bg colored BackGround text.\n
        chartreuse4bg() is a BackGround Function, if You add ForeGround property given text you can use chartreuse4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                chartreuse4bg("Hello World", Style = 0 ) = it's return chartreuse4bg color text without any style       \n
                chartreuse4bg("Hello World", Style = 1 ) = it's return chartreuse4bg color text with bold text          \n
                chartreuse4bg("Hello World", Style = 2 ) = it's return chartreuse4bg color text with light text         \n
                chartreuse4bg("Hello World", Style = 3 ) = it's return chartreuse4bg color text with Italicized style   \n
                chartreuse4bg("Hello World", Style = 4 ) = it's return chartreuse4bg color text with UnderLine          \n
                chartreuse4bg("Hello World", Style = 5 ) = it's return Blinking chartreuse4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 69, 139, 0)
                


def greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the greenbg colored BackGround text.\n
        greenbg() is a BackGround Function, if You add ForeGround property given text you can use green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                greenbg("Hello World", Style = 0 ) = it's return greenbg color text without any style       \n
                greenbg("Hello World", Style = 1 ) = it's return greenbg color text with bold text          \n
                greenbg("Hello World", Style = 2 ) = it's return greenbg color text with light text         \n
                greenbg("Hello World", Style = 3 ) = it's return greenbg color text with Italicized style   \n
                greenbg("Hello World", Style = 4 ) = it's return greenbg color text with UnderLine          \n
                greenbg("Hello World", Style = 5 ) = it's return Blinking greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 128, 0)
                


def greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the greenbg colored BackGround text.\n
        greenbg() is a BackGround Function, if You add ForeGround property given text you can use green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                greenbg("Hello World", Style = 0 ) = it's return greenbg color text without any style       \n
                greenbg("Hello World", Style = 1 ) = it's return greenbg color text with bold text          \n
                greenbg("Hello World", Style = 2 ) = it's return greenbg color text with light text         \n
                greenbg("Hello World", Style = 3 ) = it's return greenbg color text with Italicized style   \n
                greenbg("Hello World", Style = 4 ) = it's return greenbg color text with UnderLine          \n
                greenbg("Hello World", Style = 5 ) = it's return Blinking greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 128, 0)
                


def limebg( text : str, style : int = default_style ) -> str :
        """
        It will return the limebg colored BackGround text.\n
        limebg() is a BackGround Function, if You add ForeGround property given text you can use lime .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                limebg("Hello World", Style = 0 ) = it's return limebg color text without any style       \n
                limebg("Hello World", Style = 1 ) = it's return limebg color text with bold text          \n
                limebg("Hello World", Style = 2 ) = it's return limebg color text with light text         \n
                limebg("Hello World", Style = 3 ) = it's return limebg color text with Italicized style   \n
                limebg("Hello World", Style = 4 ) = it's return limebg color text with UnderLine          \n
                limebg("Hello World", Style = 5 ) = it's return Blinking limebg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 255, 0)
                


def green1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the green1bg colored BackGround text.\n
        green1bg() is a BackGround Function, if You add ForeGround property given text you can use green1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                green1bg("Hello World", Style = 0 ) = it's return green1bg color text without any style       \n
                green1bg("Hello World", Style = 1 ) = it's return green1bg color text with bold text          \n
                green1bg("Hello World", Style = 2 ) = it's return green1bg color text with light text         \n
                green1bg("Hello World", Style = 3 ) = it's return green1bg color text with Italicized style   \n
                green1bg("Hello World", Style = 4 ) = it's return green1bg color text with UnderLine          \n
                green1bg("Hello World", Style = 5 ) = it's return Blinking green1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 255, 0)
                


def green2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the green2bg colored BackGround text.\n
        green2bg() is a BackGround Function, if You add ForeGround property given text you can use green2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                green2bg("Hello World", Style = 0 ) = it's return green2bg color text without any style       \n
                green2bg("Hello World", Style = 1 ) = it's return green2bg color text with bold text          \n
                green2bg("Hello World", Style = 2 ) = it's return green2bg color text with light text         \n
                green2bg("Hello World", Style = 3 ) = it's return green2bg color text with Italicized style   \n
                green2bg("Hello World", Style = 4 ) = it's return green2bg color text with UnderLine          \n
                green2bg("Hello World", Style = 5 ) = it's return Blinking green2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 238, 0)
                


def green3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the green3bg colored BackGround text.\n
        green3bg() is a BackGround Function, if You add ForeGround property given text you can use green3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                green3bg("Hello World", Style = 0 ) = it's return green3bg color text without any style       \n
                green3bg("Hello World", Style = 1 ) = it's return green3bg color text with bold text          \n
                green3bg("Hello World", Style = 2 ) = it's return green3bg color text with light text         \n
                green3bg("Hello World", Style = 3 ) = it's return green3bg color text with Italicized style   \n
                green3bg("Hello World", Style = 4 ) = it's return green3bg color text with UnderLine          \n
                green3bg("Hello World", Style = 5 ) = it's return Blinking green3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 205, 0)
                


def green4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the green4bg colored BackGround text.\n
        green4bg() is a BackGround Function, if You add ForeGround property given text you can use green4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                green4bg("Hello World", Style = 0 ) = it's return green4bg color text without any style       \n
                green4bg("Hello World", Style = 1 ) = it's return green4bg color text with bold text          \n
                green4bg("Hello World", Style = 2 ) = it's return green4bg color text with light text         \n
                green4bg("Hello World", Style = 3 ) = it's return green4bg color text with Italicized style   \n
                green4bg("Hello World", Style = 4 ) = it's return green4bg color text with UnderLine          \n
                green4bg("Hello World", Style = 5 ) = it's return Blinking green4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 139, 0)
                


def khakibg( text : str, style : int = default_style ) -> str :
        """
        It will return the khakibg colored BackGround text.\n
        khakibg() is a BackGround Function, if You add ForeGround property given text you can use khaki .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                khakibg("Hello World", Style = 0 ) = it's return khakibg color text without any style       \n
                khakibg("Hello World", Style = 1 ) = it's return khakibg color text with bold text          \n
                khakibg("Hello World", Style = 2 ) = it's return khakibg color text with light text         \n
                khakibg("Hello World", Style = 3 ) = it's return khakibg color text with Italicized style   \n
                khakibg("Hello World", Style = 4 ) = it's return khakibg color text with UnderLine          \n
                khakibg("Hello World", Style = 5 ) = it's return Blinking khakibg color text                \n
        """
        return Colors.back_ground_color(text, style, 240, 230, 140)
                


def khaki1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the khaki1bg colored BackGround text.\n
        khaki1bg() is a BackGround Function, if You add ForeGround property given text you can use khaki1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                khaki1bg("Hello World", Style = 0 ) = it's return khaki1bg color text without any style       \n
                khaki1bg("Hello World", Style = 1 ) = it's return khaki1bg color text with bold text          \n
                khaki1bg("Hello World", Style = 2 ) = it's return khaki1bg color text with light text         \n
                khaki1bg("Hello World", Style = 3 ) = it's return khaki1bg color text with Italicized style   \n
                khaki1bg("Hello World", Style = 4 ) = it's return khaki1bg color text with UnderLine          \n
                khaki1bg("Hello World", Style = 5 ) = it's return Blinking khaki1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 246, 143)
                


def khaki2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the khaki2bg colored BackGround text.\n
        khaki2bg() is a BackGround Function, if You add ForeGround property given text you can use khaki2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                khaki2bg("Hello World", Style = 0 ) = it's return khaki2bg color text without any style       \n
                khaki2bg("Hello World", Style = 1 ) = it's return khaki2bg color text with bold text          \n
                khaki2bg("Hello World", Style = 2 ) = it's return khaki2bg color text with light text         \n
                khaki2bg("Hello World", Style = 3 ) = it's return khaki2bg color text with Italicized style   \n
                khaki2bg("Hello World", Style = 4 ) = it's return khaki2bg color text with UnderLine          \n
                khaki2bg("Hello World", Style = 5 ) = it's return Blinking khaki2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 230, 133)
                


def khaki3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the khaki3bg colored BackGround text.\n
        khaki3bg() is a BackGround Function, if You add ForeGround property given text you can use khaki3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                khaki3bg("Hello World", Style = 0 ) = it's return khaki3bg color text without any style       \n
                khaki3bg("Hello World", Style = 1 ) = it's return khaki3bg color text with bold text          \n
                khaki3bg("Hello World", Style = 2 ) = it's return khaki3bg color text with light text         \n
                khaki3bg("Hello World", Style = 3 ) = it's return khaki3bg color text with Italicized style   \n
                khaki3bg("Hello World", Style = 4 ) = it's return khaki3bg color text with UnderLine          \n
                khaki3bg("Hello World", Style = 5 ) = it's return Blinking khaki3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 198, 115)
                


def khaki4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the khaki4bg colored BackGround text.\n
        khaki4bg() is a BackGround Function, if You add ForeGround property given text you can use khaki4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                khaki4bg("Hello World", Style = 0 ) = it's return khaki4bg color text without any style       \n
                khaki4bg("Hello World", Style = 1 ) = it's return khaki4bg color text with bold text          \n
                khaki4bg("Hello World", Style = 2 ) = it's return khaki4bg color text with light text         \n
                khaki4bg("Hello World", Style = 3 ) = it's return khaki4bg color text with Italicized style   \n
                khaki4bg("Hello World", Style = 4 ) = it's return khaki4bg color text with UnderLine          \n
                khaki4bg("Hello World", Style = 5 ) = it's return Blinking khaki4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 134, 78)
                


def dark_olive_greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_olive_greenbg colored BackGround text.\n
        dark_olive_greenbg() is a BackGround Function, if You add ForeGround property given text you can use Dark_Olive_Green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_olive_greenbg("Hello World", Style = 0 ) = it's return dark_olive_greenbg color text without any style       \n
                dark_olive_greenbg("Hello World", Style = 1 ) = it's return dark_olive_greenbg color text with bold text          \n
                dark_olive_greenbg("Hello World", Style = 2 ) = it's return dark_olive_greenbg color text with light text         \n
                dark_olive_greenbg("Hello World", Style = 3 ) = it's return dark_olive_greenbg color text with Italicized style   \n
                dark_olive_greenbg("Hello World", Style = 4 ) = it's return dark_olive_greenbg color text with UnderLine          \n
                dark_olive_greenbg("Hello World", Style = 5 ) = it's return Blinking dark_olive_greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 79, 79, 47)
                


def medium_aquamarinebg( text : str, style : int = default_style ) -> str :
        """
        It will return the medium_aquamarinebg colored BackGround text.\n
        medium_aquamarinebg() is a BackGround Function, if You add ForeGround property given text you can use Medium_Aquamarine .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                medium_aquamarinebg("Hello World", Style = 0 ) = it's return medium_aquamarinebg color text without any style       \n
                medium_aquamarinebg("Hello World", Style = 1 ) = it's return medium_aquamarinebg color text with bold text          \n
                medium_aquamarinebg("Hello World", Style = 2 ) = it's return medium_aquamarinebg color text with light text         \n
                medium_aquamarinebg("Hello World", Style = 3 ) = it's return medium_aquamarinebg color text with Italicized style   \n
                medium_aquamarinebg("Hello World", Style = 4 ) = it's return medium_aquamarinebg color text with UnderLine          \n
                medium_aquamarinebg("Hello World", Style = 5 ) = it's return Blinking medium_aquamarinebg color text                \n
        """
        return Colors.back_ground_color(text, style, 35, 142, 35)
                


def medium_forest_greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the medium_forest_greenbg colored BackGround text.\n
        medium_forest_greenbg() is a BackGround Function, if You add ForeGround property given text you can use Medium_Forest_Green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                medium_forest_greenbg("Hello World", Style = 0 ) = it's return medium_forest_greenbg color text without any style       \n
                medium_forest_greenbg("Hello World", Style = 1 ) = it's return medium_forest_greenbg color text with bold text          \n
                medium_forest_greenbg("Hello World", Style = 2 ) = it's return medium_forest_greenbg color text with light text         \n
                medium_forest_greenbg("Hello World", Style = 3 ) = it's return medium_forest_greenbg color text with Italicized style   \n
                medium_forest_greenbg("Hello World", Style = 4 ) = it's return medium_forest_greenbg color text with UnderLine          \n
                medium_forest_greenbg("Hello World", Style = 5 ) = it's return Blinking medium_forest_greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 219, 219, 112)
                


def medium_sea_greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the medium_sea_greenbg colored BackGround text.\n
        medium_sea_greenbg() is a BackGround Function, if You add ForeGround property given text you can use Medium_Sea_Green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                medium_sea_greenbg("Hello World", Style = 0 ) = it's return medium_sea_greenbg color text without any style       \n
                medium_sea_greenbg("Hello World", Style = 1 ) = it's return medium_sea_greenbg color text with bold text          \n
                medium_sea_greenbg("Hello World", Style = 2 ) = it's return medium_sea_greenbg color text with light text         \n
                medium_sea_greenbg("Hello World", Style = 3 ) = it's return medium_sea_greenbg color text with Italicized style   \n
                medium_sea_greenbg("Hello World", Style = 4 ) = it's return medium_sea_greenbg color text with UnderLine          \n
                medium_sea_greenbg("Hello World", Style = 5 ) = it's return Blinking medium_sea_greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 66, 111, 66)
                


def medium_spring_greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the medium_spring_greenbg colored BackGround text.\n
        medium_spring_greenbg() is a BackGround Function, if You add ForeGround property given text you can use Medium_Spring_Green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                medium_spring_greenbg("Hello World", Style = 0 ) = it's return medium_spring_greenbg color text without any style       \n
                medium_spring_greenbg("Hello World", Style = 1 ) = it's return medium_spring_greenbg color text with bold text          \n
                medium_spring_greenbg("Hello World", Style = 2 ) = it's return medium_spring_greenbg color text with light text         \n
                medium_spring_greenbg("Hello World", Style = 3 ) = it's return medium_spring_greenbg color text with Italicized style   \n
                medium_spring_greenbg("Hello World", Style = 4 ) = it's return medium_spring_greenbg color text with UnderLine          \n
                medium_spring_greenbg("Hello World", Style = 5 ) = it's return Blinking medium_spring_greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 127, 255, 0)
                


def pale_greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the pale_greenbg colored BackGround text.\n
        pale_greenbg() is a BackGround Function, if You add ForeGround property given text you can use Pale_Green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                pale_greenbg("Hello World", Style = 0 ) = it's return pale_greenbg color text without any style       \n
                pale_greenbg("Hello World", Style = 1 ) = it's return pale_greenbg color text with bold text          \n
                pale_greenbg("Hello World", Style = 2 ) = it's return pale_greenbg color text with light text         \n
                pale_greenbg("Hello World", Style = 3 ) = it's return pale_greenbg color text with Italicized style   \n
                pale_greenbg("Hello World", Style = 4 ) = it's return pale_greenbg color text with UnderLine          \n
                pale_greenbg("Hello World", Style = 5 ) = it's return Blinking pale_greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 143, 188, 143)
                


def sea_greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the sea_greenbg colored BackGround text.\n
        sea_greenbg() is a BackGround Function, if You add ForeGround property given text you can use Sea_Green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                sea_greenbg("Hello World", Style = 0 ) = it's return sea_greenbg color text without any style       \n
                sea_greenbg("Hello World", Style = 1 ) = it's return sea_greenbg color text with bold text          \n
                sea_greenbg("Hello World", Style = 2 ) = it's return sea_greenbg color text with light text         \n
                sea_greenbg("Hello World", Style = 3 ) = it's return sea_greenbg color text with Italicized style   \n
                sea_greenbg("Hello World", Style = 4 ) = it's return sea_greenbg color text with UnderLine          \n
                sea_greenbg("Hello World", Style = 5 ) = it's return Blinking sea_greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 35, 142, 104)
                


def spring_greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the spring_greenbg colored BackGround text.\n
        spring_greenbg() is a BackGround Function, if You add ForeGround property given text you can use Spring_Green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                spring_greenbg("Hello World", Style = 0 ) = it's return spring_greenbg color text without any style       \n
                spring_greenbg("Hello World", Style = 1 ) = it's return spring_greenbg color text with bold text          \n
                spring_greenbg("Hello World", Style = 2 ) = it's return spring_greenbg color text with light text         \n
                spring_greenbg("Hello World", Style = 3 ) = it's return spring_greenbg color text with Italicized style   \n
                spring_greenbg("Hello World", Style = 4 ) = it's return spring_greenbg color text with UnderLine          \n
                spring_greenbg("Hello World", Style = 5 ) = it's return Blinking spring_greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 0, 255, 127)
                


def free_speech_greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the free_speech_greenbg colored BackGround text.\n
        free_speech_greenbg() is a BackGround Function, if You add ForeGround property given text you can use Free_Speech_Green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                free_speech_greenbg("Hello World", Style = 0 ) = it's return free_speech_greenbg color text without any style       \n
                free_speech_greenbg("Hello World", Style = 1 ) = it's return free_speech_greenbg color text with bold text          \n
                free_speech_greenbg("Hello World", Style = 2 ) = it's return free_speech_greenbg color text with light text         \n
                free_speech_greenbg("Hello World", Style = 3 ) = it's return free_speech_greenbg color text with Italicized style   \n
                free_speech_greenbg("Hello World", Style = 4 ) = it's return free_speech_greenbg color text with UnderLine          \n
                free_speech_greenbg("Hello World", Style = 5 ) = it's return Blinking free_speech_greenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 9, 249, 17)
                


def aquamarinebg( text : str, style : int = default_style ) -> str :
        """
        It will return the aquamarinebg colored BackGround text.\n
        aquamarinebg() is a BackGround Function, if You add ForeGround property given text you can use Aquamarine .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                aquamarinebg("Hello World", Style = 0 ) = it's return aquamarinebg color text without any style       \n
                aquamarinebg("Hello World", Style = 1 ) = it's return aquamarinebg color text with bold text          \n
                aquamarinebg("Hello World", Style = 2 ) = it's return aquamarinebg color text with light text         \n
                aquamarinebg("Hello World", Style = 3 ) = it's return aquamarinebg color text with Italicized style   \n
                aquamarinebg("Hello World", Style = 4 ) = it's return aquamarinebg color text with UnderLine          \n
                aquamarinebg("Hello World", Style = 5 ) = it's return Blinking aquamarinebg color text                \n
        """
        return Colors.back_ground_color(text, style, 2, 157, 116)
                


def darkorangebg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkorangebg colored BackGround text.\n
        darkorangebg() is a BackGround Function, if You add ForeGround property given text you can use DarkOrange .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkorangebg("Hello World", Style = 0 ) = it's return darkorangebg color text without any style       \n
                darkorangebg("Hello World", Style = 1 ) = it's return darkorangebg color text with bold text          \n
                darkorangebg("Hello World", Style = 2 ) = it's return darkorangebg color text with light text         \n
                darkorangebg("Hello World", Style = 3 ) = it's return darkorangebg color text with Italicized style   \n
                darkorangebg("Hello World", Style = 4 ) = it's return darkorangebg color text with UnderLine          \n
                darkorangebg("Hello World", Style = 5 ) = it's return Blinking darkorangebg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 140, 0)
                


def darkorange1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkorange1bg colored BackGround text.\n
        darkorange1bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOrange1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkorange1bg("Hello World", Style = 0 ) = it's return darkorange1bg color text without any style       \n
                darkorange1bg("Hello World", Style = 1 ) = it's return darkorange1bg color text with bold text          \n
                darkorange1bg("Hello World", Style = 2 ) = it's return darkorange1bg color text with light text         \n
                darkorange1bg("Hello World", Style = 3 ) = it's return darkorange1bg color text with Italicized style   \n
                darkorange1bg("Hello World", Style = 4 ) = it's return darkorange1bg color text with UnderLine          \n
                darkorange1bg("Hello World", Style = 5 ) = it's return Blinking darkorange1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 127, 0)
                


def darkorange2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkorange2bg colored BackGround text.\n
        darkorange2bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOrange2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkorange2bg("Hello World", Style = 0 ) = it's return darkorange2bg color text without any style       \n
                darkorange2bg("Hello World", Style = 1 ) = it's return darkorange2bg color text with bold text          \n
                darkorange2bg("Hello World", Style = 2 ) = it's return darkorange2bg color text with light text         \n
                darkorange2bg("Hello World", Style = 3 ) = it's return darkorange2bg color text with Italicized style   \n
                darkorange2bg("Hello World", Style = 4 ) = it's return darkorange2bg color text with UnderLine          \n
                darkorange2bg("Hello World", Style = 5 ) = it's return Blinking darkorange2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 118, 0)
                


def darkorange3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkorange3bg colored BackGround text.\n
        darkorange3bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOrange3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkorange3bg("Hello World", Style = 0 ) = it's return darkorange3bg color text without any style       \n
                darkorange3bg("Hello World", Style = 1 ) = it's return darkorange3bg color text with bold text          \n
                darkorange3bg("Hello World", Style = 2 ) = it's return darkorange3bg color text with light text         \n
                darkorange3bg("Hello World", Style = 3 ) = it's return darkorange3bg color text with Italicized style   \n
                darkorange3bg("Hello World", Style = 4 ) = it's return darkorange3bg color text with UnderLine          \n
                darkorange3bg("Hello World", Style = 5 ) = it's return Blinking darkorange3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 102, 0)
                


def darkorange4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkorange4bg colored BackGround text.\n
        darkorange4bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOrange4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkorange4bg("Hello World", Style = 0 ) = it's return darkorange4bg color text without any style       \n
                darkorange4bg("Hello World", Style = 1 ) = it's return darkorange4bg color text with bold text          \n
                darkorange4bg("Hello World", Style = 2 ) = it's return darkorange4bg color text with light text         \n
                darkorange4bg("Hello World", Style = 3 ) = it's return darkorange4bg color text with Italicized style   \n
                darkorange4bg("Hello World", Style = 4 ) = it's return darkorange4bg color text with UnderLine          \n
                darkorange4bg("Hello World", Style = 5 ) = it's return Blinking darkorange4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 69, 0)
                


def darksalmonbg( text : str, style : int = default_style ) -> str :
        """
        It will return the darksalmonbg colored BackGround text.\n
        darksalmonbg() is a BackGround Function, if You add ForeGround property given text you can use DarkSalmon .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darksalmonbg("Hello World", Style = 0 ) = it's return darksalmonbg color text without any style       \n
                darksalmonbg("Hello World", Style = 1 ) = it's return darksalmonbg color text with bold text          \n
                darksalmonbg("Hello World", Style = 2 ) = it's return darksalmonbg color text with light text         \n
                darksalmonbg("Hello World", Style = 3 ) = it's return darksalmonbg color text with Italicized style   \n
                darksalmonbg("Hello World", Style = 4 ) = it's return darksalmonbg color text with UnderLine          \n
                darksalmonbg("Hello World", Style = 5 ) = it's return Blinking darksalmonbg color text                \n
        """
        return Colors.back_ground_color(text, style, 233, 150, 122)
                


def lightcoralbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightcoralbg colored BackGround text.\n
        lightcoralbg() is a BackGround Function, if You add ForeGround property given text you can use LightCoral .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightcoralbg("Hello World", Style = 0 ) = it's return lightcoralbg color text without any style       \n
                lightcoralbg("Hello World", Style = 1 ) = it's return lightcoralbg color text with bold text          \n
                lightcoralbg("Hello World", Style = 2 ) = it's return lightcoralbg color text with light text         \n
                lightcoralbg("Hello World", Style = 3 ) = it's return lightcoralbg color text with Italicized style   \n
                lightcoralbg("Hello World", Style = 4 ) = it's return lightcoralbg color text with UnderLine          \n
                lightcoralbg("Hello World", Style = 5 ) = it's return Blinking lightcoralbg color text                \n
        """
        return Colors.back_ground_color(text, style, 240, 128, 128)
                


def lightsalmonbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightsalmonbg colored BackGround text.\n
        lightsalmonbg() is a BackGround Function, if You add ForeGround property given text you can use LightSalmon .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightsalmonbg("Hello World", Style = 0 ) = it's return lightsalmonbg color text without any style       \n
                lightsalmonbg("Hello World", Style = 1 ) = it's return lightsalmonbg color text with bold text          \n
                lightsalmonbg("Hello World", Style = 2 ) = it's return lightsalmonbg color text with light text         \n
                lightsalmonbg("Hello World", Style = 3 ) = it's return lightsalmonbg color text with Italicized style   \n
                lightsalmonbg("Hello World", Style = 4 ) = it's return lightsalmonbg color text with UnderLine          \n
                lightsalmonbg("Hello World", Style = 5 ) = it's return Blinking lightsalmonbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 160, 122)
                


def lightsalmon1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightsalmon1bg colored BackGround text.\n
        lightsalmon1bg() is a BackGround Function, if You add ForeGround property given text you can use LightSalmon1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightsalmon1bg("Hello World", Style = 0 ) = it's return lightsalmon1bg color text without any style       \n
                lightsalmon1bg("Hello World", Style = 1 ) = it's return lightsalmon1bg color text with bold text          \n
                lightsalmon1bg("Hello World", Style = 2 ) = it's return lightsalmon1bg color text with light text         \n
                lightsalmon1bg("Hello World", Style = 3 ) = it's return lightsalmon1bg color text with Italicized style   \n
                lightsalmon1bg("Hello World", Style = 4 ) = it's return lightsalmon1bg color text with UnderLine          \n
                lightsalmon1bg("Hello World", Style = 5 ) = it's return Blinking lightsalmon1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 160, 122)
                


def lightsalmon2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightsalmon2bg colored BackGround text.\n
        lightsalmon2bg() is a BackGround Function, if You add ForeGround property given text you can use LightSalmon2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightsalmon2bg("Hello World", Style = 0 ) = it's return lightsalmon2bg color text without any style       \n
                lightsalmon2bg("Hello World", Style = 1 ) = it's return lightsalmon2bg color text with bold text          \n
                lightsalmon2bg("Hello World", Style = 2 ) = it's return lightsalmon2bg color text with light text         \n
                lightsalmon2bg("Hello World", Style = 3 ) = it's return lightsalmon2bg color text with Italicized style   \n
                lightsalmon2bg("Hello World", Style = 4 ) = it's return lightsalmon2bg color text with UnderLine          \n
                lightsalmon2bg("Hello World", Style = 5 ) = it's return Blinking lightsalmon2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 149, 114)
                


def lightsalmon3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightsalmon3bg colored BackGround text.\n
        lightsalmon3bg() is a BackGround Function, if You add ForeGround property given text you can use LightSalmon3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightsalmon3bg("Hello World", Style = 0 ) = it's return lightsalmon3bg color text without any style       \n
                lightsalmon3bg("Hello World", Style = 1 ) = it's return lightsalmon3bg color text with bold text          \n
                lightsalmon3bg("Hello World", Style = 2 ) = it's return lightsalmon3bg color text with light text         \n
                lightsalmon3bg("Hello World", Style = 3 ) = it's return lightsalmon3bg color text with Italicized style   \n
                lightsalmon3bg("Hello World", Style = 4 ) = it's return lightsalmon3bg color text with UnderLine          \n
                lightsalmon3bg("Hello World", Style = 5 ) = it's return Blinking lightsalmon3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 129, 98)
                


def lightsalmon4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightsalmon4bg colored BackGround text.\n
        lightsalmon4bg() is a BackGround Function, if You add ForeGround property given text you can use LightSalmon4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightsalmon4bg("Hello World", Style = 0 ) = it's return lightsalmon4bg color text without any style       \n
                lightsalmon4bg("Hello World", Style = 1 ) = it's return lightsalmon4bg color text with bold text          \n
                lightsalmon4bg("Hello World", Style = 2 ) = it's return lightsalmon4bg color text with light text         \n
                lightsalmon4bg("Hello World", Style = 3 ) = it's return lightsalmon4bg color text with Italicized style   \n
                lightsalmon4bg("Hello World", Style = 4 ) = it's return lightsalmon4bg color text with UnderLine          \n
                lightsalmon4bg("Hello World", Style = 5 ) = it's return Blinking lightsalmon4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 87, 66)
                


def peachpuffbg( text : str, style : int = default_style ) -> str :
        """
        It will return the peachpuffbg colored BackGround text.\n
        peachpuffbg() is a BackGround Function, if You add ForeGround property given text you can use PeachPuff .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                peachpuffbg("Hello World", Style = 0 ) = it's return peachpuffbg color text without any style       \n
                peachpuffbg("Hello World", Style = 1 ) = it's return peachpuffbg color text with bold text          \n
                peachpuffbg("Hello World", Style = 2 ) = it's return peachpuffbg color text with light text         \n
                peachpuffbg("Hello World", Style = 3 ) = it's return peachpuffbg color text with Italicized style   \n
                peachpuffbg("Hello World", Style = 4 ) = it's return peachpuffbg color text with UnderLine          \n
                peachpuffbg("Hello World", Style = 5 ) = it's return Blinking peachpuffbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 218, 185)
                


def peachpuff1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the peachpuff1bg colored BackGround text.\n
        peachpuff1bg() is a BackGround Function, if You add ForeGround property given text you can use PeachPuff1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                peachpuff1bg("Hello World", Style = 0 ) = it's return peachpuff1bg color text without any style       \n
                peachpuff1bg("Hello World", Style = 1 ) = it's return peachpuff1bg color text with bold text          \n
                peachpuff1bg("Hello World", Style = 2 ) = it's return peachpuff1bg color text with light text         \n
                peachpuff1bg("Hello World", Style = 3 ) = it's return peachpuff1bg color text with Italicized style   \n
                peachpuff1bg("Hello World", Style = 4 ) = it's return peachpuff1bg color text with UnderLine          \n
                peachpuff1bg("Hello World", Style = 5 ) = it's return Blinking peachpuff1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 218, 185)
                


def peachpuff2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the peachpuff2bg colored BackGround text.\n
        peachpuff2bg() is a BackGround Function, if You add ForeGround property given text you can use PeachPuff2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                peachpuff2bg("Hello World", Style = 0 ) = it's return peachpuff2bg color text without any style       \n
                peachpuff2bg("Hello World", Style = 1 ) = it's return peachpuff2bg color text with bold text          \n
                peachpuff2bg("Hello World", Style = 2 ) = it's return peachpuff2bg color text with light text         \n
                peachpuff2bg("Hello World", Style = 3 ) = it's return peachpuff2bg color text with Italicized style   \n
                peachpuff2bg("Hello World", Style = 4 ) = it's return peachpuff2bg color text with UnderLine          \n
                peachpuff2bg("Hello World", Style = 5 ) = it's return Blinking peachpuff2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 203, 173)
                


def peachpuff3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the peachpuff3bg colored BackGround text.\n
        peachpuff3bg() is a BackGround Function, if You add ForeGround property given text you can use PeachPuff3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                peachpuff3bg("Hello World", Style = 0 ) = it's return peachpuff3bg color text without any style       \n
                peachpuff3bg("Hello World", Style = 1 ) = it's return peachpuff3bg color text with bold text          \n
                peachpuff3bg("Hello World", Style = 2 ) = it's return peachpuff3bg color text with light text         \n
                peachpuff3bg("Hello World", Style = 3 ) = it's return peachpuff3bg color text with Italicized style   \n
                peachpuff3bg("Hello World", Style = 4 ) = it's return peachpuff3bg color text with UnderLine          \n
                peachpuff3bg("Hello World", Style = 5 ) = it's return Blinking peachpuff3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 175, 149)
                


def peachpuff4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the peachpuff4bg colored BackGround text.\n
        peachpuff4bg() is a BackGround Function, if You add ForeGround property given text you can use PeachPuff4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                peachpuff4bg("Hello World", Style = 0 ) = it's return peachpuff4bg color text without any style       \n
                peachpuff4bg("Hello World", Style = 1 ) = it's return peachpuff4bg color text with bold text          \n
                peachpuff4bg("Hello World", Style = 2 ) = it's return peachpuff4bg color text with light text         \n
                peachpuff4bg("Hello World", Style = 3 ) = it's return peachpuff4bg color text with Italicized style   \n
                peachpuff4bg("Hello World", Style = 4 ) = it's return peachpuff4bg color text with UnderLine          \n
                peachpuff4bg("Hello World", Style = 5 ) = it's return Blinking peachpuff4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 119, 101)
                


def bisquebg( text : str, style : int = default_style ) -> str :
        """
        It will return the bisquebg colored BackGround text.\n
        bisquebg() is a BackGround Function, if You add ForeGround property given text you can use bisque .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                bisquebg("Hello World", Style = 0 ) = it's return bisquebg color text without any style       \n
                bisquebg("Hello World", Style = 1 ) = it's return bisquebg color text with bold text          \n
                bisquebg("Hello World", Style = 2 ) = it's return bisquebg color text with light text         \n
                bisquebg("Hello World", Style = 3 ) = it's return bisquebg color text with Italicized style   \n
                bisquebg("Hello World", Style = 4 ) = it's return bisquebg color text with UnderLine          \n
                bisquebg("Hello World", Style = 5 ) = it's return Blinking bisquebg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 228, 196)
                


def bisque1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the bisque1bg colored BackGround text.\n
        bisque1bg() is a BackGround Function, if You add ForeGround property given text you can use bisque1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                bisque1bg("Hello World", Style = 0 ) = it's return bisque1bg color text without any style       \n
                bisque1bg("Hello World", Style = 1 ) = it's return bisque1bg color text with bold text          \n
                bisque1bg("Hello World", Style = 2 ) = it's return bisque1bg color text with light text         \n
                bisque1bg("Hello World", Style = 3 ) = it's return bisque1bg color text with Italicized style   \n
                bisque1bg("Hello World", Style = 4 ) = it's return bisque1bg color text with UnderLine          \n
                bisque1bg("Hello World", Style = 5 ) = it's return Blinking bisque1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 228, 196)
                


def bisque2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the bisque2bg colored BackGround text.\n
        bisque2bg() is a BackGround Function, if You add ForeGround property given text you can use bisque2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                bisque2bg("Hello World", Style = 0 ) = it's return bisque2bg color text without any style       \n
                bisque2bg("Hello World", Style = 1 ) = it's return bisque2bg color text with bold text          \n
                bisque2bg("Hello World", Style = 2 ) = it's return bisque2bg color text with light text         \n
                bisque2bg("Hello World", Style = 3 ) = it's return bisque2bg color text with Italicized style   \n
                bisque2bg("Hello World", Style = 4 ) = it's return bisque2bg color text with UnderLine          \n
                bisque2bg("Hello World", Style = 5 ) = it's return Blinking bisque2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 213, 183)
                


def bisque3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the bisque3bg colored BackGround text.\n
        bisque3bg() is a BackGround Function, if You add ForeGround property given text you can use bisque3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                bisque3bg("Hello World", Style = 0 ) = it's return bisque3bg color text without any style       \n
                bisque3bg("Hello World", Style = 1 ) = it's return bisque3bg color text with bold text          \n
                bisque3bg("Hello World", Style = 2 ) = it's return bisque3bg color text with light text         \n
                bisque3bg("Hello World", Style = 3 ) = it's return bisque3bg color text with Italicized style   \n
                bisque3bg("Hello World", Style = 4 ) = it's return bisque3bg color text with UnderLine          \n
                bisque3bg("Hello World", Style = 5 ) = it's return Blinking bisque3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 183, 158)
                


def bisque4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the bisque4bg colored BackGround text.\n
        bisque4bg() is a BackGround Function, if You add ForeGround property given text you can use bisque4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                bisque4bg("Hello World", Style = 0 ) = it's return bisque4bg color text without any style       \n
                bisque4bg("Hello World", Style = 1 ) = it's return bisque4bg color text with bold text          \n
                bisque4bg("Hello World", Style = 2 ) = it's return bisque4bg color text with light text         \n
                bisque4bg("Hello World", Style = 3 ) = it's return bisque4bg color text with Italicized style   \n
                bisque4bg("Hello World", Style = 4 ) = it's return bisque4bg color text with UnderLine          \n
                bisque4bg("Hello World", Style = 5 ) = it's return Blinking bisque4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 125, 107)
                


def coralbg( text : str, style : int = default_style ) -> str :
        """
        It will return the coralbg colored BackGround text.\n
        coralbg() is a BackGround Function, if You add ForeGround property given text you can use coral .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                coralbg("Hello World", Style = 0 ) = it's return coralbg color text without any style       \n
                coralbg("Hello World", Style = 1 ) = it's return coralbg color text with bold text          \n
                coralbg("Hello World", Style = 2 ) = it's return coralbg color text with light text         \n
                coralbg("Hello World", Style = 3 ) = it's return coralbg color text with Italicized style   \n
                coralbg("Hello World", Style = 4 ) = it's return coralbg color text with UnderLine          \n
                coralbg("Hello World", Style = 5 ) = it's return Blinking coralbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 127, 80)
                


def coralbg( text : str, style : int = default_style ) -> str :
        """
        It will return the coralbg colored BackGround text.\n
        coralbg() is a BackGround Function, if You add ForeGround property given text you can use coral .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                coralbg("Hello World", Style = 0 ) = it's return coralbg color text without any style       \n
                coralbg("Hello World", Style = 1 ) = it's return coralbg color text with bold text          \n
                coralbg("Hello World", Style = 2 ) = it's return coralbg color text with light text         \n
                coralbg("Hello World", Style = 3 ) = it's return coralbg color text with Italicized style   \n
                coralbg("Hello World", Style = 4 ) = it's return coralbg color text with UnderLine          \n
                coralbg("Hello World", Style = 5 ) = it's return Blinking coralbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 127, 80)
                


def coral1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the coral1bg colored BackGround text.\n
        coral1bg() is a BackGround Function, if You add ForeGround property given text you can use coral1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                coral1bg("Hello World", Style = 0 ) = it's return coral1bg color text without any style       \n
                coral1bg("Hello World", Style = 1 ) = it's return coral1bg color text with bold text          \n
                coral1bg("Hello World", Style = 2 ) = it's return coral1bg color text with light text         \n
                coral1bg("Hello World", Style = 3 ) = it's return coral1bg color text with Italicized style   \n
                coral1bg("Hello World", Style = 4 ) = it's return coral1bg color text with UnderLine          \n
                coral1bg("Hello World", Style = 5 ) = it's return Blinking coral1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 114, 86)
                


def coral2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the coral2bg colored BackGround text.\n
        coral2bg() is a BackGround Function, if You add ForeGround property given text you can use coral2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                coral2bg("Hello World", Style = 0 ) = it's return coral2bg color text without any style       \n
                coral2bg("Hello World", Style = 1 ) = it's return coral2bg color text with bold text          \n
                coral2bg("Hello World", Style = 2 ) = it's return coral2bg color text with light text         \n
                coral2bg("Hello World", Style = 3 ) = it's return coral2bg color text with Italicized style   \n
                coral2bg("Hello World", Style = 4 ) = it's return coral2bg color text with UnderLine          \n
                coral2bg("Hello World", Style = 5 ) = it's return Blinking coral2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 106, 80)
                


def coral3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the coral3bg colored BackGround text.\n
        coral3bg() is a BackGround Function, if You add ForeGround property given text you can use coral3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                coral3bg("Hello World", Style = 0 ) = it's return coral3bg color text without any style       \n
                coral3bg("Hello World", Style = 1 ) = it's return coral3bg color text with bold text          \n
                coral3bg("Hello World", Style = 2 ) = it's return coral3bg color text with light text         \n
                coral3bg("Hello World", Style = 3 ) = it's return coral3bg color text with Italicized style   \n
                coral3bg("Hello World", Style = 4 ) = it's return coral3bg color text with UnderLine          \n
                coral3bg("Hello World", Style = 5 ) = it's return Blinking coral3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 91, 69)
                


def coral4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the coral4bg colored BackGround text.\n
        coral4bg() is a BackGround Function, if You add ForeGround property given text you can use coral4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                coral4bg("Hello World", Style = 0 ) = it's return coral4bg color text without any style       \n
                coral4bg("Hello World", Style = 1 ) = it's return coral4bg color text with bold text          \n
                coral4bg("Hello World", Style = 2 ) = it's return coral4bg color text with light text         \n
                coral4bg("Hello World", Style = 3 ) = it's return coral4bg color text with Italicized style   \n
                coral4bg("Hello World", Style = 4 ) = it's return coral4bg color text with UnderLine          \n
                coral4bg("Hello World", Style = 5 ) = it's return Blinking coral4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 62, 47)
                


def honeydewbg( text : str, style : int = default_style ) -> str :
        """
        It will return the honeydewbg colored BackGround text.\n
        honeydewbg() is a BackGround Function, if You add ForeGround property given text you can use honeydew .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                honeydewbg("Hello World", Style = 0 ) = it's return honeydewbg color text without any style       \n
                honeydewbg("Hello World", Style = 1 ) = it's return honeydewbg color text with bold text          \n
                honeydewbg("Hello World", Style = 2 ) = it's return honeydewbg color text with light text         \n
                honeydewbg("Hello World", Style = 3 ) = it's return honeydewbg color text with Italicized style   \n
                honeydewbg("Hello World", Style = 4 ) = it's return honeydewbg color text with UnderLine          \n
                honeydewbg("Hello World", Style = 5 ) = it's return Blinking honeydewbg color text                \n
        """
        return Colors.back_ground_color(text, style, 240, 255, 240)
                


def honeydew1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the honeydew1bg colored BackGround text.\n
        honeydew1bg() is a BackGround Function, if You add ForeGround property given text you can use honeydew1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                honeydew1bg("Hello World", Style = 0 ) = it's return honeydew1bg color text without any style       \n
                honeydew1bg("Hello World", Style = 1 ) = it's return honeydew1bg color text with bold text          \n
                honeydew1bg("Hello World", Style = 2 ) = it's return honeydew1bg color text with light text         \n
                honeydew1bg("Hello World", Style = 3 ) = it's return honeydew1bg color text with Italicized style   \n
                honeydew1bg("Hello World", Style = 4 ) = it's return honeydew1bg color text with UnderLine          \n
                honeydew1bg("Hello World", Style = 5 ) = it's return Blinking honeydew1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 240, 255, 240)
                


def honeydew2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the honeydew2bg colored BackGround text.\n
        honeydew2bg() is a BackGround Function, if You add ForeGround property given text you can use honeydew2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                honeydew2bg("Hello World", Style = 0 ) = it's return honeydew2bg color text without any style       \n
                honeydew2bg("Hello World", Style = 1 ) = it's return honeydew2bg color text with bold text          \n
                honeydew2bg("Hello World", Style = 2 ) = it's return honeydew2bg color text with light text         \n
                honeydew2bg("Hello World", Style = 3 ) = it's return honeydew2bg color text with Italicized style   \n
                honeydew2bg("Hello World", Style = 4 ) = it's return honeydew2bg color text with UnderLine          \n
                honeydew2bg("Hello World", Style = 5 ) = it's return Blinking honeydew2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 224, 238, 224)
                


def honeydew3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the honeydew3bg colored BackGround text.\n
        honeydew3bg() is a BackGround Function, if You add ForeGround property given text you can use honeydew3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                honeydew3bg("Hello World", Style = 0 ) = it's return honeydew3bg color text without any style       \n
                honeydew3bg("Hello World", Style = 1 ) = it's return honeydew3bg color text with bold text          \n
                honeydew3bg("Hello World", Style = 2 ) = it's return honeydew3bg color text with light text         \n
                honeydew3bg("Hello World", Style = 3 ) = it's return honeydew3bg color text with Italicized style   \n
                honeydew3bg("Hello World", Style = 4 ) = it's return honeydew3bg color text with UnderLine          \n
                honeydew3bg("Hello World", Style = 5 ) = it's return Blinking honeydew3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 193, 205, 193)
                


def honeydew4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the honeydew4bg colored BackGround text.\n
        honeydew4bg() is a BackGround Function, if You add ForeGround property given text you can use honeydew4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                honeydew4bg("Hello World", Style = 0 ) = it's return honeydew4bg color text without any style       \n
                honeydew4bg("Hello World", Style = 1 ) = it's return honeydew4bg color text with bold text          \n
                honeydew4bg("Hello World", Style = 2 ) = it's return honeydew4bg color text with light text         \n
                honeydew4bg("Hello World", Style = 3 ) = it's return honeydew4bg color text with Italicized style   \n
                honeydew4bg("Hello World", Style = 4 ) = it's return honeydew4bg color text with UnderLine          \n
                honeydew4bg("Hello World", Style = 5 ) = it's return Blinking honeydew4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 131, 139, 131)
                


def orangebg( text : str, style : int = default_style ) -> str :
        """
        It will return the orangebg colored BackGround text.\n
        orangebg() is a BackGround Function, if You add ForeGround property given text you can use orange .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orangebg("Hello World", Style = 0 ) = it's return orangebg color text without any style       \n
                orangebg("Hello World", Style = 1 ) = it's return orangebg color text with bold text          \n
                orangebg("Hello World", Style = 2 ) = it's return orangebg color text with light text         \n
                orangebg("Hello World", Style = 3 ) = it's return orangebg color text with Italicized style   \n
                orangebg("Hello World", Style = 4 ) = it's return orangebg color text with UnderLine          \n
                orangebg("Hello World", Style = 5 ) = it's return Blinking orangebg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 165, 0)
                


def orange1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orange1bg colored BackGround text.\n
        orange1bg() is a BackGround Function, if You add ForeGround property given text you can use orange1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orange1bg("Hello World", Style = 0 ) = it's return orange1bg color text without any style       \n
                orange1bg("Hello World", Style = 1 ) = it's return orange1bg color text with bold text          \n
                orange1bg("Hello World", Style = 2 ) = it's return orange1bg color text with light text         \n
                orange1bg("Hello World", Style = 3 ) = it's return orange1bg color text with Italicized style   \n
                orange1bg("Hello World", Style = 4 ) = it's return orange1bg color text with UnderLine          \n
                orange1bg("Hello World", Style = 5 ) = it's return Blinking orange1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 165, 0)
                


def orange2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orange2bg colored BackGround text.\n
        orange2bg() is a BackGround Function, if You add ForeGround property given text you can use orange2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orange2bg("Hello World", Style = 0 ) = it's return orange2bg color text without any style       \n
                orange2bg("Hello World", Style = 1 ) = it's return orange2bg color text with bold text          \n
                orange2bg("Hello World", Style = 2 ) = it's return orange2bg color text with light text         \n
                orange2bg("Hello World", Style = 3 ) = it's return orange2bg color text with Italicized style   \n
                orange2bg("Hello World", Style = 4 ) = it's return orange2bg color text with UnderLine          \n
                orange2bg("Hello World", Style = 5 ) = it's return Blinking orange2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 154, 0)
                


def orange3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orange3bg colored BackGround text.\n
        orange3bg() is a BackGround Function, if You add ForeGround property given text you can use orange3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orange3bg("Hello World", Style = 0 ) = it's return orange3bg color text without any style       \n
                orange3bg("Hello World", Style = 1 ) = it's return orange3bg color text with bold text          \n
                orange3bg("Hello World", Style = 2 ) = it's return orange3bg color text with light text         \n
                orange3bg("Hello World", Style = 3 ) = it's return orange3bg color text with Italicized style   \n
                orange3bg("Hello World", Style = 4 ) = it's return orange3bg color text with UnderLine          \n
                orange3bg("Hello World", Style = 5 ) = it's return Blinking orange3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 133, 0)
                


def orange4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orange4bg colored BackGround text.\n
        orange4bg() is a BackGround Function, if You add ForeGround property given text you can use orange4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orange4bg("Hello World", Style = 0 ) = it's return orange4bg color text without any style       \n
                orange4bg("Hello World", Style = 1 ) = it's return orange4bg color text with bold text          \n
                orange4bg("Hello World", Style = 2 ) = it's return orange4bg color text with light text         \n
                orange4bg("Hello World", Style = 3 ) = it's return orange4bg color text with Italicized style   \n
                orange4bg("Hello World", Style = 4 ) = it's return orange4bg color text with UnderLine          \n
                orange4bg("Hello World", Style = 5 ) = it's return Blinking orange4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 90, 0)
                


def salmonbg( text : str, style : int = default_style ) -> str :
        """
        It will return the salmonbg colored BackGround text.\n
        salmonbg() is a BackGround Function, if You add ForeGround property given text you can use salmon .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                salmonbg("Hello World", Style = 0 ) = it's return salmonbg color text without any style       \n
                salmonbg("Hello World", Style = 1 ) = it's return salmonbg color text with bold text          \n
                salmonbg("Hello World", Style = 2 ) = it's return salmonbg color text with light text         \n
                salmonbg("Hello World", Style = 3 ) = it's return salmonbg color text with Italicized style   \n
                salmonbg("Hello World", Style = 4 ) = it's return salmonbg color text with UnderLine          \n
                salmonbg("Hello World", Style = 5 ) = it's return Blinking salmonbg color text                \n
        """
        return Colors.back_ground_color(text, style, 250, 128, 114)
                


def salmon1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the salmon1bg colored BackGround text.\n
        salmon1bg() is a BackGround Function, if You add ForeGround property given text you can use salmon1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                salmon1bg("Hello World", Style = 0 ) = it's return salmon1bg color text without any style       \n
                salmon1bg("Hello World", Style = 1 ) = it's return salmon1bg color text with bold text          \n
                salmon1bg("Hello World", Style = 2 ) = it's return salmon1bg color text with light text         \n
                salmon1bg("Hello World", Style = 3 ) = it's return salmon1bg color text with Italicized style   \n
                salmon1bg("Hello World", Style = 4 ) = it's return salmon1bg color text with UnderLine          \n
                salmon1bg("Hello World", Style = 5 ) = it's return Blinking salmon1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 140, 105)
                


def salmon2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the salmon2bg colored BackGround text.\n
        salmon2bg() is a BackGround Function, if You add ForeGround property given text you can use salmon2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                salmon2bg("Hello World", Style = 0 ) = it's return salmon2bg color text without any style       \n
                salmon2bg("Hello World", Style = 1 ) = it's return salmon2bg color text with bold text          \n
                salmon2bg("Hello World", Style = 2 ) = it's return salmon2bg color text with light text         \n
                salmon2bg("Hello World", Style = 3 ) = it's return salmon2bg color text with Italicized style   \n
                salmon2bg("Hello World", Style = 4 ) = it's return salmon2bg color text with UnderLine          \n
                salmon2bg("Hello World", Style = 5 ) = it's return Blinking salmon2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 130, 98)
                


def salmon3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the salmon3bg colored BackGround text.\n
        salmon3bg() is a BackGround Function, if You add ForeGround property given text you can use salmon3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                salmon3bg("Hello World", Style = 0 ) = it's return salmon3bg color text without any style       \n
                salmon3bg("Hello World", Style = 1 ) = it's return salmon3bg color text with bold text          \n
                salmon3bg("Hello World", Style = 2 ) = it's return salmon3bg color text with light text         \n
                salmon3bg("Hello World", Style = 3 ) = it's return salmon3bg color text with Italicized style   \n
                salmon3bg("Hello World", Style = 4 ) = it's return salmon3bg color text with UnderLine          \n
                salmon3bg("Hello World", Style = 5 ) = it's return Blinking salmon3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 112, 84)
                


def salmon4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the salmon4bg colored BackGround text.\n
        salmon4bg() is a BackGround Function, if You add ForeGround property given text you can use salmon4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                salmon4bg("Hello World", Style = 0 ) = it's return salmon4bg color text without any style       \n
                salmon4bg("Hello World", Style = 1 ) = it's return salmon4bg color text with bold text          \n
                salmon4bg("Hello World", Style = 2 ) = it's return salmon4bg color text with light text         \n
                salmon4bg("Hello World", Style = 3 ) = it's return salmon4bg color text with Italicized style   \n
                salmon4bg("Hello World", Style = 4 ) = it's return salmon4bg color text with UnderLine          \n
                salmon4bg("Hello World", Style = 5 ) = it's return Blinking salmon4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 76, 57)
                


def siennabg( text : str, style : int = default_style ) -> str :
        """
        It will return the siennabg colored BackGround text.\n
        siennabg() is a BackGround Function, if You add ForeGround property given text you can use sienna .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                siennabg("Hello World", Style = 0 ) = it's return siennabg color text without any style       \n
                siennabg("Hello World", Style = 1 ) = it's return siennabg color text with bold text          \n
                siennabg("Hello World", Style = 2 ) = it's return siennabg color text with light text         \n
                siennabg("Hello World", Style = 3 ) = it's return siennabg color text with Italicized style   \n
                siennabg("Hello World", Style = 4 ) = it's return siennabg color text with UnderLine          \n
                siennabg("Hello World", Style = 5 ) = it's return Blinking siennabg color text                \n
        """
        return Colors.back_ground_color(text, style, 160, 82, 45)
                


def sienna1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the sienna1bg colored BackGround text.\n
        sienna1bg() is a BackGround Function, if You add ForeGround property given text you can use sienna1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                sienna1bg("Hello World", Style = 0 ) = it's return sienna1bg color text without any style       \n
                sienna1bg("Hello World", Style = 1 ) = it's return sienna1bg color text with bold text          \n
                sienna1bg("Hello World", Style = 2 ) = it's return sienna1bg color text with light text         \n
                sienna1bg("Hello World", Style = 3 ) = it's return sienna1bg color text with Italicized style   \n
                sienna1bg("Hello World", Style = 4 ) = it's return sienna1bg color text with UnderLine          \n
                sienna1bg("Hello World", Style = 5 ) = it's return Blinking sienna1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 130, 71)
                


def sienna2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the sienna2bg colored BackGround text.\n
        sienna2bg() is a BackGround Function, if You add ForeGround property given text you can use sienna2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                sienna2bg("Hello World", Style = 0 ) = it's return sienna2bg color text without any style       \n
                sienna2bg("Hello World", Style = 1 ) = it's return sienna2bg color text with bold text          \n
                sienna2bg("Hello World", Style = 2 ) = it's return sienna2bg color text with light text         \n
                sienna2bg("Hello World", Style = 3 ) = it's return sienna2bg color text with Italicized style   \n
                sienna2bg("Hello World", Style = 4 ) = it's return sienna2bg color text with UnderLine          \n
                sienna2bg("Hello World", Style = 5 ) = it's return Blinking sienna2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 121, 66)
                


def sienna3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the sienna3bg colored BackGround text.\n
        sienna3bg() is a BackGround Function, if You add ForeGround property given text you can use sienna3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                sienna3bg("Hello World", Style = 0 ) = it's return sienna3bg color text without any style       \n
                sienna3bg("Hello World", Style = 1 ) = it's return sienna3bg color text with bold text          \n
                sienna3bg("Hello World", Style = 2 ) = it's return sienna3bg color text with light text         \n
                sienna3bg("Hello World", Style = 3 ) = it's return sienna3bg color text with Italicized style   \n
                sienna3bg("Hello World", Style = 4 ) = it's return sienna3bg color text with UnderLine          \n
                sienna3bg("Hello World", Style = 5 ) = it's return Blinking sienna3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 104, 57)
                


def sienna4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the sienna4bg colored BackGround text.\n
        sienna4bg() is a BackGround Function, if You add ForeGround property given text you can use sienna4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                sienna4bg("Hello World", Style = 0 ) = it's return sienna4bg color text without any style       \n
                sienna4bg("Hello World", Style = 1 ) = it's return sienna4bg color text with bold text          \n
                sienna4bg("Hello World", Style = 2 ) = it's return sienna4bg color text with light text         \n
                sienna4bg("Hello World", Style = 3 ) = it's return sienna4bg color text with Italicized style   \n
                sienna4bg("Hello World", Style = 4 ) = it's return sienna4bg color text with UnderLine          \n
                sienna4bg("Hello World", Style = 5 ) = it's return Blinking sienna4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 71, 38)
                


def mandarian_orangebg( text : str, style : int = default_style ) -> str :
        """
        It will return the mandarian_orangebg colored BackGround text.\n
        mandarian_orangebg() is a BackGround Function, if You add ForeGround property given text you can use Mandarian_Orange .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mandarian_orangebg("Hello World", Style = 0 ) = it's return mandarian_orangebg color text without any style       \n
                mandarian_orangebg("Hello World", Style = 1 ) = it's return mandarian_orangebg color text with bold text          \n
                mandarian_orangebg("Hello World", Style = 2 ) = it's return mandarian_orangebg color text with light text         \n
                mandarian_orangebg("Hello World", Style = 3 ) = it's return mandarian_orangebg color text with Italicized style   \n
                mandarian_orangebg("Hello World", Style = 4 ) = it's return mandarian_orangebg color text with UnderLine          \n
                mandarian_orangebg("Hello World", Style = 5 ) = it's return Blinking mandarian_orangebg color text                \n
        """
        return Colors.back_ground_color(text, style, 142, 35, 35)
                


def orangebg( text : str, style : int = default_style ) -> str :
        """
        It will return the orangebg colored BackGround text.\n
        orangebg() is a BackGround Function, if You add ForeGround property given text you can use Orange .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orangebg("Hello World", Style = 0 ) = it's return orangebg color text without any style       \n
                orangebg("Hello World", Style = 1 ) = it's return orangebg color text with bold text          \n
                orangebg("Hello World", Style = 2 ) = it's return orangebg color text with light text         \n
                orangebg("Hello World", Style = 3 ) = it's return orangebg color text with Italicized style   \n
                orangebg("Hello World", Style = 4 ) = it's return orangebg color text with UnderLine          \n
                orangebg("Hello World", Style = 5 ) = it's return Blinking orangebg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 127, 0)
                


def orange_redbg( text : str, style : int = default_style ) -> str :
        """
        It will return the orange_redbg colored BackGround text.\n
        orange_redbg() is a BackGround Function, if You add ForeGround property given text you can use Orange_Red .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orange_redbg("Hello World", Style = 0 ) = it's return orange_redbg color text without any style       \n
                orange_redbg("Hello World", Style = 1 ) = it's return orange_redbg color text with bold text          \n
                orange_redbg("Hello World", Style = 2 ) = it's return orange_redbg color text with light text         \n
                orange_redbg("Hello World", Style = 3 ) = it's return orange_redbg color text with Italicized style   \n
                orange_redbg("Hello World", Style = 4 ) = it's return orange_redbg color text with UnderLine          \n
                orange_redbg("Hello World", Style = 5 ) = it's return Blinking orange_redbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 36, 0)
                


def deeppinkbg( text : str, style : int = default_style ) -> str :
        """
        It will return the deeppinkbg colored BackGround text.\n
        deeppinkbg() is a BackGround Function, if You add ForeGround property given text you can use DeepPink .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                deeppinkbg("Hello World", Style = 0 ) = it's return deeppinkbg color text without any style       \n
                deeppinkbg("Hello World", Style = 1 ) = it's return deeppinkbg color text with bold text          \n
                deeppinkbg("Hello World", Style = 2 ) = it's return deeppinkbg color text with light text         \n
                deeppinkbg("Hello World", Style = 3 ) = it's return deeppinkbg color text with Italicized style   \n
                deeppinkbg("Hello World", Style = 4 ) = it's return deeppinkbg color text with UnderLine          \n
                deeppinkbg("Hello World", Style = 5 ) = it's return Blinking deeppinkbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 20, 147)
                


def deeppink1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the deeppink1bg colored BackGround text.\n
        deeppink1bg() is a BackGround Function, if You add ForeGround property given text you can use DeepPink1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                deeppink1bg("Hello World", Style = 0 ) = it's return deeppink1bg color text without any style       \n
                deeppink1bg("Hello World", Style = 1 ) = it's return deeppink1bg color text with bold text          \n
                deeppink1bg("Hello World", Style = 2 ) = it's return deeppink1bg color text with light text         \n
                deeppink1bg("Hello World", Style = 3 ) = it's return deeppink1bg color text with Italicized style   \n
                deeppink1bg("Hello World", Style = 4 ) = it's return deeppink1bg color text with UnderLine          \n
                deeppink1bg("Hello World", Style = 5 ) = it's return Blinking deeppink1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 20, 147)
                


def deeppink2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the deeppink2bg colored BackGround text.\n
        deeppink2bg() is a BackGround Function, if You add ForeGround property given text you can use DeepPink2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                deeppink2bg("Hello World", Style = 0 ) = it's return deeppink2bg color text without any style       \n
                deeppink2bg("Hello World", Style = 1 ) = it's return deeppink2bg color text with bold text          \n
                deeppink2bg("Hello World", Style = 2 ) = it's return deeppink2bg color text with light text         \n
                deeppink2bg("Hello World", Style = 3 ) = it's return deeppink2bg color text with Italicized style   \n
                deeppink2bg("Hello World", Style = 4 ) = it's return deeppink2bg color text with UnderLine          \n
                deeppink2bg("Hello World", Style = 5 ) = it's return Blinking deeppink2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 18, 137)
                


def deeppink3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the deeppink3bg colored BackGround text.\n
        deeppink3bg() is a BackGround Function, if You add ForeGround property given text you can use DeepPink3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                deeppink3bg("Hello World", Style = 0 ) = it's return deeppink3bg color text without any style       \n
                deeppink3bg("Hello World", Style = 1 ) = it's return deeppink3bg color text with bold text          \n
                deeppink3bg("Hello World", Style = 2 ) = it's return deeppink3bg color text with light text         \n
                deeppink3bg("Hello World", Style = 3 ) = it's return deeppink3bg color text with Italicized style   \n
                deeppink3bg("Hello World", Style = 4 ) = it's return deeppink3bg color text with UnderLine          \n
                deeppink3bg("Hello World", Style = 5 ) = it's return Blinking deeppink3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 16, 118)
                


def deeppink4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the deeppink4bg colored BackGround text.\n
        deeppink4bg() is a BackGround Function, if You add ForeGround property given text you can use DeepPink4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                deeppink4bg("Hello World", Style = 0 ) = it's return deeppink4bg color text without any style       \n
                deeppink4bg("Hello World", Style = 1 ) = it's return deeppink4bg color text with bold text          \n
                deeppink4bg("Hello World", Style = 2 ) = it's return deeppink4bg color text with light text         \n
                deeppink4bg("Hello World", Style = 3 ) = it's return deeppink4bg color text with Italicized style   \n
                deeppink4bg("Hello World", Style = 4 ) = it's return deeppink4bg color text with UnderLine          \n
                deeppink4bg("Hello World", Style = 5 ) = it's return Blinking deeppink4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 10, 80)
                


def hotpinkbg( text : str, style : int = default_style ) -> str :
        """
        It will return the hotpinkbg colored BackGround text.\n
        hotpinkbg() is a BackGround Function, if You add ForeGround property given text you can use HotPink .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                hotpinkbg("Hello World", Style = 0 ) = it's return hotpinkbg color text without any style       \n
                hotpinkbg("Hello World", Style = 1 ) = it's return hotpinkbg color text with bold text          \n
                hotpinkbg("Hello World", Style = 2 ) = it's return hotpinkbg color text with light text         \n
                hotpinkbg("Hello World", Style = 3 ) = it's return hotpinkbg color text with Italicized style   \n
                hotpinkbg("Hello World", Style = 4 ) = it's return hotpinkbg color text with UnderLine          \n
                hotpinkbg("Hello World", Style = 5 ) = it's return Blinking hotpinkbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 105, 180)
                


def hotpink1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the hotpink1bg colored BackGround text.\n
        hotpink1bg() is a BackGround Function, if You add ForeGround property given text you can use HotPink1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                hotpink1bg("Hello World", Style = 0 ) = it's return hotpink1bg color text without any style       \n
                hotpink1bg("Hello World", Style = 1 ) = it's return hotpink1bg color text with bold text          \n
                hotpink1bg("Hello World", Style = 2 ) = it's return hotpink1bg color text with light text         \n
                hotpink1bg("Hello World", Style = 3 ) = it's return hotpink1bg color text with Italicized style   \n
                hotpink1bg("Hello World", Style = 4 ) = it's return hotpink1bg color text with UnderLine          \n
                hotpink1bg("Hello World", Style = 5 ) = it's return Blinking hotpink1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 110, 180)
                


def hotpink2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the hotpink2bg colored BackGround text.\n
        hotpink2bg() is a BackGround Function, if You add ForeGround property given text you can use HotPink2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                hotpink2bg("Hello World", Style = 0 ) = it's return hotpink2bg color text without any style       \n
                hotpink2bg("Hello World", Style = 1 ) = it's return hotpink2bg color text with bold text          \n
                hotpink2bg("Hello World", Style = 2 ) = it's return hotpink2bg color text with light text         \n
                hotpink2bg("Hello World", Style = 3 ) = it's return hotpink2bg color text with Italicized style   \n
                hotpink2bg("Hello World", Style = 4 ) = it's return hotpink2bg color text with UnderLine          \n
                hotpink2bg("Hello World", Style = 5 ) = it's return Blinking hotpink2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 106, 167)
                


def hotpink3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the hotpink3bg colored BackGround text.\n
        hotpink3bg() is a BackGround Function, if You add ForeGround property given text you can use HotPink3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                hotpink3bg("Hello World", Style = 0 ) = it's return hotpink3bg color text without any style       \n
                hotpink3bg("Hello World", Style = 1 ) = it's return hotpink3bg color text with bold text          \n
                hotpink3bg("Hello World", Style = 2 ) = it's return hotpink3bg color text with light text         \n
                hotpink3bg("Hello World", Style = 3 ) = it's return hotpink3bg color text with Italicized style   \n
                hotpink3bg("Hello World", Style = 4 ) = it's return hotpink3bg color text with UnderLine          \n
                hotpink3bg("Hello World", Style = 5 ) = it's return Blinking hotpink3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 96, 144)
                


def hotpink4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the hotpink4bg colored BackGround text.\n
        hotpink4bg() is a BackGround Function, if You add ForeGround property given text you can use HotPink4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                hotpink4bg("Hello World", Style = 0 ) = it's return hotpink4bg color text without any style       \n
                hotpink4bg("Hello World", Style = 1 ) = it's return hotpink4bg color text with bold text          \n
                hotpink4bg("Hello World", Style = 2 ) = it's return hotpink4bg color text with light text         \n
                hotpink4bg("Hello World", Style = 3 ) = it's return hotpink4bg color text with Italicized style   \n
                hotpink4bg("Hello World", Style = 4 ) = it's return hotpink4bg color text with UnderLine          \n
                hotpink4bg("Hello World", Style = 5 ) = it's return Blinking hotpink4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 58, 98)
                


def indianredbg( text : str, style : int = default_style ) -> str :
        """
        It will return the indianredbg colored BackGround text.\n
        indianredbg() is a BackGround Function, if You add ForeGround property given text you can use IndianRed .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                indianredbg("Hello World", Style = 0 ) = it's return indianredbg color text without any style       \n
                indianredbg("Hello World", Style = 1 ) = it's return indianredbg color text with bold text          \n
                indianredbg("Hello World", Style = 2 ) = it's return indianredbg color text with light text         \n
                indianredbg("Hello World", Style = 3 ) = it's return indianredbg color text with Italicized style   \n
                indianredbg("Hello World", Style = 4 ) = it's return indianredbg color text with UnderLine          \n
                indianredbg("Hello World", Style = 5 ) = it's return Blinking indianredbg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 92, 92)
                


def indianred1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the indianred1bg colored BackGround text.\n
        indianred1bg() is a BackGround Function, if You add ForeGround property given text you can use IndianRed1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                indianred1bg("Hello World", Style = 0 ) = it's return indianred1bg color text without any style       \n
                indianred1bg("Hello World", Style = 1 ) = it's return indianred1bg color text with bold text          \n
                indianred1bg("Hello World", Style = 2 ) = it's return indianred1bg color text with light text         \n
                indianred1bg("Hello World", Style = 3 ) = it's return indianred1bg color text with Italicized style   \n
                indianred1bg("Hello World", Style = 4 ) = it's return indianred1bg color text with UnderLine          \n
                indianred1bg("Hello World", Style = 5 ) = it's return Blinking indianred1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 106, 106)
                


def indianred2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the indianred2bg colored BackGround text.\n
        indianred2bg() is a BackGround Function, if You add ForeGround property given text you can use IndianRed2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                indianred2bg("Hello World", Style = 0 ) = it's return indianred2bg color text without any style       \n
                indianred2bg("Hello World", Style = 1 ) = it's return indianred2bg color text with bold text          \n
                indianred2bg("Hello World", Style = 2 ) = it's return indianred2bg color text with light text         \n
                indianred2bg("Hello World", Style = 3 ) = it's return indianred2bg color text with Italicized style   \n
                indianred2bg("Hello World", Style = 4 ) = it's return indianred2bg color text with UnderLine          \n
                indianred2bg("Hello World", Style = 5 ) = it's return Blinking indianred2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 99, 99)
                


def indianred3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the indianred3bg colored BackGround text.\n
        indianred3bg() is a BackGround Function, if You add ForeGround property given text you can use IndianRed3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                indianred3bg("Hello World", Style = 0 ) = it's return indianred3bg color text without any style       \n
                indianred3bg("Hello World", Style = 1 ) = it's return indianred3bg color text with bold text          \n
                indianred3bg("Hello World", Style = 2 ) = it's return indianred3bg color text with light text         \n
                indianred3bg("Hello World", Style = 3 ) = it's return indianred3bg color text with Italicized style   \n
                indianred3bg("Hello World", Style = 4 ) = it's return indianred3bg color text with UnderLine          \n
                indianred3bg("Hello World", Style = 5 ) = it's return Blinking indianred3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 85, 85)
                


def indianred4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the indianred4bg colored BackGround text.\n
        indianred4bg() is a BackGround Function, if You add ForeGround property given text you can use IndianRed4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                indianred4bg("Hello World", Style = 0 ) = it's return indianred4bg color text without any style       \n
                indianred4bg("Hello World", Style = 1 ) = it's return indianred4bg color text with bold text          \n
                indianred4bg("Hello World", Style = 2 ) = it's return indianred4bg color text with light text         \n
                indianred4bg("Hello World", Style = 3 ) = it's return indianred4bg color text with Italicized style   \n
                indianred4bg("Hello World", Style = 4 ) = it's return indianred4bg color text with UnderLine          \n
                indianred4bg("Hello World", Style = 5 ) = it's return Blinking indianred4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 58, 58)
                


def lightpinkbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightpinkbg colored BackGround text.\n
        lightpinkbg() is a BackGround Function, if You add ForeGround property given text you can use LightPink .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightpinkbg("Hello World", Style = 0 ) = it's return lightpinkbg color text without any style       \n
                lightpinkbg("Hello World", Style = 1 ) = it's return lightpinkbg color text with bold text          \n
                lightpinkbg("Hello World", Style = 2 ) = it's return lightpinkbg color text with light text         \n
                lightpinkbg("Hello World", Style = 3 ) = it's return lightpinkbg color text with Italicized style   \n
                lightpinkbg("Hello World", Style = 4 ) = it's return lightpinkbg color text with UnderLine          \n
                lightpinkbg("Hello World", Style = 5 ) = it's return Blinking lightpinkbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 182, 193)
                


def lightpink1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightpink1bg colored BackGround text.\n
        lightpink1bg() is a BackGround Function, if You add ForeGround property given text you can use LightPink1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightpink1bg("Hello World", Style = 0 ) = it's return lightpink1bg color text without any style       \n
                lightpink1bg("Hello World", Style = 1 ) = it's return lightpink1bg color text with bold text          \n
                lightpink1bg("Hello World", Style = 2 ) = it's return lightpink1bg color text with light text         \n
                lightpink1bg("Hello World", Style = 3 ) = it's return lightpink1bg color text with Italicized style   \n
                lightpink1bg("Hello World", Style = 4 ) = it's return lightpink1bg color text with UnderLine          \n
                lightpink1bg("Hello World", Style = 5 ) = it's return Blinking lightpink1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 174, 185)
                


def lightpink2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightpink2bg colored BackGround text.\n
        lightpink2bg() is a BackGround Function, if You add ForeGround property given text you can use LightPink2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightpink2bg("Hello World", Style = 0 ) = it's return lightpink2bg color text without any style       \n
                lightpink2bg("Hello World", Style = 1 ) = it's return lightpink2bg color text with bold text          \n
                lightpink2bg("Hello World", Style = 2 ) = it's return lightpink2bg color text with light text         \n
                lightpink2bg("Hello World", Style = 3 ) = it's return lightpink2bg color text with Italicized style   \n
                lightpink2bg("Hello World", Style = 4 ) = it's return lightpink2bg color text with UnderLine          \n
                lightpink2bg("Hello World", Style = 5 ) = it's return Blinking lightpink2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 162, 173)
                


def lightpink3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightpink3bg colored BackGround text.\n
        lightpink3bg() is a BackGround Function, if You add ForeGround property given text you can use LightPink3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightpink3bg("Hello World", Style = 0 ) = it's return lightpink3bg color text without any style       \n
                lightpink3bg("Hello World", Style = 1 ) = it's return lightpink3bg color text with bold text          \n
                lightpink3bg("Hello World", Style = 2 ) = it's return lightpink3bg color text with light text         \n
                lightpink3bg("Hello World", Style = 3 ) = it's return lightpink3bg color text with Italicized style   \n
                lightpink3bg("Hello World", Style = 4 ) = it's return lightpink3bg color text with UnderLine          \n
                lightpink3bg("Hello World", Style = 5 ) = it's return Blinking lightpink3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 140, 149)
                


def lightpink4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightpink4bg colored BackGround text.\n
        lightpink4bg() is a BackGround Function, if You add ForeGround property given text you can use LightPink4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightpink4bg("Hello World", Style = 0 ) = it's return lightpink4bg color text without any style       \n
                lightpink4bg("Hello World", Style = 1 ) = it's return lightpink4bg color text with bold text          \n
                lightpink4bg("Hello World", Style = 2 ) = it's return lightpink4bg color text with light text         \n
                lightpink4bg("Hello World", Style = 3 ) = it's return lightpink4bg color text with Italicized style   \n
                lightpink4bg("Hello World", Style = 4 ) = it's return lightpink4bg color text with UnderLine          \n
                lightpink4bg("Hello World", Style = 5 ) = it's return Blinking lightpink4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 95, 101)
                


def mediumvioletredbg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumvioletredbg colored BackGround text.\n
        mediumvioletredbg() is a BackGround Function, if You add ForeGround property given text you can use MediumVioletRed .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumvioletredbg("Hello World", Style = 0 ) = it's return mediumvioletredbg color text without any style       \n
                mediumvioletredbg("Hello World", Style = 1 ) = it's return mediumvioletredbg color text with bold text          \n
                mediumvioletredbg("Hello World", Style = 2 ) = it's return mediumvioletredbg color text with light text         \n
                mediumvioletredbg("Hello World", Style = 3 ) = it's return mediumvioletredbg color text with Italicized style   \n
                mediumvioletredbg("Hello World", Style = 4 ) = it's return mediumvioletredbg color text with UnderLine          \n
                mediumvioletredbg("Hello World", Style = 5 ) = it's return Blinking mediumvioletredbg color text                \n
        """
        return Colors.back_ground_color(text, style, 199, 21, 133)
                


def mistyrosebg( text : str, style : int = default_style ) -> str :
        """
        It will return the mistyrosebg colored BackGround text.\n
        mistyrosebg() is a BackGround Function, if You add ForeGround property given text you can use MistyRose .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mistyrosebg("Hello World", Style = 0 ) = it's return mistyrosebg color text without any style       \n
                mistyrosebg("Hello World", Style = 1 ) = it's return mistyrosebg color text with bold text          \n
                mistyrosebg("Hello World", Style = 2 ) = it's return mistyrosebg color text with light text         \n
                mistyrosebg("Hello World", Style = 3 ) = it's return mistyrosebg color text with Italicized style   \n
                mistyrosebg("Hello World", Style = 4 ) = it's return mistyrosebg color text with UnderLine          \n
                mistyrosebg("Hello World", Style = 5 ) = it's return Blinking mistyrosebg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 228, 225)
                


def mistyrose1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mistyrose1bg colored BackGround text.\n
        mistyrose1bg() is a BackGround Function, if You add ForeGround property given text you can use MistyRose1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mistyrose1bg("Hello World", Style = 0 ) = it's return mistyrose1bg color text without any style       \n
                mistyrose1bg("Hello World", Style = 1 ) = it's return mistyrose1bg color text with bold text          \n
                mistyrose1bg("Hello World", Style = 2 ) = it's return mistyrose1bg color text with light text         \n
                mistyrose1bg("Hello World", Style = 3 ) = it's return mistyrose1bg color text with Italicized style   \n
                mistyrose1bg("Hello World", Style = 4 ) = it's return mistyrose1bg color text with UnderLine          \n
                mistyrose1bg("Hello World", Style = 5 ) = it's return Blinking mistyrose1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 228, 225)
                


def mistyrose2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mistyrose2bg colored BackGround text.\n
        mistyrose2bg() is a BackGround Function, if You add ForeGround property given text you can use MistyRose2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mistyrose2bg("Hello World", Style = 0 ) = it's return mistyrose2bg color text without any style       \n
                mistyrose2bg("Hello World", Style = 1 ) = it's return mistyrose2bg color text with bold text          \n
                mistyrose2bg("Hello World", Style = 2 ) = it's return mistyrose2bg color text with light text         \n
                mistyrose2bg("Hello World", Style = 3 ) = it's return mistyrose2bg color text with Italicized style   \n
                mistyrose2bg("Hello World", Style = 4 ) = it's return mistyrose2bg color text with UnderLine          \n
                mistyrose2bg("Hello World", Style = 5 ) = it's return Blinking mistyrose2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 213, 210)
                


def mistyrose3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mistyrose3bg colored BackGround text.\n
        mistyrose3bg() is a BackGround Function, if You add ForeGround property given text you can use MistyRose3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mistyrose3bg("Hello World", Style = 0 ) = it's return mistyrose3bg color text without any style       \n
                mistyrose3bg("Hello World", Style = 1 ) = it's return mistyrose3bg color text with bold text          \n
                mistyrose3bg("Hello World", Style = 2 ) = it's return mistyrose3bg color text with light text         \n
                mistyrose3bg("Hello World", Style = 3 ) = it's return mistyrose3bg color text with Italicized style   \n
                mistyrose3bg("Hello World", Style = 4 ) = it's return mistyrose3bg color text with UnderLine          \n
                mistyrose3bg("Hello World", Style = 5 ) = it's return Blinking mistyrose3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 183, 181)
                


def mistyrose4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mistyrose4bg colored BackGround text.\n
        mistyrose4bg() is a BackGround Function, if You add ForeGround property given text you can use MistyRose4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mistyrose4bg("Hello World", Style = 0 ) = it's return mistyrose4bg color text without any style       \n
                mistyrose4bg("Hello World", Style = 1 ) = it's return mistyrose4bg color text with bold text          \n
                mistyrose4bg("Hello World", Style = 2 ) = it's return mistyrose4bg color text with light text         \n
                mistyrose4bg("Hello World", Style = 3 ) = it's return mistyrose4bg color text with Italicized style   \n
                mistyrose4bg("Hello World", Style = 4 ) = it's return mistyrose4bg color text with UnderLine          \n
                mistyrose4bg("Hello World", Style = 5 ) = it's return Blinking mistyrose4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 125, 123)
                


def orangeredbg( text : str, style : int = default_style ) -> str :
        """
        It will return the orangeredbg colored BackGround text.\n
        orangeredbg() is a BackGround Function, if You add ForeGround property given text you can use OrangeRed .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orangeredbg("Hello World", Style = 0 ) = it's return orangeredbg color text without any style       \n
                orangeredbg("Hello World", Style = 1 ) = it's return orangeredbg color text with bold text          \n
                orangeredbg("Hello World", Style = 2 ) = it's return orangeredbg color text with light text         \n
                orangeredbg("Hello World", Style = 3 ) = it's return orangeredbg color text with Italicized style   \n
                orangeredbg("Hello World", Style = 4 ) = it's return orangeredbg color text with UnderLine          \n
                orangeredbg("Hello World", Style = 5 ) = it's return Blinking orangeredbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 69, 0)
                


def orangered1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orangered1bg colored BackGround text.\n
        orangered1bg() is a BackGround Function, if You add ForeGround property given text you can use OrangeRed1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orangered1bg("Hello World", Style = 0 ) = it's return orangered1bg color text without any style       \n
                orangered1bg("Hello World", Style = 1 ) = it's return orangered1bg color text with bold text          \n
                orangered1bg("Hello World", Style = 2 ) = it's return orangered1bg color text with light text         \n
                orangered1bg("Hello World", Style = 3 ) = it's return orangered1bg color text with Italicized style   \n
                orangered1bg("Hello World", Style = 4 ) = it's return orangered1bg color text with UnderLine          \n
                orangered1bg("Hello World", Style = 5 ) = it's return Blinking orangered1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 69, 0)
                


def orangered2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orangered2bg colored BackGround text.\n
        orangered2bg() is a BackGround Function, if You add ForeGround property given text you can use OrangeRed2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orangered2bg("Hello World", Style = 0 ) = it's return orangered2bg color text without any style       \n
                orangered2bg("Hello World", Style = 1 ) = it's return orangered2bg color text with bold text          \n
                orangered2bg("Hello World", Style = 2 ) = it's return orangered2bg color text with light text         \n
                orangered2bg("Hello World", Style = 3 ) = it's return orangered2bg color text with Italicized style   \n
                orangered2bg("Hello World", Style = 4 ) = it's return orangered2bg color text with UnderLine          \n
                orangered2bg("Hello World", Style = 5 ) = it's return Blinking orangered2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 64, 0)
                


def orangered3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orangered3bg colored BackGround text.\n
        orangered3bg() is a BackGround Function, if You add ForeGround property given text you can use OrangeRed3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orangered3bg("Hello World", Style = 0 ) = it's return orangered3bg color text without any style       \n
                orangered3bg("Hello World", Style = 1 ) = it's return orangered3bg color text with bold text          \n
                orangered3bg("Hello World", Style = 2 ) = it's return orangered3bg color text with light text         \n
                orangered3bg("Hello World", Style = 3 ) = it's return orangered3bg color text with Italicized style   \n
                orangered3bg("Hello World", Style = 4 ) = it's return orangered3bg color text with UnderLine          \n
                orangered3bg("Hello World", Style = 5 ) = it's return Blinking orangered3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 55, 0)
                


def orangered4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orangered4bg colored BackGround text.\n
        orangered4bg() is a BackGround Function, if You add ForeGround property given text you can use OrangeRed4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orangered4bg("Hello World", Style = 0 ) = it's return orangered4bg color text without any style       \n
                orangered4bg("Hello World", Style = 1 ) = it's return orangered4bg color text with bold text          \n
                orangered4bg("Hello World", Style = 2 ) = it's return orangered4bg color text with light text         \n
                orangered4bg("Hello World", Style = 3 ) = it's return orangered4bg color text with Italicized style   \n
                orangered4bg("Hello World", Style = 4 ) = it's return orangered4bg color text with UnderLine          \n
                orangered4bg("Hello World", Style = 5 ) = it's return Blinking orangered4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 37, 0)
                


def palevioletredbg( text : str, style : int = default_style ) -> str :
        """
        It will return the palevioletredbg colored BackGround text.\n
        palevioletredbg() is a BackGround Function, if You add ForeGround property given text you can use PaleVioletRed .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palevioletredbg("Hello World", Style = 0 ) = it's return palevioletredbg color text without any style       \n
                palevioletredbg("Hello World", Style = 1 ) = it's return palevioletredbg color text with bold text          \n
                palevioletredbg("Hello World", Style = 2 ) = it's return palevioletredbg color text with light text         \n
                palevioletredbg("Hello World", Style = 3 ) = it's return palevioletredbg color text with Italicized style   \n
                palevioletredbg("Hello World", Style = 4 ) = it's return palevioletredbg color text with UnderLine          \n
                palevioletredbg("Hello World", Style = 5 ) = it's return Blinking palevioletredbg color text                \n
        """
        return Colors.back_ground_color(text, style, 219, 112, 147)
                


def palevioletred1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the palevioletred1bg colored BackGround text.\n
        palevioletred1bg() is a BackGround Function, if You add ForeGround property given text you can use PaleVioletRed1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palevioletred1bg("Hello World", Style = 0 ) = it's return palevioletred1bg color text without any style       \n
                palevioletred1bg("Hello World", Style = 1 ) = it's return palevioletred1bg color text with bold text          \n
                palevioletred1bg("Hello World", Style = 2 ) = it's return palevioletred1bg color text with light text         \n
                palevioletred1bg("Hello World", Style = 3 ) = it's return palevioletred1bg color text with Italicized style   \n
                palevioletred1bg("Hello World", Style = 4 ) = it's return palevioletred1bg color text with UnderLine          \n
                palevioletred1bg("Hello World", Style = 5 ) = it's return Blinking palevioletred1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 130, 171)
                


def palevioletred2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the palevioletred2bg colored BackGround text.\n
        palevioletred2bg() is a BackGround Function, if You add ForeGround property given text you can use PaleVioletRed2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palevioletred2bg("Hello World", Style = 0 ) = it's return palevioletred2bg color text without any style       \n
                palevioletred2bg("Hello World", Style = 1 ) = it's return palevioletred2bg color text with bold text          \n
                palevioletred2bg("Hello World", Style = 2 ) = it's return palevioletred2bg color text with light text         \n
                palevioletred2bg("Hello World", Style = 3 ) = it's return palevioletred2bg color text with Italicized style   \n
                palevioletred2bg("Hello World", Style = 4 ) = it's return palevioletred2bg color text with UnderLine          \n
                palevioletred2bg("Hello World", Style = 5 ) = it's return Blinking palevioletred2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 121, 159)
                


def palevioletred3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the palevioletred3bg colored BackGround text.\n
        palevioletred3bg() is a BackGround Function, if You add ForeGround property given text you can use PaleVioletRed3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palevioletred3bg("Hello World", Style = 0 ) = it's return palevioletred3bg color text without any style       \n
                palevioletred3bg("Hello World", Style = 1 ) = it's return palevioletred3bg color text with bold text          \n
                palevioletred3bg("Hello World", Style = 2 ) = it's return palevioletred3bg color text with light text         \n
                palevioletred3bg("Hello World", Style = 3 ) = it's return palevioletred3bg color text with Italicized style   \n
                palevioletred3bg("Hello World", Style = 4 ) = it's return palevioletred3bg color text with UnderLine          \n
                palevioletred3bg("Hello World", Style = 5 ) = it's return Blinking palevioletred3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 104, 137)
                


def palevioletred4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the palevioletred4bg colored BackGround text.\n
        palevioletred4bg() is a BackGround Function, if You add ForeGround property given text you can use PaleVioletRed4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palevioletred4bg("Hello World", Style = 0 ) = it's return palevioletred4bg color text without any style       \n
                palevioletred4bg("Hello World", Style = 1 ) = it's return palevioletred4bg color text with bold text          \n
                palevioletred4bg("Hello World", Style = 2 ) = it's return palevioletred4bg color text with light text         \n
                palevioletred4bg("Hello World", Style = 3 ) = it's return palevioletred4bg color text with Italicized style   \n
                palevioletred4bg("Hello World", Style = 4 ) = it's return palevioletred4bg color text with UnderLine          \n
                palevioletred4bg("Hello World", Style = 5 ) = it's return Blinking palevioletred4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 71, 93)
                


def violetredbg( text : str, style : int = default_style ) -> str :
        """
        It will return the violetredbg colored BackGround text.\n
        violetredbg() is a BackGround Function, if You add ForeGround property given text you can use VioletRed .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                violetredbg("Hello World", Style = 0 ) = it's return violetredbg color text without any style       \n
                violetredbg("Hello World", Style = 1 ) = it's return violetredbg color text with bold text          \n
                violetredbg("Hello World", Style = 2 ) = it's return violetredbg color text with light text         \n
                violetredbg("Hello World", Style = 3 ) = it's return violetredbg color text with Italicized style   \n
                violetredbg("Hello World", Style = 4 ) = it's return violetredbg color text with UnderLine          \n
                violetredbg("Hello World", Style = 5 ) = it's return Blinking violetredbg color text                \n
        """
        return Colors.back_ground_color(text, style, 208, 32, 144)
                


def violetred1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the violetred1bg colored BackGround text.\n
        violetred1bg() is a BackGround Function, if You add ForeGround property given text you can use VioletRed1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                violetred1bg("Hello World", Style = 0 ) = it's return violetred1bg color text without any style       \n
                violetred1bg("Hello World", Style = 1 ) = it's return violetred1bg color text with bold text          \n
                violetred1bg("Hello World", Style = 2 ) = it's return violetred1bg color text with light text         \n
                violetred1bg("Hello World", Style = 3 ) = it's return violetred1bg color text with Italicized style   \n
                violetred1bg("Hello World", Style = 4 ) = it's return violetred1bg color text with UnderLine          \n
                violetred1bg("Hello World", Style = 5 ) = it's return Blinking violetred1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 62, 150)
                


def violetred2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the violetred2bg colored BackGround text.\n
        violetred2bg() is a BackGround Function, if You add ForeGround property given text you can use VioletRed2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                violetred2bg("Hello World", Style = 0 ) = it's return violetred2bg color text without any style       \n
                violetred2bg("Hello World", Style = 1 ) = it's return violetred2bg color text with bold text          \n
                violetred2bg("Hello World", Style = 2 ) = it's return violetred2bg color text with light text         \n
                violetred2bg("Hello World", Style = 3 ) = it's return violetred2bg color text with Italicized style   \n
                violetred2bg("Hello World", Style = 4 ) = it's return violetred2bg color text with UnderLine          \n
                violetred2bg("Hello World", Style = 5 ) = it's return Blinking violetred2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 58, 140)
                


def violetred3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the violetred3bg colored BackGround text.\n
        violetred3bg() is a BackGround Function, if You add ForeGround property given text you can use VioletRed3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                violetred3bg("Hello World", Style = 0 ) = it's return violetred3bg color text without any style       \n
                violetred3bg("Hello World", Style = 1 ) = it's return violetred3bg color text with bold text          \n
                violetred3bg("Hello World", Style = 2 ) = it's return violetred3bg color text with light text         \n
                violetred3bg("Hello World", Style = 3 ) = it's return violetred3bg color text with Italicized style   \n
                violetred3bg("Hello World", Style = 4 ) = it's return violetred3bg color text with UnderLine          \n
                violetred3bg("Hello World", Style = 5 ) = it's return Blinking violetred3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 50, 120)
                


def violetred4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the violetred4bg colored BackGround text.\n
        violetred4bg() is a BackGround Function, if You add ForeGround property given text you can use VioletRed4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                violetred4bg("Hello World", Style = 0 ) = it's return violetred4bg color text without any style       \n
                violetred4bg("Hello World", Style = 1 ) = it's return violetred4bg color text with bold text          \n
                violetred4bg("Hello World", Style = 2 ) = it's return violetred4bg color text with light text         \n
                violetred4bg("Hello World", Style = 3 ) = it's return violetred4bg color text with Italicized style   \n
                violetred4bg("Hello World", Style = 4 ) = it's return violetred4bg color text with UnderLine          \n
                violetred4bg("Hello World", Style = 5 ) = it's return Blinking violetred4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 34, 82)
                


def firebrickbg( text : str, style : int = default_style ) -> str :
        """
        It will return the firebrickbg colored BackGround text.\n
        firebrickbg() is a BackGround Function, if You add ForeGround property given text you can use firebrick .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                firebrickbg("Hello World", Style = 0 ) = it's return firebrickbg color text without any style       \n
                firebrickbg("Hello World", Style = 1 ) = it's return firebrickbg color text with bold text          \n
                firebrickbg("Hello World", Style = 2 ) = it's return firebrickbg color text with light text         \n
                firebrickbg("Hello World", Style = 3 ) = it's return firebrickbg color text with Italicized style   \n
                firebrickbg("Hello World", Style = 4 ) = it's return firebrickbg color text with UnderLine          \n
                firebrickbg("Hello World", Style = 5 ) = it's return Blinking firebrickbg color text                \n
        """
        return Colors.back_ground_color(text, style, 178, 34, 34)
                


def firebrick1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the firebrick1bg colored BackGround text.\n
        firebrick1bg() is a BackGround Function, if You add ForeGround property given text you can use firebrick1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                firebrick1bg("Hello World", Style = 0 ) = it's return firebrick1bg color text without any style       \n
                firebrick1bg("Hello World", Style = 1 ) = it's return firebrick1bg color text with bold text          \n
                firebrick1bg("Hello World", Style = 2 ) = it's return firebrick1bg color text with light text         \n
                firebrick1bg("Hello World", Style = 3 ) = it's return firebrick1bg color text with Italicized style   \n
                firebrick1bg("Hello World", Style = 4 ) = it's return firebrick1bg color text with UnderLine          \n
                firebrick1bg("Hello World", Style = 5 ) = it's return Blinking firebrick1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 48, 48)
                


def firebrick2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the firebrick2bg colored BackGround text.\n
        firebrick2bg() is a BackGround Function, if You add ForeGround property given text you can use firebrick2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                firebrick2bg("Hello World", Style = 0 ) = it's return firebrick2bg color text without any style       \n
                firebrick2bg("Hello World", Style = 1 ) = it's return firebrick2bg color text with bold text          \n
                firebrick2bg("Hello World", Style = 2 ) = it's return firebrick2bg color text with light text         \n
                firebrick2bg("Hello World", Style = 3 ) = it's return firebrick2bg color text with Italicized style   \n
                firebrick2bg("Hello World", Style = 4 ) = it's return firebrick2bg color text with UnderLine          \n
                firebrick2bg("Hello World", Style = 5 ) = it's return Blinking firebrick2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 44, 44)
                


def firebrick3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the firebrick3bg colored BackGround text.\n
        firebrick3bg() is a BackGround Function, if You add ForeGround property given text you can use firebrick3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                firebrick3bg("Hello World", Style = 0 ) = it's return firebrick3bg color text without any style       \n
                firebrick3bg("Hello World", Style = 1 ) = it's return firebrick3bg color text with bold text          \n
                firebrick3bg("Hello World", Style = 2 ) = it's return firebrick3bg color text with light text         \n
                firebrick3bg("Hello World", Style = 3 ) = it's return firebrick3bg color text with Italicized style   \n
                firebrick3bg("Hello World", Style = 4 ) = it's return firebrick3bg color text with UnderLine          \n
                firebrick3bg("Hello World", Style = 5 ) = it's return Blinking firebrick3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 38, 38)
                


def firebrick4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the firebrick4bg colored BackGround text.\n
        firebrick4bg() is a BackGround Function, if You add ForeGround property given text you can use firebrick4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                firebrick4bg("Hello World", Style = 0 ) = it's return firebrick4bg color text without any style       \n
                firebrick4bg("Hello World", Style = 1 ) = it's return firebrick4bg color text with bold text          \n
                firebrick4bg("Hello World", Style = 2 ) = it's return firebrick4bg color text with light text         \n
                firebrick4bg("Hello World", Style = 3 ) = it's return firebrick4bg color text with Italicized style   \n
                firebrick4bg("Hello World", Style = 4 ) = it's return firebrick4bg color text with UnderLine          \n
                firebrick4bg("Hello World", Style = 5 ) = it's return Blinking firebrick4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 26, 26)
                


def pinkbg( text : str, style : int = default_style ) -> str :
        """
        It will return the pinkbg colored BackGround text.\n
        pinkbg() is a BackGround Function, if You add ForeGround property given text you can use pink .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                pinkbg("Hello World", Style = 0 ) = it's return pinkbg color text without any style       \n
                pinkbg("Hello World", Style = 1 ) = it's return pinkbg color text with bold text          \n
                pinkbg("Hello World", Style = 2 ) = it's return pinkbg color text with light text         \n
                pinkbg("Hello World", Style = 3 ) = it's return pinkbg color text with Italicized style   \n
                pinkbg("Hello World", Style = 4 ) = it's return pinkbg color text with UnderLine          \n
                pinkbg("Hello World", Style = 5 ) = it's return Blinking pinkbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 192, 203)
                


def pink1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the pink1bg colored BackGround text.\n
        pink1bg() is a BackGround Function, if You add ForeGround property given text you can use pink1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                pink1bg("Hello World", Style = 0 ) = it's return pink1bg color text without any style       \n
                pink1bg("Hello World", Style = 1 ) = it's return pink1bg color text with bold text          \n
                pink1bg("Hello World", Style = 2 ) = it's return pink1bg color text with light text         \n
                pink1bg("Hello World", Style = 3 ) = it's return pink1bg color text with Italicized style   \n
                pink1bg("Hello World", Style = 4 ) = it's return pink1bg color text with UnderLine          \n
                pink1bg("Hello World", Style = 5 ) = it's return Blinking pink1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 181, 197)
                


def pink2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the pink2bg colored BackGround text.\n
        pink2bg() is a BackGround Function, if You add ForeGround property given text you can use pink2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                pink2bg("Hello World", Style = 0 ) = it's return pink2bg color text without any style       \n
                pink2bg("Hello World", Style = 1 ) = it's return pink2bg color text with bold text          \n
                pink2bg("Hello World", Style = 2 ) = it's return pink2bg color text with light text         \n
                pink2bg("Hello World", Style = 3 ) = it's return pink2bg color text with Italicized style   \n
                pink2bg("Hello World", Style = 4 ) = it's return pink2bg color text with UnderLine          \n
                pink2bg("Hello World", Style = 5 ) = it's return Blinking pink2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 169, 184)
                


def pink3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the pink3bg colored BackGround text.\n
        pink3bg() is a BackGround Function, if You add ForeGround property given text you can use pink3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                pink3bg("Hello World", Style = 0 ) = it's return pink3bg color text without any style       \n
                pink3bg("Hello World", Style = 1 ) = it's return pink3bg color text with bold text          \n
                pink3bg("Hello World", Style = 2 ) = it's return pink3bg color text with light text         \n
                pink3bg("Hello World", Style = 3 ) = it's return pink3bg color text with Italicized style   \n
                pink3bg("Hello World", Style = 4 ) = it's return pink3bg color text with UnderLine          \n
                pink3bg("Hello World", Style = 5 ) = it's return Blinking pink3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 145, 158)
                


def pink4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the pink4bg colored BackGround text.\n
        pink4bg() is a BackGround Function, if You add ForeGround property given text you can use pink4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                pink4bg("Hello World", Style = 0 ) = it's return pink4bg color text without any style       \n
                pink4bg("Hello World", Style = 1 ) = it's return pink4bg color text with bold text          \n
                pink4bg("Hello World", Style = 2 ) = it's return pink4bg color text with light text         \n
                pink4bg("Hello World", Style = 3 ) = it's return pink4bg color text with Italicized style   \n
                pink4bg("Hello World", Style = 4 ) = it's return pink4bg color text with UnderLine          \n
                pink4bg("Hello World", Style = 5 ) = it's return Blinking pink4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 99, 108)
                


def fleshbg( text : str, style : int = default_style ) -> str :
        """
        It will return the fleshbg colored BackGround text.\n
        fleshbg() is a BackGround Function, if You add ForeGround property given text you can use Flesh .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                fleshbg("Hello World", Style = 0 ) = it's return fleshbg color text without any style       \n
                fleshbg("Hello World", Style = 1 ) = it's return fleshbg color text with bold text          \n
                fleshbg("Hello World", Style = 2 ) = it's return fleshbg color text with light text         \n
                fleshbg("Hello World", Style = 3 ) = it's return fleshbg color text with Italicized style   \n
                fleshbg("Hello World", Style = 4 ) = it's return fleshbg color text with UnderLine          \n
                fleshbg("Hello World", Style = 5 ) = it's return Blinking fleshbg color text                \n
        """
        return Colors.back_ground_color(text, style, 245, 204, 176)
                


def feldsparbg( text : str, style : int = default_style ) -> str :
        """
        It will return the feldsparbg colored BackGround text.\n
        feldsparbg() is a BackGround Function, if You add ForeGround property given text you can use Feldspar .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                feldsparbg("Hello World", Style = 0 ) = it's return feldsparbg color text without any style       \n
                feldsparbg("Hello World", Style = 1 ) = it's return feldsparbg color text with bold text          \n
                feldsparbg("Hello World", Style = 2 ) = it's return feldsparbg color text with light text         \n
                feldsparbg("Hello World", Style = 3 ) = it's return feldsparbg color text with Italicized style   \n
                feldsparbg("Hello World", Style = 4 ) = it's return feldsparbg color text with UnderLine          \n
                feldsparbg("Hello World", Style = 5 ) = it's return Blinking feldsparbg color text                \n
        """
        return Colors.back_ground_color(text, style, 209, 146, 117)
                


def redbg( text : str, style : int = default_style ) -> str :
        """
        It will return the redbg colored BackGround text.\n
        redbg() is a BackGround Function, if You add ForeGround property given text you can use red .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                redbg("Hello World", Style = 0 ) = it's return redbg color text without any style       \n
                redbg("Hello World", Style = 1 ) = it's return redbg color text with bold text          \n
                redbg("Hello World", Style = 2 ) = it's return redbg color text with light text         \n
                redbg("Hello World", Style = 3 ) = it's return redbg color text with Italicized style   \n
                redbg("Hello World", Style = 4 ) = it's return redbg color text with UnderLine          \n
                redbg("Hello World", Style = 5 ) = it's return Blinking redbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 0, 0)
                


def red1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the red1bg colored BackGround text.\n
        red1bg() is a BackGround Function, if You add ForeGround property given text you can use red1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                red1bg("Hello World", Style = 0 ) = it's return red1bg color text without any style       \n
                red1bg("Hello World", Style = 1 ) = it's return red1bg color text with bold text          \n
                red1bg("Hello World", Style = 2 ) = it's return red1bg color text with light text         \n
                red1bg("Hello World", Style = 3 ) = it's return red1bg color text with Italicized style   \n
                red1bg("Hello World", Style = 4 ) = it's return red1bg color text with UnderLine          \n
                red1bg("Hello World", Style = 5 ) = it's return Blinking red1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 0, 0)
                


def red2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the red2bg colored BackGround text.\n
        red2bg() is a BackGround Function, if You add ForeGround property given text you can use red2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                red2bg("Hello World", Style = 0 ) = it's return red2bg color text without any style       \n
                red2bg("Hello World", Style = 1 ) = it's return red2bg color text with bold text          \n
                red2bg("Hello World", Style = 2 ) = it's return red2bg color text with light text         \n
                red2bg("Hello World", Style = 3 ) = it's return red2bg color text with Italicized style   \n
                red2bg("Hello World", Style = 4 ) = it's return red2bg color text with UnderLine          \n
                red2bg("Hello World", Style = 5 ) = it's return Blinking red2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 0, 0)
                


def red3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the red3bg colored BackGround text.\n
        red3bg() is a BackGround Function, if You add ForeGround property given text you can use red3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                red3bg("Hello World", Style = 0 ) = it's return red3bg color text without any style       \n
                red3bg("Hello World", Style = 1 ) = it's return red3bg color text with bold text          \n
                red3bg("Hello World", Style = 2 ) = it's return red3bg color text with light text         \n
                red3bg("Hello World", Style = 3 ) = it's return red3bg color text with Italicized style   \n
                red3bg("Hello World", Style = 4 ) = it's return red3bg color text with UnderLine          \n
                red3bg("Hello World", Style = 5 ) = it's return Blinking red3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 0, 0)
                


def red4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the red4bg colored BackGround text.\n
        red4bg() is a BackGround Function, if You add ForeGround property given text you can use red4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                red4bg("Hello World", Style = 0 ) = it's return red4bg color text without any style       \n
                red4bg("Hello World", Style = 1 ) = it's return red4bg color text with bold text          \n
                red4bg("Hello World", Style = 2 ) = it's return red4bg color text with light text         \n
                red4bg("Hello World", Style = 3 ) = it's return red4bg color text with Italicized style   \n
                red4bg("Hello World", Style = 4 ) = it's return red4bg color text with UnderLine          \n
                red4bg("Hello World", Style = 5 ) = it's return Blinking red4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 0, 0)
                


def tomatobg( text : str, style : int = default_style ) -> str :
        """
        It will return the tomatobg colored BackGround text.\n
        tomatobg() is a BackGround Function, if You add ForeGround property given text you can use tomato .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tomatobg("Hello World", Style = 0 ) = it's return tomatobg color text without any style       \n
                tomatobg("Hello World", Style = 1 ) = it's return tomatobg color text with bold text          \n
                tomatobg("Hello World", Style = 2 ) = it's return tomatobg color text with light text         \n
                tomatobg("Hello World", Style = 3 ) = it's return tomatobg color text with Italicized style   \n
                tomatobg("Hello World", Style = 4 ) = it's return tomatobg color text with UnderLine          \n
                tomatobg("Hello World", Style = 5 ) = it's return Blinking tomatobg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 99, 71)
                


def tomato1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the tomato1bg colored BackGround text.\n
        tomato1bg() is a BackGround Function, if You add ForeGround property given text you can use tomato1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tomato1bg("Hello World", Style = 0 ) = it's return tomato1bg color text without any style       \n
                tomato1bg("Hello World", Style = 1 ) = it's return tomato1bg color text with bold text          \n
                tomato1bg("Hello World", Style = 2 ) = it's return tomato1bg color text with light text         \n
                tomato1bg("Hello World", Style = 3 ) = it's return tomato1bg color text with Italicized style   \n
                tomato1bg("Hello World", Style = 4 ) = it's return tomato1bg color text with UnderLine          \n
                tomato1bg("Hello World", Style = 5 ) = it's return Blinking tomato1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 99, 71)
                


def tomato2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the tomato2bg colored BackGround text.\n
        tomato2bg() is a BackGround Function, if You add ForeGround property given text you can use tomato2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tomato2bg("Hello World", Style = 0 ) = it's return tomato2bg color text without any style       \n
                tomato2bg("Hello World", Style = 1 ) = it's return tomato2bg color text with bold text          \n
                tomato2bg("Hello World", Style = 2 ) = it's return tomato2bg color text with light text         \n
                tomato2bg("Hello World", Style = 3 ) = it's return tomato2bg color text with Italicized style   \n
                tomato2bg("Hello World", Style = 4 ) = it's return tomato2bg color text with UnderLine          \n
                tomato2bg("Hello World", Style = 5 ) = it's return Blinking tomato2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 92, 66)
                


def tomato3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the tomato3bg colored BackGround text.\n
        tomato3bg() is a BackGround Function, if You add ForeGround property given text you can use tomato3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tomato3bg("Hello World", Style = 0 ) = it's return tomato3bg color text without any style       \n
                tomato3bg("Hello World", Style = 1 ) = it's return tomato3bg color text with bold text          \n
                tomato3bg("Hello World", Style = 2 ) = it's return tomato3bg color text with light text         \n
                tomato3bg("Hello World", Style = 3 ) = it's return tomato3bg color text with Italicized style   \n
                tomato3bg("Hello World", Style = 4 ) = it's return tomato3bg color text with UnderLine          \n
                tomato3bg("Hello World", Style = 5 ) = it's return Blinking tomato3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 79, 57)
                


def tomato4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the tomato4bg colored BackGround text.\n
        tomato4bg() is a BackGround Function, if You add ForeGround property given text you can use tomato4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                tomato4bg("Hello World", Style = 0 ) = it's return tomato4bg color text without any style       \n
                tomato4bg("Hello World", Style = 1 ) = it's return tomato4bg color text with bold text          \n
                tomato4bg("Hello World", Style = 2 ) = it's return tomato4bg color text with light text         \n
                tomato4bg("Hello World", Style = 3 ) = it's return tomato4bg color text with Italicized style   \n
                tomato4bg("Hello World", Style = 4 ) = it's return tomato4bg color text with UnderLine          \n
                tomato4bg("Hello World", Style = 5 ) = it's return Blinking tomato4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 54, 38)
                


def dusty_rosebg( text : str, style : int = default_style ) -> str :
        """
        It will return the dusty_rosebg colored BackGround text.\n
        dusty_rosebg() is a BackGround Function, if You add ForeGround property given text you can use Dusty_Rose .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dusty_rosebg("Hello World", Style = 0 ) = it's return dusty_rosebg color text without any style       \n
                dusty_rosebg("Hello World", Style = 1 ) = it's return dusty_rosebg color text with bold text          \n
                dusty_rosebg("Hello World", Style = 2 ) = it's return dusty_rosebg color text with light text         \n
                dusty_rosebg("Hello World", Style = 3 ) = it's return dusty_rosebg color text with Italicized style   \n
                dusty_rosebg("Hello World", Style = 4 ) = it's return dusty_rosebg color text with UnderLine          \n
                dusty_rosebg("Hello World", Style = 5 ) = it's return Blinking dusty_rosebg color text                \n
        """
        return Colors.back_ground_color(text, style, 133, 99, 99)
                


def firebrickbg( text : str, style : int = default_style ) -> str :
        """
        It will return the firebrickbg colored BackGround text.\n
        firebrickbg() is a BackGround Function, if You add ForeGround property given text you can use Firebrick .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                firebrickbg("Hello World", Style = 0 ) = it's return firebrickbg color text without any style       \n
                firebrickbg("Hello World", Style = 1 ) = it's return firebrickbg color text with bold text          \n
                firebrickbg("Hello World", Style = 2 ) = it's return firebrickbg color text with light text         \n
                firebrickbg("Hello World", Style = 3 ) = it's return firebrickbg color text with Italicized style   \n
                firebrickbg("Hello World", Style = 4 ) = it's return firebrickbg color text with UnderLine          \n
                firebrickbg("Hello World", Style = 5 ) = it's return Blinking firebrickbg color text                \n
        """
        return Colors.back_ground_color(text, style, 142, 35, 35)
                


def indian_redbg( text : str, style : int = default_style ) -> str :
        """
        It will return the indian_redbg colored BackGround text.\n
        indian_redbg() is a BackGround Function, if You add ForeGround property given text you can use Indian_Red .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                indian_redbg("Hello World", Style = 0 ) = it's return indian_redbg color text without any style       \n
                indian_redbg("Hello World", Style = 1 ) = it's return indian_redbg color text with bold text          \n
                indian_redbg("Hello World", Style = 2 ) = it's return indian_redbg color text with light text         \n
                indian_redbg("Hello World", Style = 3 ) = it's return indian_redbg color text with Italicized style   \n
                indian_redbg("Hello World", Style = 4 ) = it's return indian_redbg color text with UnderLine          \n
                indian_redbg("Hello World", Style = 5 ) = it's return Blinking indian_redbg color text                \n
        """
        return Colors.back_ground_color(text, style, 245, 204, 176)
                


def pinkbg( text : str, style : int = default_style ) -> str :
        """
        It will return the pinkbg colored BackGround text.\n
        pinkbg() is a BackGround Function, if You add ForeGround property given text you can use Pink .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                pinkbg("Hello World", Style = 0 ) = it's return pinkbg color text without any style       \n
                pinkbg("Hello World", Style = 1 ) = it's return pinkbg color text with bold text          \n
                pinkbg("Hello World", Style = 2 ) = it's return pinkbg color text with light text         \n
                pinkbg("Hello World", Style = 3 ) = it's return pinkbg color text with Italicized style   \n
                pinkbg("Hello World", Style = 4 ) = it's return pinkbg color text with UnderLine          \n
                pinkbg("Hello World", Style = 5 ) = it's return Blinking pinkbg color text                \n
        """
        return Colors.back_ground_color(text, style, 188, 143, 143)
                


def salmonbg( text : str, style : int = default_style ) -> str :
        """
        It will return the salmonbg colored BackGround text.\n
        salmonbg() is a BackGround Function, if You add ForeGround property given text you can use Salmon .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                salmonbg("Hello World", Style = 0 ) = it's return salmonbg color text without any style       \n
                salmonbg("Hello World", Style = 1 ) = it's return salmonbg color text with bold text          \n
                salmonbg("Hello World", Style = 2 ) = it's return salmonbg color text with light text         \n
                salmonbg("Hello World", Style = 3 ) = it's return salmonbg color text with Italicized style   \n
                salmonbg("Hello World", Style = 4 ) = it's return salmonbg color text with UnderLine          \n
                salmonbg("Hello World", Style = 5 ) = it's return Blinking salmonbg color text                \n
        """
        return Colors.back_ground_color(text, style, 111, 66, 66)
                


def scarletbg( text : str, style : int = default_style ) -> str :
        """
        It will return the scarletbg colored BackGround text.\n
        scarletbg() is a BackGround Function, if You add ForeGround property given text you can use Scarlet .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                scarletbg("Hello World", Style = 0 ) = it's return scarletbg color text without any style       \n
                scarletbg("Hello World", Style = 1 ) = it's return scarletbg color text with bold text          \n
                scarletbg("Hello World", Style = 2 ) = it's return scarletbg color text with light text         \n
                scarletbg("Hello World", Style = 3 ) = it's return scarletbg color text with Italicized style   \n
                scarletbg("Hello World", Style = 4 ) = it's return scarletbg color text with UnderLine          \n
                scarletbg("Hello World", Style = 5 ) = it's return Blinking scarletbg color text                \n
        """
        return Colors.back_ground_color(text, style, 140, 23, 23)
                


def spicy_pinkbg( text : str, style : int = default_style ) -> str :
        """
        It will return the spicy_pinkbg colored BackGround text.\n
        spicy_pinkbg() is a BackGround Function, if You add ForeGround property given text you can use Spicy_Pink .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                spicy_pinkbg("Hello World", Style = 0 ) = it's return spicy_pinkbg color text without any style       \n
                spicy_pinkbg("Hello World", Style = 1 ) = it's return spicy_pinkbg color text with bold text          \n
                spicy_pinkbg("Hello World", Style = 2 ) = it's return spicy_pinkbg color text with light text         \n
                spicy_pinkbg("Hello World", Style = 3 ) = it's return spicy_pinkbg color text with Italicized style   \n
                spicy_pinkbg("Hello World", Style = 4 ) = it's return spicy_pinkbg color text with UnderLine          \n
                spicy_pinkbg("Hello World", Style = 5 ) = it's return Blinking spicy_pinkbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 28, 174)
                


def free_speech_magentabg( text : str, style : int = default_style ) -> str :
        """
        It will return the free_speech_magentabg colored BackGround text.\n
        free_speech_magentabg() is a BackGround Function, if You add ForeGround property given text you can use Free_Speech_Magenta .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                free_speech_magentabg("Hello World", Style = 0 ) = it's return free_speech_magentabg color text without any style       \n
                free_speech_magentabg("Hello World", Style = 1 ) = it's return free_speech_magentabg color text with bold text          \n
                free_speech_magentabg("Hello World", Style = 2 ) = it's return free_speech_magentabg color text with light text         \n
                free_speech_magentabg("Hello World", Style = 3 ) = it's return free_speech_magentabg color text with Italicized style   \n
                free_speech_magentabg("Hello World", Style = 4 ) = it's return free_speech_magentabg color text with UnderLine          \n
                free_speech_magentabg("Hello World", Style = 5 ) = it's return Blinking free_speech_magentabg color text                \n
        """
        return Colors.back_ground_color(text, style, 227, 91, 216)
                


def free_speech_redbg( text : str, style : int = default_style ) -> str :
        """
        It will return the free_speech_redbg colored BackGround text.\n
        free_speech_redbg() is a BackGround Function, if You add ForeGround property given text you can use Free_Speech_Red .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                free_speech_redbg("Hello World", Style = 0 ) = it's return free_speech_redbg color text without any style       \n
                free_speech_redbg("Hello World", Style = 1 ) = it's return free_speech_redbg color text with bold text          \n
                free_speech_redbg("Hello World", Style = 2 ) = it's return free_speech_redbg color text with light text         \n
                free_speech_redbg("Hello World", Style = 3 ) = it's return free_speech_redbg color text with Italicized style   \n
                free_speech_redbg("Hello World", Style = 4 ) = it's return free_speech_redbg color text with UnderLine          \n
                free_speech_redbg("Hello World", Style = 5 ) = it's return Blinking free_speech_redbg color text                \n
        """
        return Colors.back_ground_color(text, style, 192, 0, 0)
                


def darkorchidbg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkorchidbg colored BackGround text.\n
        darkorchidbg() is a BackGround Function, if You add ForeGround property given text you can use DarkOrchid .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkorchidbg("Hello World", Style = 0 ) = it's return darkorchidbg color text without any style       \n
                darkorchidbg("Hello World", Style = 1 ) = it's return darkorchidbg color text with bold text          \n
                darkorchidbg("Hello World", Style = 2 ) = it's return darkorchidbg color text with light text         \n
                darkorchidbg("Hello World", Style = 3 ) = it's return darkorchidbg color text with Italicized style   \n
                darkorchidbg("Hello World", Style = 4 ) = it's return darkorchidbg color text with UnderLine          \n
                darkorchidbg("Hello World", Style = 5 ) = it's return Blinking darkorchidbg color text                \n
        """
        return Colors.back_ground_color(text, style, 153, 50, 204)
                


def darkorchid1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkorchid1bg colored BackGround text.\n
        darkorchid1bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOrchid1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkorchid1bg("Hello World", Style = 0 ) = it's return darkorchid1bg color text without any style       \n
                darkorchid1bg("Hello World", Style = 1 ) = it's return darkorchid1bg color text with bold text          \n
                darkorchid1bg("Hello World", Style = 2 ) = it's return darkorchid1bg color text with light text         \n
                darkorchid1bg("Hello World", Style = 3 ) = it's return darkorchid1bg color text with Italicized style   \n
                darkorchid1bg("Hello World", Style = 4 ) = it's return darkorchid1bg color text with UnderLine          \n
                darkorchid1bg("Hello World", Style = 5 ) = it's return Blinking darkorchid1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 191, 62, 255)
                


def darkorchid2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkorchid2bg colored BackGround text.\n
        darkorchid2bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOrchid2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkorchid2bg("Hello World", Style = 0 ) = it's return darkorchid2bg color text without any style       \n
                darkorchid2bg("Hello World", Style = 1 ) = it's return darkorchid2bg color text with bold text          \n
                darkorchid2bg("Hello World", Style = 2 ) = it's return darkorchid2bg color text with light text         \n
                darkorchid2bg("Hello World", Style = 3 ) = it's return darkorchid2bg color text with Italicized style   \n
                darkorchid2bg("Hello World", Style = 4 ) = it's return darkorchid2bg color text with UnderLine          \n
                darkorchid2bg("Hello World", Style = 5 ) = it's return Blinking darkorchid2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 178, 58, 238)
                


def darkorchid3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkorchid3bg colored BackGround text.\n
        darkorchid3bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOrchid3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkorchid3bg("Hello World", Style = 0 ) = it's return darkorchid3bg color text without any style       \n
                darkorchid3bg("Hello World", Style = 1 ) = it's return darkorchid3bg color text with bold text          \n
                darkorchid3bg("Hello World", Style = 2 ) = it's return darkorchid3bg color text with light text         \n
                darkorchid3bg("Hello World", Style = 3 ) = it's return darkorchid3bg color text with Italicized style   \n
                darkorchid3bg("Hello World", Style = 4 ) = it's return darkorchid3bg color text with UnderLine          \n
                darkorchid3bg("Hello World", Style = 5 ) = it's return Blinking darkorchid3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 154, 50, 205)
                


def darkorchid4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkorchid4bg colored BackGround text.\n
        darkorchid4bg() is a BackGround Function, if You add ForeGround property given text you can use DarkOrchid4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkorchid4bg("Hello World", Style = 0 ) = it's return darkorchid4bg color text without any style       \n
                darkorchid4bg("Hello World", Style = 1 ) = it's return darkorchid4bg color text with bold text          \n
                darkorchid4bg("Hello World", Style = 2 ) = it's return darkorchid4bg color text with light text         \n
                darkorchid4bg("Hello World", Style = 3 ) = it's return darkorchid4bg color text with Italicized style   \n
                darkorchid4bg("Hello World", Style = 4 ) = it's return darkorchid4bg color text with UnderLine          \n
                darkorchid4bg("Hello World", Style = 5 ) = it's return Blinking darkorchid4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 104, 34, 139)
                


def darkvioletbg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkvioletbg colored BackGround text.\n
        darkvioletbg() is a BackGround Function, if You add ForeGround property given text you can use DarkViolet .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkvioletbg("Hello World", Style = 0 ) = it's return darkvioletbg color text without any style       \n
                darkvioletbg("Hello World", Style = 1 ) = it's return darkvioletbg color text with bold text          \n
                darkvioletbg("Hello World", Style = 2 ) = it's return darkvioletbg color text with light text         \n
                darkvioletbg("Hello World", Style = 3 ) = it's return darkvioletbg color text with Italicized style   \n
                darkvioletbg("Hello World", Style = 4 ) = it's return darkvioletbg color text with UnderLine          \n
                darkvioletbg("Hello World", Style = 5 ) = it's return Blinking darkvioletbg color text                \n
        """
        return Colors.back_ground_color(text, style, 148, 0, 211)
                


def lavenderblushbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lavenderblushbg colored BackGround text.\n
        lavenderblushbg() is a BackGround Function, if You add ForeGround property given text you can use LavenderBlush .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lavenderblushbg("Hello World", Style = 0 ) = it's return lavenderblushbg color text without any style       \n
                lavenderblushbg("Hello World", Style = 1 ) = it's return lavenderblushbg color text with bold text          \n
                lavenderblushbg("Hello World", Style = 2 ) = it's return lavenderblushbg color text with light text         \n
                lavenderblushbg("Hello World", Style = 3 ) = it's return lavenderblushbg color text with Italicized style   \n
                lavenderblushbg("Hello World", Style = 4 ) = it's return lavenderblushbg color text with UnderLine          \n
                lavenderblushbg("Hello World", Style = 5 ) = it's return Blinking lavenderblushbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 240, 245)
                


def lavenderblush1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lavenderblush1bg colored BackGround text.\n
        lavenderblush1bg() is a BackGround Function, if You add ForeGround property given text you can use LavenderBlush1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lavenderblush1bg("Hello World", Style = 0 ) = it's return lavenderblush1bg color text without any style       \n
                lavenderblush1bg("Hello World", Style = 1 ) = it's return lavenderblush1bg color text with bold text          \n
                lavenderblush1bg("Hello World", Style = 2 ) = it's return lavenderblush1bg color text with light text         \n
                lavenderblush1bg("Hello World", Style = 3 ) = it's return lavenderblush1bg color text with Italicized style   \n
                lavenderblush1bg("Hello World", Style = 4 ) = it's return lavenderblush1bg color text with UnderLine          \n
                lavenderblush1bg("Hello World", Style = 5 ) = it's return Blinking lavenderblush1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 240, 245)
                


def lavenderblush2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lavenderblush2bg colored BackGround text.\n
        lavenderblush2bg() is a BackGround Function, if You add ForeGround property given text you can use LavenderBlush2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lavenderblush2bg("Hello World", Style = 0 ) = it's return lavenderblush2bg color text without any style       \n
                lavenderblush2bg("Hello World", Style = 1 ) = it's return lavenderblush2bg color text with bold text          \n
                lavenderblush2bg("Hello World", Style = 2 ) = it's return lavenderblush2bg color text with light text         \n
                lavenderblush2bg("Hello World", Style = 3 ) = it's return lavenderblush2bg color text with Italicized style   \n
                lavenderblush2bg("Hello World", Style = 4 ) = it's return lavenderblush2bg color text with UnderLine          \n
                lavenderblush2bg("Hello World", Style = 5 ) = it's return Blinking lavenderblush2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 224, 229)
                


def lavenderblush3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lavenderblush3bg colored BackGround text.\n
        lavenderblush3bg() is a BackGround Function, if You add ForeGround property given text you can use LavenderBlush3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lavenderblush3bg("Hello World", Style = 0 ) = it's return lavenderblush3bg color text without any style       \n
                lavenderblush3bg("Hello World", Style = 1 ) = it's return lavenderblush3bg color text with bold text          \n
                lavenderblush3bg("Hello World", Style = 2 ) = it's return lavenderblush3bg color text with light text         \n
                lavenderblush3bg("Hello World", Style = 3 ) = it's return lavenderblush3bg color text with Italicized style   \n
                lavenderblush3bg("Hello World", Style = 4 ) = it's return lavenderblush3bg color text with UnderLine          \n
                lavenderblush3bg("Hello World", Style = 5 ) = it's return Blinking lavenderblush3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 193, 197)
                


def lavenderblush4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lavenderblush4bg colored BackGround text.\n
        lavenderblush4bg() is a BackGround Function, if You add ForeGround property given text you can use LavenderBlush4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lavenderblush4bg("Hello World", Style = 0 ) = it's return lavenderblush4bg color text without any style       \n
                lavenderblush4bg("Hello World", Style = 1 ) = it's return lavenderblush4bg color text with bold text          \n
                lavenderblush4bg("Hello World", Style = 2 ) = it's return lavenderblush4bg color text with light text         \n
                lavenderblush4bg("Hello World", Style = 3 ) = it's return lavenderblush4bg color text with Italicized style   \n
                lavenderblush4bg("Hello World", Style = 4 ) = it's return lavenderblush4bg color text with UnderLine          \n
                lavenderblush4bg("Hello World", Style = 5 ) = it's return Blinking lavenderblush4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 131, 134)
                


def mediumorchidbg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumorchidbg colored BackGround text.\n
        mediumorchidbg() is a BackGround Function, if You add ForeGround property given text you can use MediumOrchid .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumorchidbg("Hello World", Style = 0 ) = it's return mediumorchidbg color text without any style       \n
                mediumorchidbg("Hello World", Style = 1 ) = it's return mediumorchidbg color text with bold text          \n
                mediumorchidbg("Hello World", Style = 2 ) = it's return mediumorchidbg color text with light text         \n
                mediumorchidbg("Hello World", Style = 3 ) = it's return mediumorchidbg color text with Italicized style   \n
                mediumorchidbg("Hello World", Style = 4 ) = it's return mediumorchidbg color text with UnderLine          \n
                mediumorchidbg("Hello World", Style = 5 ) = it's return Blinking mediumorchidbg color text                \n
        """
        return Colors.back_ground_color(text, style, 186, 85, 211)
                


def mediumorchid1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumorchid1bg colored BackGround text.\n
        mediumorchid1bg() is a BackGround Function, if You add ForeGround property given text you can use MediumOrchid1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumorchid1bg("Hello World", Style = 0 ) = it's return mediumorchid1bg color text without any style       \n
                mediumorchid1bg("Hello World", Style = 1 ) = it's return mediumorchid1bg color text with bold text          \n
                mediumorchid1bg("Hello World", Style = 2 ) = it's return mediumorchid1bg color text with light text         \n
                mediumorchid1bg("Hello World", Style = 3 ) = it's return mediumorchid1bg color text with Italicized style   \n
                mediumorchid1bg("Hello World", Style = 4 ) = it's return mediumorchid1bg color text with UnderLine          \n
                mediumorchid1bg("Hello World", Style = 5 ) = it's return Blinking mediumorchid1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 224, 102, 255)
                


def mediumorchid2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumorchid2bg colored BackGround text.\n
        mediumorchid2bg() is a BackGround Function, if You add ForeGround property given text you can use MediumOrchid2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumorchid2bg("Hello World", Style = 0 ) = it's return mediumorchid2bg color text without any style       \n
                mediumorchid2bg("Hello World", Style = 1 ) = it's return mediumorchid2bg color text with bold text          \n
                mediumorchid2bg("Hello World", Style = 2 ) = it's return mediumorchid2bg color text with light text         \n
                mediumorchid2bg("Hello World", Style = 3 ) = it's return mediumorchid2bg color text with Italicized style   \n
                mediumorchid2bg("Hello World", Style = 4 ) = it's return mediumorchid2bg color text with UnderLine          \n
                mediumorchid2bg("Hello World", Style = 5 ) = it's return Blinking mediumorchid2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 209, 95, 238)
                


def mediumorchid3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumorchid3bg colored BackGround text.\n
        mediumorchid3bg() is a BackGround Function, if You add ForeGround property given text you can use MediumOrchid3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumorchid3bg("Hello World", Style = 0 ) = it's return mediumorchid3bg color text without any style       \n
                mediumorchid3bg("Hello World", Style = 1 ) = it's return mediumorchid3bg color text with bold text          \n
                mediumorchid3bg("Hello World", Style = 2 ) = it's return mediumorchid3bg color text with light text         \n
                mediumorchid3bg("Hello World", Style = 3 ) = it's return mediumorchid3bg color text with Italicized style   \n
                mediumorchid3bg("Hello World", Style = 4 ) = it's return mediumorchid3bg color text with UnderLine          \n
                mediumorchid3bg("Hello World", Style = 5 ) = it's return Blinking mediumorchid3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 180, 82, 205)
                


def mediumorchid4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumorchid4bg colored BackGround text.\n
        mediumorchid4bg() is a BackGround Function, if You add ForeGround property given text you can use MediumOrchid4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumorchid4bg("Hello World", Style = 0 ) = it's return mediumorchid4bg color text without any style       \n
                mediumorchid4bg("Hello World", Style = 1 ) = it's return mediumorchid4bg color text with bold text          \n
                mediumorchid4bg("Hello World", Style = 2 ) = it's return mediumorchid4bg color text with light text         \n
                mediumorchid4bg("Hello World", Style = 3 ) = it's return mediumorchid4bg color text with Italicized style   \n
                mediumorchid4bg("Hello World", Style = 4 ) = it's return mediumorchid4bg color text with UnderLine          \n
                mediumorchid4bg("Hello World", Style = 5 ) = it's return Blinking mediumorchid4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 122, 55, 139)
                


def mediumpurplebg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumpurplebg colored BackGround text.\n
        mediumpurplebg() is a BackGround Function, if You add ForeGround property given text you can use MediumPurple .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumpurplebg("Hello World", Style = 0 ) = it's return mediumpurplebg color text without any style       \n
                mediumpurplebg("Hello World", Style = 1 ) = it's return mediumpurplebg color text with bold text          \n
                mediumpurplebg("Hello World", Style = 2 ) = it's return mediumpurplebg color text with light text         \n
                mediumpurplebg("Hello World", Style = 3 ) = it's return mediumpurplebg color text with Italicized style   \n
                mediumpurplebg("Hello World", Style = 4 ) = it's return mediumpurplebg color text with UnderLine          \n
                mediumpurplebg("Hello World", Style = 5 ) = it's return Blinking mediumpurplebg color text                \n
        """
        return Colors.back_ground_color(text, style, 147, 112, 219)
                


def medium_orchidbg( text : str, style : int = default_style ) -> str :
        """
        It will return the medium_orchidbg colored BackGround text.\n
        medium_orchidbg() is a BackGround Function, if You add ForeGround property given text you can use Medium_Orchid .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                medium_orchidbg("Hello World", Style = 0 ) = it's return medium_orchidbg color text without any style       \n
                medium_orchidbg("Hello World", Style = 1 ) = it's return medium_orchidbg color text with bold text          \n
                medium_orchidbg("Hello World", Style = 2 ) = it's return medium_orchidbg color text with light text         \n
                medium_orchidbg("Hello World", Style = 3 ) = it's return medium_orchidbg color text with Italicized style   \n
                medium_orchidbg("Hello World", Style = 4 ) = it's return medium_orchidbg color text with UnderLine          \n
                medium_orchidbg("Hello World", Style = 5 ) = it's return Blinking medium_orchidbg color text                \n
        """
        return Colors.back_ground_color(text, style, 147, 112, 219)
                


def mediumpurple1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumpurple1bg colored BackGround text.\n
        mediumpurple1bg() is a BackGround Function, if You add ForeGround property given text you can use MediumPurple1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumpurple1bg("Hello World", Style = 0 ) = it's return mediumpurple1bg color text without any style       \n
                mediumpurple1bg("Hello World", Style = 1 ) = it's return mediumpurple1bg color text with bold text          \n
                mediumpurple1bg("Hello World", Style = 2 ) = it's return mediumpurple1bg color text with light text         \n
                mediumpurple1bg("Hello World", Style = 3 ) = it's return mediumpurple1bg color text with Italicized style   \n
                mediumpurple1bg("Hello World", Style = 4 ) = it's return mediumpurple1bg color text with UnderLine          \n
                mediumpurple1bg("Hello World", Style = 5 ) = it's return Blinking mediumpurple1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 171, 130, 255)
                


def dark_orchidbg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_orchidbg colored BackGround text.\n
        dark_orchidbg() is a BackGround Function, if You add ForeGround property given text you can use Dark_Orchid .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_orchidbg("Hello World", Style = 0 ) = it's return dark_orchidbg color text without any style       \n
                dark_orchidbg("Hello World", Style = 1 ) = it's return dark_orchidbg color text with bold text          \n
                dark_orchidbg("Hello World", Style = 2 ) = it's return dark_orchidbg color text with light text         \n
                dark_orchidbg("Hello World", Style = 3 ) = it's return dark_orchidbg color text with Italicized style   \n
                dark_orchidbg("Hello World", Style = 4 ) = it's return dark_orchidbg color text with UnderLine          \n
                dark_orchidbg("Hello World", Style = 5 ) = it's return Blinking dark_orchidbg color text                \n
        """
        return Colors.back_ground_color(text, style, 153, 50, 205)
                


def mediumpurple2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumpurple2bg colored BackGround text.\n
        mediumpurple2bg() is a BackGround Function, if You add ForeGround property given text you can use MediumPurple2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumpurple2bg("Hello World", Style = 0 ) = it's return mediumpurple2bg color text without any style       \n
                mediumpurple2bg("Hello World", Style = 1 ) = it's return mediumpurple2bg color text with bold text          \n
                mediumpurple2bg("Hello World", Style = 2 ) = it's return mediumpurple2bg color text with light text         \n
                mediumpurple2bg("Hello World", Style = 3 ) = it's return mediumpurple2bg color text with Italicized style   \n
                mediumpurple2bg("Hello World", Style = 4 ) = it's return mediumpurple2bg color text with UnderLine          \n
                mediumpurple2bg("Hello World", Style = 5 ) = it's return Blinking mediumpurple2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 159, 121, 238)
                


def mediumpurple3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumpurple3bg colored BackGround text.\n
        mediumpurple3bg() is a BackGround Function, if You add ForeGround property given text you can use MediumPurple3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumpurple3bg("Hello World", Style = 0 ) = it's return mediumpurple3bg color text without any style       \n
                mediumpurple3bg("Hello World", Style = 1 ) = it's return mediumpurple3bg color text with bold text          \n
                mediumpurple3bg("Hello World", Style = 2 ) = it's return mediumpurple3bg color text with light text         \n
                mediumpurple3bg("Hello World", Style = 3 ) = it's return mediumpurple3bg color text with Italicized style   \n
                mediumpurple3bg("Hello World", Style = 4 ) = it's return mediumpurple3bg color text with UnderLine          \n
                mediumpurple3bg("Hello World", Style = 5 ) = it's return Blinking mediumpurple3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 137, 104, 205)
                


def mediumpurple4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the mediumpurple4bg colored BackGround text.\n
        mediumpurple4bg() is a BackGround Function, if You add ForeGround property given text you can use MediumPurple4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                mediumpurple4bg("Hello World", Style = 0 ) = it's return mediumpurple4bg color text without any style       \n
                mediumpurple4bg("Hello World", Style = 1 ) = it's return mediumpurple4bg color text with bold text          \n
                mediumpurple4bg("Hello World", Style = 2 ) = it's return mediumpurple4bg color text with light text         \n
                mediumpurple4bg("Hello World", Style = 3 ) = it's return mediumpurple4bg color text with Italicized style   \n
                mediumpurple4bg("Hello World", Style = 4 ) = it's return mediumpurple4bg color text with UnderLine          \n
                mediumpurple4bg("Hello World", Style = 5 ) = it's return Blinking mediumpurple4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 93, 71, 139)
                


def lavenderbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lavenderbg colored BackGround text.\n
        lavenderbg() is a BackGround Function, if You add ForeGround property given text you can use lavender .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lavenderbg("Hello World", Style = 0 ) = it's return lavenderbg color text without any style       \n
                lavenderbg("Hello World", Style = 1 ) = it's return lavenderbg color text with bold text          \n
                lavenderbg("Hello World", Style = 2 ) = it's return lavenderbg color text with light text         \n
                lavenderbg("Hello World", Style = 3 ) = it's return lavenderbg color text with Italicized style   \n
                lavenderbg("Hello World", Style = 4 ) = it's return lavenderbg color text with UnderLine          \n
                lavenderbg("Hello World", Style = 5 ) = it's return Blinking lavenderbg color text                \n
        """
        return Colors.back_ground_color(text, style, 230, 230, 250)
                


def magentabg( text : str, style : int = default_style ) -> str :
        """
        It will return the magentabg colored BackGround text.\n
        magentabg() is a BackGround Function, if You add ForeGround property given text you can use magenta .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                magentabg("Hello World", Style = 0 ) = it's return magentabg color text without any style       \n
                magentabg("Hello World", Style = 1 ) = it's return magentabg color text with bold text          \n
                magentabg("Hello World", Style = 2 ) = it's return magentabg color text with light text         \n
                magentabg("Hello World", Style = 3 ) = it's return magentabg color text with Italicized style   \n
                magentabg("Hello World", Style = 4 ) = it's return magentabg color text with UnderLine          \n
                magentabg("Hello World", Style = 5 ) = it's return Blinking magentabg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 0, 255)
                


def fuchsiabg( text : str, style : int = default_style ) -> str :
        """
        It will return the fuchsiabg colored BackGround text.\n
        fuchsiabg() is a BackGround Function, if You add ForeGround property given text you can use fuchsia .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                fuchsiabg("Hello World", Style = 0 ) = it's return fuchsiabg color text without any style       \n
                fuchsiabg("Hello World", Style = 1 ) = it's return fuchsiabg color text with bold text          \n
                fuchsiabg("Hello World", Style = 2 ) = it's return fuchsiabg color text with light text         \n
                fuchsiabg("Hello World", Style = 3 ) = it's return fuchsiabg color text with Italicized style   \n
                fuchsiabg("Hello World", Style = 4 ) = it's return fuchsiabg color text with UnderLine          \n
                fuchsiabg("Hello World", Style = 5 ) = it's return Blinking fuchsiabg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 0, 255)
                


def magenta1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the magenta1bg colored BackGround text.\n
        magenta1bg() is a BackGround Function, if You add ForeGround property given text you can use magenta1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                magenta1bg("Hello World", Style = 0 ) = it's return magenta1bg color text without any style       \n
                magenta1bg("Hello World", Style = 1 ) = it's return magenta1bg color text with bold text          \n
                magenta1bg("Hello World", Style = 2 ) = it's return magenta1bg color text with light text         \n
                magenta1bg("Hello World", Style = 3 ) = it's return magenta1bg color text with Italicized style   \n
                magenta1bg("Hello World", Style = 4 ) = it's return magenta1bg color text with UnderLine          \n
                magenta1bg("Hello World", Style = 5 ) = it's return Blinking magenta1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 0, 255)
                


def magenta2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the magenta2bg colored BackGround text.\n
        magenta2bg() is a BackGround Function, if You add ForeGround property given text you can use magenta2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                magenta2bg("Hello World", Style = 0 ) = it's return magenta2bg color text without any style       \n
                magenta2bg("Hello World", Style = 1 ) = it's return magenta2bg color text with bold text          \n
                magenta2bg("Hello World", Style = 2 ) = it's return magenta2bg color text with light text         \n
                magenta2bg("Hello World", Style = 3 ) = it's return magenta2bg color text with Italicized style   \n
                magenta2bg("Hello World", Style = 4 ) = it's return magenta2bg color text with UnderLine          \n
                magenta2bg("Hello World", Style = 5 ) = it's return Blinking magenta2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 0, 238)
                


def magenta3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the magenta3bg colored BackGround text.\n
        magenta3bg() is a BackGround Function, if You add ForeGround property given text you can use magenta3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                magenta3bg("Hello World", Style = 0 ) = it's return magenta3bg color text without any style       \n
                magenta3bg("Hello World", Style = 1 ) = it's return magenta3bg color text with bold text          \n
                magenta3bg("Hello World", Style = 2 ) = it's return magenta3bg color text with light text         \n
                magenta3bg("Hello World", Style = 3 ) = it's return magenta3bg color text with Italicized style   \n
                magenta3bg("Hello World", Style = 4 ) = it's return magenta3bg color text with UnderLine          \n
                magenta3bg("Hello World", Style = 5 ) = it's return Blinking magenta3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 0, 205)
                


def magenta4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the magenta4bg colored BackGround text.\n
        magenta4bg() is a BackGround Function, if You add ForeGround property given text you can use magenta4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                magenta4bg("Hello World", Style = 0 ) = it's return magenta4bg color text without any style       \n
                magenta4bg("Hello World", Style = 1 ) = it's return magenta4bg color text with bold text          \n
                magenta4bg("Hello World", Style = 2 ) = it's return magenta4bg color text with light text         \n
                magenta4bg("Hello World", Style = 3 ) = it's return magenta4bg color text with Italicized style   \n
                magenta4bg("Hello World", Style = 4 ) = it's return magenta4bg color text with UnderLine          \n
                magenta4bg("Hello World", Style = 5 ) = it's return Blinking magenta4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 0, 139)
                


def maroonbg( text : str, style : int = default_style ) -> str :
        """
        It will return the maroonbg colored BackGround text.\n
        maroonbg() is a BackGround Function, if You add ForeGround property given text you can use maroon .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                maroonbg("Hello World", Style = 0 ) = it's return maroonbg color text without any style       \n
                maroonbg("Hello World", Style = 1 ) = it's return maroonbg color text with bold text          \n
                maroonbg("Hello World", Style = 2 ) = it's return maroonbg color text with light text         \n
                maroonbg("Hello World", Style = 3 ) = it's return maroonbg color text with Italicized style   \n
                maroonbg("Hello World", Style = 4 ) = it's return maroonbg color text with UnderLine          \n
                maroonbg("Hello World", Style = 5 ) = it's return Blinking maroonbg color text                \n
        """
        return Colors.back_ground_color(text, style, 176, 48, 96)
                


def maroon1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the maroon1bg colored BackGround text.\n
        maroon1bg() is a BackGround Function, if You add ForeGround property given text you can use maroon1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                maroon1bg("Hello World", Style = 0 ) = it's return maroon1bg color text without any style       \n
                maroon1bg("Hello World", Style = 1 ) = it's return maroon1bg color text with bold text          \n
                maroon1bg("Hello World", Style = 2 ) = it's return maroon1bg color text with light text         \n
                maroon1bg("Hello World", Style = 3 ) = it's return maroon1bg color text with Italicized style   \n
                maroon1bg("Hello World", Style = 4 ) = it's return maroon1bg color text with UnderLine          \n
                maroon1bg("Hello World", Style = 5 ) = it's return Blinking maroon1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 52, 179)
                


def maroon2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the maroon2bg colored BackGround text.\n
        maroon2bg() is a BackGround Function, if You add ForeGround property given text you can use maroon2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                maroon2bg("Hello World", Style = 0 ) = it's return maroon2bg color text without any style       \n
                maroon2bg("Hello World", Style = 1 ) = it's return maroon2bg color text with bold text          \n
                maroon2bg("Hello World", Style = 2 ) = it's return maroon2bg color text with light text         \n
                maroon2bg("Hello World", Style = 3 ) = it's return maroon2bg color text with Italicized style   \n
                maroon2bg("Hello World", Style = 4 ) = it's return maroon2bg color text with UnderLine          \n
                maroon2bg("Hello World", Style = 5 ) = it's return Blinking maroon2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 48, 167)
                


def maroon3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the maroon3bg colored BackGround text.\n
        maroon3bg() is a BackGround Function, if You add ForeGround property given text you can use maroon3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                maroon3bg("Hello World", Style = 0 ) = it's return maroon3bg color text without any style       \n
                maroon3bg("Hello World", Style = 1 ) = it's return maroon3bg color text with bold text          \n
                maroon3bg("Hello World", Style = 2 ) = it's return maroon3bg color text with light text         \n
                maroon3bg("Hello World", Style = 3 ) = it's return maroon3bg color text with Italicized style   \n
                maroon3bg("Hello World", Style = 4 ) = it's return maroon3bg color text with UnderLine          \n
                maroon3bg("Hello World", Style = 5 ) = it's return Blinking maroon3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 41, 144)
                


def maroon4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the maroon4bg colored BackGround text.\n
        maroon4bg() is a BackGround Function, if You add ForeGround property given text you can use maroon4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                maroon4bg("Hello World", Style = 0 ) = it's return maroon4bg color text without any style       \n
                maroon4bg("Hello World", Style = 1 ) = it's return maroon4bg color text with bold text          \n
                maroon4bg("Hello World", Style = 2 ) = it's return maroon4bg color text with light text         \n
                maroon4bg("Hello World", Style = 3 ) = it's return maroon4bg color text with Italicized style   \n
                maroon4bg("Hello World", Style = 4 ) = it's return maroon4bg color text with UnderLine          \n
                maroon4bg("Hello World", Style = 5 ) = it's return Blinking maroon4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 28, 98)
                


def orchidbg( text : str, style : int = default_style ) -> str :
        """
        It will return the orchidbg colored BackGround text.\n
        orchidbg() is a BackGround Function, if You add ForeGround property given text you can use orchid .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orchidbg("Hello World", Style = 0 ) = it's return orchidbg color text without any style       \n
                orchidbg("Hello World", Style = 1 ) = it's return orchidbg color text with bold text          \n
                orchidbg("Hello World", Style = 2 ) = it's return orchidbg color text with light text         \n
                orchidbg("Hello World", Style = 3 ) = it's return orchidbg color text with Italicized style   \n
                orchidbg("Hello World", Style = 4 ) = it's return orchidbg color text with UnderLine          \n
                orchidbg("Hello World", Style = 5 ) = it's return Blinking orchidbg color text                \n
        """
        return Colors.back_ground_color(text, style, 218, 112, 214)
                


def orchidbg( text : str, style : int = default_style ) -> str :
        """
        It will return the orchidbg colored BackGround text.\n
        orchidbg() is a BackGround Function, if You add ForeGround property given text you can use Orchid .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orchidbg("Hello World", Style = 0 ) = it's return orchidbg color text without any style       \n
                orchidbg("Hello World", Style = 1 ) = it's return orchidbg color text with bold text          \n
                orchidbg("Hello World", Style = 2 ) = it's return orchidbg color text with light text         \n
                orchidbg("Hello World", Style = 3 ) = it's return orchidbg color text with Italicized style   \n
                orchidbg("Hello World", Style = 4 ) = it's return orchidbg color text with UnderLine          \n
                orchidbg("Hello World", Style = 5 ) = it's return Blinking orchidbg color text                \n
        """
        return Colors.back_ground_color(text, style, 219, 112, 219)
                


def orchid1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orchid1bg colored BackGround text.\n
        orchid1bg() is a BackGround Function, if You add ForeGround property given text you can use orchid1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orchid1bg("Hello World", Style = 0 ) = it's return orchid1bg color text without any style       \n
                orchid1bg("Hello World", Style = 1 ) = it's return orchid1bg color text with bold text          \n
                orchid1bg("Hello World", Style = 2 ) = it's return orchid1bg color text with light text         \n
                orchid1bg("Hello World", Style = 3 ) = it's return orchid1bg color text with Italicized style   \n
                orchid1bg("Hello World", Style = 4 ) = it's return orchid1bg color text with UnderLine          \n
                orchid1bg("Hello World", Style = 5 ) = it's return Blinking orchid1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 131, 250)
                


def orchid2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orchid2bg colored BackGround text.\n
        orchid2bg() is a BackGround Function, if You add ForeGround property given text you can use orchid2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orchid2bg("Hello World", Style = 0 ) = it's return orchid2bg color text without any style       \n
                orchid2bg("Hello World", Style = 1 ) = it's return orchid2bg color text with bold text          \n
                orchid2bg("Hello World", Style = 2 ) = it's return orchid2bg color text with light text         \n
                orchid2bg("Hello World", Style = 3 ) = it's return orchid2bg color text with Italicized style   \n
                orchid2bg("Hello World", Style = 4 ) = it's return orchid2bg color text with UnderLine          \n
                orchid2bg("Hello World", Style = 5 ) = it's return Blinking orchid2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 122, 233)
                


def orchid3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orchid3bg colored BackGround text.\n
        orchid3bg() is a BackGround Function, if You add ForeGround property given text you can use orchid3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orchid3bg("Hello World", Style = 0 ) = it's return orchid3bg color text without any style       \n
                orchid3bg("Hello World", Style = 1 ) = it's return orchid3bg color text with bold text          \n
                orchid3bg("Hello World", Style = 2 ) = it's return orchid3bg color text with light text         \n
                orchid3bg("Hello World", Style = 3 ) = it's return orchid3bg color text with Italicized style   \n
                orchid3bg("Hello World", Style = 4 ) = it's return orchid3bg color text with UnderLine          \n
                orchid3bg("Hello World", Style = 5 ) = it's return Blinking orchid3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 105, 201)
                


def orchid4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the orchid4bg colored BackGround text.\n
        orchid4bg() is a BackGround Function, if You add ForeGround property given text you can use orchid4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                orchid4bg("Hello World", Style = 0 ) = it's return orchid4bg color text without any style       \n
                orchid4bg("Hello World", Style = 1 ) = it's return orchid4bg color text with bold text          \n
                orchid4bg("Hello World", Style = 2 ) = it's return orchid4bg color text with light text         \n
                orchid4bg("Hello World", Style = 3 ) = it's return orchid4bg color text with Italicized style   \n
                orchid4bg("Hello World", Style = 4 ) = it's return orchid4bg color text with UnderLine          \n
                orchid4bg("Hello World", Style = 5 ) = it's return Blinking orchid4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 71, 137)
                


def plumbg( text : str, style : int = default_style ) -> str :
        """
        It will return the plumbg colored BackGround text.\n
        plumbg() is a BackGround Function, if You add ForeGround property given text you can use plum .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                plumbg("Hello World", Style = 0 ) = it's return plumbg color text without any style       \n
                plumbg("Hello World", Style = 1 ) = it's return plumbg color text with bold text          \n
                plumbg("Hello World", Style = 2 ) = it's return plumbg color text with light text         \n
                plumbg("Hello World", Style = 3 ) = it's return plumbg color text with Italicized style   \n
                plumbg("Hello World", Style = 4 ) = it's return plumbg color text with UnderLine          \n
                plumbg("Hello World", Style = 5 ) = it's return Blinking plumbg color text                \n
        """
        return Colors.back_ground_color(text, style, 221, 160, 221)
                


def plum1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the plum1bg colored BackGround text.\n
        plum1bg() is a BackGround Function, if You add ForeGround property given text you can use plum1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                plum1bg("Hello World", Style = 0 ) = it's return plum1bg color text without any style       \n
                plum1bg("Hello World", Style = 1 ) = it's return plum1bg color text with bold text          \n
                plum1bg("Hello World", Style = 2 ) = it's return plum1bg color text with light text         \n
                plum1bg("Hello World", Style = 3 ) = it's return plum1bg color text with Italicized style   \n
                plum1bg("Hello World", Style = 4 ) = it's return plum1bg color text with UnderLine          \n
                plum1bg("Hello World", Style = 5 ) = it's return Blinking plum1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 187, 255)
                


def plum2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the plum2bg colored BackGround text.\n
        plum2bg() is a BackGround Function, if You add ForeGround property given text you can use plum2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                plum2bg("Hello World", Style = 0 ) = it's return plum2bg color text without any style       \n
                plum2bg("Hello World", Style = 1 ) = it's return plum2bg color text with bold text          \n
                plum2bg("Hello World", Style = 2 ) = it's return plum2bg color text with light text         \n
                plum2bg("Hello World", Style = 3 ) = it's return plum2bg color text with Italicized style   \n
                plum2bg("Hello World", Style = 4 ) = it's return plum2bg color text with UnderLine          \n
                plum2bg("Hello World", Style = 5 ) = it's return Blinking plum2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 174, 238)
                


def plum3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the plum3bg colored BackGround text.\n
        plum3bg() is a BackGround Function, if You add ForeGround property given text you can use plum3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                plum3bg("Hello World", Style = 0 ) = it's return plum3bg color text without any style       \n
                plum3bg("Hello World", Style = 1 ) = it's return plum3bg color text with bold text          \n
                plum3bg("Hello World", Style = 2 ) = it's return plum3bg color text with light text         \n
                plum3bg("Hello World", Style = 3 ) = it's return plum3bg color text with Italicized style   \n
                plum3bg("Hello World", Style = 4 ) = it's return plum3bg color text with UnderLine          \n
                plum3bg("Hello World", Style = 5 ) = it's return Blinking plum3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 150, 205)
                


def plum4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the plum4bg colored BackGround text.\n
        plum4bg() is a BackGround Function, if You add ForeGround property given text you can use plum4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                plum4bg("Hello World", Style = 0 ) = it's return plum4bg color text without any style       \n
                plum4bg("Hello World", Style = 1 ) = it's return plum4bg color text with bold text          \n
                plum4bg("Hello World", Style = 2 ) = it's return plum4bg color text with light text         \n
                plum4bg("Hello World", Style = 3 ) = it's return plum4bg color text with Italicized style   \n
                plum4bg("Hello World", Style = 4 ) = it's return plum4bg color text with UnderLine          \n
                plum4bg("Hello World", Style = 5 ) = it's return Blinking plum4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 102, 139)
                


def purplebg( text : str, style : int = default_style ) -> str :
        """
        It will return the purplebg colored BackGround text.\n
        purplebg() is a BackGround Function, if You add ForeGround property given text you can use purple .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                purplebg("Hello World", Style = 0 ) = it's return purplebg color text without any style       \n
                purplebg("Hello World", Style = 1 ) = it's return purplebg color text with bold text          \n
                purplebg("Hello World", Style = 2 ) = it's return purplebg color text with light text         \n
                purplebg("Hello World", Style = 3 ) = it's return purplebg color text with Italicized style   \n
                purplebg("Hello World", Style = 4 ) = it's return purplebg color text with UnderLine          \n
                purplebg("Hello World", Style = 5 ) = it's return Blinking purplebg color text                \n
        """
        return Colors.back_ground_color(text, style, 128, 0, 128)
                


def purplebg( text : str, style : int = default_style ) -> str :
        """
        It will return the purplebg colored BackGround text.\n
        purplebg() is a BackGround Function, if You add ForeGround property given text you can use purple .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                purplebg("Hello World", Style = 0 ) = it's return purplebg color text without any style       \n
                purplebg("Hello World", Style = 1 ) = it's return purplebg color text with bold text          \n
                purplebg("Hello World", Style = 2 ) = it's return purplebg color text with light text         \n
                purplebg("Hello World", Style = 3 ) = it's return purplebg color text with Italicized style   \n
                purplebg("Hello World", Style = 4 ) = it's return purplebg color text with UnderLine          \n
                purplebg("Hello World", Style = 5 ) = it's return Blinking purplebg color text                \n
        """
        return Colors.back_ground_color(text, style, 128, 0, 128)
                


def purple1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the purple1bg colored BackGround text.\n
        purple1bg() is a BackGround Function, if You add ForeGround property given text you can use purple1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                purple1bg("Hello World", Style = 0 ) = it's return purple1bg color text without any style       \n
                purple1bg("Hello World", Style = 1 ) = it's return purple1bg color text with bold text          \n
                purple1bg("Hello World", Style = 2 ) = it's return purple1bg color text with light text         \n
                purple1bg("Hello World", Style = 3 ) = it's return purple1bg color text with Italicized style   \n
                purple1bg("Hello World", Style = 4 ) = it's return purple1bg color text with UnderLine          \n
                purple1bg("Hello World", Style = 5 ) = it's return Blinking purple1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 155, 48, 255)
                


def purple2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the purple2bg colored BackGround text.\n
        purple2bg() is a BackGround Function, if You add ForeGround property given text you can use purple2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                purple2bg("Hello World", Style = 0 ) = it's return purple2bg color text without any style       \n
                purple2bg("Hello World", Style = 1 ) = it's return purple2bg color text with bold text          \n
                purple2bg("Hello World", Style = 2 ) = it's return purple2bg color text with light text         \n
                purple2bg("Hello World", Style = 3 ) = it's return purple2bg color text with Italicized style   \n
                purple2bg("Hello World", Style = 4 ) = it's return purple2bg color text with UnderLine          \n
                purple2bg("Hello World", Style = 5 ) = it's return Blinking purple2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 145, 44, 238)
                


def purple3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the purple3bg colored BackGround text.\n
        purple3bg() is a BackGround Function, if You add ForeGround property given text you can use purple3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                purple3bg("Hello World", Style = 0 ) = it's return purple3bg color text without any style       \n
                purple3bg("Hello World", Style = 1 ) = it's return purple3bg color text with bold text          \n
                purple3bg("Hello World", Style = 2 ) = it's return purple3bg color text with light text         \n
                purple3bg("Hello World", Style = 3 ) = it's return purple3bg color text with Italicized style   \n
                purple3bg("Hello World", Style = 4 ) = it's return purple3bg color text with UnderLine          \n
                purple3bg("Hello World", Style = 5 ) = it's return Blinking purple3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 125, 38, 205)
                


def purple4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the purple4bg colored BackGround text.\n
        purple4bg() is a BackGround Function, if You add ForeGround property given text you can use purple4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                purple4bg("Hello World", Style = 0 ) = it's return purple4bg color text without any style       \n
                purple4bg("Hello World", Style = 1 ) = it's return purple4bg color text with bold text          \n
                purple4bg("Hello World", Style = 2 ) = it's return purple4bg color text with light text         \n
                purple4bg("Hello World", Style = 3 ) = it's return purple4bg color text with Italicized style   \n
                purple4bg("Hello World", Style = 4 ) = it's return purple4bg color text with UnderLine          \n
                purple4bg("Hello World", Style = 5 ) = it's return Blinking purple4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 85, 26, 139)
                


def thistlebg( text : str, style : int = default_style ) -> str :
        """
        It will return the thistlebg colored BackGround text.\n
        thistlebg() is a BackGround Function, if You add ForeGround property given text you can use thistle .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                thistlebg("Hello World", Style = 0 ) = it's return thistlebg color text without any style       \n
                thistlebg("Hello World", Style = 1 ) = it's return thistlebg color text with bold text          \n
                thistlebg("Hello World", Style = 2 ) = it's return thistlebg color text with light text         \n
                thistlebg("Hello World", Style = 3 ) = it's return thistlebg color text with Italicized style   \n
                thistlebg("Hello World", Style = 4 ) = it's return thistlebg color text with UnderLine          \n
                thistlebg("Hello World", Style = 5 ) = it's return Blinking thistlebg color text                \n
        """
        return Colors.back_ground_color(text, style, 216, 191, 216)
                


def thistle1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the thistle1bg colored BackGround text.\n
        thistle1bg() is a BackGround Function, if You add ForeGround property given text you can use thistle1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                thistle1bg("Hello World", Style = 0 ) = it's return thistle1bg color text without any style       \n
                thistle1bg("Hello World", Style = 1 ) = it's return thistle1bg color text with bold text          \n
                thistle1bg("Hello World", Style = 2 ) = it's return thistle1bg color text with light text         \n
                thistle1bg("Hello World", Style = 3 ) = it's return thistle1bg color text with Italicized style   \n
                thistle1bg("Hello World", Style = 4 ) = it's return thistle1bg color text with UnderLine          \n
                thistle1bg("Hello World", Style = 5 ) = it's return Blinking thistle1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 225, 255)
                


def thistle2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the thistle2bg colored BackGround text.\n
        thistle2bg() is a BackGround Function, if You add ForeGround property given text you can use thistle2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                thistle2bg("Hello World", Style = 0 ) = it's return thistle2bg color text without any style       \n
                thistle2bg("Hello World", Style = 1 ) = it's return thistle2bg color text with bold text          \n
                thistle2bg("Hello World", Style = 2 ) = it's return thistle2bg color text with light text         \n
                thistle2bg("Hello World", Style = 3 ) = it's return thistle2bg color text with Italicized style   \n
                thistle2bg("Hello World", Style = 4 ) = it's return thistle2bg color text with UnderLine          \n
                thistle2bg("Hello World", Style = 5 ) = it's return Blinking thistle2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 210, 238)
                


def thistle3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the thistle3bg colored BackGround text.\n
        thistle3bg() is a BackGround Function, if You add ForeGround property given text you can use thistle3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                thistle3bg("Hello World", Style = 0 ) = it's return thistle3bg color text without any style       \n
                thistle3bg("Hello World", Style = 1 ) = it's return thistle3bg color text with bold text          \n
                thistle3bg("Hello World", Style = 2 ) = it's return thistle3bg color text with light text         \n
                thistle3bg("Hello World", Style = 3 ) = it's return thistle3bg color text with Italicized style   \n
                thistle3bg("Hello World", Style = 4 ) = it's return thistle3bg color text with UnderLine          \n
                thistle3bg("Hello World", Style = 5 ) = it's return Blinking thistle3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 181, 205)
                


def thistle4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the thistle4bg colored BackGround text.\n
        thistle4bg() is a BackGround Function, if You add ForeGround property given text you can use thistle4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                thistle4bg("Hello World", Style = 0 ) = it's return thistle4bg color text without any style       \n
                thistle4bg("Hello World", Style = 1 ) = it's return thistle4bg color text with bold text          \n
                thistle4bg("Hello World", Style = 2 ) = it's return thistle4bg color text with light text         \n
                thistle4bg("Hello World", Style = 3 ) = it's return thistle4bg color text with Italicized style   \n
                thistle4bg("Hello World", Style = 4 ) = it's return thistle4bg color text with UnderLine          \n
                thistle4bg("Hello World", Style = 5 ) = it's return Blinking thistle4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 123, 139)
                


def violetbg( text : str, style : int = default_style ) -> str :
        """
        It will return the violetbg colored BackGround text.\n
        violetbg() is a BackGround Function, if You add ForeGround property given text you can use violet .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                violetbg("Hello World", Style = 0 ) = it's return violetbg color text without any style       \n
                violetbg("Hello World", Style = 1 ) = it's return violetbg color text with bold text          \n
                violetbg("Hello World", Style = 2 ) = it's return violetbg color text with light text         \n
                violetbg("Hello World", Style = 3 ) = it's return violetbg color text with Italicized style   \n
                violetbg("Hello World", Style = 4 ) = it's return violetbg color text with UnderLine          \n
                violetbg("Hello World", Style = 5 ) = it's return Blinking violetbg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 130, 238)
                


def violet_bluebg( text : str, style : int = default_style ) -> str :
        """
        It will return the violet_bluebg colored BackGround text.\n
        violet_bluebg() is a BackGround Function, if You add ForeGround property given text you can use violet_blue .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                violet_bluebg("Hello World", Style = 0 ) = it's return violet_bluebg color text without any style       \n
                violet_bluebg("Hello World", Style = 1 ) = it's return violet_bluebg color text with bold text          \n
                violet_bluebg("Hello World", Style = 2 ) = it's return violet_bluebg color text with light text         \n
                violet_bluebg("Hello World", Style = 3 ) = it's return violet_bluebg color text with Italicized style   \n
                violet_bluebg("Hello World", Style = 4 ) = it's return violet_bluebg color text with UnderLine          \n
                violet_bluebg("Hello World", Style = 5 ) = it's return Blinking violet_bluebg color text                \n
        """
        return Colors.back_ground_color(text, style, 159, 95, 159)
                


def dark_purplebg( text : str, style : int = default_style ) -> str :
        """
        It will return the dark_purplebg colored BackGround text.\n
        dark_purplebg() is a BackGround Function, if You add ForeGround property given text you can use Dark_Purple .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                dark_purplebg("Hello World", Style = 0 ) = it's return dark_purplebg color text without any style       \n
                dark_purplebg("Hello World", Style = 1 ) = it's return dark_purplebg color text with bold text          \n
                dark_purplebg("Hello World", Style = 2 ) = it's return dark_purplebg color text with light text         \n
                dark_purplebg("Hello World", Style = 3 ) = it's return dark_purplebg color text with Italicized style   \n
                dark_purplebg("Hello World", Style = 4 ) = it's return dark_purplebg color text with UnderLine          \n
                dark_purplebg("Hello World", Style = 5 ) = it's return Blinking dark_purplebg color text                \n
        """
        return Colors.back_ground_color(text, style, 135, 31, 120)
                


def maroonbg( text : str, style : int = default_style ) -> str :
        """
        It will return the maroonbg colored BackGround text.\n
        maroonbg() is a BackGround Function, if You add ForeGround property given text you can use Maroon .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                maroonbg("Hello World", Style = 0 ) = it's return maroonbg color text without any style       \n
                maroonbg("Hello World", Style = 1 ) = it's return maroonbg color text with bold text          \n
                maroonbg("Hello World", Style = 2 ) = it's return maroonbg color text with light text         \n
                maroonbg("Hello World", Style = 3 ) = it's return maroonbg color text with Italicized style   \n
                maroonbg("Hello World", Style = 4 ) = it's return maroonbg color text with UnderLine          \n
                maroonbg("Hello World", Style = 5 ) = it's return Blinking maroonbg color text                \n
        """
        return Colors.back_ground_color(text, style, 128, 0, 0)
                


def maroonbg( text : str, style : int = default_style ) -> str :
        """
        It will return the maroonbg colored BackGround text.\n
        maroonbg() is a BackGround Function, if You add ForeGround property given text you can use Maroon .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                maroonbg("Hello World", Style = 0 ) = it's return maroonbg color text without any style       \n
                maroonbg("Hello World", Style = 1 ) = it's return maroonbg color text with bold text          \n
                maroonbg("Hello World", Style = 2 ) = it's return maroonbg color text with light text         \n
                maroonbg("Hello World", Style = 3 ) = it's return maroonbg color text with Italicized style   \n
                maroonbg("Hello World", Style = 4 ) = it's return maroonbg color text with UnderLine          \n
                maroonbg("Hello World", Style = 5 ) = it's return Blinking maroonbg color text                \n
        """
        return Colors.back_ground_color(text, style, 128, 0, 0)
                


def medium_violet_redbg( text : str, style : int = default_style ) -> str :
        """
        It will return the medium_violet_redbg colored BackGround text.\n
        medium_violet_redbg() is a BackGround Function, if You add ForeGround property given text you can use Medium_Violet_Red .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                medium_violet_redbg("Hello World", Style = 0 ) = it's return medium_violet_redbg color text without any style       \n
                medium_violet_redbg("Hello World", Style = 1 ) = it's return medium_violet_redbg color text with bold text          \n
                medium_violet_redbg("Hello World", Style = 2 ) = it's return medium_violet_redbg color text with light text         \n
                medium_violet_redbg("Hello World", Style = 3 ) = it's return medium_violet_redbg color text with Italicized style   \n
                medium_violet_redbg("Hello World", Style = 4 ) = it's return medium_violet_redbg color text with UnderLine          \n
                medium_violet_redbg("Hello World", Style = 5 ) = it's return Blinking medium_violet_redbg color text                \n
        """
        return Colors.back_ground_color(text, style, 219, 112, 147)
                


def neon_pinkbg( text : str, style : int = default_style ) -> str :
        """
        It will return the neon_pinkbg colored BackGround text.\n
        neon_pinkbg() is a BackGround Function, if You add ForeGround property given text you can use Neon_Pink .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                neon_pinkbg("Hello World", Style = 0 ) = it's return neon_pinkbg color text without any style       \n
                neon_pinkbg("Hello World", Style = 1 ) = it's return neon_pinkbg color text with bold text          \n
                neon_pinkbg("Hello World", Style = 2 ) = it's return neon_pinkbg color text with light text         \n
                neon_pinkbg("Hello World", Style = 3 ) = it's return neon_pinkbg color text with Italicized style   \n
                neon_pinkbg("Hello World", Style = 4 ) = it's return neon_pinkbg color text with UnderLine          \n
                neon_pinkbg("Hello World", Style = 5 ) = it's return Blinking neon_pinkbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 110, 199)
                


def plumbg( text : str, style : int = default_style ) -> str :
        """
        It will return the plumbg colored BackGround text.\n
        plumbg() is a BackGround Function, if You add ForeGround property given text you can use Plum .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                plumbg("Hello World", Style = 0 ) = it's return plumbg color text without any style       \n
                plumbg("Hello World", Style = 1 ) = it's return plumbg color text with bold text          \n
                plumbg("Hello World", Style = 2 ) = it's return plumbg color text with light text         \n
                plumbg("Hello World", Style = 3 ) = it's return plumbg color text with Italicized style   \n
                plumbg("Hello World", Style = 4 ) = it's return plumbg color text with UnderLine          \n
                plumbg("Hello World", Style = 5 ) = it's return Blinking plumbg color text                \n
        """
        return Colors.back_ground_color(text, style, 234, 173, 234)
                


def thistlebg( text : str, style : int = default_style ) -> str :
        """
        It will return the thistlebg colored BackGround text.\n
        thistlebg() is a BackGround Function, if You add ForeGround property given text you can use Thistle .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                thistlebg("Hello World", Style = 0 ) = it's return thistlebg color text without any style       \n
                thistlebg("Hello World", Style = 1 ) = it's return thistlebg color text with bold text          \n
                thistlebg("Hello World", Style = 2 ) = it's return thistlebg color text with light text         \n
                thistlebg("Hello World", Style = 3 ) = it's return thistlebg color text with Italicized style   \n
                thistlebg("Hello World", Style = 4 ) = it's return thistlebg color text with UnderLine          \n
                thistlebg("Hello World", Style = 5 ) = it's return Blinking thistlebg color text                \n
        """
        return Colors.back_ground_color(text, style, 216, 191, 216)
                


def turquoisebg( text : str, style : int = default_style ) -> str :
        """
        It will return the turquoisebg colored BackGround text.\n
        turquoisebg() is a BackGround Function, if You add ForeGround property given text you can use Turquoise .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                turquoisebg("Hello World", Style = 0 ) = it's return turquoisebg color text without any style       \n
                turquoisebg("Hello World", Style = 1 ) = it's return turquoisebg color text with bold text          \n
                turquoisebg("Hello World", Style = 2 ) = it's return turquoisebg color text with light text         \n
                turquoisebg("Hello World", Style = 3 ) = it's return turquoisebg color text with Italicized style   \n
                turquoisebg("Hello World", Style = 4 ) = it's return turquoisebg color text with UnderLine          \n
                turquoisebg("Hello World", Style = 5 ) = it's return Blinking turquoisebg color text                \n
        """
        return Colors.back_ground_color(text, style, 173, 234, 234)
                


def violetbg( text : str, style : int = default_style ) -> str :
        """
        It will return the violetbg colored BackGround text.\n
        violetbg() is a BackGround Function, if You add ForeGround property given text you can use Violet .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                violetbg("Hello World", Style = 0 ) = it's return violetbg color text without any style       \n
                violetbg("Hello World", Style = 1 ) = it's return violetbg color text with bold text          \n
                violetbg("Hello World", Style = 2 ) = it's return violetbg color text with light text         \n
                violetbg("Hello World", Style = 3 ) = it's return violetbg color text with Italicized style   \n
                violetbg("Hello World", Style = 4 ) = it's return violetbg color text with UnderLine          \n
                violetbg("Hello World", Style = 5 ) = it's return Blinking violetbg color text                \n
        """
        return Colors.back_ground_color(text, style, 79, 47, 79)
                


def violet_redbg( text : str, style : int = default_style ) -> str :
        """
        It will return the violet_redbg colored BackGround text.\n
        violet_redbg() is a BackGround Function, if You add ForeGround property given text you can use Violet_Red .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                violet_redbg("Hello World", Style = 0 ) = it's return violet_redbg color text without any style       \n
                violet_redbg("Hello World", Style = 1 ) = it's return violet_redbg color text with bold text          \n
                violet_redbg("Hello World", Style = 2 ) = it's return violet_redbg color text with light text         \n
                violet_redbg("Hello World", Style = 3 ) = it's return violet_redbg color text with Italicized style   \n
                violet_redbg("Hello World", Style = 4 ) = it's return violet_redbg color text with UnderLine          \n
                violet_redbg("Hello World", Style = 5 ) = it's return Blinking violet_redbg color text                \n
        """
        return Colors.back_ground_color(text, style, 204, 50, 153)
                


def antiquewhitebg( text : str, style : int = default_style ) -> str :
        """
        It will return the antiquewhitebg colored BackGround text.\n
        antiquewhitebg() is a BackGround Function, if You add ForeGround property given text you can use AntiqueWhite .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                antiquewhitebg("Hello World", Style = 0 ) = it's return antiquewhitebg color text without any style       \n
                antiquewhitebg("Hello World", Style = 1 ) = it's return antiquewhitebg color text with bold text          \n
                antiquewhitebg("Hello World", Style = 2 ) = it's return antiquewhitebg color text with light text         \n
                antiquewhitebg("Hello World", Style = 3 ) = it's return antiquewhitebg color text with Italicized style   \n
                antiquewhitebg("Hello World", Style = 4 ) = it's return antiquewhitebg color text with UnderLine          \n
                antiquewhitebg("Hello World", Style = 5 ) = it's return Blinking antiquewhitebg color text                \n
        """
        return Colors.back_ground_color(text, style, 250, 235, 215)
                


def antiquewhite1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the antiquewhite1bg colored BackGround text.\n
        antiquewhite1bg() is a BackGround Function, if You add ForeGround property given text you can use AntiqueWhite1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                antiquewhite1bg("Hello World", Style = 0 ) = it's return antiquewhite1bg color text without any style       \n
                antiquewhite1bg("Hello World", Style = 1 ) = it's return antiquewhite1bg color text with bold text          \n
                antiquewhite1bg("Hello World", Style = 2 ) = it's return antiquewhite1bg color text with light text         \n
                antiquewhite1bg("Hello World", Style = 3 ) = it's return antiquewhite1bg color text with Italicized style   \n
                antiquewhite1bg("Hello World", Style = 4 ) = it's return antiquewhite1bg color text with UnderLine          \n
                antiquewhite1bg("Hello World", Style = 5 ) = it's return Blinking antiquewhite1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 239, 219)
                


def antiquewhite2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the antiquewhite2bg colored BackGround text.\n
        antiquewhite2bg() is a BackGround Function, if You add ForeGround property given text you can use AntiqueWhite2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                antiquewhite2bg("Hello World", Style = 0 ) = it's return antiquewhite2bg color text without any style       \n
                antiquewhite2bg("Hello World", Style = 1 ) = it's return antiquewhite2bg color text with bold text          \n
                antiquewhite2bg("Hello World", Style = 2 ) = it's return antiquewhite2bg color text with light text         \n
                antiquewhite2bg("Hello World", Style = 3 ) = it's return antiquewhite2bg color text with Italicized style   \n
                antiquewhite2bg("Hello World", Style = 4 ) = it's return antiquewhite2bg color text with UnderLine          \n
                antiquewhite2bg("Hello World", Style = 5 ) = it's return Blinking antiquewhite2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 223, 204)
                


def antiquewhite3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the antiquewhite3bg colored BackGround text.\n
        antiquewhite3bg() is a BackGround Function, if You add ForeGround property given text you can use AntiqueWhite3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                antiquewhite3bg("Hello World", Style = 0 ) = it's return antiquewhite3bg color text without any style       \n
                antiquewhite3bg("Hello World", Style = 1 ) = it's return antiquewhite3bg color text with bold text          \n
                antiquewhite3bg("Hello World", Style = 2 ) = it's return antiquewhite3bg color text with light text         \n
                antiquewhite3bg("Hello World", Style = 3 ) = it's return antiquewhite3bg color text with Italicized style   \n
                antiquewhite3bg("Hello World", Style = 4 ) = it's return antiquewhite3bg color text with UnderLine          \n
                antiquewhite3bg("Hello World", Style = 5 ) = it's return Blinking antiquewhite3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 192, 176)
                


def antiquewhite4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the antiquewhite4bg colored BackGround text.\n
        antiquewhite4bg() is a BackGround Function, if You add ForeGround property given text you can use AntiqueWhite4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                antiquewhite4bg("Hello World", Style = 0 ) = it's return antiquewhite4bg color text without any style       \n
                antiquewhite4bg("Hello World", Style = 1 ) = it's return antiquewhite4bg color text with bold text          \n
                antiquewhite4bg("Hello World", Style = 2 ) = it's return antiquewhite4bg color text with light text         \n
                antiquewhite4bg("Hello World", Style = 3 ) = it's return antiquewhite4bg color text with Italicized style   \n
                antiquewhite4bg("Hello World", Style = 4 ) = it's return antiquewhite4bg color text with UnderLine          \n
                antiquewhite4bg("Hello World", Style = 5 ) = it's return Blinking antiquewhite4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 131, 120)
                


def floralwhitebg( text : str, style : int = default_style ) -> str :
        """
        It will return the floralwhitebg colored BackGround text.\n
        floralwhitebg() is a BackGround Function, if You add ForeGround property given text you can use FloralWhite .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                floralwhitebg("Hello World", Style = 0 ) = it's return floralwhitebg color text without any style       \n
                floralwhitebg("Hello World", Style = 1 ) = it's return floralwhitebg color text with bold text          \n
                floralwhitebg("Hello World", Style = 2 ) = it's return floralwhitebg color text with light text         \n
                floralwhitebg("Hello World", Style = 3 ) = it's return floralwhitebg color text with Italicized style   \n
                floralwhitebg("Hello World", Style = 4 ) = it's return floralwhitebg color text with UnderLine          \n
                floralwhitebg("Hello World", Style = 5 ) = it's return Blinking floralwhitebg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 250, 240)
                


def ghostwhitebg( text : str, style : int = default_style ) -> str :
        """
        It will return the ghostwhitebg colored BackGround text.\n
        ghostwhitebg() is a BackGround Function, if You add ForeGround property given text you can use GhostWhite .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                ghostwhitebg("Hello World", Style = 0 ) = it's return ghostwhitebg color text without any style       \n
                ghostwhitebg("Hello World", Style = 1 ) = it's return ghostwhitebg color text with bold text          \n
                ghostwhitebg("Hello World", Style = 2 ) = it's return ghostwhitebg color text with light text         \n
                ghostwhitebg("Hello World", Style = 3 ) = it's return ghostwhitebg color text with Italicized style   \n
                ghostwhitebg("Hello World", Style = 4 ) = it's return ghostwhitebg color text with UnderLine          \n
                ghostwhitebg("Hello World", Style = 5 ) = it's return Blinking ghostwhitebg color text                \n
        """
        return Colors.back_ground_color(text, style, 248, 248, 255)
                


def navajowhitebg( text : str, style : int = default_style ) -> str :
        """
        It will return the navajowhitebg colored BackGround text.\n
        navajowhitebg() is a BackGround Function, if You add ForeGround property given text you can use NavajoWhite .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                navajowhitebg("Hello World", Style = 0 ) = it's return navajowhitebg color text without any style       \n
                navajowhitebg("Hello World", Style = 1 ) = it's return navajowhitebg color text with bold text          \n
                navajowhitebg("Hello World", Style = 2 ) = it's return navajowhitebg color text with light text         \n
                navajowhitebg("Hello World", Style = 3 ) = it's return navajowhitebg color text with Italicized style   \n
                navajowhitebg("Hello World", Style = 4 ) = it's return navajowhitebg color text with UnderLine          \n
                navajowhitebg("Hello World", Style = 5 ) = it's return Blinking navajowhitebg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 222, 173)
                


def navajowhite1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the navajowhite1bg colored BackGround text.\n
        navajowhite1bg() is a BackGround Function, if You add ForeGround property given text you can use NavajoWhite1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                navajowhite1bg("Hello World", Style = 0 ) = it's return navajowhite1bg color text without any style       \n
                navajowhite1bg("Hello World", Style = 1 ) = it's return navajowhite1bg color text with bold text          \n
                navajowhite1bg("Hello World", Style = 2 ) = it's return navajowhite1bg color text with light text         \n
                navajowhite1bg("Hello World", Style = 3 ) = it's return navajowhite1bg color text with Italicized style   \n
                navajowhite1bg("Hello World", Style = 4 ) = it's return navajowhite1bg color text with UnderLine          \n
                navajowhite1bg("Hello World", Style = 5 ) = it's return Blinking navajowhite1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 222, 173)
                


def navajowhite2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the navajowhite2bg colored BackGround text.\n
        navajowhite2bg() is a BackGround Function, if You add ForeGround property given text you can use NavajoWhite2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                navajowhite2bg("Hello World", Style = 0 ) = it's return navajowhite2bg color text without any style       \n
                navajowhite2bg("Hello World", Style = 1 ) = it's return navajowhite2bg color text with bold text          \n
                navajowhite2bg("Hello World", Style = 2 ) = it's return navajowhite2bg color text with light text         \n
                navajowhite2bg("Hello World", Style = 3 ) = it's return navajowhite2bg color text with Italicized style   \n
                navajowhite2bg("Hello World", Style = 4 ) = it's return navajowhite2bg color text with UnderLine          \n
                navajowhite2bg("Hello World", Style = 5 ) = it's return Blinking navajowhite2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 207, 161)
                


def navajowhite3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the navajowhite3bg colored BackGround text.\n
        navajowhite3bg() is a BackGround Function, if You add ForeGround property given text you can use NavajoWhite3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                navajowhite3bg("Hello World", Style = 0 ) = it's return navajowhite3bg color text without any style       \n
                navajowhite3bg("Hello World", Style = 1 ) = it's return navajowhite3bg color text with bold text          \n
                navajowhite3bg("Hello World", Style = 2 ) = it's return navajowhite3bg color text with light text         \n
                navajowhite3bg("Hello World", Style = 3 ) = it's return navajowhite3bg color text with Italicized style   \n
                navajowhite3bg("Hello World", Style = 4 ) = it's return navajowhite3bg color text with UnderLine          \n
                navajowhite3bg("Hello World", Style = 5 ) = it's return Blinking navajowhite3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 179, 139)
                


def navajowhite4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the navajowhite4bg colored BackGround text.\n
        navajowhite4bg() is a BackGround Function, if You add ForeGround property given text you can use NavajoWhite4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                navajowhite4bg("Hello World", Style = 0 ) = it's return navajowhite4bg color text without any style       \n
                navajowhite4bg("Hello World", Style = 1 ) = it's return navajowhite4bg color text with bold text          \n
                navajowhite4bg("Hello World", Style = 2 ) = it's return navajowhite4bg color text with light text         \n
                navajowhite4bg("Hello World", Style = 3 ) = it's return navajowhite4bg color text with Italicized style   \n
                navajowhite4bg("Hello World", Style = 4 ) = it's return navajowhite4bg color text with UnderLine          \n
                navajowhite4bg("Hello World", Style = 5 ) = it's return Blinking navajowhite4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 121, 94)
                


def oldlacebg( text : str, style : int = default_style ) -> str :
        """
        It will return the oldlacebg colored BackGround text.\n
        oldlacebg() is a BackGround Function, if You add ForeGround property given text you can use OldLace .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                oldlacebg("Hello World", Style = 0 ) = it's return oldlacebg color text without any style       \n
                oldlacebg("Hello World", Style = 1 ) = it's return oldlacebg color text with bold text          \n
                oldlacebg("Hello World", Style = 2 ) = it's return oldlacebg color text with light text         \n
                oldlacebg("Hello World", Style = 3 ) = it's return oldlacebg color text with Italicized style   \n
                oldlacebg("Hello World", Style = 4 ) = it's return oldlacebg color text with UnderLine          \n
                oldlacebg("Hello World", Style = 5 ) = it's return Blinking oldlacebg color text                \n
        """
        return Colors.back_ground_color(text, style, 253, 245, 230)
                


def whitesmokebg( text : str, style : int = default_style ) -> str :
        """
        It will return the whitesmokebg colored BackGround text.\n
        whitesmokebg() is a BackGround Function, if You add ForeGround property given text you can use WhiteSmoke .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                whitesmokebg("Hello World", Style = 0 ) = it's return whitesmokebg color text without any style       \n
                whitesmokebg("Hello World", Style = 1 ) = it's return whitesmokebg color text with bold text          \n
                whitesmokebg("Hello World", Style = 2 ) = it's return whitesmokebg color text with light text         \n
                whitesmokebg("Hello World", Style = 3 ) = it's return whitesmokebg color text with Italicized style   \n
                whitesmokebg("Hello World", Style = 4 ) = it's return whitesmokebg color text with UnderLine          \n
                whitesmokebg("Hello World", Style = 5 ) = it's return Blinking whitesmokebg color text                \n
        """
        return Colors.back_ground_color(text, style, 245, 245, 245)
                


def gainsborobg( text : str, style : int = default_style ) -> str :
        """
        It will return the gainsborobg colored BackGround text.\n
        gainsborobg() is a BackGround Function, if You add ForeGround property given text you can use gainsboro .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                gainsborobg("Hello World", Style = 0 ) = it's return gainsborobg color text without any style       \n
                gainsborobg("Hello World", Style = 1 ) = it's return gainsborobg color text with bold text          \n
                gainsborobg("Hello World", Style = 2 ) = it's return gainsborobg color text with light text         \n
                gainsborobg("Hello World", Style = 3 ) = it's return gainsborobg color text with Italicized style   \n
                gainsborobg("Hello World", Style = 4 ) = it's return gainsborobg color text with UnderLine          \n
                gainsborobg("Hello World", Style = 5 ) = it's return Blinking gainsborobg color text                \n
        """
        return Colors.back_ground_color(text, style, 220, 220, 220)
                


def ivorybg( text : str, style : int = default_style ) -> str :
        """
        It will return the ivorybg colored BackGround text.\n
        ivorybg() is a BackGround Function, if You add ForeGround property given text you can use ivory .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                ivorybg("Hello World", Style = 0 ) = it's return ivorybg color text without any style       \n
                ivorybg("Hello World", Style = 1 ) = it's return ivorybg color text with bold text          \n
                ivorybg("Hello World", Style = 2 ) = it's return ivorybg color text with light text         \n
                ivorybg("Hello World", Style = 3 ) = it's return ivorybg color text with Italicized style   \n
                ivorybg("Hello World", Style = 4 ) = it's return ivorybg color text with UnderLine          \n
                ivorybg("Hello World", Style = 5 ) = it's return Blinking ivorybg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 255, 240)
                


def ivory1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the ivory1bg colored BackGround text.\n
        ivory1bg() is a BackGround Function, if You add ForeGround property given text you can use ivory1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                ivory1bg("Hello World", Style = 0 ) = it's return ivory1bg color text without any style       \n
                ivory1bg("Hello World", Style = 1 ) = it's return ivory1bg color text with bold text          \n
                ivory1bg("Hello World", Style = 2 ) = it's return ivory1bg color text with light text         \n
                ivory1bg("Hello World", Style = 3 ) = it's return ivory1bg color text with Italicized style   \n
                ivory1bg("Hello World", Style = 4 ) = it's return ivory1bg color text with UnderLine          \n
                ivory1bg("Hello World", Style = 5 ) = it's return Blinking ivory1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 255, 240)
                


def ivory2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the ivory2bg colored BackGround text.\n
        ivory2bg() is a BackGround Function, if You add ForeGround property given text you can use ivory2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                ivory2bg("Hello World", Style = 0 ) = it's return ivory2bg color text without any style       \n
                ivory2bg("Hello World", Style = 1 ) = it's return ivory2bg color text with bold text          \n
                ivory2bg("Hello World", Style = 2 ) = it's return ivory2bg color text with light text         \n
                ivory2bg("Hello World", Style = 3 ) = it's return ivory2bg color text with Italicized style   \n
                ivory2bg("Hello World", Style = 4 ) = it's return ivory2bg color text with UnderLine          \n
                ivory2bg("Hello World", Style = 5 ) = it's return Blinking ivory2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 238, 224)
                


def ivory3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the ivory3bg colored BackGround text.\n
        ivory3bg() is a BackGround Function, if You add ForeGround property given text you can use ivory3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                ivory3bg("Hello World", Style = 0 ) = it's return ivory3bg color text without any style       \n
                ivory3bg("Hello World", Style = 1 ) = it's return ivory3bg color text with bold text          \n
                ivory3bg("Hello World", Style = 2 ) = it's return ivory3bg color text with light text         \n
                ivory3bg("Hello World", Style = 3 ) = it's return ivory3bg color text with Italicized style   \n
                ivory3bg("Hello World", Style = 4 ) = it's return ivory3bg color text with UnderLine          \n
                ivory3bg("Hello World", Style = 5 ) = it's return Blinking ivory3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 205, 193)
                


def ivory4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the ivory4bg colored BackGround text.\n
        ivory4bg() is a BackGround Function, if You add ForeGround property given text you can use ivory4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                ivory4bg("Hello World", Style = 0 ) = it's return ivory4bg color text without any style       \n
                ivory4bg("Hello World", Style = 1 ) = it's return ivory4bg color text with bold text          \n
                ivory4bg("Hello World", Style = 2 ) = it's return ivory4bg color text with light text         \n
                ivory4bg("Hello World", Style = 3 ) = it's return ivory4bg color text with Italicized style   \n
                ivory4bg("Hello World", Style = 4 ) = it's return ivory4bg color text with UnderLine          \n
                ivory4bg("Hello World", Style = 5 ) = it's return Blinking ivory4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 139, 131)
                


def linenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the linenbg colored BackGround text.\n
        linenbg() is a BackGround Function, if You add ForeGround property given text you can use linen .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                linenbg("Hello World", Style = 0 ) = it's return linenbg color text without any style       \n
                linenbg("Hello World", Style = 1 ) = it's return linenbg color text with bold text          \n
                linenbg("Hello World", Style = 2 ) = it's return linenbg color text with light text         \n
                linenbg("Hello World", Style = 3 ) = it's return linenbg color text with Italicized style   \n
                linenbg("Hello World", Style = 4 ) = it's return linenbg color text with UnderLine          \n
                linenbg("Hello World", Style = 5 ) = it's return Blinking linenbg color text                \n
        """
        return Colors.back_ground_color(text, style, 250, 240, 230)
                


def seashellbg( text : str, style : int = default_style ) -> str :
        """
        It will return the seashellbg colored BackGround text.\n
        seashellbg() is a BackGround Function, if You add ForeGround property given text you can use seashell .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                seashellbg("Hello World", Style = 0 ) = it's return seashellbg color text without any style       \n
                seashellbg("Hello World", Style = 1 ) = it's return seashellbg color text with bold text          \n
                seashellbg("Hello World", Style = 2 ) = it's return seashellbg color text with light text         \n
                seashellbg("Hello World", Style = 3 ) = it's return seashellbg color text with Italicized style   \n
                seashellbg("Hello World", Style = 4 ) = it's return seashellbg color text with UnderLine          \n
                seashellbg("Hello World", Style = 5 ) = it's return Blinking seashellbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 245, 238)
                


def seashell1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the seashell1bg colored BackGround text.\n
        seashell1bg() is a BackGround Function, if You add ForeGround property given text you can use seashell1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                seashell1bg("Hello World", Style = 0 ) = it's return seashell1bg color text without any style       \n
                seashell1bg("Hello World", Style = 1 ) = it's return seashell1bg color text with bold text          \n
                seashell1bg("Hello World", Style = 2 ) = it's return seashell1bg color text with light text         \n
                seashell1bg("Hello World", Style = 3 ) = it's return seashell1bg color text with Italicized style   \n
                seashell1bg("Hello World", Style = 4 ) = it's return seashell1bg color text with UnderLine          \n
                seashell1bg("Hello World", Style = 5 ) = it's return Blinking seashell1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 245, 238)
                


def seashell2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the seashell2bg colored BackGround text.\n
        seashell2bg() is a BackGround Function, if You add ForeGround property given text you can use seashell2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                seashell2bg("Hello World", Style = 0 ) = it's return seashell2bg color text without any style       \n
                seashell2bg("Hello World", Style = 1 ) = it's return seashell2bg color text with bold text          \n
                seashell2bg("Hello World", Style = 2 ) = it's return seashell2bg color text with light text         \n
                seashell2bg("Hello World", Style = 3 ) = it's return seashell2bg color text with Italicized style   \n
                seashell2bg("Hello World", Style = 4 ) = it's return seashell2bg color text with UnderLine          \n
                seashell2bg("Hello World", Style = 5 ) = it's return Blinking seashell2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 229, 222)
                


def seashell3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the seashell3bg colored BackGround text.\n
        seashell3bg() is a BackGround Function, if You add ForeGround property given text you can use seashell3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                seashell3bg("Hello World", Style = 0 ) = it's return seashell3bg color text without any style       \n
                seashell3bg("Hello World", Style = 1 ) = it's return seashell3bg color text with bold text          \n
                seashell3bg("Hello World", Style = 2 ) = it's return seashell3bg color text with light text         \n
                seashell3bg("Hello World", Style = 3 ) = it's return seashell3bg color text with Italicized style   \n
                seashell3bg("Hello World", Style = 4 ) = it's return seashell3bg color text with UnderLine          \n
                seashell3bg("Hello World", Style = 5 ) = it's return Blinking seashell3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 197, 191)
                


def seashell4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the seashell4bg colored BackGround text.\n
        seashell4bg() is a BackGround Function, if You add ForeGround property given text you can use seashell4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                seashell4bg("Hello World", Style = 0 ) = it's return seashell4bg color text without any style       \n
                seashell4bg("Hello World", Style = 1 ) = it's return seashell4bg color text with bold text          \n
                seashell4bg("Hello World", Style = 2 ) = it's return seashell4bg color text with light text         \n
                seashell4bg("Hello World", Style = 3 ) = it's return seashell4bg color text with Italicized style   \n
                seashell4bg("Hello World", Style = 4 ) = it's return seashell4bg color text with UnderLine          \n
                seashell4bg("Hello World", Style = 5 ) = it's return Blinking seashell4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 134, 130)
                


def snowbg( text : str, style : int = default_style ) -> str :
        """
        It will return the snowbg colored BackGround text.\n
        snowbg() is a BackGround Function, if You add ForeGround property given text you can use snow .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                snowbg("Hello World", Style = 0 ) = it's return snowbg color text without any style       \n
                snowbg("Hello World", Style = 1 ) = it's return snowbg color text with bold text          \n
                snowbg("Hello World", Style = 2 ) = it's return snowbg color text with light text         \n
                snowbg("Hello World", Style = 3 ) = it's return snowbg color text with Italicized style   \n
                snowbg("Hello World", Style = 4 ) = it's return snowbg color text with UnderLine          \n
                snowbg("Hello World", Style = 5 ) = it's return Blinking snowbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 250, 250)
                


def snow1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the snow1bg colored BackGround text.\n
        snow1bg() is a BackGround Function, if You add ForeGround property given text you can use snow1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                snow1bg("Hello World", Style = 0 ) = it's return snow1bg color text without any style       \n
                snow1bg("Hello World", Style = 1 ) = it's return snow1bg color text with bold text          \n
                snow1bg("Hello World", Style = 2 ) = it's return snow1bg color text with light text         \n
                snow1bg("Hello World", Style = 3 ) = it's return snow1bg color text with Italicized style   \n
                snow1bg("Hello World", Style = 4 ) = it's return snow1bg color text with UnderLine          \n
                snow1bg("Hello World", Style = 5 ) = it's return Blinking snow1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 250, 250)
                


def snow2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the snow2bg colored BackGround text.\n
        snow2bg() is a BackGround Function, if You add ForeGround property given text you can use snow2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                snow2bg("Hello World", Style = 0 ) = it's return snow2bg color text without any style       \n
                snow2bg("Hello World", Style = 1 ) = it's return snow2bg color text with bold text          \n
                snow2bg("Hello World", Style = 2 ) = it's return snow2bg color text with light text         \n
                snow2bg("Hello World", Style = 3 ) = it's return snow2bg color text with Italicized style   \n
                snow2bg("Hello World", Style = 4 ) = it's return snow2bg color text with UnderLine          \n
                snow2bg("Hello World", Style = 5 ) = it's return Blinking snow2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 233, 233)
                


def snow3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the snow3bg colored BackGround text.\n
        snow3bg() is a BackGround Function, if You add ForeGround property given text you can use snow3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                snow3bg("Hello World", Style = 0 ) = it's return snow3bg color text without any style       \n
                snow3bg("Hello World", Style = 1 ) = it's return snow3bg color text with bold text          \n
                snow3bg("Hello World", Style = 2 ) = it's return snow3bg color text with light text         \n
                snow3bg("Hello World", Style = 3 ) = it's return snow3bg color text with Italicized style   \n
                snow3bg("Hello World", Style = 4 ) = it's return snow3bg color text with UnderLine          \n
                snow3bg("Hello World", Style = 5 ) = it's return Blinking snow3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 201, 201)
                


def snow4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the snow4bg colored BackGround text.\n
        snow4bg() is a BackGround Function, if You add ForeGround property given text you can use snow4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                snow4bg("Hello World", Style = 0 ) = it's return snow4bg color text without any style       \n
                snow4bg("Hello World", Style = 1 ) = it's return snow4bg color text with bold text          \n
                snow4bg("Hello World", Style = 2 ) = it's return snow4bg color text with light text         \n
                snow4bg("Hello World", Style = 3 ) = it's return snow4bg color text with Italicized style   \n
                snow4bg("Hello World", Style = 4 ) = it's return snow4bg color text with UnderLine          \n
                snow4bg("Hello World", Style = 5 ) = it's return Blinking snow4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 137, 137)
                


def wheatbg( text : str, style : int = default_style ) -> str :
        """
        It will return the wheatbg colored BackGround text.\n
        wheatbg() is a BackGround Function, if You add ForeGround property given text you can use wheat .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                wheatbg("Hello World", Style = 0 ) = it's return wheatbg color text without any style       \n
                wheatbg("Hello World", Style = 1 ) = it's return wheatbg color text with bold text          \n
                wheatbg("Hello World", Style = 2 ) = it's return wheatbg color text with light text         \n
                wheatbg("Hello World", Style = 3 ) = it's return wheatbg color text with Italicized style   \n
                wheatbg("Hello World", Style = 4 ) = it's return wheatbg color text with UnderLine          \n
                wheatbg("Hello World", Style = 5 ) = it's return Blinking wheatbg color text                \n
        """
        return Colors.back_ground_color(text, style, 245, 222, 179)
                


def wheat1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the wheat1bg colored BackGround text.\n
        wheat1bg() is a BackGround Function, if You add ForeGround property given text you can use wheat1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                wheat1bg("Hello World", Style = 0 ) = it's return wheat1bg color text without any style       \n
                wheat1bg("Hello World", Style = 1 ) = it's return wheat1bg color text with bold text          \n
                wheat1bg("Hello World", Style = 2 ) = it's return wheat1bg color text with light text         \n
                wheat1bg("Hello World", Style = 3 ) = it's return wheat1bg color text with Italicized style   \n
                wheat1bg("Hello World", Style = 4 ) = it's return wheat1bg color text with UnderLine          \n
                wheat1bg("Hello World", Style = 5 ) = it's return Blinking wheat1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 231, 186)
                


def wheat2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the wheat2bg colored BackGround text.\n
        wheat2bg() is a BackGround Function, if You add ForeGround property given text you can use wheat2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                wheat2bg("Hello World", Style = 0 ) = it's return wheat2bg color text without any style       \n
                wheat2bg("Hello World", Style = 1 ) = it's return wheat2bg color text with bold text          \n
                wheat2bg("Hello World", Style = 2 ) = it's return wheat2bg color text with light text         \n
                wheat2bg("Hello World", Style = 3 ) = it's return wheat2bg color text with Italicized style   \n
                wheat2bg("Hello World", Style = 4 ) = it's return wheat2bg color text with UnderLine          \n
                wheat2bg("Hello World", Style = 5 ) = it's return Blinking wheat2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 216, 174)
                


def wheat3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the wheat3bg colored BackGround text.\n
        wheat3bg() is a BackGround Function, if You add ForeGround property given text you can use wheat3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                wheat3bg("Hello World", Style = 0 ) = it's return wheat3bg color text without any style       \n
                wheat3bg("Hello World", Style = 1 ) = it's return wheat3bg color text with bold text          \n
                wheat3bg("Hello World", Style = 2 ) = it's return wheat3bg color text with light text         \n
                wheat3bg("Hello World", Style = 3 ) = it's return wheat3bg color text with Italicized style   \n
                wheat3bg("Hello World", Style = 4 ) = it's return wheat3bg color text with UnderLine          \n
                wheat3bg("Hello World", Style = 5 ) = it's return Blinking wheat3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 186, 150)
                


def wheat4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the wheat4bg colored BackGround text.\n
        wheat4bg() is a BackGround Function, if You add ForeGround property given text you can use wheat4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                wheat4bg("Hello World", Style = 0 ) = it's return wheat4bg color text without any style       \n
                wheat4bg("Hello World", Style = 1 ) = it's return wheat4bg color text with bold text          \n
                wheat4bg("Hello World", Style = 2 ) = it's return wheat4bg color text with light text         \n
                wheat4bg("Hello World", Style = 3 ) = it's return wheat4bg color text with Italicized style   \n
                wheat4bg("Hello World", Style = 4 ) = it's return wheat4bg color text with UnderLine          \n
                wheat4bg("Hello World", Style = 5 ) = it's return Blinking wheat4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 126, 102)
                


def whitebg( text : str, style : int = default_style ) -> str :
        """
        It will return the whitebg colored BackGround text.\n
        whitebg() is a BackGround Function, if You add ForeGround property given text you can use white .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                whitebg("Hello World", Style = 0 ) = it's return whitebg color text without any style       \n
                whitebg("Hello World", Style = 1 ) = it's return whitebg color text with bold text          \n
                whitebg("Hello World", Style = 2 ) = it's return whitebg color text with light text         \n
                whitebg("Hello World", Style = 3 ) = it's return whitebg color text with Italicized style   \n
                whitebg("Hello World", Style = 4 ) = it's return whitebg color text with UnderLine          \n
                whitebg("Hello World", Style = 5 ) = it's return Blinking whitebg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 255, 255)
                


def quartzbg( text : str, style : int = default_style ) -> str :
        """
        It will return the quartzbg colored BackGround text.\n
        quartzbg() is a BackGround Function, if You add ForeGround property given text you can use Quartz .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                quartzbg("Hello World", Style = 0 ) = it's return quartzbg color text without any style       \n
                quartzbg("Hello World", Style = 1 ) = it's return quartzbg color text with bold text          \n
                quartzbg("Hello World", Style = 2 ) = it's return quartzbg color text with light text         \n
                quartzbg("Hello World", Style = 3 ) = it's return quartzbg color text with Italicized style   \n
                quartzbg("Hello World", Style = 4 ) = it's return quartzbg color text with UnderLine          \n
                quartzbg("Hello World", Style = 5 ) = it's return Blinking quartzbg color text                \n
        """
        return Colors.back_ground_color(text, style, 217, 217, 243)
                


def wheatbg( text : str, style : int = default_style ) -> str :
        """
        It will return the wheatbg colored BackGround text.\n
        wheatbg() is a BackGround Function, if You add ForeGround property given text you can use Wheat .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                wheatbg("Hello World", Style = 0 ) = it's return wheatbg color text without any style       \n
                wheatbg("Hello World", Style = 1 ) = it's return wheatbg color text with bold text          \n
                wheatbg("Hello World", Style = 2 ) = it's return wheatbg color text with light text         \n
                wheatbg("Hello World", Style = 3 ) = it's return wheatbg color text with Italicized style   \n
                wheatbg("Hello World", Style = 4 ) = it's return wheatbg color text with UnderLine          \n
                wheatbg("Hello World", Style = 5 ) = it's return Blinking wheatbg color text                \n
        """
        return Colors.back_ground_color(text, style, 216, 216, 191)
                


def blanchedalmondbg( text : str, style : int = default_style ) -> str :
        """
        It will return the blanchedalmondbg colored BackGround text.\n
        blanchedalmondbg() is a BackGround Function, if You add ForeGround property given text you can use BlanchedAlmond .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                blanchedalmondbg("Hello World", Style = 0 ) = it's return blanchedalmondbg color text without any style       \n
                blanchedalmondbg("Hello World", Style = 1 ) = it's return blanchedalmondbg color text with bold text          \n
                blanchedalmondbg("Hello World", Style = 2 ) = it's return blanchedalmondbg color text with light text         \n
                blanchedalmondbg("Hello World", Style = 3 ) = it's return blanchedalmondbg color text with Italicized style   \n
                blanchedalmondbg("Hello World", Style = 4 ) = it's return blanchedalmondbg color text with UnderLine          \n
                blanchedalmondbg("Hello World", Style = 5 ) = it's return Blinking blanchedalmondbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 235, 205)
                


def darkgoldenrodbg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkgoldenrodbg colored BackGround text.\n
        darkgoldenrodbg() is a BackGround Function, if You add ForeGround property given text you can use DarkGoldenrod .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkgoldenrodbg("Hello World", Style = 0 ) = it's return darkgoldenrodbg color text without any style       \n
                darkgoldenrodbg("Hello World", Style = 1 ) = it's return darkgoldenrodbg color text with bold text          \n
                darkgoldenrodbg("Hello World", Style = 2 ) = it's return darkgoldenrodbg color text with light text         \n
                darkgoldenrodbg("Hello World", Style = 3 ) = it's return darkgoldenrodbg color text with Italicized style   \n
                darkgoldenrodbg("Hello World", Style = 4 ) = it's return darkgoldenrodbg color text with UnderLine          \n
                darkgoldenrodbg("Hello World", Style = 5 ) = it's return Blinking darkgoldenrodbg color text                \n
        """
        return Colors.back_ground_color(text, style, 184, 134, 11)
                


def darkgoldenrod1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkgoldenrod1bg colored BackGround text.\n
        darkgoldenrod1bg() is a BackGround Function, if You add ForeGround property given text you can use DarkGoldenrod1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkgoldenrod1bg("Hello World", Style = 0 ) = it's return darkgoldenrod1bg color text without any style       \n
                darkgoldenrod1bg("Hello World", Style = 1 ) = it's return darkgoldenrod1bg color text with bold text          \n
                darkgoldenrod1bg("Hello World", Style = 2 ) = it's return darkgoldenrod1bg color text with light text         \n
                darkgoldenrod1bg("Hello World", Style = 3 ) = it's return darkgoldenrod1bg color text with Italicized style   \n
                darkgoldenrod1bg("Hello World", Style = 4 ) = it's return darkgoldenrod1bg color text with UnderLine          \n
                darkgoldenrod1bg("Hello World", Style = 5 ) = it's return Blinking darkgoldenrod1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 185, 15)
                


def darkgoldenrod2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkgoldenrod2bg colored BackGround text.\n
        darkgoldenrod2bg() is a BackGround Function, if You add ForeGround property given text you can use DarkGoldenrod2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkgoldenrod2bg("Hello World", Style = 0 ) = it's return darkgoldenrod2bg color text without any style       \n
                darkgoldenrod2bg("Hello World", Style = 1 ) = it's return darkgoldenrod2bg color text with bold text          \n
                darkgoldenrod2bg("Hello World", Style = 2 ) = it's return darkgoldenrod2bg color text with light text         \n
                darkgoldenrod2bg("Hello World", Style = 3 ) = it's return darkgoldenrod2bg color text with Italicized style   \n
                darkgoldenrod2bg("Hello World", Style = 4 ) = it's return darkgoldenrod2bg color text with UnderLine          \n
                darkgoldenrod2bg("Hello World", Style = 5 ) = it's return Blinking darkgoldenrod2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 173, 14)
                


def darkgoldenrod3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkgoldenrod3bg colored BackGround text.\n
        darkgoldenrod3bg() is a BackGround Function, if You add ForeGround property given text you can use DarkGoldenrod3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkgoldenrod3bg("Hello World", Style = 0 ) = it's return darkgoldenrod3bg color text without any style       \n
                darkgoldenrod3bg("Hello World", Style = 1 ) = it's return darkgoldenrod3bg color text with bold text          \n
                darkgoldenrod3bg("Hello World", Style = 2 ) = it's return darkgoldenrod3bg color text with light text         \n
                darkgoldenrod3bg("Hello World", Style = 3 ) = it's return darkgoldenrod3bg color text with Italicized style   \n
                darkgoldenrod3bg("Hello World", Style = 4 ) = it's return darkgoldenrod3bg color text with UnderLine          \n
                darkgoldenrod3bg("Hello World", Style = 5 ) = it's return Blinking darkgoldenrod3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 149, 12)
                


def darkgoldenrod4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the darkgoldenrod4bg colored BackGround text.\n
        darkgoldenrod4bg() is a BackGround Function, if You add ForeGround property given text you can use DarkGoldenrod4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                darkgoldenrod4bg("Hello World", Style = 0 ) = it's return darkgoldenrod4bg color text without any style       \n
                darkgoldenrod4bg("Hello World", Style = 1 ) = it's return darkgoldenrod4bg color text with bold text          \n
                darkgoldenrod4bg("Hello World", Style = 2 ) = it's return darkgoldenrod4bg color text with light text         \n
                darkgoldenrod4bg("Hello World", Style = 3 ) = it's return darkgoldenrod4bg color text with Italicized style   \n
                darkgoldenrod4bg("Hello World", Style = 4 ) = it's return darkgoldenrod4bg color text with UnderLine          \n
                darkgoldenrod4bg("Hello World", Style = 5 ) = it's return Blinking darkgoldenrod4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 101, 8)
                


def lemonchiffonbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lemonchiffonbg colored BackGround text.\n
        lemonchiffonbg() is a BackGround Function, if You add ForeGround property given text you can use LemonChiffon .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lemonchiffonbg("Hello World", Style = 0 ) = it's return lemonchiffonbg color text without any style       \n
                lemonchiffonbg("Hello World", Style = 1 ) = it's return lemonchiffonbg color text with bold text          \n
                lemonchiffonbg("Hello World", Style = 2 ) = it's return lemonchiffonbg color text with light text         \n
                lemonchiffonbg("Hello World", Style = 3 ) = it's return lemonchiffonbg color text with Italicized style   \n
                lemonchiffonbg("Hello World", Style = 4 ) = it's return lemonchiffonbg color text with UnderLine          \n
                lemonchiffonbg("Hello World", Style = 5 ) = it's return Blinking lemonchiffonbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 250, 205)
                


def lemonchiffon1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lemonchiffon1bg colored BackGround text.\n
        lemonchiffon1bg() is a BackGround Function, if You add ForeGround property given text you can use LemonChiffon1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lemonchiffon1bg("Hello World", Style = 0 ) = it's return lemonchiffon1bg color text without any style       \n
                lemonchiffon1bg("Hello World", Style = 1 ) = it's return lemonchiffon1bg color text with bold text          \n
                lemonchiffon1bg("Hello World", Style = 2 ) = it's return lemonchiffon1bg color text with light text         \n
                lemonchiffon1bg("Hello World", Style = 3 ) = it's return lemonchiffon1bg color text with Italicized style   \n
                lemonchiffon1bg("Hello World", Style = 4 ) = it's return lemonchiffon1bg color text with UnderLine          \n
                lemonchiffon1bg("Hello World", Style = 5 ) = it's return Blinking lemonchiffon1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 250, 205)
                


def lemonchiffon2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lemonchiffon2bg colored BackGround text.\n
        lemonchiffon2bg() is a BackGround Function, if You add ForeGround property given text you can use LemonChiffon2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lemonchiffon2bg("Hello World", Style = 0 ) = it's return lemonchiffon2bg color text without any style       \n
                lemonchiffon2bg("Hello World", Style = 1 ) = it's return lemonchiffon2bg color text with bold text          \n
                lemonchiffon2bg("Hello World", Style = 2 ) = it's return lemonchiffon2bg color text with light text         \n
                lemonchiffon2bg("Hello World", Style = 3 ) = it's return lemonchiffon2bg color text with Italicized style   \n
                lemonchiffon2bg("Hello World", Style = 4 ) = it's return lemonchiffon2bg color text with UnderLine          \n
                lemonchiffon2bg("Hello World", Style = 5 ) = it's return Blinking lemonchiffon2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 233, 191)
                


def lemonchiffon3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lemonchiffon3bg colored BackGround text.\n
        lemonchiffon3bg() is a BackGround Function, if You add ForeGround property given text you can use LemonChiffon3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lemonchiffon3bg("Hello World", Style = 0 ) = it's return lemonchiffon3bg color text without any style       \n
                lemonchiffon3bg("Hello World", Style = 1 ) = it's return lemonchiffon3bg color text with bold text          \n
                lemonchiffon3bg("Hello World", Style = 2 ) = it's return lemonchiffon3bg color text with light text         \n
                lemonchiffon3bg("Hello World", Style = 3 ) = it's return lemonchiffon3bg color text with Italicized style   \n
                lemonchiffon3bg("Hello World", Style = 4 ) = it's return lemonchiffon3bg color text with UnderLine          \n
                lemonchiffon3bg("Hello World", Style = 5 ) = it's return Blinking lemonchiffon3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 201, 165)
                


def lemonchiffon4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lemonchiffon4bg colored BackGround text.\n
        lemonchiffon4bg() is a BackGround Function, if You add ForeGround property given text you can use LemonChiffon4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lemonchiffon4bg("Hello World", Style = 0 ) = it's return lemonchiffon4bg color text without any style       \n
                lemonchiffon4bg("Hello World", Style = 1 ) = it's return lemonchiffon4bg color text with bold text          \n
                lemonchiffon4bg("Hello World", Style = 2 ) = it's return lemonchiffon4bg color text with light text         \n
                lemonchiffon4bg("Hello World", Style = 3 ) = it's return lemonchiffon4bg color text with Italicized style   \n
                lemonchiffon4bg("Hello World", Style = 4 ) = it's return lemonchiffon4bg color text with UnderLine          \n
                lemonchiffon4bg("Hello World", Style = 5 ) = it's return Blinking lemonchiffon4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 137, 112)
                


def lightgoldenrodbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightgoldenrodbg colored BackGround text.\n
        lightgoldenrodbg() is a BackGround Function, if You add ForeGround property given text you can use LightGoldenrod .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightgoldenrodbg("Hello World", Style = 0 ) = it's return lightgoldenrodbg color text without any style       \n
                lightgoldenrodbg("Hello World", Style = 1 ) = it's return lightgoldenrodbg color text with bold text          \n
                lightgoldenrodbg("Hello World", Style = 2 ) = it's return lightgoldenrodbg color text with light text         \n
                lightgoldenrodbg("Hello World", Style = 3 ) = it's return lightgoldenrodbg color text with Italicized style   \n
                lightgoldenrodbg("Hello World", Style = 4 ) = it's return lightgoldenrodbg color text with UnderLine          \n
                lightgoldenrodbg("Hello World", Style = 5 ) = it's return Blinking lightgoldenrodbg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 221, 130)
                


def lightgoldenrod1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightgoldenrod1bg colored BackGround text.\n
        lightgoldenrod1bg() is a BackGround Function, if You add ForeGround property given text you can use LightGoldenrod1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightgoldenrod1bg("Hello World", Style = 0 ) = it's return lightgoldenrod1bg color text without any style       \n
                lightgoldenrod1bg("Hello World", Style = 1 ) = it's return lightgoldenrod1bg color text with bold text          \n
                lightgoldenrod1bg("Hello World", Style = 2 ) = it's return lightgoldenrod1bg color text with light text         \n
                lightgoldenrod1bg("Hello World", Style = 3 ) = it's return lightgoldenrod1bg color text with Italicized style   \n
                lightgoldenrod1bg("Hello World", Style = 4 ) = it's return lightgoldenrod1bg color text with UnderLine          \n
                lightgoldenrod1bg("Hello World", Style = 5 ) = it's return Blinking lightgoldenrod1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 236, 139)
                


def lightgoldenrod2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightgoldenrod2bg colored BackGround text.\n
        lightgoldenrod2bg() is a BackGround Function, if You add ForeGround property given text you can use LightGoldenrod2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightgoldenrod2bg("Hello World", Style = 0 ) = it's return lightgoldenrod2bg color text without any style       \n
                lightgoldenrod2bg("Hello World", Style = 1 ) = it's return lightgoldenrod2bg color text with bold text          \n
                lightgoldenrod2bg("Hello World", Style = 2 ) = it's return lightgoldenrod2bg color text with light text         \n
                lightgoldenrod2bg("Hello World", Style = 3 ) = it's return lightgoldenrod2bg color text with Italicized style   \n
                lightgoldenrod2bg("Hello World", Style = 4 ) = it's return lightgoldenrod2bg color text with UnderLine          \n
                lightgoldenrod2bg("Hello World", Style = 5 ) = it's return Blinking lightgoldenrod2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 220, 130)
                


def lightgoldenrod3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightgoldenrod3bg colored BackGround text.\n
        lightgoldenrod3bg() is a BackGround Function, if You add ForeGround property given text you can use LightGoldenrod3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightgoldenrod3bg("Hello World", Style = 0 ) = it's return lightgoldenrod3bg color text without any style       \n
                lightgoldenrod3bg("Hello World", Style = 1 ) = it's return lightgoldenrod3bg color text with bold text          \n
                lightgoldenrod3bg("Hello World", Style = 2 ) = it's return lightgoldenrod3bg color text with light text         \n
                lightgoldenrod3bg("Hello World", Style = 3 ) = it's return lightgoldenrod3bg color text with Italicized style   \n
                lightgoldenrod3bg("Hello World", Style = 4 ) = it's return lightgoldenrod3bg color text with UnderLine          \n
                lightgoldenrod3bg("Hello World", Style = 5 ) = it's return Blinking lightgoldenrod3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 190, 112)
                


def lightgoldenrod4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightgoldenrod4bg colored BackGround text.\n
        lightgoldenrod4bg() is a BackGround Function, if You add ForeGround property given text you can use LightGoldenrod4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightgoldenrod4bg("Hello World", Style = 0 ) = it's return lightgoldenrod4bg color text without any style       \n
                lightgoldenrod4bg("Hello World", Style = 1 ) = it's return lightgoldenrod4bg color text with bold text          \n
                lightgoldenrod4bg("Hello World", Style = 2 ) = it's return lightgoldenrod4bg color text with light text         \n
                lightgoldenrod4bg("Hello World", Style = 3 ) = it's return lightgoldenrod4bg color text with Italicized style   \n
                lightgoldenrod4bg("Hello World", Style = 4 ) = it's return lightgoldenrod4bg color text with UnderLine          \n
                lightgoldenrod4bg("Hello World", Style = 5 ) = it's return Blinking lightgoldenrod4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 129, 76)
                


def lightgoldenrodyellowbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightgoldenrodyellowbg colored BackGround text.\n
        lightgoldenrodyellowbg() is a BackGround Function, if You add ForeGround property given text you can use LightGoldenrodYellow .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightgoldenrodyellowbg("Hello World", Style = 0 ) = it's return lightgoldenrodyellowbg color text without any style       \n
                lightgoldenrodyellowbg("Hello World", Style = 1 ) = it's return lightgoldenrodyellowbg color text with bold text          \n
                lightgoldenrodyellowbg("Hello World", Style = 2 ) = it's return lightgoldenrodyellowbg color text with light text         \n
                lightgoldenrodyellowbg("Hello World", Style = 3 ) = it's return lightgoldenrodyellowbg color text with Italicized style   \n
                lightgoldenrodyellowbg("Hello World", Style = 4 ) = it's return lightgoldenrodyellowbg color text with UnderLine          \n
                lightgoldenrodyellowbg("Hello World", Style = 5 ) = it's return Blinking lightgoldenrodyellowbg color text                \n
        """
        return Colors.back_ground_color(text, style, 250, 250, 210)
                


def lightyellowbg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightyellowbg colored BackGround text.\n
        lightyellowbg() is a BackGround Function, if You add ForeGround property given text you can use LightYellow .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightyellowbg("Hello World", Style = 0 ) = it's return lightyellowbg color text without any style       \n
                lightyellowbg("Hello World", Style = 1 ) = it's return lightyellowbg color text with bold text          \n
                lightyellowbg("Hello World", Style = 2 ) = it's return lightyellowbg color text with light text         \n
                lightyellowbg("Hello World", Style = 3 ) = it's return lightyellowbg color text with Italicized style   \n
                lightyellowbg("Hello World", Style = 4 ) = it's return lightyellowbg color text with UnderLine          \n
                lightyellowbg("Hello World", Style = 5 ) = it's return Blinking lightyellowbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 255, 224)
                


def lightyellow1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightyellow1bg colored BackGround text.\n
        lightyellow1bg() is a BackGround Function, if You add ForeGround property given text you can use LightYellow1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightyellow1bg("Hello World", Style = 0 ) = it's return lightyellow1bg color text without any style       \n
                lightyellow1bg("Hello World", Style = 1 ) = it's return lightyellow1bg color text with bold text          \n
                lightyellow1bg("Hello World", Style = 2 ) = it's return lightyellow1bg color text with light text         \n
                lightyellow1bg("Hello World", Style = 3 ) = it's return lightyellow1bg color text with Italicized style   \n
                lightyellow1bg("Hello World", Style = 4 ) = it's return lightyellow1bg color text with UnderLine          \n
                lightyellow1bg("Hello World", Style = 5 ) = it's return Blinking lightyellow1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 255, 224)
                


def lightyellow2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightyellow2bg colored BackGround text.\n
        lightyellow2bg() is a BackGround Function, if You add ForeGround property given text you can use LightYellow2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightyellow2bg("Hello World", Style = 0 ) = it's return lightyellow2bg color text without any style       \n
                lightyellow2bg("Hello World", Style = 1 ) = it's return lightyellow2bg color text with bold text          \n
                lightyellow2bg("Hello World", Style = 2 ) = it's return lightyellow2bg color text with light text         \n
                lightyellow2bg("Hello World", Style = 3 ) = it's return lightyellow2bg color text with Italicized style   \n
                lightyellow2bg("Hello World", Style = 4 ) = it's return lightyellow2bg color text with UnderLine          \n
                lightyellow2bg("Hello World", Style = 5 ) = it's return Blinking lightyellow2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 238, 209)
                


def lightyellow3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightyellow3bg colored BackGround text.\n
        lightyellow3bg() is a BackGround Function, if You add ForeGround property given text you can use LightYellow3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightyellow3bg("Hello World", Style = 0 ) = it's return lightyellow3bg color text without any style       \n
                lightyellow3bg("Hello World", Style = 1 ) = it's return lightyellow3bg color text with bold text          \n
                lightyellow3bg("Hello World", Style = 2 ) = it's return lightyellow3bg color text with light text         \n
                lightyellow3bg("Hello World", Style = 3 ) = it's return lightyellow3bg color text with Italicized style   \n
                lightyellow3bg("Hello World", Style = 4 ) = it's return lightyellow3bg color text with UnderLine          \n
                lightyellow3bg("Hello World", Style = 5 ) = it's return Blinking lightyellow3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 205, 180)
                


def lightyellow4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the lightyellow4bg colored BackGround text.\n
        lightyellow4bg() is a BackGround Function, if You add ForeGround property given text you can use LightYellow4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                lightyellow4bg("Hello World", Style = 0 ) = it's return lightyellow4bg color text without any style       \n
                lightyellow4bg("Hello World", Style = 1 ) = it's return lightyellow4bg color text with bold text          \n
                lightyellow4bg("Hello World", Style = 2 ) = it's return lightyellow4bg color text with light text         \n
                lightyellow4bg("Hello World", Style = 3 ) = it's return lightyellow4bg color text with Italicized style   \n
                lightyellow4bg("Hello World", Style = 4 ) = it's return lightyellow4bg color text with UnderLine          \n
                lightyellow4bg("Hello World", Style = 5 ) = it's return Blinking lightyellow4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 139, 122)
                


def palegoldenrodbg( text : str, style : int = default_style ) -> str :
        """
        It will return the palegoldenrodbg colored BackGround text.\n
        palegoldenrodbg() is a BackGround Function, if You add ForeGround property given text you can use PaleGoldenrod .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                palegoldenrodbg("Hello World", Style = 0 ) = it's return palegoldenrodbg color text without any style       \n
                palegoldenrodbg("Hello World", Style = 1 ) = it's return palegoldenrodbg color text with bold text          \n
                palegoldenrodbg("Hello World", Style = 2 ) = it's return palegoldenrodbg color text with light text         \n
                palegoldenrodbg("Hello World", Style = 3 ) = it's return palegoldenrodbg color text with Italicized style   \n
                palegoldenrodbg("Hello World", Style = 4 ) = it's return palegoldenrodbg color text with UnderLine          \n
                palegoldenrodbg("Hello World", Style = 5 ) = it's return Blinking palegoldenrodbg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 232, 170)
                


def papayawhipbg( text : str, style : int = default_style ) -> str :
        """
        It will return the papayawhipbg colored BackGround text.\n
        papayawhipbg() is a BackGround Function, if You add ForeGround property given text you can use PapayaWhip .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                papayawhipbg("Hello World", Style = 0 ) = it's return papayawhipbg color text without any style       \n
                papayawhipbg("Hello World", Style = 1 ) = it's return papayawhipbg color text with bold text          \n
                papayawhipbg("Hello World", Style = 2 ) = it's return papayawhipbg color text with light text         \n
                papayawhipbg("Hello World", Style = 3 ) = it's return papayawhipbg color text with Italicized style   \n
                papayawhipbg("Hello World", Style = 4 ) = it's return papayawhipbg color text with UnderLine          \n
                papayawhipbg("Hello World", Style = 5 ) = it's return Blinking papayawhipbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 239, 213)
                


def cornsilkbg( text : str, style : int = default_style ) -> str :
        """
        It will return the cornsilkbg colored BackGround text.\n
        cornsilkbg() is a BackGround Function, if You add ForeGround property given text you can use cornsilk .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cornsilkbg("Hello World", Style = 0 ) = it's return cornsilkbg color text without any style       \n
                cornsilkbg("Hello World", Style = 1 ) = it's return cornsilkbg color text with bold text          \n
                cornsilkbg("Hello World", Style = 2 ) = it's return cornsilkbg color text with light text         \n
                cornsilkbg("Hello World", Style = 3 ) = it's return cornsilkbg color text with Italicized style   \n
                cornsilkbg("Hello World", Style = 4 ) = it's return cornsilkbg color text with UnderLine          \n
                cornsilkbg("Hello World", Style = 5 ) = it's return Blinking cornsilkbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 248, 220)
                


def cornsilk1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cornsilk1bg colored BackGround text.\n
        cornsilk1bg() is a BackGround Function, if You add ForeGround property given text you can use cornsilk1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cornsilk1bg("Hello World", Style = 0 ) = it's return cornsilk1bg color text without any style       \n
                cornsilk1bg("Hello World", Style = 1 ) = it's return cornsilk1bg color text with bold text          \n
                cornsilk1bg("Hello World", Style = 2 ) = it's return cornsilk1bg color text with light text         \n
                cornsilk1bg("Hello World", Style = 3 ) = it's return cornsilk1bg color text with Italicized style   \n
                cornsilk1bg("Hello World", Style = 4 ) = it's return cornsilk1bg color text with UnderLine          \n
                cornsilk1bg("Hello World", Style = 5 ) = it's return Blinking cornsilk1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 248, 220)
                


def cornsilk2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cornsilk2bg colored BackGround text.\n
        cornsilk2bg() is a BackGround Function, if You add ForeGround property given text you can use cornsilk2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cornsilk2bg("Hello World", Style = 0 ) = it's return cornsilk2bg color text without any style       \n
                cornsilk2bg("Hello World", Style = 1 ) = it's return cornsilk2bg color text with bold text          \n
                cornsilk2bg("Hello World", Style = 2 ) = it's return cornsilk2bg color text with light text         \n
                cornsilk2bg("Hello World", Style = 3 ) = it's return cornsilk2bg color text with Italicized style   \n
                cornsilk2bg("Hello World", Style = 4 ) = it's return cornsilk2bg color text with UnderLine          \n
                cornsilk2bg("Hello World", Style = 5 ) = it's return Blinking cornsilk2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 232, 205)
                


def cornsilk3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cornsilk3bg colored BackGround text.\n
        cornsilk3bg() is a BackGround Function, if You add ForeGround property given text you can use cornsilk3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cornsilk3bg("Hello World", Style = 0 ) = it's return cornsilk3bg color text without any style       \n
                cornsilk3bg("Hello World", Style = 1 ) = it's return cornsilk3bg color text with bold text          \n
                cornsilk3bg("Hello World", Style = 2 ) = it's return cornsilk3bg color text with light text         \n
                cornsilk3bg("Hello World", Style = 3 ) = it's return cornsilk3bg color text with Italicized style   \n
                cornsilk3bg("Hello World", Style = 4 ) = it's return cornsilk3bg color text with UnderLine          \n
                cornsilk3bg("Hello World", Style = 5 ) = it's return Blinking cornsilk3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 200, 177)
                


def cornsilk4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the cornsilk4bg colored BackGround text.\n
        cornsilk4bg() is a BackGround Function, if You add ForeGround property given text you can use cornsilk4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                cornsilk4bg("Hello World", Style = 0 ) = it's return cornsilk4bg color text without any style       \n
                cornsilk4bg("Hello World", Style = 1 ) = it's return cornsilk4bg color text with bold text          \n
                cornsilk4bg("Hello World", Style = 2 ) = it's return cornsilk4bg color text with light text         \n
                cornsilk4bg("Hello World", Style = 3 ) = it's return cornsilk4bg color text with Italicized style   \n
                cornsilk4bg("Hello World", Style = 4 ) = it's return cornsilk4bg color text with UnderLine          \n
                cornsilk4bg("Hello World", Style = 5 ) = it's return Blinking cornsilk4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 136, 120)
                


def goldenrodbg( text : str, style : int = default_style ) -> str :
        """
        It will return the goldenrodbg colored BackGround text.\n
        goldenrodbg() is a BackGround Function, if You add ForeGround property given text you can use goldenrod .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                goldenrodbg("Hello World", Style = 0 ) = it's return goldenrodbg color text without any style       \n
                goldenrodbg("Hello World", Style = 1 ) = it's return goldenrodbg color text with bold text          \n
                goldenrodbg("Hello World", Style = 2 ) = it's return goldenrodbg color text with light text         \n
                goldenrodbg("Hello World", Style = 3 ) = it's return goldenrodbg color text with Italicized style   \n
                goldenrodbg("Hello World", Style = 4 ) = it's return goldenrodbg color text with UnderLine          \n
                goldenrodbg("Hello World", Style = 5 ) = it's return Blinking goldenrodbg color text                \n
        """
        return Colors.back_ground_color(text, style, 218, 165, 32)
                


def goldenrod1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the goldenrod1bg colored BackGround text.\n
        goldenrod1bg() is a BackGround Function, if You add ForeGround property given text you can use goldenrod1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                goldenrod1bg("Hello World", Style = 0 ) = it's return goldenrod1bg color text without any style       \n
                goldenrod1bg("Hello World", Style = 1 ) = it's return goldenrod1bg color text with bold text          \n
                goldenrod1bg("Hello World", Style = 2 ) = it's return goldenrod1bg color text with light text         \n
                goldenrod1bg("Hello World", Style = 3 ) = it's return goldenrod1bg color text with Italicized style   \n
                goldenrod1bg("Hello World", Style = 4 ) = it's return goldenrod1bg color text with UnderLine          \n
                goldenrod1bg("Hello World", Style = 5 ) = it's return Blinking goldenrod1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 193, 37)
                


def goldenrod2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the goldenrod2bg colored BackGround text.\n
        goldenrod2bg() is a BackGround Function, if You add ForeGround property given text you can use goldenrod2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                goldenrod2bg("Hello World", Style = 0 ) = it's return goldenrod2bg color text without any style       \n
                goldenrod2bg("Hello World", Style = 1 ) = it's return goldenrod2bg color text with bold text          \n
                goldenrod2bg("Hello World", Style = 2 ) = it's return goldenrod2bg color text with light text         \n
                goldenrod2bg("Hello World", Style = 3 ) = it's return goldenrod2bg color text with Italicized style   \n
                goldenrod2bg("Hello World", Style = 4 ) = it's return goldenrod2bg color text with UnderLine          \n
                goldenrod2bg("Hello World", Style = 5 ) = it's return Blinking goldenrod2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 180, 34)
                


def goldenrod3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the goldenrod3bg colored BackGround text.\n
        goldenrod3bg() is a BackGround Function, if You add ForeGround property given text you can use goldenrod3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                goldenrod3bg("Hello World", Style = 0 ) = it's return goldenrod3bg color text without any style       \n
                goldenrod3bg("Hello World", Style = 1 ) = it's return goldenrod3bg color text with bold text          \n
                goldenrod3bg("Hello World", Style = 2 ) = it's return goldenrod3bg color text with light text         \n
                goldenrod3bg("Hello World", Style = 3 ) = it's return goldenrod3bg color text with Italicized style   \n
                goldenrod3bg("Hello World", Style = 4 ) = it's return goldenrod3bg color text with UnderLine          \n
                goldenrod3bg("Hello World", Style = 5 ) = it's return Blinking goldenrod3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 155, 29)
                


def goldenrod4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the goldenrod4bg colored BackGround text.\n
        goldenrod4bg() is a BackGround Function, if You add ForeGround property given text you can use goldenrod4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                goldenrod4bg("Hello World", Style = 0 ) = it's return goldenrod4bg color text without any style       \n
                goldenrod4bg("Hello World", Style = 1 ) = it's return goldenrod4bg color text with bold text          \n
                goldenrod4bg("Hello World", Style = 2 ) = it's return goldenrod4bg color text with light text         \n
                goldenrod4bg("Hello World", Style = 3 ) = it's return goldenrod4bg color text with Italicized style   \n
                goldenrod4bg("Hello World", Style = 4 ) = it's return goldenrod4bg color text with UnderLine          \n
                goldenrod4bg("Hello World", Style = 5 ) = it's return Blinking goldenrod4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 105, 20)
                


def moccasinbg( text : str, style : int = default_style ) -> str :
        """
        It will return the moccasinbg colored BackGround text.\n
        moccasinbg() is a BackGround Function, if You add ForeGround property given text you can use moccasin .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                moccasinbg("Hello World", Style = 0 ) = it's return moccasinbg color text without any style       \n
                moccasinbg("Hello World", Style = 1 ) = it's return moccasinbg color text with bold text          \n
                moccasinbg("Hello World", Style = 2 ) = it's return moccasinbg color text with light text         \n
                moccasinbg("Hello World", Style = 3 ) = it's return moccasinbg color text with Italicized style   \n
                moccasinbg("Hello World", Style = 4 ) = it's return moccasinbg color text with UnderLine          \n
                moccasinbg("Hello World", Style = 5 ) = it's return Blinking moccasinbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 228, 181)
                


def yellowbg( text : str, style : int = default_style ) -> str :
        """
        It will return the yellowbg colored BackGround text.\n
        yellowbg() is a BackGround Function, if You add ForeGround property given text you can use yellow .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                yellowbg("Hello World", Style = 0 ) = it's return yellowbg color text without any style       \n
                yellowbg("Hello World", Style = 1 ) = it's return yellowbg color text with bold text          \n
                yellowbg("Hello World", Style = 2 ) = it's return yellowbg color text with light text         \n
                yellowbg("Hello World", Style = 3 ) = it's return yellowbg color text with Italicized style   \n
                yellowbg("Hello World", Style = 4 ) = it's return yellowbg color text with UnderLine          \n
                yellowbg("Hello World", Style = 5 ) = it's return Blinking yellowbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 255, 0)
                


def yellow1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the yellow1bg colored BackGround text.\n
        yellow1bg() is a BackGround Function, if You add ForeGround property given text you can use yellow1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                yellow1bg("Hello World", Style = 0 ) = it's return yellow1bg color text without any style       \n
                yellow1bg("Hello World", Style = 1 ) = it's return yellow1bg color text with bold text          \n
                yellow1bg("Hello World", Style = 2 ) = it's return yellow1bg color text with light text         \n
                yellow1bg("Hello World", Style = 3 ) = it's return yellow1bg color text with Italicized style   \n
                yellow1bg("Hello World", Style = 4 ) = it's return yellow1bg color text with UnderLine          \n
                yellow1bg("Hello World", Style = 5 ) = it's return Blinking yellow1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 255, 0)
                


def yellow2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the yellow2bg colored BackGround text.\n
        yellow2bg() is a BackGround Function, if You add ForeGround property given text you can use yellow2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                yellow2bg("Hello World", Style = 0 ) = it's return yellow2bg color text without any style       \n
                yellow2bg("Hello World", Style = 1 ) = it's return yellow2bg color text with bold text          \n
                yellow2bg("Hello World", Style = 2 ) = it's return yellow2bg color text with light text         \n
                yellow2bg("Hello World", Style = 3 ) = it's return yellow2bg color text with Italicized style   \n
                yellow2bg("Hello World", Style = 4 ) = it's return yellow2bg color text with UnderLine          \n
                yellow2bg("Hello World", Style = 5 ) = it's return Blinking yellow2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 238, 0)
                


def yellow3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the yellow3bg colored BackGround text.\n
        yellow3bg() is a BackGround Function, if You add ForeGround property given text you can use yellow3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                yellow3bg("Hello World", Style = 0 ) = it's return yellow3bg color text without any style       \n
                yellow3bg("Hello World", Style = 1 ) = it's return yellow3bg color text with bold text          \n
                yellow3bg("Hello World", Style = 2 ) = it's return yellow3bg color text with light text         \n
                yellow3bg("Hello World", Style = 3 ) = it's return yellow3bg color text with Italicized style   \n
                yellow3bg("Hello World", Style = 4 ) = it's return yellow3bg color text with UnderLine          \n
                yellow3bg("Hello World", Style = 5 ) = it's return Blinking yellow3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 205, 0)
                


def yellow4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the yellow4bg colored BackGround text.\n
        yellow4bg() is a BackGround Function, if You add ForeGround property given text you can use yellow4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                yellow4bg("Hello World", Style = 0 ) = it's return yellow4bg color text without any style       \n
                yellow4bg("Hello World", Style = 1 ) = it's return yellow4bg color text with bold text          \n
                yellow4bg("Hello World", Style = 2 ) = it's return yellow4bg color text with light text         \n
                yellow4bg("Hello World", Style = 3 ) = it's return yellow4bg color text with Italicized style   \n
                yellow4bg("Hello World", Style = 4 ) = it's return yellow4bg color text with UnderLine          \n
                yellow4bg("Hello World", Style = 5 ) = it's return Blinking yellow4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 139, 0)
                


def goldbg( text : str, style : int = default_style ) -> str :
        """
        It will return the goldbg colored BackGround text.\n
        goldbg() is a BackGround Function, if You add ForeGround property given text you can use gold .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                goldbg("Hello World", Style = 0 ) = it's return goldbg color text without any style       \n
                goldbg("Hello World", Style = 1 ) = it's return goldbg color text with bold text          \n
                goldbg("Hello World", Style = 2 ) = it's return goldbg color text with light text         \n
                goldbg("Hello World", Style = 3 ) = it's return goldbg color text with Italicized style   \n
                goldbg("Hello World", Style = 4 ) = it's return goldbg color text with UnderLine          \n
                goldbg("Hello World", Style = 5 ) = it's return Blinking goldbg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 215, 0)
                


def gold1bg( text : str, style : int = default_style ) -> str :
        """
        It will return the gold1bg colored BackGround text.\n
        gold1bg() is a BackGround Function, if You add ForeGround property given text you can use gold1 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                gold1bg("Hello World", Style = 0 ) = it's return gold1bg color text without any style       \n
                gold1bg("Hello World", Style = 1 ) = it's return gold1bg color text with bold text          \n
                gold1bg("Hello World", Style = 2 ) = it's return gold1bg color text with light text         \n
                gold1bg("Hello World", Style = 3 ) = it's return gold1bg color text with Italicized style   \n
                gold1bg("Hello World", Style = 4 ) = it's return gold1bg color text with UnderLine          \n
                gold1bg("Hello World", Style = 5 ) = it's return Blinking gold1bg color text                \n
        """
        return Colors.back_ground_color(text, style, 255, 215, 0)
                


def gold2bg( text : str, style : int = default_style ) -> str :
        """
        It will return the gold2bg colored BackGround text.\n
        gold2bg() is a BackGround Function, if You add ForeGround property given text you can use gold2 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                gold2bg("Hello World", Style = 0 ) = it's return gold2bg color text without any style       \n
                gold2bg("Hello World", Style = 1 ) = it's return gold2bg color text with bold text          \n
                gold2bg("Hello World", Style = 2 ) = it's return gold2bg color text with light text         \n
                gold2bg("Hello World", Style = 3 ) = it's return gold2bg color text with Italicized style   \n
                gold2bg("Hello World", Style = 4 ) = it's return gold2bg color text with UnderLine          \n
                gold2bg("Hello World", Style = 5 ) = it's return Blinking gold2bg color text                \n
        """
        return Colors.back_ground_color(text, style, 238, 201, 0)
                


def gold3bg( text : str, style : int = default_style ) -> str :
        """
        It will return the gold3bg colored BackGround text.\n
        gold3bg() is a BackGround Function, if You add ForeGround property given text you can use gold3 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                gold3bg("Hello World", Style = 0 ) = it's return gold3bg color text without any style       \n
                gold3bg("Hello World", Style = 1 ) = it's return gold3bg color text with bold text          \n
                gold3bg("Hello World", Style = 2 ) = it's return gold3bg color text with light text         \n
                gold3bg("Hello World", Style = 3 ) = it's return gold3bg color text with Italicized style   \n
                gold3bg("Hello World", Style = 4 ) = it's return gold3bg color text with UnderLine          \n
                gold3bg("Hello World", Style = 5 ) = it's return Blinking gold3bg color text                \n
        """
        return Colors.back_ground_color(text, style, 205, 173, 0)
                


def gold4bg( text : str, style : int = default_style ) -> str :
        """
        It will return the gold4bg colored BackGround text.\n
        gold4bg() is a BackGround Function, if You add ForeGround property given text you can use gold4 .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                gold4bg("Hello World", Style = 0 ) = it's return gold4bg color text without any style       \n
                gold4bg("Hello World", Style = 1 ) = it's return gold4bg color text with bold text          \n
                gold4bg("Hello World", Style = 2 ) = it's return gold4bg color text with light text         \n
                gold4bg("Hello World", Style = 3 ) = it's return gold4bg color text with Italicized style   \n
                gold4bg("Hello World", Style = 4 ) = it's return gold4bg color text with UnderLine          \n
                gold4bg("Hello World", Style = 5 ) = it's return Blinking gold4bg color text                \n
        """
        return Colors.back_ground_color(text, style, 139, 117, 0)
                


def goldenrodbg( text : str, style : int = default_style ) -> str :
        """
        It will return the goldenrodbg colored BackGround text.\n
        goldenrodbg() is a BackGround Function, if You add ForeGround property given text you can use Goldenrod .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                goldenrodbg("Hello World", Style = 0 ) = it's return goldenrodbg color text without any style       \n
                goldenrodbg("Hello World", Style = 1 ) = it's return goldenrodbg color text with bold text          \n
                goldenrodbg("Hello World", Style = 2 ) = it's return goldenrodbg color text with light text         \n
                goldenrodbg("Hello World", Style = 3 ) = it's return goldenrodbg color text with Italicized style   \n
                goldenrodbg("Hello World", Style = 4 ) = it's return goldenrodbg color text with UnderLine          \n
                goldenrodbg("Hello World", Style = 5 ) = it's return Blinking goldenrodbg color text                \n
        """
        return Colors.back_ground_color(text, style, 219, 219, 112)
                


def medium_goldenrodbg( text : str, style : int = default_style ) -> str :
        """
        It will return the medium_goldenrodbg colored BackGround text.\n
        medium_goldenrodbg() is a BackGround Function, if You add ForeGround property given text you can use Medium_Goldenrod .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                medium_goldenrodbg("Hello World", Style = 0 ) = it's return medium_goldenrodbg color text without any style       \n
                medium_goldenrodbg("Hello World", Style = 1 ) = it's return medium_goldenrodbg color text with bold text          \n
                medium_goldenrodbg("Hello World", Style = 2 ) = it's return medium_goldenrodbg color text with light text         \n
                medium_goldenrodbg("Hello World", Style = 3 ) = it's return medium_goldenrodbg color text with Italicized style   \n
                medium_goldenrodbg("Hello World", Style = 4 ) = it's return medium_goldenrodbg color text with UnderLine          \n
                medium_goldenrodbg("Hello World", Style = 5 ) = it's return Blinking medium_goldenrodbg color text                \n
        """
        return Colors.back_ground_color(text, style, 234, 234, 174)
                


def yellow_greenbg( text : str, style : int = default_style ) -> str :
        """
        It will return the yellow_greenbg colored BackGround text.\n
        yellow_greenbg() is a BackGround Function, if You add ForeGround property given text you can use Yellow_Green .\n
        How to use this function :\n
            text = it's need a string input like ['text' (or) "text"] \n
            Style = [
                                Normal     = 0 \n
                                Bold       = 1 \n
                                Light      = 2 \n
                                Italicized = 3 \n
                                UnderLined = 4 \n        
                                Blink      = 5 \n
                        ]
            Example :\n
                yellow_greenbg("Hello World", Style = 0 ) = it's return yellow_greenbg color text without any style       \n
                yellow_greenbg("Hello World", Style = 1 ) = it's return yellow_greenbg color text with bold text          \n
                yellow_greenbg("Hello World", Style = 2 ) = it's return yellow_greenbg color text with light text         \n
                yellow_greenbg("Hello World", Style = 3 ) = it's return yellow_greenbg color text with Italicized style   \n
                yellow_greenbg("Hello World", Style = 4 ) = it's return yellow_greenbg color text with UnderLine          \n
                yellow_greenbg("Hello World", Style = 5 ) = it's return Blinking yellow_greenbg color text                \n
        """
        
        return Colors.back_ground_color(text, style, 153, 204, 50)
                


