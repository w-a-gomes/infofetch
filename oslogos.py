#!/usr/bin/env python3
# https://github.com/w-a-gomes/systemutils
import colors


class Logo(object):
    """Create an object of type 'Logo'

    Create operating system logos using ANSI code.
    """
    def __init__(self, os_name_id: str = 'linux-kernel'):
        """Class constructor"""
        self.__os_id = os_name_id
        self.__accent_color = '\033[32m'
        self.__list_of_supported_logos = [
            'arch-linux',
            'debian', 'deepin',
            'elementary-os', 'endless',
            'fedora',
            'kde-neon',
            'linux-kernel', 'linux-mint', 'lubuntu',
            'mageia', 'manjaro', 'mx',
            'opensuse',
            'solus',
            'ubuntu', 'ubuntu-budgie',
            'xubuntu',
        ]

    def set_os_name_id(self, os_name_id: str = None) -> None:
        """Configures the operating system identity

        Change the identity of the operating system to change the logo.

        :param os_name_id:
        """
        if os_name_id:
            self.__os_id = os_name_id

    def get_list_of_supported_logos(self) -> list:
        """Get a list of the logos supported by this script

        Logically, the name of the logo will be the name of the operating system.

        :return: List of the logos supported by this script
        """
        return self.__list_of_supported_logos

    def get_colored_ansi_code_as_list(self) -> list:
        """Gets the logo in list format

        Each item on the list is a line from the logo.

        :return: List with the logo lines on each item
        """
        return self.get_colored_ansi_code().split('\n')

    def get_accent_color(self) -> str:
        """Gets the accent color of the logo

        Use to decorate.

        :return: String with the accent color of the logo
        """
        self.get_colored_ansi_code()
        return self.__accent_color

    # noinspection SpellCheckingInspection
    def get_colored_ansi_code(self) -> str:
        """Gets the logo as ANSI code

        The logo will be automatically chosen by looking at the name of the operating system.

        :return: String with logo as ANSI code
        """
        color = colors.Color()
        blue = color.get_style(color='blue')
        blue_dark = color.get_style(color='blue', style='dark')
        blue_bold = color.get_style(color='blue', style='bold')
        red = color.get_style(color='red')
        red_bold = color.get_style(color='red', style='bold')
        white = color.get_style(color='white')
        white_bold = color.get_style(color='white', style='bold')
        green = color.get_style(color='green')
        green_back = color.get_style(color='green', background='green')
        cyan = color.get_style(color='cyan')
        yellow = color.get_style(color='yellow')
        reset = color.reset_style()

        default_logo = """
{}               .''''''''.               
{}              .'''''''''''              
{}              ,MN{}'''{}NMN:{}''.             
{}              l{}M{}N{}';'{}N{}M{}N{};'''             
{}              :{}xXMMMMXxx{}'''             
{}             .o{}xMMMMMXx'{},''.            
{}             .k{}M{}'xNNK'{}MMd{}'''.           
{}           ..{}dMMMMMMMMMMMl{}''''.         
{}          .,{}OMMMMMMMMMMMMMd{}'''''.       
{}        .'c{}NMMMMMMMMMMMMMMM0{},''''.      
{}       .'o{}MMMMMMMMMMMMMMMMMMK{}''''''.    
{}      '',{}WMMMMMMMMMMMMMMMMMMM{}:''''''    
{}     .::,x{}WMMMMMMMMMMMMMMMMMMc{}'''''.    
{}   .:kKKk{}l,d{}NMMMMMMMMMMMMMWO{}xK{}'''':{}kx   
{}dkkkkkkkkkx{};'c0{}MMMMMMMMMMMW{}kkkkxxxkkk:  
{}kkkkkkkkkkkkd{}:cX{}MMMMMMMMNko{}kkkkkkkkkkkk;
{}kkkkkkkkkkkkkko{}:lodddoc{},''{}okkkkkkkkkk'  
{}.;kkkkkkkkkkkkk{}.'''''':;..{}kkkkkkkkk'    
{}   ''':xkkkkk'           'kkkkx'
{}""".format(
            blue,
            blue,
            white, blue, white, blue,
            white, blue, white, blue, white, blue, white, blue,
            blue, yellow, blue,
            blue, yellow, blue,
            blue, white, yellow, white, blue,
            blue, white, blue,
            blue, white, blue,
            blue, white, blue,
            blue, white, blue,
            blue, white, blue,
            blue, white, blue,
            yellow, blue, white, yellow, blue, yellow,
            yellow, blue, white, yellow,
            yellow, blue, white, yellow,
            yellow, white, blue, yellow,
            yellow, blue, yellow,
            yellow,
            reset
        )

        if self.__os_id == 'arch-linux' or self.__os_id == 'archlinux' or self.__os_id == 'arch':
            self.__accent_color = blue
            return """
{}                   ..                   
{}                   O0                   
{}                  xMMO                  
{}                 oMMMMO                 
{}                lMMMMMMk                
{}               :MMMMMMMM0               
{}              lcckMMMMMMMK              
{}             xMMMN0NMMMMMMK.            
{}            kMMMMMMMMMMMMMMX.           
{}          .KMMMMMMMMMMMMMMMMW,          
{}         .XMMMMMMMMMMMMMMMMMMMc         
{}        ,WMMMMMMWo.  .cNMMMMMMMo        
{}       cMMMMMMMM'      .NMMMMMMMk       
{}      xMMMMMMMMO        oMMMMMNKNK.     
{}    .KMMMMMMMMMk        lMMMMMMli:.     
{}   'NMMMMMMWKko;        'lx0NMMMMMMO,   
{}  :WMMNkl,.                   'ckXMMMo  
{} xXx:.                            .;dKk 
{}''                                    .'
{}""".format(
                blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue,
                blue, blue, blue, blue, blue, blue, blue, blue, reset
            )

        elif self.__os_id == 'debian':
            self.__accent_color = red
            return """
{}                .:c'....                
{}            .ckXMMMMWMMMNOol:.          
{}         .dXMMMW0o:;,,,:lxKMMMNo.       
{}        xMMMKc.            .lNMMWd      
{}      .XMXc.                  xMMNO     
{}     cMW:          .:;,'.      dMK,     
{}    ,MMc         ,o'            WM;     
{}    xMx         :l              NMd     
{}    xM;         K.              WX.     
{}    xM'         dk            .0X.      
{}    oMo         .ok'   .    .l0l        
{}    .MN           .d0olclodko'          
{}     oMNd            ....               
{}      oMW:                              
{}       ,NW;                             
{}         oWO.                           
{}           cKK:                         
{}             .cddc.                     
{}                 .;;.
{}""".format(
                red, red, red, red, red, red, red, red, red, red, red,
                red, red, red, red, red, red, red, red, reset
            )

        elif self.__os_id == 'deepin':
            self.__accent_color = blue
            return """
{}               .';::::;'.               
{}          .,:looo{}xXXXXXK0O{}o:'.          
{}       .:loooooo{}kMMMMMMMX{}kooool;.       
{}     'loooooooo{}OMMMMMW{}0doooooooool'     
{}   .l{}x{}llllllll{}xMMMMW{}Ooo{}xO0XNNWWWMWO{}l.   
{}  ,d{}NW{}olllllll{}XMMM0{}x{}OxkMKNNWMMMMMMMX{}o'  
{} ,o{}WMMK{}llllllo{}MMM{}kl{}NN{}ld{}MO{}O{}N{}dk{}WMMMMMMN{}o' 
{}.l{}XMMMMO{}llllll{}MMK{}l{}0W{}dl{}0M{}dx{}MX{}lo{}NMMMMMMK{}l 
{}'d{}MMMMMM0{}lcccc{}KM{}0{}00{}ol{}kMX{}lk{}MM{}dlx{}MMMMMMM{}o'
{},x{}MMMMMMMN{}xccc{}lKW0{}x{}OXMN{}ol{}NMM{}ocl{}WMMMMMM{}d,
{}'o{}MMMMMMMMMXk{}lcc{}d0XNKk{}lo{}XMM0{}ccc{}WMMMMMM{}l.
{} c{}KMMMMMMMMMMMX{}Okdoddk{}KMMWk{}cccx{}MMMMMM0{}c 
{} 'l{}NMMMMMMMMMMMMMMMMMMWKk{}ccccl{}NMMMMMX{}c. 
{}  .cod{}xO0KKXXXXXXK0Oxoc{}:::::l{}XMMMMMK{}c.  
{}   .;:::::::::::::::::::::c{}kWMMMMW{}x;.   
{}     .;:::::::::::::::::l{}kNMMMMX{}x;.     
{}       .';::::::::::co{}OXMMMWK{}kc'.       
{}           .',;;:l{}dO00Okx{}o:'.           
{}                ...''...
{}""".format(
                blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue,
                blue, white, blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue,
                reset
            )

        elif self.__os_id == 'elementary-os' or self.__os_id == 'elementary' or self.__os_id == 'elementaryos':
            self.__accent_color = blue
            return """
{}              .',::ccc:,'.              
{}          .,:ccc{}looooool{}ccc:,.          
{}       ':ll{}ok0KKK0{}OOOO{}0KKK0ko{}ll:'       
{}     ,cl{}d0X0{}xoll{}dkOOOOkd{}llok{}KXOo{}lc;.    
{}   'cl{}dXX{}xlll{}d0Kk{}olllld{}0Nk{}llllk{}XKo{}lc,   
{}  ;ll{}0Nd{}lll{}dXXd{}lllllllll{}dMk{}lllll{}xNO{}ll:  
{} :ll{}XX{}llll{}OM0{}llllllllllll{}N0{}llllllo{}N0{}ll: 
{}'ll{}0W{}llll{}OM0{}llllllllllll{}xMd{}lllllllx{}Mk{}ll'
{}:ll{}WO{}llll{}WW{}llllllllllll{}kWx{}lllllll{}dNNN{}llc
{}clo{}Mx{}lllo{}MN{}llllllllll{}xX0o{}llllllo{}0N{}x{}OW{}llc
{}:ll{}WO{}llll{}XM{}dlllllll{}kX0o{}llllllo{}OWO{}ll{}KX{}llc
{}'ll{}OW{}olllo{}NWx{}ll{}okKKk{}llllllld{}KNO{}olld{}Mk{}ll'
{} :ll{}XX{}lllo{}xNMNWNko{}lllll{}ok0NKk{}llllo{}N0{}ll: 
{}  ;ll{}0WNNXKO{}xx{}0NWNNXNNNKOx{}llllll{}kNO{}ll:  
{}   'cld{}XXx{}llllllllllllllllllll{}kXK{}olc,   
{}     ,clo{}0XKk{}olllllllllllld{}kKXO{}olc;     
{}       ':llo{}k0KKKo{}0OO0{}oKKK0x{}oll:'       
{}          .,:cll{}XkookK{}lllc:,.           
{}              .';:cccc:;'.
{}""".format(
                blue,
                blue, white, blue,
                blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue,
                blue, white, blue, white, blue,
                blue, white, blue, white, blue,
                blue, white, blue,
                blue,
                reset
            )

        elif self.__os_id == 'endless' or self.__os_id == 'endless-os' or self.__os_id == 'endlessos':
            self.__accent_color = red_bold
            return """
                                        
                                        
                                        
                                        
                                        
{}                         ,o'            
{}  ,clc:;..           .cOWNd.            
{};WWxodxOXWWKxc'   ,dXMKo.         ...   
{}WM,       .,lKMMNMMNc      'cx0NMNXXWWk.
{}0Md     .;okXMXxco0WMKxlxXMXkl,.     lMX
{} dNWXXWWX0dc'     .:NMMXMMKo;.       'MW
{}    ..         .oKMKo,   .:d0NMX0kxdkNWc
{}            .xNWO:.            .,:cc:'  
{}            .l,                         
                                        
                                        
                                        
                                        
                     
{}""".format(
                red_bold, red_bold, red_bold, red_bold, red_bold, red_bold,
                red_bold, red_bold, red_bold, reset
            )

        elif self.__os_id == 'fedora':
            self.__accent_color = blue
            return """
{}                ........                
{}           ...''''''''''''...           
{}        .'''''''''''''{},clool:,{}'.        
{}     .'''''''''''''{}cONMMMMMMMX{}:;,{}'.     
{}    '''''''''''''{};KMMMMWK0000x{}ccc;{}''    
{}  .'''''''''''''{};NMMMXl{},''''',{}:ccc:{}''.  
{} .''''''''''''''{}dMMMW{};'''''''''{}:ccc,{}''. 
{} '''''''''''''''{}xMMMW{}'''''''''{},:ccc,{}''' 
{}.'''''''''''''''{}xMMMW{},,,,'''{},;:ccc;{}''''.
{}.'''''{},;:c{}dNMMMMMMMMMMMMMW0{}ccccc:,{}'''''.
{}.''{},;:cccc{}dXWWWWMMMMMWWWWWO{}cc:;,{}'''''''.
{}.'{},:ccc:;{},''''''{}xMMMW{}'''''''''''''''''' 
{}.'{}:ccc:{}'''''''''{}xMMMW{}'''''''''''''''''  
{}.'{}:ccc:{}'''''''''{}OMMMN{}''''''''''''''''   
{}.'{};cccc;{},'''''{}:kMMMMd{}''''''''''''''.    
{}.''{},:cc{}lOK00KNMMMMNo{}'''''''''''''.      
{}.''''{},:{}dMMMMMMMW0o{},'''''''''''..        
{} .''''''{};clooc;{}''''''''''...            
{}    ''''''''''''''''''''
{}""".format(
                blue,
                blue,
                blue, white,     blue,
                blue, white,     blue_bold, blue,
                blue, white,     blue_bold, blue,
                blue, white,     blue,      blue_bold, blue,
                blue, white,     blue,      blue_bold, blue,
                blue, white,     blue,      blue_bold, blue,
                blue, white,     blue,      blue_bold, blue,
                blue, blue_bold, white,     blue_bold, blue,
                blue, blue_bold, white,     blue_bold, blue,
                blue, blue_bold, blue,      white,     blue,
                blue, blue_bold, blue,      white,     blue,
                blue, blue_bold, blue,      white,     blue,
                blue, blue_bold, blue,      white,     blue,
                blue, blue_bold, white,     blue,
                blue, blue_bold, white,     blue,
                blue, white,     blue,
                blue,
                reset
            )

        elif self.__os_id == 'neon' or self.__os_id == 'kde-neon' or self.__os_id == 'kdeneon':
            self.__accent_color = cyan
            return """
{}              .,:cllllc:,.              
{}         ..;cllllo{}dkkd{}ollllc;..         
{}       'cll{}okkkkkkkkkkkkkkkko{}llc'       
{}    .:l{}xxOOko{}llllll{}xx{}llllll{}okOOxx{}l:.    
{}   ;l{}l{}dX{}x{}O{}ll{}ll{}xkkk0OO0kkkx{}ll{}ll{}O{}x{}Xd{}ll;   
{}  c{}ll{}O0o{}l{}llx{}OOd{}lll{}lll{}lll{}l{}dOO{}xl{}ll{}o0O{}l{}lc  
{} c{}ll{}0k{}ll{}l{}o0k{}ll{}lll{}lll{}lll{}lll{}ll{}k0o{}l{}ll{}k0{}llc 
{},l{}l{}k0{}l{}ll{}oXo{}ll{}l{}lll{}oxkkxo{}ll{}l{}lll{}oXo{}lll{}0k{}l{}l,
{}cl{}oXo{}lll{}Kx{}llllll{}0WMMMMW0{}llllll{}xK{}lll{}oXo{}lc
{}ll{}K{}k{}K{}lll{}No{}lllll{}dMMMMMMMMd{}lllll{}oN{}lll{}K{}k{}K{}ll
{}cl{}lXo{}lll{}0x{}llllll{}0WMMMMW0{}llllll{}x0{}lll{}oXl{}lc
{},l{}l{}k0{}l{}ll{}oXo{}ll{}l{}lll{}oxkkxo{}l{}ll{}lll{}oXo{}lll{}0k{}ll,
{} c{}ll{}0k{}ll{}l{}o0k{}ll{}llll{}ll{}lll{}lll{}ll{}k0o{}l{}ll{}k0{}llc 
{}  c{}ll{}O0o{}l{}ll{}dOOd{}lll{}lll{}lll{}l{}dOOd{}l{}ll{}o0O{}l{}lc  
{}   ,ll{}dX{}x{}O{}llll{}xkkk0OO0kkkd{}llll{}O{}x{}Xd{}ll,   
{}    .;l{}xxOOkd{}llllll{}xx{}llllll{}dkOOxx{}l;.    
{}       'cll{}oxkkkkkkkkkkkkkkxo{}llc'       
{}          .,clllll{}dkkd{}lllllc,.          
{}              .,:cllllc:,.
{}""".format(
                green,
                green, white, green,
                green, white, green,
                green, white, green, white, green, white, green,
                cyan,  green, white, green, white, cyan,  green, white, green, cyan,  white, green, white, cyan,
                green, cyan,  white, green, cyan,  white, cyan,  green, cyan,  green, white, cyan,  green, white, cyan,
                green,
                cyan,  green, white, cyan,  green, white, cyan,  green, cyan,  green, cyan,  green, white, cyan,  green,
                white, cyan,
                cyan,  green, white, cyan,  green, white, cyan,  green, cyan,  white, cyan,  green, cyan,  white, cyan,
                white, green, cyan,
                cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,
                cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,
                cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,  white, cyan,
                blue,  cyan,  white, cyan,  blue,  white, cyan,  blue,  cyan,  white, cyan,  blue,  cyan,  white, cyan,
                white, blue,
                cyan,  blue,  white, cyan,  blue,  white, cyan,  blue,  cyan,  blue,  cyan,  blue,  white, cyan,  blue,
                white, cyan,
                cyan,  cyan,  white, blue,  cyan,  white, cyan,  blue,  cyan,  blue,  white, cyan,  blue,  white, cyan,
                blue,
                blue,  white, blue,  white, blue,  white, blue,  white, blue,  white, blue,
                blue,  white, blue,  white, blue,  white, blue,
                blue,  white, blue,
                blue,  white, blue,
                blue,
                reset
            )

        elif self.__os_id == 'linux-kernel' or self.__os_id == 'linuxkernel':
            self.__accent_color = yellow
            return default_logo

        elif self.__os_id == 'linuxmint' or self.__os_id == 'linux-mint':
            self.__accent_color = green
            return """
                                        
{}dddddddddddddddddddddddddddol:'.        
{}MMMWWWWWWWWWWWWWWWWWWNNNNNNWWMMMNk;     
{}MMM{}XXXXXKKKKK000000OOOOkkkkkxxk0{}XWMWd   
{}MMM{}KKKKKKK{}XWNX{}000OOOOkkkkkkxxxxxdd{}0WMN, 
{}MMMWWNX{}Okk{}KMMN{}kkkkk{}OKKKKO{}k{}k{}0KK0O{}dddd{}NMM,
{}llllkMMX{}kk{}0MMN{}xxx{}kNMMMMMMMMMMMMMMK{}dox{}MMX
{}    ,MMN{}xx{}0MMX{}xxx{}NMMX{}xdk{}WMMX{}xdx{}NMM0{}oo{}MMM
{}    ,MMX{}dd{}0MMX{}ddd{}WMMO{}ddd{}XMM0{}doo{}KMMK{}lo{}MMM
{}    ,MMX{}dd{}OMMX{}oo{}o{}WMMO{}ooo{}XMM0{}ooo{}KMMK{}oo{}MMM
{}    ,MMX{}oo{}OMMX{}o{}oo{}NMMO{}lll{}XMM0{}ool{}0MMK{}oo{}MMM
{}    ,MMX{}oo{}kMMX{}lllooollllooollll{}k00k{}lo{}MMM
{}    .WMW{}ol{}dWMMO{}lcccccccccccccox{}O00d{}lo{}MMM
{}     lMMK{}lco{}KMMMNNNN000000000000Od{}llo{}MMM
{}      lWMN{}xcclx{}O0000k00000000do{}lllllo{}MMM
{}       .kMMW0{}xl::::::::::::::cccccco0{}MMM
{}         .ckNMMMWNNXXXNNNNNNNNNNNNNMMMMM
{}             .';cloooooooooooooooooooooo
                                        
{}""".format(
                white,
                white,
                white, green, white,
                white, green, white, green, white,
                white, green, white, green, white, green, cyan,  white, cyan,  white,
                white, green, white, green, white, cyan,  white,
                white, green, white, green, white, cyan,  white, cyan,  white, cyan,  white,
                white, green, white, green, white, cyan,  white, cyan,  white, cyan,  white,
                white, green, white, green, cyan,  white, cyan,  white, cyan,  white, cyan,  white,
                white, green, white, green, cyan,  white, cyan,  white, cyan,  white, cyan,  white,
                white, green, white, cyan,  white, cyan,  white,
                white, green, white, cyan,  white, cyan,  white,
                white, green, white, cyan,  white,
                white, cyan,  white, cyan,  white,
                white, cyan,  white,
                white,
                white,
                reset
            )

        elif self.__os_id == 'lubuntu':
            self.__accent_color = blue
            return """
{}             .:d0XWMMWX0d:.             
{}         .ck00{}OxdollllodxO{}00kc.         
{}      .dK0{}dccccccccccccccccccd{}0Kd.      
{}    'OX{}dcccccccccccccc{};i'{}cccccccd{}KO'    
{}   xN{}dcccccccccccc{}idOXXd{}ccccccccccd{}Nx   
{} .K0{}cccccccccc{}ik0NMMMMO{}ccccccccccccc{}0K. 
{} XK{}cccccccc{}d0NMMMMMMMMMK{}occcccccccccc{}KX 
{}oW{}lcccc{}ikKWMMMMMMMMMMMMMMk{}ccccccccccc{}lWo
{}X0{}cc{}oOXMMMMMMMMMMMXKNMMMMMO{}ccccccccccc{}0X
{}M0ONWXClkWMMMMMM0{}occc{}l0MMMMk{}cccccccccc{}kM
{}XX{}dlccc{}lKMPlMMX{}occccccco{}XMMW{}occccccccc{}0X
{}oW{}lccc{}dNK{}ok{}MWk{}ccccccccccc{}KMMX{}cccccccc{}lWo
{} KK{}c{}l0X{}ol{}KM0l{}ccccccccccccc{}0MMd{}ccccccc{}KK 
{} .KKK{}xcd{}WNd{}cccccccccccccccc{}0MX{}cccccc{}KK. 
{}   dNdOWO{}ccccccccccccccccccc{}KM{}occc{}dNd   
{}    .OMO{}cccccccccccccccccccc{}lN0{}cx{}XO.    
{}      .oK0xl{}cccccccccccccccc{}lOWKo.      
{}         .cx0KOkddooooddxO00xc.         
{}              ;dOXWMMWXOd;
{}""".format(
                white,
                white, blue, white,
                white, blue, white,
                white, blue, white, blue, white,
                white, blue, white, blue, white,
                white, blue, white, blue, white,
                white, blue, white, blue, white,
                white, blue, white, blue, white,
                white, blue, white, blue, white,
                white, blue, white, blue, white,
                white, blue, white, blue, white, blue, white,
                white, blue, white, blue, white, blue, white, blue, white,
                white, blue, white, blue, white, blue, white, blue, white,
                white, blue, white, blue, white, blue, white,
                white, blue, white, blue, white,
                white, blue, white, blue, white,
                white, blue, white,
                white,
                white,
                reset
            )

        elif self.__os_id == 'mageia':
            self.__accent_color = blue_bold
            return """
{}               .°°.                    
{}                °°.°°,                 
{}                  `..´                 
{}                .°°°.                  
{}                '...'                  
{}             .''''..°°°.               
{}             '    ''...'               
{}              ''''                     
{}          ,,,           ,,,            
{}         kMNXMXOdooodkKWWXMX.          
{}       .XMk    '''''''    :WM:         
{}       OMO                 cMW.        
{}       WM;                 .MM;        
{}       0Md                 ;MM.        
{}       .WM;               .XMd         
{}        'NMx.            cWMo          
{}          lNMOc'.    .;xNWk'           
{}            'o0NMMWWMWKx'              
{}                '''''                  
{}""".format(
                blue_bold, blue_bold, blue_bold, blue_bold, blue_bold, blue_bold, blue_bold, blue_bold,
                white, white, white, white, white, white, white, white, white, white, white, reset
            )

        elif self.__os_id == 'manjaro':
            self.__accent_color = green
            return """
                                        
   {} ......................{}  {}.......... {} 
   {}.MMMMMMMMMMMMMMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMMMMMMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMMMMMMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMMMMMMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMo{}              {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}dkkkkkkkko{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {}.MMMMMMMMMl{}  {}XMMMMMMMMK{}  {}oMMMMMMMMM.{} 
   {} ......... {}  {}..........{}  {} ......... {} 

{}""".format(
                green_back, reset, green_back, reset,
                green_back, reset, green_back, reset,
                green_back, reset, green_back, reset,
                green_back, reset, green_back, reset,
                green_back, reset, green_back, reset,
                green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                green_back, reset, green_back, reset, green_back, reset,
                reset
            )

        elif self.__os_id == 'mx' or self.__os_id == 'mx-linux' or self.__os_id == 'mxlinux':
            self.__accent_color = red
            return """
{}   ,xolllllllllllllllllllllllllllllllox'
{}   M                                  .W
{}   M                                  .W
{}   M        :KMx.            oWN'     .W
{}   M       'KMMMMd.        lWMO.      .W
{}   M         ,KMMMWo     cNM0'        .W
{}   M           ;XMMMWl :NMK,          .W
{}   M             :NMMMMMX;            .W
{}   M           cO' OMMMMN:            .W
{}   M         :XMMMNMNxWMMMX;          .W
{}   M       ,KMMMMMMMO. dWMMMK,:,      .W
{}   M     '0MMMMMMMMMMMd..xMMMMMM0.    .W
{}   M   .OMMMMMMMMMMMMMMWo :MMMMMMMk.  .W
{}   M .xMMMMMMMMMMMMMMMMMMWMMMMMMMMMMx..W
{}   M .'''''''''''''''''''''''''''''''..W
{}   M                                  .W
{}   M                                  .W
{}   ,dlcccccccccccccccccccccccccccccccld'
{}                                        
{}
{}""".format(
                white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold,
                white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold, white_bold,
                white_bold, white_bold, white_bold, white_bold, reset
            )

        elif self.__os_id == 'opensuse':
            self.__accent_color = green
            return """
{}             'lkKNWMMWNKkl'             
{}         'oONMWKOxdoodxOKNMNOo'         
{}      .xNMXd;.            .;dKMNx.      
{}    ,0MXl {}..                  {}.lXM0,    
{}  .kMMK{},. kMMNK0kdl::.           {}cNMk.  
{} .XMM{}MMMMWWMMMMMMMMMMMWKko;.      {}.OMX. 
{}.NMM{}MMMMMMMMMMMMMMMWx:{},,,,{}oXXc      {}OMN.
{}xMMK{}MMMMMMMMMMMMMMN.,{}KM0kOo{} kMk     {}.NMx
{}NMM{}MMMMMMMMMMMMMMMk {}KMW..dM'{}'MMx     {}dMN
{}MMM{}MMMMMMMMMWkNMMMW'{}.kWMMX.{}.OMMMc    {}cMM
{}NMM{}MMMMMMMMMMk.':NKWOlpppppNMY:''    {}dMN
{}dMMK{}MMMMMMMMMMWKKx''''''''´,,xxMN   {}.NMd
{}.XMMM{}MMMMMMMMMMMMMMMMMMMMMMMMMMN'   {}0MX.
{} .KMMM{}MMMMMMMMMMMMMMMMMMMMWKkl'   {}.0MK. 
{}   xMMM{}d:;:ccoddxxxdolc;'.       {}oWMx   
{}    .kWNd'                    'dNWk.    
{}      .oXMNkc'            'ckNMXo.      
{}         .ckXMMN0OkxxkO0XMMXkc.         
{}             .:x0NWMMWN0x:.
{}""".format(
                white_bold, white_bold, white_bold,
                white_bold, green, white_bold,
                white_bold, green, white_bold,
                white_bold, green, white_bold,
                white_bold, green, white_bold, green, white_bold,
                white_bold, green, white_bold, green, white_bold,
                white_bold, green, white_bold, green, white_bold,
                white_bold, green, white_bold, green, white_bold,
                white_bold, green, white_bold,
                white_bold, green, white_bold,
                white_bold, green, white_bold,
                white_bold, green, white_bold,
                white_bold, green, white_bold,
                white_bold,
                white_bold,
                white_bold,
                white_bold,
                reset
            )

        elif self.__os_id == 'solus':
            self.__accent_color = blue_dark
            return """
{}            .                           
{}            ''............              
{}        ....{}dX{}:...............          
{}      .....:{}WMMx{}'................       
{}    ......;{}NMMMMX{};.................     
{}  .......,{}XMMMMMMW{}o.................    
{} .......,{}XMMMMMMMMM{};'{}c{}'..............   
{} ......;{}XMMMMMMMMMMl{}.{}lNx{},.............  
{}......:{}NMMMMMMMMMMMd.{}.{}OMWk{};;{}lxdc{},...... 
{}.....l{}WMMMMMMMMMMMMk.{}.{}cMMMWk{},'{}lKMN0d{}:'. 
{}...'{}xMMMMMMMMMMMMMMK.{}.,{}MMMMMWo{}..{}oWMMMN;{}.
{}..'{}0MMMMMMMMMMMMMMMN.{}.;{}MMMMMMM0{},.{}xMWO:{}. 
{}.'{}xKNWMMMMMMMMMMMMMM{},.{}oMMMMMMMMX{},{}'{}ol{}kx  
{}  ....',;{}:ccloddxkOO{};'{};;;;;''{}oll{}dkko{},   
{}   'lcc:::;;;;;;;;:::{}clodxxxxxdc{},',.    
{}    ':llooodddddddoollc:;{},',,,,,,.      
{}       ,,,,,,,,,,,,,,,,,,,,,,,,,        
{}          ,,,,,,,,,,,,,,,,,,,           
{}               ,,,,,,,,,
{}""".format(
                blue_dark,
                blue_dark,
                blue_dark, white, blue_dark,
                blue_dark, white, blue_dark,
                blue_dark, white, blue_dark,
                blue_dark, white, blue_dark,
                blue_dark, white, blue_dark, white, blue_dark,
                blue_dark, white, blue_dark, white, blue_dark,
                blue_dark, white, blue_dark, white, blue_dark, white, blue_dark,
                blue_dark, white, blue_dark, white, blue_dark, white, blue_dark,
                blue_dark, white, blue_dark, white, blue_dark, white, blue_dark,
                blue_dark, white, blue_dark, white, blue_dark, white, blue_dark,
                blue_dark, white, blue_dark, white, blue_dark, white, blue_dark, white,
                blue_dark, white, blue_dark, white, blue_dark, white, blue_bold,
                blue_dark, white, blue_bold,
                white, blue_bold,
                blue_bold,
                blue_bold,
                blue_bold,
                reset
            )

        elif self.__os_id == 'ubuntu':
            self.__accent_color = red
            return """
{}              ;d0XWMMWX0d;              
{}         .ck0K0{}kxddddddxk{}0K0kc.         
{}      .oK0k{}ollllllllllllllllo{}x0Ko.      
{}    .OX{}xolllllllllllllll{}k0KOd{}llo{}xXO.    
{}   dN{}xlllllllll{}idkkOOk{}xx{}MMMMX{}lllll{}xNd   
{} .KK{}olllllll{}dOx{}k{}iMMMMMMOONNi{}dllllllo{}KK. 
{} KK{}ollllll{}o0MMMl{}x{}OkxxkOKWWNW0o{}llllllo{}KK 
{}oW{}ollllll{}dNMMWO{}ollllllllo{}OWMMNd{}llllllo{}Wo
{}X0{}lllx{}KXK{}k{}KMM{}xllllllllllllx{}MMMK{}lllllll{}0X
{}MO{}llo{}MMMMM{}o{}WN{}llllllllllllllkOOklllllll{}OM
{}X0{}lll{}x0K0{}k{}XMM{}xllllllllllll{}xMMMK{}lllllll{}0X
{}lW{}ollllll{}oNMMMOo{}llllllllo{}0MMMN{}ollllllo{}Wl
{} KK{}ollllll{}o0WMW{}x{}x0OkkO0XWNNW0{}ollllllo{}KK 
{}  KK{}olllllll{}ok{}dk{}MMMMMMMOOXXP{}dllllllo{}KK  
{}   dNx{}lllllllll{}odxkkkkd{}x{}MMMMX{}lllll{}xNd   
{}    .OXk{}olllllllllllllll{}x0KOo{}llo{}kXO.    
{}      .oKKk{}ollllllllllllllllo{}kKKo.      
{}         .:x0K0k{}xxddddxx{}k0K0x:.         
{}              ,oOXWMMWXOo,
{}""".format(
                white,
                white, red, white,
                white, red, white,
                white, red, white, red, white,
                white, red, white, red, white, red, white,
                white, red, white, red, white, red, white,
                white, red, white, red, white, red, white,
                white, red, white, red, white, red, white,
                white, red, white, red, white, red, white, red, white,
                white, red, white, red, white, red, white,
                white, red, white, red, white, red, white, red, white,
                white, red, white, red, white, red, white,
                white, red, white, red, white, red, white,
                white, red, white, red, white, red, white,
                white, red, white, red, white, red, white,
                white, red, white, red, white,
                white, red, white,
                white, red, white,
                white,
                reset
            )

        elif self.__os_id == 'ubuntubudgie' or self.__os_id == 'ubuntu-budgie':
            self.__accent_color = blue
            return """
{}             .:d0XWMMWX0d:.             
{}         .lkXMMMMMMMMMMWXKXKkc.         
{}      .oXMMMMMMMMMMMKc.      'o0o.      
{}    'OMMMMMMMMMMMMMc            ;XO'    
{}   xMMMMNXXNMMMMMM0               KMx   
{} .XMXo'     lKMMMMN.              'MMX. 
{} XN:       OMMMMMMMNc             .MMMX 
{}oN.        ;WMMMMMMMMMXOxkO0Od'   kMMMMo
{}Nc          .OMMMMMMMMMMMMMMMMM',0MMMMMN
{}M;            KMMMMMMMMMMMMMMMWNMMMMMMMM
{}N0            0MMMMMMMMMMMMMMMMMMMMMMMMX
{}oMK'         dMMMMMMMMNo'.  .,dWMMMMMMMo
{} XMMXxc,,,ckWMMMMMMMMx         .KMMMMMX 
{} .KMMMMMMMMMMMMWMMMMx           'MMMMK. 
{}   dMMMMMMMMMMM,:l:.            ;MMMd   
{}    .kMMMMMMMMM0.              'NMk.    
{}      .lXMMMMMMMWo.          ,kXl.      
{}         .cxXMMMMMMNOdolloxxxc.         
{}              ;dOXWMMWXOd;
{}""".format(
                blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue,
                blue, blue, blue, blue, blue, blue, reset
            )

        elif self.__os_id == 'xubuntu':
            self.__accent_color = blue
            return """
{}              ..',,,,,,'..              
{}          ..,;;;;;;;;;;;;;;,..          
{}       .,;;;;;;;;;;;;;;;;;;;;;;,.       
{}     .;;;;;;;;;;;;;;;;;;;;{}c{};;;;;;;'     
{}   .;;;;;;;;;;:{}loc{};;;;;;;{}cW{}c;;:{}xl{};;;.   
{}  ';;;;;;{}oxo{};;{}XMMWo{};;;;;;{}xW{}:;l{}N0{}:;;;;'  
{} ';;;;;;{}xMMM0{}:{}XMMM0{};;;;;;{}K0{};x{}WO{};;;;;;;' 
{}.;;;;;;;{}oMMMMKkMMMXlc{}:;;;{}0{}co{}Wd{};;;;;;;;;.
{}';;;;;;;:{}WMMMMMMMMMMMMWNK0kxl{};;;;;;;;;;'
{},;;;;;;;{}0MMMMMMMMMMMMMMMMMMMMNOl{};;;;;;;,
{}';;;;;;{}lMMMMMMMMMMMMMMMMMMMMMMMWl{};;;;;;'
{}.;;;;;;{}kMMMMMMMMMMMMMMMMMMMMMMM0{}:;;;;;;.
{} ';;;;;{}kMMMMMMMMMMMMMMMMMMMWKxc{};;;;;;;' 
{}  ';;;;{}cWMMMMMMMMMMMMMMN0kl{}:;;;;;;;;;'  
{}   .;;;;{}cOXWMMMMWNKOxoc{};;;;;;;;;;;;;.   
{}     .;;;;;;{}ccc{}:;;;;;;;;;;;;;;;;;;.     
{}       .';;;;;;;;;;;;;;;;;;;;;;'.       
{}          ..';;;;;;;;;;;;;;'..          
{}               ..',,,,'..
{}""".format(
                blue,
                blue,
                blue,
                blue, white, blue,
                blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue, white, blue,
                blue, white, blue, white, blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue, white, blue,
                blue,
                blue,
                blue,
                reset
            )

        else:
            self.__accent_color = yellow
            return default_logo


if __name__ == '__main__':
    logo = Logo()  # ubuntu
    print(logo.get_colored_ansi_code())

    for distro_name in logo.get_list_of_supported_logos():
        logo.set_os_name_id(distro_name)
        print(distro_name)
        print(logo.get_colored_ansi_code())
