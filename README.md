# Terminal Designer
We are thrilled to announce the release of TerminalDesigner version 0.0.1! TerminalDesigner is a powerful Python package that brings advanced text processing capabilities to the terminal environment, allowing you to create visually appealing and dynamic text-based designs.

Key Features:

1. Text Styling: With TerminalDesigner, you can easily modify the background and foreground colors of your text, enabling you to create eye-catching designs that stand out in the terminal.
    
2. ASCII Art Conversion: Convert your images into ASCII art directly from the terminal. TerminalDesigner provides a built-in function that converts images into a collection of ASCII characters, allowing you to display images in a unique and creative way.
    
3. Random Text Color: Add a touch of randomness to your text by applying random colors. This feature is perfect for creating vibrant and dynamic visual effects or generating unique designs every time.
    
4. Easy Integration: TerminalDesigner is designed to be easy to use and integrate into your Python projects. Simply install the package using pip and import it into your code to start leveraging its powerful text processing capabilities.
    
5. Comprehensive Documentation: We have provided detailed documentation to guide you through the installation process, usage instructions, and examples of how to leverage the various features of TerminalDesigner. The documentation will help you quickly get up to speed and make the most out of the package.
    

To install TerminalDesigner version 0.0.1, run the following command in your terminal:

Copy code

`pip install TerminalDesigner==0.0.1` 

We are continuously working on improving TerminalDesigner and adding more exciting features. Your feedback and suggestions are highly appreciated as they will help us shape the future development of this package.

