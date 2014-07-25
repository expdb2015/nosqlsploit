from os import name
if name == 'nt':
    '''windows color table'''
    #global BLACK,BLUE,GREEN,CYAN,RED,PURPLE,YELLOW,WHITE,GREY
    BLACK = 0x0
    BLUE  = 0x01
    GREEN = 0x02
    CYAN  = 0x03
    RED   = 0x04
    PURPLE= 0x05
    YELLOW= 0x06
    WHITE = 0x07
    GREY  = 0x08
else:
    '''linux color table'''
    #global BLACK,BLUE,GREEN,CYAN,RED,PURPLE,YELLOW,WHITE,GREY
    BLACK = '\033[0m'
    BLUE  = '\033[34m'
    GREEN = '\033[32m'
    CYAN  = '\033[36m'
    RED   = '\033[31m'
    PURPLE= '\033[35m'
    YELLOW= '\033[33m'
    WHITE = '\033[37m'
    GREY  = '\033[38m'

winCode   = """
class prettyPrint:
    '''windows cmd color'''
    try:
        STD_INPUT_HANDLE = -10
        STD_OUTPUT_HANDLE= -11
        STD_ERROR_HANDLE = -12
        import ctypes
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        def set_cmd_text_color(self, color, text="",handle=std_out_handle):
            '''set color'''
            self.ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
            return text
        def resetColor(self):
            '''reset color'''
            self.set_cmd_text_color(RED|GREEN|BLUE)
        def prettyPrint(self,msg,color=BLACK,enter=1):
            '''print color message'''
            self.set_cmd_text_color(color|color|color)
            if enter == 1:
                print msg
            else:
                print msg,
            self.resetColor()
    except:
        pass
"""

linuxCode    = """
class prettyPrint:
    '''linux terminal color'''
    def set_cmd_text_color(self, color, text=""):
        return color+text+BLACK
    def prettyPrint(self,msg,color=BLACK,enter=1):
        '''print color message'''
        if enter == 1:
            print color+msg+BLACK
        else:
            print color+msg+BLACK,
"""

if __name__ == '__main__':
    print __doc__
else:
    if name == 'nt':
        exec(winCode)
        prettyPrint = prettyPrint()
    else:
        exec(linuxCode)
        prettyPrint = prettyPrint()
