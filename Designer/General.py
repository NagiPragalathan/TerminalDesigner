from .ForeGroundColor import *
from .Color import colors
from PIL import Image
from .Values import tuple_name, hex_name, name_hex
import os


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".","A","B","C","D","E","F","G","H","I"]
ListOfColors : list = list(rgb.keys())
Type = ""


class image_:
    path = ""
    def __init__(self,Path : str) -> None :
        self.path = Path
    def rgb_value(self) -> list :
        """ it's return the Pixles of the image """
        self.img = Image.open(self.path)
        pix = list(self.img.getdata())
        return pix
    def img_size(self) -> tuple:
        """it's return the size of the image return type tuple"""
        self.img = Image.open(self.path)
        width, height = self.img.size
        return (width, height)
    
    def used_colors(self,graph_view=False,return_graph_view=False,graph_view_with_rgb=False,view_text=".") -> Union[str,tuple]:
        """ it's return the tuple.the tuple have used colors in the image 
            if the graph_view is true it print the colors in the terminal.\n
            if the return_graph_view is true it return the colors value.\n
            if graph_view_with_rgb is true print or return the rgb values with bg color.\n
            view_text is used to print the given text with used background. 
            """
        
        rgb_val : list = self.rgb_value()
        rm_dup = list(set(rgb_val))
        width = os.get_terminal_size().columns
        widthCenterPoint = int(width/2)
        if(graph_view):
            if return_graph_view:
                str_ = ""
                for x,i in enumerate(rm_dup):
                    if graph_view_with_rgb:
                        str_= str_+rgb_to_txt(f"{i}",i,type_="bg")
                    elif(graph_view_with_rgb==None):
                        str_= str_+rgb_to_txt(f"{x}",i,type_="bg")
                    else:
                        str_= str_+rgb_to_txt(f"{view_text}",i,type_="bg")
                return str_
            else:
                for x,i in enumerate(rm_dup):
                    if graph_view_with_rgb:
                        print(rgb_to_txt(f"{i}",i,type_="bg"),end="")
                    elif(graph_view_with_rgb==None):
                        print(rgb_to_txt(f"{x}",i,type_="bg"),end="")
                    else:
                        print(rgb_to_txt(f"{view_text}",i,type_="bg"),end="")
        else:
            return rm_dup
    def most_used_color(self) -> str:
        """it return the tuple it have most used color which is rgb."""
        rgb_val : list = self.rgb_value()
        rm_dup = list(set(rgb_val))
        for i in rm_dup:
            max=0
            return_ = tuple()
            if(max < rgb_val.count(i)):
                max = rgb_val.count(i)
                return_ = i
        return return_

def img_to_ascii(Path) -> str :
    """ it's convert image to ascii code """
    a=Image.open(Path).convert('L')
    pixels = a.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def start( String : str ,Type_ : str = "fg", style : int = 0) -> str :
    """ it's apply the given colors in terminal which is after printing this start function.it's until apply the given color to text until will call the end function.
        >def start( String : str ,Type_ : str ="fg", style : int = 0) -> str :
         ## Parameters
        * **String** = it's need a string type input.
        * **Type_** : it's need the only two input that is nether "bg" nor "fg".
        * **style** : it's need an int type input.
            ## values 
            - Normal     = 0
            - Bold       = 1
            - Light      = 2
            - Italicized = 3
            - UnderLined = 4        
            - Blink      = 5
                    Example:\n
                        #import all the functions from General model\n
                        start("red") \n
                        #its apply the red color after printing text in the terminal
    """
    global Type
    Type = Type_
    value : list = colors.get(String.upper())
    if( Type == "fg" ):
        print("\033[{};38;2;{};{};{}m' '".format( style, value[0], value[1], value[2]))
        return "\033[{};38;2;{};{};{}m' '".format( style, value[0], value[1], value[2])
    else:
        print("\033[{};48;2;{};{};{}m' '".format( style, value[0], value[1], value[2]))
        return "\033[{};48;2;{};{};{}m' '".format( style, value[0], value[1], value[2])
    
def stop() -> str :
    """it's stop the applying colors which is performed by start.\n
        Example:\n
                    start("blue")\n
                    stop()\n
                    #it's apply the blue color to the text between start() and end().
    """
    if( Type == "fg" ):
        print("\033[0;38;0;255;255;255m")
        return "\033[0;38;0;255;255;255m"
    else:
        print("\033[0;48;0;255;255;255m")
        return "\033[0;48;0;255;255;255m"
    
def clrscreen() -> None :
    """ ## it just clear the terminal's screen.\n
        >def clrscreen() -> None :
        
            Example:
                #import module & call
                clrscreen()
                #after calling screen will clear."""
    print("clearing...")
    os.system("clear || cls")