For more information and code examples, please visit the official TerminalDesigner GitHub repository: [TerminalDesigner](https://github.com/NagiPragalathan/TerminalDesigner)

We hope you enjoy using TerminalDesigner 0.0.1 and that it brings a new level of creativity and visual appeal to your terminal-based projects. Thank you for your support, and happy coding!

The tutorial titled "Python Terminal Processing with TerminalDesigner Module" provides a step-by-step guide on how to install TerminalDesigner, explains the various features and functions of the module, and demonstrates practical examples of using TerminalDesigner for text styling, ASCII art conversion, and random text color generation.

By following this tutorial, you will gain a deeper understanding of TerminalDesigner and how to leverage its capabilities to enhance your terminal-based projects. The tutorial is designed to be beginner-friendly and provides clear explanations along with code snippets to help you grasp the concepts easily.

You can access the tutorial on GeeksforGeeks by visiting the following link: [Python Terminal Processing with TerminalDesigner Module](https://www.geeksforgeeks.org/python-terminal-processing-with-terminaldesigner-module/)

We hope this additional resource helps you further explore and master the TerminalDesigner module. Happy learning!

## Install the Package from python
    https://pypi.org/project/TerminalDesigner/0.0.1/
    
(or)

    pip install TerminalDesigner==0.0.1

After installation you can import the package using

    import Designer

## There are 7 python files.
- BackGroundColor.py
- Color.py
- ForeGroundColor.py
- General.py
- HexName.py
- RandomColor.py
- Values.py

There are **255** different shades with **610** colors combinations. these colors are handle with **6** Modules :-
- BackGroundColor.py
- Color.py
- ForeGroundColor.py
- General.py
- HexName.py
- RandomColor.py
_____________________________________________________________________________

# 1.BackGroundColor Module
it have **610** color named functions and set_default_stylebg() extra one of the function.
>Note : this function names are have colors name + bg
**for example : redbg("hello"),bluebg("world")**

It is easy to use we just import the BackGroundColor Function From Designer and call the names of the colors.
It will return the colored BackGround text.
## How to use functions in the module:
* **text** = it's need a string input like ['text' (or) "text"]
* **Style** :-
    - Normal     = 0
    - Bold       = 1
    - Light      = 2
    - Italicized = 3
    - UnderLined = 4        
    - Blink      = 5
* ## Example :
    >**Nameof theFunction**("Hello World", Style = 0 ) it's return color text without any style    

    >**Nameof theFunction**("Hello World", Style = 1 ) it's return color text with bold text       

    >**Nameof theFunction**("Hello World", Style = 2 ) it's return color text with light text      

    >**Nameof theFunction**("Hello World", Style = 3 ) it's return color text with Italicized style

    >**Nameof theFunction**("Hello World", Style = 4 ) it's return color text with UnderLine       

    >**Nameof theFunction**<("Hello World", Style = 5 ) it's return Blinking  color text             


## for example:
        #import the all functions BackGroundColor Module then just call

        print(redbg("hello")+bluebg("world"))
        print(brownbg("it's"),pinkbg("realy"),greenbg("interesting"))
        print(redbg("hello"+pinkbg("world")))
## BackGround Module set_default_stylebg() function
  >its,s need only one parameter String type it's return type is None.

  >it's used to change the default values (or) change the value of style to all colors
 ## Ex : set_default_stylebg(3) then it chenge the Italicized style to all color_function
----------------------------------------------------
* Some style propertys
    - Normal     = 0
    - Bold       = 1
    - Light      = 2
    - Italicized = 3
    - UnderLined = 4        
    - Blink      = 5

> **Return**: it's return None Value,it's not return any values just it change the changes in BackGroundColor file.
        
---------------------------------------------------------------------------

# 2.ForeGroundColor Module
    

it have **610** color named functions and set_default_style() extra one of the function.
It is easy to use we just import the ForeGroundColor Function From Designer and call the names of the colors.
It will return the colored ForeGround text.
## How to use functions in the module:
* **text** = it's need a string input like ['text' (or) "text"]
* **Style** :-
    - Normal     = 0
    - Bold       = 1
    - Light      = 2
    - Italicized = 3
    - UnderLined = 4        
    - Blink      = 5
* ## Example :
    >**Nameof theFunction**("Hello World", Style = 0 ) it's return color text without any style    

    >**Nameof theFunction**("Hello World", Style = 1 ) it's return color text with bold text       

    >**Nameof theFunction**("Hello World", Style = 2 ) it's return color text with light text      

    >**Nameof theFunction**("Hello World", Style = 3 ) it's return color text with Italicized style

    >**Nameof theFunction**("Hello World", Style = 4 ) it's return color text with UnderLine       

    >**Nameof theFunction**<("Hello World", Style = 5 ) it's return Blinking  color text             


## for example:
        #import the all functions BackGroundColor Module then just call

        print(red("hello")+blue("world"))
        print(brown("it's"),pink("pink"),green("interesting"))
        print(red("hello"+pink("world")))
# BackGround Module set_default_style() function
  >its,s need only one parameter String type it's return type is None.

  >it's used to change the default values (or) change the value of style to all colors
 ## Ex : set_default_stylebg(3) then it change the Italicized style to all color_function
----------------------------------------------------
* Some style propertys
    - Normal     = 0
    - Bold       = 1
    - Light      = 2
    - Italicized = 3
    - UnderLined = 4        
    - Blink      = 5

> **Return**: it's **return None** Value,it's not return any values just it change the changes in BackGroundColor file.

# 3. HaxName Module

> **Note**: it's just like ForeGround Module these function names are hax value names.

it have **610** color named functions and *set_default_style()* extra one of the function.
It is easy to use we just import the ForeGroundColor Function From Designer and call the names of the colors.
It will return the colored ForeGround text.
## How to use functions in the module:
* **text** = it's need a string input like ['text' (or) "text"]
* **Style** :-
    - Normal     = 0
    - Bold       = 1
    - Light      = 2
    - Italicized = 3
    - UnderLined = 4        
    - Blink      = 5
* ## Example :
    >**Nameof theFunction**("Hello World", Style = 0 ) it's return color text without any style    

    >**Nameof theFunction**("Hello World", Style = 1 ) it's return color text with bold text       

    >**Nameof theFunction**("Hello World", Style = 2 ) it's return color text with light text      

    >**Nameof theFunction**("Hello World", Style = 3 ) it's return color text with Italicized style

    >**Nameof theFunction**("Hello World", Style = 4 ) it's return color text with UnderLine       

    >**Nameof theFunction**<("Hello World", Style = 5 ) it's return Blinking  color text             


## for example:
        #import the all functions BackGroundColor Module then just call

        print(red("hello")+blue("world"))
        print(brown("it's"),pink("relay"),green("interesting"))
        print(red("hello"+pink("world")))
# BackGround Module set_default_style() function
  >its,s need only one parameter String type it's return type is None.

  >it's used to change the default values (or) change the value of style to all colors
 ## Ex : set_default_stylebg(3) then it change the Italicized style to all color_function
----------------------------------------------------
* Some style propertys
    - **Normal**     = 0
    - **Bold**       = 1
    - **Light**      = 2
    - **Italicized** = 3
    - **UnderLined** = 4        
    - **Blink**      = 5

> **Return**: it's **return None** Value,it's not return any values just it change the changes in BackGroundColor file.
-----------------------------------------------------

# 4.RandomColor Module
There are 6 ( *functions frd2b, frb2d, brd2b, brb2d, bgrandomclr, fgrandomclr* ) this function are performance are based on random.

* ## fgrandomclr()
    it's return the random colored ForeGround text(stringType) based on given text.
    >def fgrandomclr( String : str ) -> str :

    <h2 style="color:red" >import  the RandomColor Module from Designer

        Example:
        fgrandomclr("The")
* ## bgrandomclr()
    it's return the random colored BackGround(stringType) text based on given text.
    >def bgrandomclr( String : str ) -> str :
        
        Example:
             bgrandomclr( "world" ):
* ## brb2d()
    its's return the bright to dull color given text for BackGround.
    >def brb2d(String : str) -> str:

        Example:
             print(brb2d("is"))
* ## brd2b()
    its's return the dull to bright color given text for BackGround.

    >def brd2b(String : str) -> str:

        Example:
            print(brd2b("Fake"))
* ## frb2d()
    its's return the bright to dull color given text for ForeGround
    >def frb2d(String : str) -> str:

        Example:
            print(frb2d("hello"))
* ## frd2b()
    its's return the dull to bright color given text for ForeGround
    >def frd2b(String : str) -> str:

        Example:
            print(frd2b("hello"))

-----------------------------------------------------

# 5.General Module
This Model have generally used functions. it's have**one class** and **14** functions:
* # class
    * # image_
        it's need to file path of the image.
            
            Example :
            image_ = image_("/file/path/file.jpg")
       *  ## rgb_value()
            it's return the Pixels of the image.
            > def rgb_value(self) -> list :
                Example :
                    print(image_.rgb_value())
        * ## img_size()
            it's return the size of the image.
            >def img_size(self) -> tuple:
                Example:
                    print(image_.img_size())
        * ## used_colors() 
            it's return the tuple.the tuple have used colors in the image.
            >def used_colors(self,graph_view= False, return_graph_view = False, graph_view_with_rgb=False,view_text="") -> Union[str,tuple]:
            
            ## Parameters
            * **graph_view** - if the graph_view is true it print the colors in the terminal
            * **return_graph_view** - if the return_graph_view is true it return the colors value.
            * **graph_view_with_rgb** - if graph_view_with_rgb is true print or return the rgb values with bg color
            * **view_text** - view_text is used to print the given text with used background.
                    Example:
                        image_.used_colors()
                        #it return the used colors in tuple type.
        * # most_used_color()
            it return the tuple it have most used color which is rgb.
            >def most_used_color(self) -> str:
                Example:
                    image_.most_used_color()
                    # it return most  used color of rgb value which is tuple.

* # Functions
    * # img_to_ascii()
        it's very interesting module,it's convert image into ascii code.the return type is string.
        >def img_to_ascii(Path) -> str :

            Example :
                path = "/file/patch/image.jpg " 
                img_to_ascii()
                # it's return string which is replicate image.
    * # start()
         it's apply the given colors in terminal which is after printing this start function.it's until apply the given color to text until will call the end function.
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
                    Example:
                        #import all the functions from General model
                        start("red")
                        #its apply the red color after printing text in the terminal
    * # stop()
        it's stop the applying colors which is performed by start.
        >def stop() -> str :

            Example:
                start("blue")
                stop()
                #it's apply the blue color to the text between start() and end().
    * # clrscreen()
        it just clear the terminal's screen.
        >def clrscreen() -> None :
        
            Example:
                #import module & call
                clrscreen()
                #after calling screen will clear.
    
    * # Fullbgclr()
        it's apply background and foreground color to total terminal screen based on given parameters.
        >def Fullbgclr( FColor : str, BColor :str ) -> None:
        ## Parameters
        * FColor = it's need the string value to__ForeGround__ of the text.
        - BColor = it's need the string value to__BackGround__ of the text.
        ## These values are suitable inputs :
        * `{'BLACK': 0, 'BLUE': 1, 'GREEN': 2,'AQUA': 3, 'RED': 4, 'PURPLE': 5, 'YELLOW':6, 'WHITE ': 7, 'GRAY': 8, 'LIGHT BLUE': 9,'LIGHT GREEN': 'A', 'BRIGHT WHITE': 'F','LIGHT AQUA': 'B', 'LIGHT YELLOW': 'E','LIGHT RED': 'C', 'LIGHT PURPLE': 'D'}`
        * `1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B','C', 'D',' E', 'F'`

                Example:
                    Fullbgclr("red","black")
    * # color()
        it apply the color given string and just return the rgb value of the given text.
        >def color(TColor : str, String:str)->str:

        # Parameters
        Tolor : it need a Color name to apply.
        String : it's need a string value

            Example : 
                color("red","hello")
    
     * # image_art()
        it's also very interesting module,it's convert image into colored text code.the colored text are replicate the image in terminal.the return type is string.
        >Note : it's Only get JPG File and using below ( 150 X 150 )px image is more suitable
        function :
        >def img_to_ascii(Path) -> str :
        ## Parameters
        - Character = it takes string (or)   - character using this output are replicate given image
        - Path = it's need Path of the file
        - Type = it's need inputs like ForeGround["fg"] (or) BackGround["bg"] so based on that the output replicate

                Example :
                    image_art(Character : str, Path: str)
                    image_art( "*", /../../)
                    path = "/file/patch/image.jpg " 
                    # it's return colored string which is replicate image.
    * ## rgb_to_txt
        it's used to print the colored text based on given rgb value
        >Note : it's take single (r,g,b) value.
        >def rgb_to_txt(text : str, rgb : tuple style : int = 0,type_ : str ="fg") ->  str:
        
            Example:
                rgb_to_txt("str",(255,255,255))
    * ## rgb_to_name()
        there is the module under development so the rgb values in data it's return name of the data else it return 0.
        
        >def rgb_to_name(rgb_val : tuple) -> Union[str,int] :
        
            Example:
                rgb_to_name((0,0,0))
        
    * # name_to_rgb()
        there is the module under development so the given name in data it's return value of the data else it return None. 
        >def name_to_rgb(Name_of the_color : str )-> tuple :

            Example:
                name_to_rgb("red")
    
    * # hex_to_name()
        there is the module under development so the given hex in data it's return value of thr data else it return None.
        >def hex_to_name(Name_of the_color : str )-> str:   
            Example:

                hex_to_name("#FFFFFF")
    * # name_to_hex()
        there is the module under development so the given name in data it's return value of the data else it return None.
        > name_to_hex(hex_val : str ) -> str:

            Example:
            name_to_hex("green")
    * # rgb_to_hex()
        there is the module under development so the given rgb in data it's return value of the data else it return None. 
        >def rgb_to_hex(rgb_val : tuple ) -> str:
        
            Example:
                rgb_to_hex((0,0,0))
    * # hex_to_rgb()
        there is the module under development so the given hex in data it's return value of the data else it return None. 
        >def hex_to_rgb(rgb_val : str ) -> tuple:

            Example:
                hex_to_rgb("#FFFFFF")

-------------------------------------------------------

# 6.Color Module
 it have one class that is **Colors**.
 Color's have two functions. 
 * fore_ground_color
 * back_ground_color 
     -----------------------------------------
     * ## fore_ground_color()
         it's return the color code of the given text. it's return the color code based on given RGB.
         >fore_ground_color(text : str, r : int, g : int, b : int, style : int = 0)
         # Parameters
          * text = it's need a string input\n
          *  r, b, g = This is the RGB color code like white RGB(255,255,255)\n
          * # Style:
             - Normal     = 0
             - Bold       = 1
             - Light      = 2
             - Italicized = 3
             - UnderLined = 4        
             - Blink      = 5
         
             Example :
                 #import the function from colors module
                 fore_ground_color("hello",0,0,0,2)
     --------------------------------------------
     * ## back_ground_color()
         it's return the BackGround color code of the given text. it's return the color code based on given RGB.
         > back_ground_color(text : str, r : int, g : int, b : int, style : int = 0)
         # Parameters
          * text = it's need a string input\n
          *  r, b, g = This is the RGB color code like white RGB(255,255,255)\n
          * # Style:
             - Normal     = 0
             - Bold       = 1
             - Light      = 2
             - Italicized = 3
             - UnderLined = 4        
             - Blink      = 5
         
             Example :
                 #import the function from colors module
                 back_ground_color("black",0,0,0,3)
------------------------------------------------------
* # 7.Values
    this is have the colors and rgb values to the variables.
    ## variables
    - ValuesNRH
    - hex_name
    - name_hex 
    - tuple_name
    - rgb
    - colors
----------------------------------------
# Performance
 it perform terminal color operations.
 ## Like
 - ForeGround
 - BackGround
 
 Each module are perform each works.

-----------------------------------------
# Author
**Name** : Nagi Pragalatha.N

**Email** : nagipragalathan@gmail.com

**About** : https://nagipragalathan.github.io/Personal_website/about.html

**GitHub** :  https://github.com/NagiPragalathan/

**Contact** : [InstaGram](https://instagram.com/mr_lazy_05?igshid=YmMyMTA2M2Y=),[FaceBook](https://www.facebook.com/profile.php?id=100081414617956),[LinkedIn](https://www.linkedin.com/in/nagi-pragalathan-n-a03a55230)

--------------------------------------------
# Package
**Name** : Designer

**Version** : 0.0.0.1

**License** : MIT

--------------------------------------------

# Thank you for visiting--

--------------------------------------------


#  BackGroundColor Module's functions

        Grey(), Grey_Silver(), grey(), LightGray(), LightSlateGrey(), SlateGray(), SlateGray1(), SlateGray2(), SlateGray3(), SlateGray4(), black(), grey0(), grey1(), grey2(), grey3(), grey4(), grey5(), grey6(), grey7(), grey8(), grey9(), grey10(), grey11(), grey12(), grey13(), light_black(), grey14(), grey15(), grey16(), grey17(), grey18(), grey19(), grey20(), grey21(), grey22(), grey23(), grey24(), grey25(), grey26(), grey27(), grey28(), grey29(), grey30(), grey31(), grey32(), grey33(), light_gray(), grey34(), grey35(), grey36(), grey37(), grey38(), grey39(), grey40(), grey41_DimGrey(), grey42(), grey43(), grey44(), grey45(), grey46(), grey47(), grey48(), grey49(), grey50(), grey51(), grey52(), grey53(), grey54(), grey55(), grey56(), grey57(), grey58(), grey59(), grey60(), grey61(), grey62(), grey63(), grey64(), grey65(), grey66(), grey67(), grey68(), grey69(), grey70(), grey71(), grey72(), grey73(), grey74(), grey75(), grey76(), grey77(), grey78(), grey79(), grey80(), grey81(), grey82(), grey83(), grey84(), grey85(), grey86(), grey87(), grey88(), grey89(), grey90(), grey91(), grey92(), grey93(), grey94(), grey95(), grey96(), grey97(), grey98(), grey99(), grey100_White(), Dark_Slate_Grey(), Dim_Grey(), Light_Grey(), Very_Light_Grey(), Free_Speech_Grey(), AliceBlue(), BlueViolet(), Cadet_Blue(), CadetBlue(), CadetBlue1(), CadetBlue2(), CadetBlue3(), CadetBlue4(), Corn_Flower_Blue(), CornflowerBlue(), DarkSlateBlue(), DarkTurquoise(), DeepSkyBlue(), DeepSkyBlue1(), DeepSkyBlue2(), DeepSkyBlue3(), DeepSkyBlue4(), DodgerBlue(), DodgerBlue1(), DodgerBlue2(), DodgerBlue3(), DodgerBlue4(), LightBlue(), LightBlue1(), LightBlue2(), LightBlue3(), LightBlue4(), LightCyan(), LightCyan1(), LightCyan2(), LightCyan3(), LightCyan4(), LightSkyBlue(), LightSkyBlue1(), LightSkyBlue2(), LightSkyBlue3(), LightSkyBlue4(), LightSlateBlue(), LightSteelBlue(), LightSteelBlue1(), LightSteelBlue2(), LightSteelBlue3(), LightSteelBlue4(), Aquamarine(), MediumBlue(), MediumSlateBlue(), MediumTurquoise(), MidnightBlue(), NavyBlue(), PaleTurquoise(), PaleTurquoise1(), PaleTurquoise2(), PaleTurquoise3(), PaleTurquoise4(), PowderBlue(), RoyalBlue(), RoyalBlue1(), RoyalBlue2(), RoyalBlue3(), RoyalBlue4(), RoyalBlue5(), SkyBlue(), SkyBlue1(), SkyBlue2(), SkyBlue3(), SkyBlue4(), SlateBlue(), SlateBlue1(), SlateBlue2(), SlateBlue3(), SlateBlue4(), SteelBlue(), SteelBlue1(), SteelBlue2(), SteelBlue3(), SteelBlue4(), aquamarine(), aquamarine1(), aquamarine2(), MediumAquamarine(), aquamarine4(), azure(), azure1(), azure2(), azure3(), azure4(), blue(), blue1(), blue2(), blue3(), blue4(), aqua(), cyan(), cyan1(), cyan2(), cyan3(), cyan4(), navy(), teal(), turquoise(), turquoise1(), turquoise2(), turquoise3(), turquoise4(), DarkSlateGray(), DarkSlateGray1(), DarkSlateGray2(), DarkSlateGray3(), DarkSlateGray4(), Dark_Slate_Blue(), Dark_Turquoise(), Medium_Slate_Blue(), Medium_Turquoise(), Midnight_Blue(), Navy_Blue(), Neon_Blue(), New_Midnight_Blue(), Rich_Blue(), Sky_Blue(), Slate_Blue(), Summer_Sky(), Iris_Blue(), Free_Speech_Blue(), RosyBrown(), RosyBrown1(), RosyBrown2(), RosyBrown3(), RosyBrown4(), SaddleBrown(), SandyBrown(), beige(), brown(), brown1(), brown2(), brown3(), brown4(), dark_brown(), burlywood(), burlywood1(), burlywood2(), burlywood3(), burlywood4(), baker_chocolate(), chocolate(), chocolate1(), chocolate2(), chocolate3(), chocolate4(), peru(), tan(), tan1(), tan2(), tan3(), tan4(), Dark_Tan(), Dark_Wood(), Light_Wood(), Medium_Wood(), New_Tan(), Semi_Sweet_Chocolate(), Sienna(), Tan(), Very_Dark_Brown(), Dark_Green(), DarkGreen(), dark_green_copper(), DarkKhaki(), DarkOliveGreen(), DarkOliveGreen1(), DarkOliveGreen2(), DarkOliveGreen3(), DarkOliveGreen4(), olive(), DarkSeaGreen(), DarkSeaGreen1(), DarkSeaGreen2(), DarkSeaGreen3(), DarkSeaGreen4(), ForestGreen(), GreenYellow(), LawnGreen(), LightSeaGreen(), LimeGreen(), MediumSeaGreen(), MediumSpringGreen(), MintCream(), OliveDrab(), OliveDrab1(), OliveDrab2(), OliveDrab3(), OliveDrab4(), PaleGreen(), PaleGreen1(), PaleGreen2(), PaleGreen3(), PaleGreen4(), SeaGreen_SeaGreen4(), SeaGreen1(), SeaGreen2(), SeaGreen3(), SpringGreen(), SpringGreen1(), SpringGreen2(), SpringGreen3(), SpringGreen4(), YellowGreen(), chartreuse(), chartreuse1(), chartreuse2(), chartreuse3(), chartreuse4(), green(), lime(), green1(), green2(), green3(), green4(), khaki(), khaki1(), khaki2(), khaki3(), khaki4(), Dark_Olive_Green(), Medium_Aquamarine(), Medium_Forest_Green(), Medium_Sea_Green(), Medium_Spring_Green(), Pale_Green(), Sea_Green(), Spring_Green(), Free_Speech_Green(), DarkOrange(), DarkOrange1(), DarkOrange2(), DarkOrange3(), DarkOrange4(), DarkSalmon(), LightCoral(), LightSalmon(), LightSalmon1(), LightSalmon2(), LightSalmon3(), LightSalmon4(), PeachPuff(), PeachPuff1(), PeachPuff2(), PeachPuff3(), PeachPuff4(), bisque(), bisque1(), bisque2(), bisque3(), bisque4(), coral(), coral1(), coral2(), coral3(), coral4(), honeydew(), honeydew1(), honeydew2(), honeydew3(), honeydew4(), orange(), orange1(), orange2(), orange3(), orange4(), salmon(), salmon1(), salmon2(), salmon3(), salmon4(), sienna(), sienna1(), sienna2(), sienna3(), sienna4(), Mandarian_Orange(), Orange(), Orange_Red(), DeepPink(), DeepPink1(), DeepPink2(), DeepPink3(), DeepPink4(), HotPink(), HotPink1(), HotPink2(), HotPink3(), HotPink4(), IndianRed(), IndianRed1(), IndianRed2(), IndianRed3(), IndianRed4(), LightPink(), LightPink1(), LightPink2(), LightPink3(), LightPink4(), MediumVioletRed(), MistyRose(), MistyRose1(), MistyRose2(), MistyRose3(), MistyRose4(), OrangeRed(), OrangeRed1(), OrangeRed2(), OrangeRed3(), OrangeRed4(), PaleVioletRed(), PaleVioletRed1(), PaleVioletRed2(), PaleVioletRed3(), PaleVioletRed4(), VioletRed(), VioletRed1(), VioletRed2(), VioletRed3(), VioletRed4(), firebrick(), firebrick1(), firebrick2(), firebrick3(), firebrick4(), pink(), pink1(), pink2(), pink3(), pink4(), Flesh(), Feldspar(), red(), red1(), red2(), red3(), red4(), tomato(), tomato1(), tomato2(), tomato3(), tomato4(), Dusty_Rose(), Firebrick(), Indian_Red(), Pink(), Salmon(), Scarlet(), Spicy_Pink(), Free_Speech_Magenta(), Free_Speech_Red(), DarkOrchid(), DarkOrchid1(), DarkOrchid2(), DarkOrchid3(), DarkOrchid4(), DarkViolet(), LavenderBlush(), LavenderBlush1(), LavenderBlush2(), LavenderBlush3(), LavenderBlush4(), MediumOrchid(), MediumOrchid1(), MediumOrchid2(), MediumOrchid3(), MediumOrchid4(), MediumPurple(), Medium_Orchid(), MediumPurple1(), Dark_Orchid(), MediumPurple2(), MediumPurple3(), MediumPurple4(), lavender(), magenta(), fuchsia(), magenta1(), magenta2(), magenta3(), magenta4(), maroon(), maroon1(), maroon2(), maroon3(), maroon4(), orchid(), Orchid(), orchid1(), orchid2(), orchid3(), orchid4(), plum(), plum1(), plum2(), plum3(), plum4(), purple(), purple1(), purple2(), purple3(), purple4(), thistle(), thistle1(), thistle2(), thistle3(), thistle4(), violet(), violet_blue(), Dark_Purple(), Maroon(), Medium_Violet_Red(), Neon_Pink(), Plum(), Thistle(), Turquoise(), Violet(), Violet_Red(), AntiqueWhite(), AntiqueWhite1(), AntiqueWhite2(), AntiqueWhite3(), AntiqueWhite4(), FloralWhite(), GhostWhite(), NavajoWhite(), NavajoWhite1(), NavajoWhite2(), NavajoWhite3(), NavajoWhite4(), OldLace(), WhiteSmoke(), gainsboro(), ivory(), ivory1(), ivory2(), ivory3(), ivory4(), linen(), seashell(), seashell1(), seashell2(), seashell3(), seashell4(), snow(), snow1(), snow2(), snow3(), snow4(), wheat(), wheat1().

# ForeGround Module's function

        Greybg(), Grey_Silverbg(), greybg(), LightGraybg(), LightSlateGreybg(), SlateGraybg(), SlateGray1bg(), SlateGray2bg(), SlateGray3bg(), SlateGray4bg(), blackbg(), grey0bg(), grey1bg(), grey2bg(), grey3bg(), grey4bg(), grey5bg(), grey6bg(), grey7bg(), grey8bg(), grey9bg(), grey10bg(), grey11bg(), grey12bg(), grey13bg(), light_blackbg(), grey14bg(), grey15bg(), grey16bg(), grey17bg(), grey18bg(), grey19bg(), grey20bg(), grey21bg(), grey22bg(), grey23bg(), grey24bg(), grey25bg(), grey26bg(), grey27bg(), grey28bg(), grey29bg(), grey30bg(), grey31bg(), grey32bg(), grey33bg(), light_graybg(), grey34bg(), grey35bg(), grey36bg(), grey37bg(), grey38bg(), grey39bg(), grey40bg(), grey41_DimGreybg(), grey42bg(), grey43bg(), grey44bg(), grey45bg(), grey46bg(), grey47bg(), grey48bg(), grey49bg(), grey50bg(), grey51bg(), grey52bg(), grey53bg(), grey54bg(), grey55bg(), grey56bg(), grey57bg(), grey58bg(), grey59bg(), grey60bg(), grey61bg(), grey62bg(), grey63bg(), grey64bg(), grey65bg(), grey66bg(), grey67bg(), grey68bg(), grey69bg(), grey70bg(), grey71bg(), grey72bg(), grey73bg(), grey74bg(), grey75bg(), grey76bg(), grey77bg(), grey78bg(), grey79bg(), grey80bg(), grey81bg(), grey82bg(), grey83bg(), grey84bg(), grey85bg(), grey86bg(), grey87bg(), grey88bg(), grey89bg(), grey90bg(), grey91bg(), grey92bg(), grey93bg(), grey94bg(), grey95bg(), grey96bg(), grey97bg(), grey98bg(), grey99bg(), grey100_Whitebg(), Dark_Slate_Greybg(), Dim_Greybg(), Light_Greybg(), Very_Light_Greybg(), Free_Speech_Greybg(), AliceBluebg(), BlueVioletbg(), Cadet_Bluebg(), CadetBluebg(), CadetBlue1bg(), CadetBlue2bg(), CadetBlue3bg(), CadetBlue4bg(), Corn_Flower_Bluebg(), CornflowerBluebg(), DarkSlateBluebg(), DarkTurquoisebg(), DeepSkyBluebg(), DeepSkyBlue1bg(), DeepSkyBlue2bg(), DeepSkyBlue3bg(), DeepSkyBlue4bg(), DodgerBluebg(), DodgerBlue1bg(), DodgerBlue2bg(), DodgerBlue3bg(), DodgerBlue4bg(), LightBluebg(), LightBlue1bg(), LightBlue2bg(), LightBlue3bg(), LightBlue4bg(), LightCyanbg(), LightCyan1bg(), LightCyan2bg(), LightCyan3bg(), LightCyan4bg(), LightSkyBluebg(), LightSkyBlue1bg(), LightSkyBlue2bg(), LightSkyBlue3bg(), LightSkyBlue4bg(), LightSlateBluebg(), LightSteelBluebg(), LightSteelBlue1bg(), LightSteelBlue2bg(), LightSteelBlue3bg(), LightSteelBlue4bg(), Aquamarinebg(), MediumBluebg(), MediumSlateBluebg(), MediumTurquoisebg(), MidnightBluebg(), NavyBluebg(), PaleTurquoisebg(), PaleTurquoise1bg(), PaleTurquoise2bg(), PaleTurquoise3bg(), PaleTurquoise4bg(), PowderBluebg(), RoyalBluebg(), RoyalBlue1bg(), RoyalBlue2bg(), RoyalBlue3bg(), RoyalBlue4bg(), RoyalBlue5bg(), SkyBluebg(), SkyBlue1bg(), SkyBlue2bg(), SkyBlue3bg(), SkyBlue4bg(), SlateBluebg(), SlateBlue1bg(), SlateBlue2bg(), SlateBlue3bg(), SlateBlue4bg(), SteelBluebg(), SteelBlue1bg(), SteelBlue2bg(), SteelBlue3bg(), SteelBlue4bg(), aquamarinebg(), aquamarine1bg(), aquamarine2bg(), MediumAquamarinebg(), aquamarine4bg(), azurebg(), azure1bg(), azure2bg(), azure3bg(), azure4bg(), bluebg(), blue1bg(), blue2bg(), blue3bg(), blue4bg(), aquabg(), cyanbg(), cyan1bg(), cyan2bg(), cyan3bg(), cyan4bg(), navybg(), tealbg(), turquoisebg(), turquoise1bg(), turquoise2bg(), turquoise3bg(), turquoise4bg(), DarkSlateGraybg(), DarkSlateGray1bg(), DarkSlateGray2bg(), DarkSlateGray3bg(), DarkSlateGray4bg(), Dark_Slate_Bluebg(), Dark_Turquoisebg(), Medium_Slate_Bluebg(), Medium_Turquoisebg(), Midnight_Bluebg(), Navy_Bluebg(), Neon_Bluebg(), New_Midnight_Bluebg(), Rich_Bluebg(), Sky_Bluebg(), Slate_Bluebg(), Summer_Skybg(), Iris_Bluebg(), Free_Speech_Bluebg(), RosyBrownbg(), RosyBrown1bg(), RosyBrown2bg(), RosyBrown3bg(), RosyBrown4bg(), SaddleBrownbg(), SandyBrownbg(), beigebg(), brownbg(), brown1bg(), brown2bg(), brown3bg(), brown4bg(), dark_brownbg(), burlywoodbg(), burlywood1bg(), burlywood2bg(), burlywood3bg(), burlywood4bg(), baker_chocolatebg(), chocolatebg(), chocolate1bg(), chocolate2bg(), chocolate3bg(), chocolate4bg(), perubg(), tanbg(), tan1bg(), tan2bg(), tan3bg(), tan4bg(), Dark_Tanbg(), Dark_Woodbg(), Light_Woodbg(), Medium_Woodbg(), New_Tanbg(), Semi_Sweet_Chocolatebg(), Siennabg(), Tanbg(), Very_Dark_Brownbg(), Dark_Greenbg(), DarkGreenbg(), dark_green_copperbg(), DarkKhakibg(), DarkOliveGreenbg(), DarkOliveGreen1bg(), DarkOliveGreen2bg(), DarkOliveGreen3bg(), DarkOliveGreen4bg(), olivebg(), DarkSeaGreenbg(), DarkSeaGreen1bg(), DarkSeaGreen2bg(), DarkSeaGreen3bg(), DarkSeaGreen4bg(), ForestGreenbg(), GreenYellowbg(), LawnGreenbg(), LightSeaGreenbg(), LimeGreenbg(), MediumSeaGreenbg(), MediumSpringGreenbg(), MintCreambg(), OliveDrabbg(), OliveDrab1bg(), OliveDrab2bg(), OliveDrab3bg(), OliveDrab4bg(), PaleGreenbg(), PaleGreen1bg(), PaleGreen2bg(), PaleGreen3bg(), PaleGreen4bg(), SeaGreen_SeaGreen4bg(), SeaGreen1bg(), SeaGreen2bg(), SeaGreen3bg(), SpringGreenbg(), SpringGreen1bg(), SpringGreen2bg(), SpringGreen3bg(), SpringGreen4bg(), YellowGreenbg(), chartreusebg(), chartreuse1bg(), chartreuse2bg(), chartreuse3bg(), chartreuse4bg(), greenbg(), limebg(), green1bg(), green2bg(), green3bg(), green4bg(), khakibg(), khaki1bg(), khaki2bg(), khaki3bg(), khaki4bg(), Dark_Olive_Greenbg(), Medium_Aquamarinebg(), Medium_Forest_Greenbg(), Medium_Sea_Greenbg(), Medium_Spring_Greenbg(), Pale_Greenbg(), Sea_Greenbg(), Spring_Greenbg(), Free_Speech_Greenbg(), DarkOrangebg(), DarkOrange1bg(), DarkOrange2bg(), DarkOrange3bg(), DarkOrange4bg(), DarkSalmonbg(), LightCoralbg(), LightSalmonbg(), LightSalmon1bg(), LightSalmon2bg(), LightSalmon3bg(), LightSalmon4bg(), PeachPuffbg(), PeachPuff1bg(), PeachPuff2bg(), PeachPuff3bg(), PeachPuff4bg(), bisquebg(), bisque1bg(), bisque2bg(), bisque3bg(), bisque4bg(), coralbg(), coral1bg(), coral2bg(), coral3bg(), coral4bg(), honeydewbg(), honeydew1bg(), honeydew2bg(), honeydew3bg(), honeydew4bg(), orangebg(), orange1bg(), orange2bg(), orange3bg(), orange4bg(), salmonbg(), salmon1bg(), salmon2bg(), salmon3bg(), salmon4bg(), siennabg(), sienna1bg(), sienna2bg(), sienna3bg(), sienna4bg(), Mandarian_Orangebg(), Orangebg(), Orange_Redbg(), DeepPinkbg(), DeepPink1bg(), DeepPink2bg(), DeepPink3bg(), DeepPink4bg(), HotPinkbg(), HotPink1bg(), HotPink2bg(), HotPink3bg(), HotPink4bg(), IndianRedbg(), IndianRed1bg(), IndianRed2bg(), IndianRed3bg(), IndianRed4bg(), LightPinkbg(), LightPink1bg(), LightPink2bg(), LightPink3bg(), LightPink4bg(), MediumVioletRedbg(), MistyRosebg(), MistyRose1bg(), MistyRose2bg(), MistyRose3bg(), MistyRose4bg(), OrangeRedbg(), OrangeRed1bg(), OrangeRed2bg(), OrangeRed3bg(), OrangeRed4bg(), PaleVioletRedbg(), PaleVioletRed1bg(), PaleVioletRed2bg(), PaleVioletRed3bg(), PaleVioletRed4bg(), VioletRedbg(), VioletRed1bg(), VioletRed2bg(), VioletRed3bg(), VioletRed4bg(), firebrickbg(), firebrick1bg(), firebrick2bg(), firebrick3bg(), firebrick4bg(), pinkbg(), pink1bg(), pink2bg(), pink3bg(), pink4bg(), Fleshbg(), Feldsparbg(), redbg(), red1bg(), red2bg(), red3bg(), red4bg(), tomatobg(), tomato1bg(), tomato2bg(), tomato3bg(), tomato4bg(), Dusty_Rosebg(), Firebrickbg(), Indian_Redbg(), Pinkbg(), Salmonbg(), Scarletbg(), Spicy_Pinkbg(), Free_Speech_Magentabg(), Free_Speech_Redbg(), DarkOrchidbg(), DarkOrchid1bg(), DarkOrchid2bg(), DarkOrchid3bg(), DarkOrchid4bg(), DarkVioletbg(), LavenderBlushbg(), LavenderBlush1bg(), LavenderBlush2bg(), LavenderBlush3bg(), LavenderBlush4bg(), MediumOrchidbg(), MediumOrchid1bg(), MediumOrchid2bg(), MediumOrchid3bg(), MediumOrchid4bg(), MediumPurplebg(), Medium_Orchidbg(), MediumPurple1bg(), Dark_Orchidbg(), MediumPurple2bg(), MediumPurple3bg(), MediumPurple4bg(), lavenderbg(), magentabg(), fuchsiabg(), magenta1bg(), magenta2bg(), magenta3bg(), magenta4bg(), maroonbg(), maroon1bg(), maroon2bg(), maroon3bg(), maroon4bg(), orchidbg(), Orchidbg(), orchid1bg(), orchid2bg(), orchid3bg(), orchid4bg(), plumbg(), plum1bg(), plum2bg(), plum3bg(), plum4bg(), purplebg(), purple1bg(), purple2bg(), purple3bg(), purple4bg(), thistlebg(), thistle1bg(), thistle2bg(), thistle3bg(), thistle4bg(), violetbg(), violet_bluebg(), Dark_Purplebg(), Maroonbg(), Medium_Violet_Redbg(), Neon_Pinkbg(), Plumbg(), Thistlebg(), Turquoisebg(), Violetbg(), Violet_Redbg(), AntiqueWhitebg(), AntiqueWhite1bg(), AntiqueWhite2bg(), AntiqueWhite3bg(), AntiqueWhite4bg(), FloralWhitebg(), GhostWhitebg(), NavajoWhitebg(), NavajoWhite1bg(), NavajoWhite2bg(), NavajoWhite3bg(), NavajoWhite4bg(), OldLacebg(), WhiteSmokebg(), gainsborobg(), ivorybg(), ivory1bg(), ivory2bg(), ivory3bg(), ivory4bg(), linenbg(), seashellbg(), seashell1bg(), seashell2bg(), seashell3bg(), seashell4bg(), snowbg(), snow1bg(), snow2bg(), snow3bg(), snow4bg(), wheatbg(), wheat1bg().

# HexName Mosule's functions
        h545454(), hC0C0C0(), hBEBEBE(), hD3D3D3(), h778899(), h708090(), hC6E2FF(), hB9D3EE(), h9FB6CD(), h6C7B8B(), h000000(), h030303(), h050505(), h080808(), h0A0A0A(), h0D0D0D(), h0F0F0F(), h121212(), h141414(), h171717(), h1A1A1A(), h1C1C1C(), h1F1F1F(), h212121(), h222222(), h242424(), h262626(), h292929(), h2B2B2B(), h2E2E2E(), h303030(), h333333(), h363636(), h383838(), h3B3B3B(), h3D3D3D(), h404040(), h424242(), h454545(), h474747(), h4A4A4A(), h4D4D4D(), h4F4F4F(), h525252(), h555555(), h575757(), h595959(), h5C5C5C(), h5E5E5E(), h616161(), h636363(), h666666(), h696969(), h6B6B6B(), h6E6E6E(), h707070(), h737373(), h757575(), h787878(), h7A7A7A(), h7D7D7D(), h7F7F7F(), h828282(), h858585(), h878787(), h8A8A8A(), h8C8C8C(), h8F8F8F(), h919191(), h949494(), h969696(), h999999(), h9C9C9C(), h9E9E9E(), hA1A1A1(), hA3A3A3(), hA6A6A6(), hA8A8A8(), hABABAB(), hADADAD(), hB0B0B0(), hB3B3B3(), hB5B5B5(), hB8B8B8(), hBABABA(), hBDBDBD(), hBFBFBF(), hC2C2C2(), hC4C4C4(), hC7C7C7(), hC9C9C9(), hCCCCCC(), hCFCFCF(), hD1D1D1(), hD4D4D4(), hD6D6D6(), hD9D9D9(), hDBDBDB(), hDEDEDE(), hE0E0E0(), hE3E3E3(), hE5E5E5(), hE8E8E8(), hEBEBEB(), hEDEDED(), hF0F0F0(), hF2F2F2(), hF5F5F5(), hF7F7F7(), hFAFAFA(), hFCFCFC(), hFFFFFF(), h2F4F4F(), hDBDB70(), hCDCDCD(), h635688(), hF0F8FF(), h8A2BE2(), h5F9F9F(), h5F9EA0(), h98F5FF(), h8EE5EE(), h7AC5CD(), h53868B(), h42426F(), h6495ED(), h483D8B(), h00CED1(), h00BFFF(), h00B2EE(), h009ACD(), h00688B(), h1E90FF(), h1C86EE(), h1874CD(), h104E8B(), hADD8E6(), hBFEFFF(), hB2DFEE(), h9AC0CD(), h68838B(), hE0FFFF(), hD1EEEE(), hB4CDCD(), h7A8B8B(), h87CEFA(), hB0E2FF(), hA4D3EE(), h8DB6CD(), h607B8B(), h8470FF(), hB0C4DE(), hCAE1FF(), hBCD2EE(), hA2B5CD(), h6E7B8B(), h70DB93(), h0000CD(), h7B68EE(), h48D1CC(), h191970(), h000080(), hAFEEEE(), hBBFFFF(), hAEEEEE(), h96CDCD(), h668B8B(), hB0E0E6(), h4169E1(), h4876FF(), h436EEE(), h3A5FCD(), h27408B(), h002266(), h87CEEB(), h87CEFF(), h7EC0EE(), h6CA6CD(), h4A708B(), h6A5ACD(), h836FFF(), h7A67EE(), h6959CD(), h473C8B(), h4682B4(), h63B8FF(), h5CACEE(), h4F94CD(), h36648B(), h7FFFD4(), h76EEC6(), h66CDAA(), h458B74(), hF0FFFF(), hE0EEEE(), hC1CDCD(), h838B8B(), h0000FF(), h0000EE(), h00008B(), h00FFFF(), h00EEEE(), h00CDCD(), h008B8B(), h008080(), h40E0D0(), h00F5FF(), h00E5EE(), h00C5CD(), h00868B(), h97FFFF(), h8DEEEE(), h79CDCD(), h528B8B(), h241882(), h7093DB(), hCD7F32(), h7F00FF(), h70DBDB(), h2F2F4F(), h23238E(), h4D4DFF(), h00009C(), h5959AB(), h3299CC(), h007FFF(), h38B0DE(), h03B4C8(), h4156C5(), hBC8F8F(), hFFC1C1(), hEEB4B4(), hCD9B9B(), h8B6969(), h8B4513(), hF4A460(), hF5F5DC(), hA52A2A(), hA62A2A(), hFF4040(), hEE3B3B(), hCD3333(), h8B2323(), h5C4033(), hDEB887(), hFFD39B(), hEEC591(), hCDAA7D(), h8B7355(), h5C3317(), hD2691E(), hFF7F24(), hEE7621(), hCD661D(), hCD853F(), hD2B48C(), hFFA54F(), hEE9A49(), h8B5A2B(), h97694F(), h855E42(), h856363(), hA68064(), hEBC79E(), h6B4226(), h8E6B23(), hDB9370(), h2F4F2F(), h006400(), h4A766E(), hBDB76B(), h556B2F(), hCAFF70(), hBCEE68(), hA2CD5A(), h6E8B3D(), h808000(), h8FBC8F(), hC1FFC1(), hB4EEB4(), h9BCD9B(), h698B69(), h228B22(), hADFF2F(), h7CFC00(), h20B2AA(), h32CD32(), h3CB371(), h00FA9A(), hF5FFFA(), h6B8E23(), hC0FF3E(), hB3EE3A(), h9ACD32(), h698B22(), h98FB98(), h9AFF9A(), h90EE90(), h7CCD7C(), h548B54(), h2E8B57(), h54FF9F(), h4EEE94(), h43CD80(), h00FF7F(), h00EE76(), h00CD66(), h008B45(), h7FFF00(), h76EE00(), h66CD00(), h458B00(), h00FF00(), h008000(), h00EE00(), h00CD00(), h008B00(), hF0E68C(), hFFF68F(), hEEE685(), hCDC673(), h8B864E(), h4F4F2F(), hD19275(), h8E2323(), h238E23(), h426F42(), h238E68(), h09F911(), h029D74(), hFF8C00(), hFF7F00(), hEE7600(), hCD6600(), h8B4500(), hE9967A(), hF08080(), hFFA07A(), hEE9572(), hCD8162(), h8B5742(), hFFDAB9(), hEECBAD(), hCDAF95(), h8B7765(), hFFE4C4(), hEED5B7(), hCDB79E(), h8B7D6B(), hFF7F50(), hFF7256(), hEE6A50(), hCD5B45(), h8B3E2F(), hF0FFF0(), hE0EEE0(), hC1CDC1(), h838B83(), hFFA500(), hEE9A00(), hCD8500(), h8B5A00(), hFA8072(), hFF8C69(), hEE8262(), hCD7054(), h8B4C39(), hA0522D(), hFF8247(), hEE7942(), hCD6839(), h8B4726(), hFF2400(), hFF1493(), hEE1289(), hCD1076(), h8B0A50(), hFF69B4(), hFF6EB4(), hEE6AA7(), hCD6090(), h8B3A62(), hCD5C5C(), hFF6A6A(), hEE6363(), hCD5555(), h8B3A3A(), hFFB6C1(), hFFAEB9(), hEEA2AD(), hCD8C95(), h8B5F65(), hC71585(), hFFE4E1(), hEED5D2(), hCDB7B5(), h8B7D7B(), hFF4500(), hEE4000(), hCD3700(), h8B2500(), hDB7093(), hFF82AB(), hEE799F(), hCD6889(), h8B475D(), hD02090(), hFF3E96(), hEE3A8C(), hCD3278(), h8B2252(), hB22222(), hFF3030(), hEE2C2C(), hCD2626(), h8B1A1A(), hFFC0CB(), hFFB5C5(), hEEA9B8(), hCD919E(), h8B636C(), hF5CCB0(), hFF0000(), hEE0000(), hCD0000(), h8B0000(), hFF6347(), hEE5C42(), hCD4F39(), h8B3626(), h6F4242(), h8C1717(), hFF1CAE(), hE35BD8(), hC00000(), h9932CC(), hBF3EFF(), hB23AEE(), h9A32CD(), h68228B(), h9400D3(), hFFF0F5(), hEEE0E5(), hCDC1C5(), h8B8386(), hBA55D3(), hE066FF(), hD15FEE(), hB452CD(), h7A378B(), h9370DB(), hAB82FF(), h9932CD(), h9F79EE(), h8968CD(), h5D478B(), hE6E6FA(), hFF00FF(), hEE00EE(), hCD00CD(), h8B008B(), hB03060(), hFF34B3(), hEE30A7(), hCD2990(), h8B1C62(), hDA70D6(), hDB70DB(), hFF83FA(), hEE7AE9(), hCD69C9(), h8B4789(), hDDA0DD(), hFFBBFF(), hEEAEEE(), hCD96CD(), h8B668B(), hA020F0(), h800080(), h9B30FF(), h912CEE(), h7D26CD(), h551A8B(), hD8BFD8(), hFFE1FF(), hEED2EE(), hCDB5CD(), h8B7B8B(), hEE82EE(), h9F5F9F(), h871F78(), h800000(), hFF6EC7(), hEAADEA(), hADEAEA(), h4F2F4F(), hCC3299(), hFAEBD7(), hFFEFDB(), hEEDFCC(), hCDC0B0(), h8B8378(), hFFFAF0(), hF8F8FF(), hFFDEAD(), hEECFA1(), hCDB38B(), h8B795E(), hFDF5E6(), hDCDCDC(), hFFFFF0(), hEEEEE0(), hCDCDC1(), h8B8B83(), hFAF0E6(), hFFF5EE(), hEEE5DE(), hCDC5BF(), h8B8682(), hFFFAFA(), hEEE9E9(), hCDC9C9(), h8B8989(), hF5DEB3(), hFFE7BA(), hEED8AE(), hCDBA96(), h8B7E66(), hD9D9F3(), hD8D8BF(), hFFEBCD(), hB8860B(), hFFB90F(), hEEAD0E(), hCD950C(), h8B6508(), hFFFACD(), hEEE9BF(), hCDC9A5(), h8B8970(), hEEDD82(), hFFEC8B(), hEEDC82(), hCDBE70(), h8B814C(), hFAFAD2(), hFFFFE0(), hEEEED1(), hCDCDB4(), h8B8B7A(), hEEE8AA(), hFFEFD5(), hFFF8DC(), hEEE8CD(), hCDC8B1(), h8B8878(), hDAA520(), hFFC125(), hEEB422(), hCD9B1D(), h8B6914(), hFFE4B5(), hFFFF00(), hEEEE00(), hCDCD00(), h8B8B00(), hFFD700(), hEEC900(), hCDAD00(), h8B7500(), hEAEAAE(), h99CC32().
