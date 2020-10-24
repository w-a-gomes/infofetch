#!/usr/bin/env python3
import re
import sys

import osinfo
import oslogos


class InfoFetch(object):
    def __init__(self, custom_logo: str = None):
        self.__custom_logo = custom_logo
        self.__os_info = osinfo.OsInfo()
        self.__os_logo = oslogos.Logo()
        if self.__custom_logo:
            self.__os_logo.set_os_name_id(self.__custom_logo)

        self.__logo_list = self.__os_logo.get_colored_ansi_code_as_list()
        self.__info_list = self.get_info()
        self.__resolve_color_bar()

    @staticmethod
    def illusion_float(logo_list: list, info_list: list, width_chars):
        # Listas com a mesma quantidade de itens
        while len(logo_list) < len(info_list):
            logo_list.append(' ')
        while len(info_list) < len(logo_list):
            info_list.append(' ')

        full_list = list()
        for line_logo, line_info in zip(logo_list, info_list):
            # Contar quantos caracteres na linha da logo faltam para ficar igual 'width_chars'
            re_color = re.compile(r'\x1b[^m]*m')
            clean_line = re_color.sub('', line_logo)  # Remove caracteres invisíveis de cores da contagem
            if len(clean_line) < width_chars:
                missing_characters = width_chars - len(clean_line)
                line_logo = line_logo + ' '*missing_characters

            full_list.append(line_logo + ' ' + line_info)

        return full_list

    def __resolve_color_bar(self):
        color_bar = '\033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m  \033[0m'
        if len(self.__info_list) <= len(self.__logo_list):
            self.__info_list.append(color_bar)
        else:
            self.__logo_list.append(color_bar)

    def get_info(self):
        accent_color = self.__os_logo.get_accent_color()
        head = accent_color + 'Matrix' + '\033[m'
        return [
            head,
            '\033[m' + '-'*len(head),
            accent_color + 'OS: ' + '\033[m' + '',
            accent_color + 'Architecture: ' + '\033[m' + '',
            accent_color + 'Kernel: ' + '\033[m' + '',
            accent_color + 'Board: ' + '\033[m' + '',
            accent_color + 'CPU: ' + '\033[m' + '',
            accent_color + 'GPU: ' + '\033[m' + '',
            accent_color + 'RAM: ' + '\033[m' + '',
            accent_color + 'Swap: ' + '\033[m' + '',
            accent_color + 'Resolution: ' + '\033[m' + '',
            accent_color + 'Uptime: ' + '\033[m' + '',
            accent_color + 'Shell: ' + '\033[m' + '',
            accent_color + 'DE: ' + '\033[m' + '',
            accent_color + 'WM: ' + '\033[m' + '',
            accent_color + 'Packages: ' + '\033[m' + '',
            accent_color + 'Font: ' + '\033[m' + '',
            accent_color + 'Browser: ' + '\033[m' + '',
        ]

    def main(self):
        for i in self.illusion_float(self.__logo_list, self.__info_list, 40):
            print(i)


if __name__ == '__main__':
    fetch = InfoFetch()
    fetch.main()