def Fullbgclr( FColor : str, BColor : str ) -> None:
    """it's apply background and foreground color to total terminal screen based on given parameters.\n
        >def Fullbgclr( FColor : str, BColor :str ) -> None:\n
        ## Parameters
        * FColor = it's need the string value to__ForeGround__ of the text.
        - BColor = it's need the string value to__BackGround__ of the text.
        ## These values are suitable inputs :
        * `{'BLACK': 0, 'BLUE': 1, 'GREEN': 2,'AQUA': 3, 'RED': 4, 'PURPLE': 5, 'YELLOW':6, 'WHITE ': 7, 'GRAY': 8, 'LIGHT BLUE': 9,'LIGHT GREEN': 'A', 'BRIGHT WHITE': 'F','LIGHT AQUA': 'B', 'LIGHT YELLOW': 'E','LIGHT RED': 'C', 'LIGHT PURPLE': 'D'}`
        * `1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B','C', 'D',' E', 'F'`

                Example:
                    Fullbgclr("red","black")"""
    Values : dict = {'BLACK': 0, 'BLUE': 1, 'GREEN': 2, 'AQUA': 3, 'RED': 4, 'PURPLE': 5, 'YELLOW': 6, 'WHITE ': 7, 'GRAY': 8, 'LIGHT BLUE': 9, 'LIGHT GREEN': 'A', 'BRIGHT WHITE': 'F', 'LIGHT AQUA': 'B', 'LIGHT YELLOW': 'E', 'LIGHT RED': 'C', 'LIGHT PURPLE': 'D'
              ,"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","A":"A","F":"F","B":"B","E":"E","C":"C","D":"D"}    
    try:
        fval : str = Values.get(str(FColor).upper())
        bval : str = Values.get(str(BColor).upper())
        os.system("color "+str(fval)+str(bval))
    except:
        raise ValueError("""Undefind value (non-listed value) select values between { 0 : "Black", 1 : "Blue", 2 : "Green", 3 : "Aqua", 4 : "Red", 5 : "Purple", 6 : "Yellow", 7 : "White ", 8 : "Gray", 9 : "Light Blue", "A" : "Light Green", "F" : "Bright White", "B" : "Light Aqua", "E" : "Light Yellow", "C" : "Light Red", "D" : "Light Purple"}""")

def color(TColor : str, String:str)->str:
    """it apply the color given string and just return the rgb value of the given text.\n
        >def color(TColor : str, String:str)->str:

        # Parameters
        
        Tolor : it need a Color name to apply.
        String : it's need a string value

            Example : 
                color("red","hello")"""
    value : list = list(colors.get(TColor.upper()))
    return "\033[0;38;2;{};{};{}m{}\033[0;38;0;255;255;255m".format(value[0], value[1], value[2], String)

def rgb_to_txt(text : str, rgb : tuple,style : int = 0,type_ : str ="fg") ->  str:
    """ it's used to print the colored text based on given rgb value\n
        Note : it's take single (r,g,b) value"""
    try:
        if ( type_ == "fg" ):
            return "\033[{};38;2;{};{};{}m{}\033[0;38;2;255;255;255m".format(style,rgb[0], rgb[1], rgb[2], text)
        else:
            return "\033[{};48;2;{};{};{}m{}\033[0;48;0;255;255;255m".format(style,rgb[0], rgb[1], rgb[2], text)
            
    except:
        raise TypeError(" Unsupported input type it needs a tuple() ")
    
    
    
def image_art(Character : str, Path : str,Type = "fg") -> str :
    """ it's return the Coloerd text based on given image\n
    -------------------------------------------------------------------------------------------\n
        Note : it's Only get JPG File and using below ( 150 X 150 )px image is more suitable  |\n
    -------------------------------------------------------------------------------------------\n
        ex : image_art(Character : str, Path : str)\n
        Character = it takes string (or) character using this output are replicate given image\n
        Path = it's need Path of the file\n
        Type = it's need inputs like ForeGround["fg"] (or) BackGround["bg"] so based on that the output replicate\n
        for example : image_art( "*", /../../)
    """
    rgb : image_ =image_(Path)
    val : image_ = rgb.rgb_value()
    Size = rgb.img_size()
    try:
        print("prossing...")
        text_art : str = ""
        count : int = 0
        for i in range(Size[0]):
            text_art = text_art + "\n"
            for j in range(Size[1]):
                count : int = count + 1
                text_art : str = text_art + rgb_to_txt(Character,val[count-1],type_=Type)
        return text_art 
    except:
        raise TypeError(" Unsupported image type (or) file")

def rgb_to_name(rgb_val : tuple) -> Union[str,int] :
        """ there is the module under development so the rgb values in datas it's return name of the data else it return 0."""
        datas = tuple_name
        data=list(datas.keys())
        if rgb_val in data:
            return datas.get(rgb_val)
        else:
            return 0
        
def name_to_rgb(Name_ofthe_color : str ) -> tuple :
    """ there is the module under development so the given name in datas it's return value of the data else it return None."""
    return colors.get(Name_ofthe_color.upper())

def hex_to_name(Name_ofthe_color : str ) -> str:
    """ there is the module under development so the given hex in datas it's return value of the data else it return None."""
    return hex_name.get(Name_ofthe_color)
def name_to_hex(hex_val : str ) -> str:
    """ there is the module under development so the given name in datas it's return value of the data else it return None."""
    return name_hex.get(hex_val)

def rgb_to_hex(rgb_val : tuple ) -> str:
    """ there is the module under development so the given rgb in datas it's return value of the data else it return None."""
    return name_to_hex(rgb_to_name(rgb_val))

def hex_to_rgb(rgb_val : str ) -> tuple:
    """ there is the module under development so the given hex in datas it's return value of the data else it return None."""
    return name_to_rgb(hex_to_name(rgb_val))
    
