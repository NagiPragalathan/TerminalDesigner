from random import choice
from .ForeGroundColor import *
from .Color import colors

ListOfColors : list = list(rgb.keys())
Type = ""

def fgrandomclr( String : str ) -> str :
    """ it's return the random colored ForeGround text(stringType) based on given text. """
    Return : str = " "
    for i in String :
        Choice : str = choice(ListOfColors)
        value : list = rgb.get(Choice)
        Return : str = Return + "\033[0;38;2;{};{};{}m{}\033[0;38;0;255;255;255m".format(value[0], value[1], value[2], i)
    return Return

def bgrandomclr( String : str ) -> str :
    """ it's return the random colored BackGround(stringType) text based on given text """
    
    Return : str = " "
    for i in String :
        Choice : str = choice(ListOfColors)
        value : list = rgb.get(Choice)
        Return : str = Return + "\033[0;48;2;{};{};{}m{}\033[0;48;0;255;255;255m".format(value[0], value[1], value[2], i)
    return Return

def brb2d(String : str) -> str :
    """ its's return the bright to dull color given text for BackGround"""
    Return : str = " "
    Choice : str = choice(ListOfColors)
    index : int = ListOfColors.index(Choice)
    for i,x in enumerate(String):
        value : list = rgb.get(ListOfColors[index+i])
        Return : str = Return + "\033[0;48;2;{};{};{}m{}\033[0;48;0;255;255;255m".format(value[0], value[1], value[2], x)
    return Return

def brd2b(String : str):
    """ its's return the dull to bright color given text for BackGround"""

    Return : str = " "
    reversed = ListOfColors[::-1]
    Choice : str = choice(reversed)
    index : int = reversed.index(Choice)
    for i,x in enumerate(String):
        value : list = rgb.get(reversed[index+i])
        Return : str = Return + "\033[0;48;2;{};{};{}m{}\033[0;48;0;255;255;255m".format(value[0], value[1], value[2], x)
    return Return
def frb2d(String : str) -> str :
    """ its's return the bright to dull color given text for ForeGround"""
    Return : str = " "
    Choice : str = choice(ListOfColors)
    index : int = ListOfColors.index(Choice)
    for i,x in enumerate(String):
        value : list = rgb.get(ListOfColors[index+i])
        Return : str = Return + "\033[0;38;2;{};{};{}m{}\033[0;38;0;255;255;255m".format(value[0], value[1], value[2], x)
    return Return

def frd2b(String : str):
    """ its's return the dull to bright color given text for ForeGround"""
    
    Return : str = ""
    reversed = ListOfColors[::-1]
    Choice : str = choice(reversed)
    index : int = reversed.index(Choice)
    for i,x in enumerate(String):
        value : list = rgb.get(reversed[index+i])
        Return : str = Return + "\033[0;38;2;{};{};{}m{}\033[0;38;0;255;255;255m".format(value[0], value[1], value[2], x)
        
    return Return       
    

    
